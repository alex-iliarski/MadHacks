from webpage.doctor_handler import Speciality, Gender, Insurence, Language
from dotenv import load_dotenv, find_dotenv
import os
from webpage.dist import distance
import pprint
import certifi
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://i0dev:{password}@cluster0.gxz66kc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

doctors_db = client.doctors
doctors_collection = doctors_db.doctors_collection


def find_doctors(
    zip_code,
    within_miles=50,
    specialization=Speciality.GENERAL_PRACTITIONER,
    years_of_experience=3,
    insurence=Insurence.ALINA_HEALTH,
    language=Language.ENGLISH,
    gender=Gender.MALE,
):
    query = {
        "specialty": specialization.name,
        "years_of_experience": {"$gte": years_of_experience},
        "insurance_accepted": insurence.name,
        "languages": language.name,
        "gender": gender.name,
    }
    docs = []
    for doctor in doctors_collection.find(query):
        if distance(zip_code, doctor["address"]["zip_code"]) <= within_miles:
            docs.append(doctor)
    return docs


# printer = pprint.PrettyPrinter(indent=4)

# for doctor in find_doctors("53792", within_miles=10):
#     printer.pprint(doctor)
