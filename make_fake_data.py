from dotenv import load_dotenv, find_dotenv
import os
import certifi
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://i0dev:{password}@cluster0.gxz66kc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

doctors_db = client.doctors
doctors_collection = doctors_db.doctors_collection


doctor = {
    "first_name": "Alex",
    "last_name": "Iliarski",
    "age": 20,
    "gender": "MALE",
    "specialty": "SURGEON",
    "available": True,
    "address": {
        "street": "500 SE Harvard St",
        "city": "Minneapolis",
        "state": "MN",
        "zip": "55455",
    },
    "insurance_accepted": ["ALLIANZ"],
    "phone": "612-257-1776",
    "email": "alexiliarski@gmail.com",
    "avatar_url": "https://cdn.discordapp.com/attachments/1078854245866016848/1081788370084167780/Screenshot_2023-03-04_at_10.00.42_PM.png",
    "languages": ["ENGLISH"],
    "pronouns": ["he", "him"],
    "degree": "MD",
    "years_of_experience": 5,
    "college": "University of University",
}


def insert_doctor(doctor):
    collection = doctors_collection
    inserted_id = collection.insert_one(doctor).inserted_id
    print(inserted_id)


insert_doctor(doctor)
