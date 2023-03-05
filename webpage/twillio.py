from twilio.rest import Client
from query import get_doc_by_id
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

sid = os.environ.get("TWILIO_ACOUNT_ID")
token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(sid, token)


def message_doc(doc_id, message):
    doctor = get_doc_by_id(doc_id)
    client.messages.create(
        body=message,
        from_="+13159037882",
        to="+1" + doctor["phone"],
    )


message_doc("6403ce94cfc8fce87221aab2", "Hello, this is a test message")
