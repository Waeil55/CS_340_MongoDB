from pymongo import MongoClient

class AnimalShelterCRUD:
    def __init__(self, username, password, host, port, db, collection):
        # MongoDB connection URI
        self.uri = f"mongodb://{username}:{password}@{host}:{port}/{db}"
        try:
            self.client = MongoClient(self.uri)
            self.database = self.client[db]
            self.collection = self.database[collection]
            # Test the connection
            self.client.server_info()
        except Exception as e:
            print(f"Failed to connect to the database. Error: {e}")
            raise

    def create(self, data):
        """
        Inserts a new document into the collection.
        :param data: A dictionary containing the data to be inserted.
        :return: The ID of the inserted document.
        """
        if data is not None:
            insert_result = self.collection.insert_one(data)
            return insert_result.inserted_id
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query=None):
        """
        Retrieves documents from the collection based on the provided query.
        :param query: A dictionary specifying the query to filter documents.
                      If None, all documents in the collection are returned.
        :return: A list of documents matching the query.
        """
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def update(self, query, data_update):
        """
        Updates documents in the collection based on the provided query.
        :param query: A dictionary specifying the documents to update.
        :param data_update: A dictionary specifying the fields and values to update.
        :return: The number of documents updated.
        """
        if query is not None and data_update is not None:
            update_result = self.collection.update_many(query, {"$set": data_update})
            return update_result.modified_count
        else:
            raise ValueError("Query or data_update parameter is empty")

    def delete(self, query):
        """
        Deletes documents from the collection based on the provided query.
        :param query: A dictionary specifying the documents to delete.
        :return: The number of documents deleted.
        """
        if query is not None:
            delete_result = self.collection.delete_many(query)
            return delete_result.deleted_count
        else:
            raise ValueError("Query parameter is empty")