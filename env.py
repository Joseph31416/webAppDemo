import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
TYPE = os.environ.get("TYPE")
PROJECT_ID = os.environ.get("PROJECT_ID")
PRIVATE_KEY_ID = os.environ.get("PRIVATE_KEY_ID")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
CLIENT_EMAIL = os.environ.get("CLIENT_EMAIL")
CLIENT_ID = os.environ.get("CLIENT_ID")
AUTH_URI = os.environ.get("AUTH_URI")
TOKEN_URI = os.environ.get("TOKEN_URI")
AUTH_PROVIDER_x509_CERT_URL = os.environ.get("AUTH_PROVIDER_x509_CERT_URL")
CLIENT_x509_CERT_URL = os.environ.get("CLIENT_x509_CERT_URL")
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
CLOUD_PROJECT = os.environ.get("CLOUD_PROJECT")
MODEL_NAME = os.environ.get("MODEL_NAME")
VERSION_NAME = os.environ.get("VERSION_NAME")
REGION = os.environ.get("REGION")
