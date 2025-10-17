#!/usr/bin/env python3
import os
import pickle
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")


def connect_to_drive():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                SCOPES,
            )
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)
    return service


def main():
    print("Connecting to Google Drive...")
    service = connect_to_drive()
    print("✓ Connected successfully!\n")

    print("First 10 files in your Drive:")
    results = (
        service.files().list(pageSize=10, fields="files(id, name, mimeType)").execute()
    )
    items = results.get("files", [])

    if not items:
        print("No files found.")
    else:
        for item in items:
            print(f"  • {item['name']} ({item['mimeType']})")

    return service


if __name__ == "__main__":
    main()
