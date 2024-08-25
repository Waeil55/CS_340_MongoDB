{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9035e929-0f20-4545-9647-fed2823e2431",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:root:Connected to MongoDB successfully\n"
     ]
    }
   ],
   "source": [
    "from pymongo import MongoClient\n",
    "import logging\n",
    "\n",
    "# Configure logging\n",
    "logging.basicConfig(level=logging.INFO)\n",
    "\n",
    "# Connect to MongoDB\n",
    "try:\n",
    "    client = MongoClient('mongodb://localhost:27017')\n",
    "    db = client['AAC']  # Use the \"AAC\" database\n",
    "    collection = db['animals']  # Use the \"animals\" collection\n",
    "    logging.info(\"Connected to MongoDB successfully\")\n",
    "except Exception as e:\n",
    "    logging.error(f\"Failed to connect to MongoDB: {e}\")\n",
    "    raise\n",
    "\n",
    "class AnimalShelter:\n",
    "    def __init__(self, collection):\n",
    "        self.collection = collection\n",
    "\n",
    "    def create(self, data):\n",
    "        try:\n",
    "            self.collection.insert_one(data)\n",
    "            logging.info(\"Document inserted successfully\")\n",
    "            return True\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Failed to insert document: {e}\")\n",
    "            return False\n",
    "\n",
    "    def read(self, query):\n",
    "        try:\n",
    "            result = self.collection.find(query)\n",
    "            logging.info(\"Query executed successfully\")\n",
    "            return result\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Failed to execute query: {e}\")\n",
    "            return str(e)\n",
    "\n",
    "    def update(self, query, data):\n",
    "        try:\n",
    "            update_result = self.collection.update_many(query, {'$set': data})\n",
    "            logging.info(f\"Documents updated: {update_result.modified_count}\")\n",
    "            return True\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Failed to update documents: {e}\")\n",
    "            return str(e)\n",
    "\n",
    "    def delete(self, query):\n",
    "        try:\n",
    "            delete_result = self.collection.delete_many(query)\n",
    "            logging.info(f\"Documents deleted: {delete_result.deleted_count}\")\n",
    "            return True\n",
    "        except Exception as e:\n",
    "            logging.error(f\"Failed to delete documents: {e}\")\n",
    "            return str(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "364fdac1-2bbc-4699-92a6-68cae3a08ed0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:root:Document inserted successfully\n",
      "INFO:root:Animal added successfully\n",
      "INFO:root:Query executed successfully\n",
      "INFO:root:Documents updated: 1\n",
      "INFO:root:Animal updated successfully\n",
      "INFO:root:Documents deleted: 0\n",
      "INFO:root:Animal deleted successfully\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': ObjectId('66b003eebb6f23fb2fb546bc'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b0044cbb6f23fb2fb546be'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b00464bb6f23fb2fb546c0'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b0056ebb6f23fb2fb546c2'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b00574bb6f23fb2fb546c4'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b005cbbb6f23fb2fb546c6'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b005e6bb6f23fb2fb546c7'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b005f8bb6f23fb2fb546c8'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b0060bbb6f23fb2fb546c9'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b0061cbb6f23fb2fb546ca'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b00626bb6f23fb2fb546cb'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b00645bb6f23fb2fb546cc'), 'name': 'Buddy', 'species': 'Dog'}\n",
      "{'_id': ObjectId('66b00658bb6f23fb2fb546cd'), 'name': 'Fido', 'species': 'Dog'}\n"
     ]
    }
   ],
   "source": [
    "\n",
    "animal_shelter = AnimalShelter(collection)\n",
    "\n",
    "# Example usage:\n",
    "animal_data = {\"name\": \"Fido\", \"species\": \"Dog\"}\n",
    "if animal_shelter.create(animal_data):\n",
    "    logging.info(\"Animal added successfully\")\n",
    "\n",
    "query = {\"species\": \"Dog\"}\n",
    "result = animal_shelter.read(query)\n",
    "for animal in result:\n",
    "    print(animal)\n",
    "\n",
    "update_query = {\"species\": \"Dog\"}\n",
    "update_data = {\"name\": \"Buddy\"}\n",
    "if animal_shelter.update(update_query, update_data):\n",
    "    logging.info(\"Animal updated successfully\")\n",
    "\n",
    "delete_query = {\"species\": \"Cat\"}\n",
    "if animal_shelter.delete(delete_query):\n",
    "    logging.info(\"Animal deleted successfully\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "160ac1c0-e572-4793-8a99-ed0e98b8e0b3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
