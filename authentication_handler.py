from env import TYPE, PROJECT_ID, PRIVATE_KEY_ID, PRIVATE_KEY, CLIENT_EMAIL, CLIENT_ID, AUTH_URI, \
    TOKEN_URI, AUTH_PROVIDER_x509_CERT_URL, CLIENT_x509_CERT_URL, GOOGLE_APPLICATION_CREDENTIALS
import json
import os


def create_creds():
    output = {
        "type": TYPE,
        "project_id": PROJECT_ID,
        "private_key_id": PRIVATE_KEY_ID,
        "private_key": PRIVATE_KEY.replace('\\n', '\n'),
        "client_email": CLIENT_EMAIL,
        "client_id": CLIENT_ID,
        "auth_uri": AUTH_URI,
        "token_uri": TOKEN_URI,
        "auth_provider_x509_cert_url": AUTH_PROVIDER_x509_CERT_URL,
        "client_x509_cert_url": CLIENT_x509_CERT_URL
    }
    with open(GOOGLE_APPLICATION_CREDENTIALS, "w") as f:
        json.dump(output, f)


def clear_creds():
    os.remove(GOOGLE_APPLICATION_CREDENTIALS)


