# Email to Task Automation

A small Python script that watches your Gmail inbox, finds emails whose subject contains `ALERT`, and creates a high-priority Todoist task for each one.

## Features

- Authenticates with the Gmail API using OAuth 2.0 (credentials are cached in `token.pickle`).
- Reads the subject, sender, and plain-text body of recent inbox messages.
- Creates a Todoist task with the subject as the title and the sender/body as the description.
- Prints which emails were processed and which were ignored.

## Requirements

- Python 3.x
- A Google Cloud project with the Gmail API enabled and an OAuth client ID (`credentials.json`)
- A Todoist API token

Python packages used:

- `google-api-python-client`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `python-dotenv`
- `requests`

## Setup

1. Clone/download this repository and create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

2. Install the dependencies:

   ```bash
   pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 python-dotenv requests
   ```

   (You can also add them to `requirements.txt` and run `pip install -r requirements.txt`.)

3. Add your Google OAuth `credentials.json` file to the project root. On the first run a browser window opens for Gmail authorization; the resulting token is saved to `token.pickle` for future runs.

4. Create a `.env` file in the project root with your Todoist token:

   ```env
   TODOIST_API_TOKEN=your_token_here
   ```

## Usage

Run the automation from the project root:

```bash
python main.py
```

By default it checks the 9 most recent messages in `INBOX`. Any email with `ALERT` in the subject (case-insensitive) becomes a Todoist task; all others are reported as ignored.

## Project Structure

- `main.py` - entry point; lists inbox messages and dispatches alerts
- `gmail_auth.py` - Gmail OAuth authentication and service setup
- `email_reader.py` - extracts subject, sender, and body from a message
- `todolist.py` - creates tasks through the Todoist REST API
- `config.py` - loads the Todoist token from the `.env` file
- `test_gmail.py`, `test_reader.py`, `test_todoist.py` - quick connectivity checks

## Notes

- Credentials and tokens (`credentials.json`, `token.pickle`, `token.json`, `.env`) are gitignored and should never be committed.
- The Gmail scope used is read-only; the script does not modify your mailbox.
