import requests
from config import TODOIST_API_TOKEN

def create_task(subject, sender, body):

    url = "https://api.todoist.com/api/v1/tasks"

    headers = {
        "Authorization": f"Bearer {TODOIST_API_TOKEN}"
    }

    data = {
        "content": subject,
        "description": f"Sender: {sender}\n\nEmail:\n{body}",
        "priority": 4
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code in (200, 201):
        print("Task created:", subject)
    else:
        print("Task creation failed:", response.status_code, response.text)