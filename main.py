from gmail_auth import authenticate_gmail
from email_reader import get_email_details
from todolist import create_task

def main():

    service = authenticate_gmail()

    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        maxResults=9
    ).execute()

    messages = results.get("messages", [])

    for msg in messages:

        subject, sender, body = get_email_details(
            service, msg["id"]
        )

        if "ALERT" in subject.upper():
            create_task(subject, sender, body)
            print("ALERT detected:", subject)
        else:
            print("Ignored:", subject)

    print("\nAutomation completed successfully!")

if __name__ == "__main__":
    main()