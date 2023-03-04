from doctor_handler import Speciality, Gender, Insurence, Language
from dotenv import load_dotenv, find_dotenv
import os
import pprint
import certifi
from pymongo import MongoClient

zip_code = 55345
within_miles = 15
specialization = Speciality.GENERAL_PRACTITIONER
years_of_experience = 3
insurence = Insurence.ALINA_HEALTH
language = Language.ENGLISH
gender = Gender.MALE


query = {
    "specialization": specialization.name,
    "years_of_experience": {"$gte": years_of_experience},
    "insurence": insurence.name,
    "language": language.name,
    "gender": gender.name,
}


# todo search for doctors in a given zip code

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://i0dev:{password}@cluster0.gxz66kc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string, tlsCAFile=certifi.where())

doctors_db = client.doctors
doctors_collection = doctors_db.doctors_collection


def get_doctors_with_query(query):
    return doctors_collection.find(query)


printer = pprint.PrettyPrinter(indent=4)

for doctor in get_doctors_with_query(query):
    printer.pprint(doctor)