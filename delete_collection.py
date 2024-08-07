import ollama
import chromadb
import csv
#from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
import chromadb.utils.embedding_functions as embedding_functions
from time import process_time

print("\n   - - The Airqiv Document Explorer  - -       ")
print("          - - www.airqiv.com  - -       ")
print("\nAI-Assistant Document Explorer")
print("Copyright (c) <2024>, <Paul Bjerk>")
print("All rights reserved.")
print("\nThis source code is licensed under the BSD2-style license found at https://opensource.org/license/bsd-2-clause .\n")
print("The app leverages open-sourced LLMs using the Ollama app and a vector database using ChromaDB")


def delete_documents(collection):
    fieldnames = ["FOLDERNAME", "LANGUAGE", "PHOTONAME", "UNIQUEPHOTO", "PHOTOTEXT", "NAMESMENTIONED","COUNTRIESMENTIONED","INSTRUCTION","CONTEXT","RESPONSE"]
    with open(file_path, mode="r") as old_file, open(str("all-"+collection+"-documents.csv"), mode="a") as new_file:
        current = csv.DictReader(old_file, fieldnames=fieldnames)
        next(current, None)
        all_files = csv.DictWriter(new_file, fieldnames=fieldnames)
        for row in current:
            all_files.writerow(row)

client = chromadb.PersistentClient(path="chromadb/phototextvectors")

currentingest = input("What CSV file do you want to delete? (enter the filename only, without the .csv suffix) It's best to copy-paste to avoid typos ")
archive_collection = input("What archive collection does this belong to? \n These records will be removed from the archive collection.")
archive_collection = str("all-"+archive_collection+"-documents")
#print(archive_collection.peek()) # returns a list of the first 10 items in the collection
topic_collection = input("What topic collection does this belong to? \n These records will be removed from the topic collection.")
topic_collection = str("all-"+topic_collection+"-documents")
#print(topic_collection.peek()) # returns a list of the first 10 items in the collection
user_auth = input("Is this the collection you wish to delete? Type y or n: ")
#archive_collection.count() # returns the number of items in the collection
#topic_collection.count() # returns the number of items in the collection
#collection.modify(name="new_name") # Rename the collection

#"Chroma supports deleting items from a collection by id using .delete. \n "
# "The embeddings, documents, and metadata associated with each item will be deleted.\n"
# "⚠️ Naturally, this is a destructive operation, and cannot be undone.\n"
# ".delete also supports the where= filter.\n"
# "If no ids are supplied, it will delete all items in the collection that match the where filter."

#collection.delete(
    #ids=["id1", "id2", "id3",...],
	#where={"chapter": "20"}
#)
if user_auth == "y":
    #collection = client.get_collection(name="test") # Get a collection object from an existing collection, by name. Will raise an exception if it's not found.
    #collection = client.get_or_create_collection(name="test") # Get a collection object from an existing collection, by name. If it doesn't exist, create it.
    #collection = client.get_collection(name=currentingest)
    #client.delete_collection(name=currentingest) # Delete a collection and all associated embeddings, documents, and metadata. ⚠️ This is destructive and not reversible
    client.delete_collection(name=archive_collection) # Delete a collection and all associated embeddings, documents, and metadata. ⚠️ This is destructive and not reversible
    client.delete_collection(name=topic_collection) # Delete a collection and all associated embeddings, documents, and metadata. ⚠️ This is destructive and not reversible

    #collection = client.get_collection(name=str("all-"+ archive_collection +"-documents"))
    #collection.delete(
        #ids=["id1", "id2", "id3",...],
        #where={"FOLDERNAME": currentingest}
    #)

    #collection = client.get_collection(name=str("all-" + topic_collection + "-documents"))
    #collection.delete(
        #ids=["id1", "id2", "id3", ...],
        #where={"FOLDERNAME": currentingest}
    #)

    #delete_documents(archive_collection)
    #delete_documents(topic_collection)
else:
    print("We won't delete anything for now. \nIf you want to try again type python3 delete.collecction.py again in the Terminal.")


exit()
