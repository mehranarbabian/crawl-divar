from pymongo import MongoClient


def get_mongo_collection():
    # Create a connection to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI if needed

    # Select the database
    db = client['Divar']

    # Select the collection
    collection = db['appartement']
    return collection


def save_collection_mongo(items):
    collection = get_mongo_collection()
    result = collection.insert_many(items)

    # Print the inserted IDs
    print(f"Documents inserted with IDs: {result.inserted_ids}")


def clean_mongo():
    collection = get_mongo_collection()
    # Delete all documents in the collection
    result = collection.delete_many({})

    print(f"Deleted {result.deleted_count} documents.")


def get_all_tokens():
    collection = get_mongo_collection()
    projection = {"token": 1, "_id": 0}  # Replace 'username' with the field you want to retrieve

    # Fetch all documents with the specified projection
    documents = collection.find({}, projection)
    tokens = [doc['token'] for doc in collection.find({}, projection)]

    return tokens


def add_field_to_record_by_token(name, value, token):
    collection = get_mongo_collection()

    # Define the filter to find the document you want to update
    filter = {"token": token}  # Replace with the appropriate filter

    # Define the field and value to add
    update = {"$set": {name: value}}  # Replace with your field and value

    # Update the document
    result = collection.update_one(filter, update)

    # Check if the update was successful
    if result.matched_count > 0:
        print("Document updated successfully.")
    else:
        print("No document matched the filter.")
