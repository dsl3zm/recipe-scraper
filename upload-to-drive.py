import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
# using drive.file scope allows access only to files created or opened by the app.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def get_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists("credentials.json"):
                print("Error: 'credentials.json' not found.")
                print("Please download your OAuth 2.0 Client ID JSON from the Google Cloud Console,")
                print("rename it to 'credentials.json', and place it in this directory.")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8099)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_or_create_folder(service, folder_name):
    # Search for the folder
    # Note: With drive.file scope, this only finds folders created by this app.
    query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])

    if not items:
        # Create folder
        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder"
        }
        file = service.files().create(body=file_metadata, fields="id").execute()
        print(f"Created folder '{folder_name}' with ID: {file.get('id')}")
        return file.get("id")
    else:
        print(f"Found folder '{folder_name}' with ID: {items[0].get('id')}")
        return items[0].get("id")

def main():
    creds = get_credentials()
    if not creds:
        return

    try:
        service = build("drive", "v3", credentials=creds)
        
        folder_id = get_or_create_folder(service, "Recipes")
        
        recipes_dir = os.path.join(os.path.dirname(__file__), "recipes")
        if not os.path.exists(recipes_dir):
            print(f"No recipes directory found at {recipes_dir}")
            return

        files = os.listdir(recipes_dir)
        if not files:
             print("No files found in recipes directory.")
             return

        for filename in files:
            file_path = os.path.join(recipes_dir, filename)
            if os.path.isfile(file_path) and not filename.startswith('.'):
                print(f"Uploading {filename}...")
                
                file_metadata = {
                    "name": filename,
                    "parents": [folder_id]
                }
                
                media = MediaFileUpload(file_path, mimetype="application/json")
                
                file = (
                    service.files()
                    .create(body=file_metadata, media_body=media, fields="id")
                    .execute()
                )
                print(f"Uploaded File ID: {file.get('id')}")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()