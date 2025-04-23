from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define OAuth scope
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

# Authenticate and get access token
def authenticate():
    creds = None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

    print(f"Access Token: {creds.token}")
    return creds.token

# Generate access token
access_token = authenticate()
print("Your access token:", access_token)
