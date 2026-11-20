import base64

def get_email_details(service, message_id):

    message = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    headers = message["payload"]["headers"]

    subject = sender = ""

    for header in headers:
        if header["name"].lower() == "subject":
            subject = header["value"]

        elif header["name"].lower() == "from":
            sender = header["value"]

    def extract_body(payload):
        if payload.get("mimeType") == "text/plain":
            data = payload.get("body", {}).get("data")
            if data:
                return base64.urlsafe_b64decode(data).decode(
                    "utf-8", errors="replace"
                )

        for part in payload.get("parts", []):
            result = extract_body(part)
            if result:
                return result

        return ""

    body = extract_body(message["payload"])

    return subject, sender, body