# Google Drive API Quick Connect

Simple Python script to connect to Google Drive API.

## Setup

1. Create `.env` file from template:

```bash
touch .env
```

2. Edit `.env` and set your client secret filename:

```
CLIENT_SECRET_FILE=your_client_secret_file.json
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python gdrive_connect.py
```

5. On first run, it will open your browser for OAuth authentication. After that, credentials are saved in `token.pickle` for future use.

## Usage

The script connects to Google Drive and lists the first 10 files as a demo. You can modify the `main()` function to add your own functionality.

## Permissions

Current scope: `drive.readonly` (read-only access)

- To modify files, change SCOPES to `['https://www.googleapis.com/auth/drive']`
- After changing scopes, delete `token.pickle` to re-authenticate
