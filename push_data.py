import os
import sys
import pandas as pd
import pymongo
import certifi

from dotenv import load_dotenv

from networksecurity.exception.exception import NetwokSecurityException


load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

ca = certifi.where()


class NetworkDataExtract:

    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetwokSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):

        try:
            # Read CSV
            data = pd.read_csv(file_path)

            # Reset index
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame into list of dictionaries
            records = data.to_dict(orient="records")

            return records

        except Exception as e:
            raise NetwokSecurityException(e, sys)

    def insert_data(self, records, database, collection):

        try:
            self.records = records

            # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=ca
            )

            # Select database
            self.database = self.mongo_client[database]

            # Select collection
            self.collection = self.database[collection]

            # Insert records
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetwokSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "SALMAN"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()

    # CSV → List of dictionaries
    records = networkobj.csv_to_json_converter(FILE_PATH)

    print(f"Total records: {len(records)}")

    # Insert into MongoDB
    no_of_records = networkobj.insert_data(
        records,
        DATABASE,
        COLLECTION
    )

    print(f"Inserted records: {no_of_records}")


