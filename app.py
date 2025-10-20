from flask import Flask, request, jsonify
import os, jwt, time, requests, hmac, hashlib
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Configs
GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
PRIVATE_KEY_PATH = os.getenv("GITHUB_PRIVATE_KEY_PATH")

# Read private key
PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY")
if not PRIVATE_KEY and PRIVATE_KEY_PATH:
    try:
        with open(PRIVATE_KEY_PATH, "r") as f:
            PRIVATE_KEY = f.read()
    except FileNotFoundError:
        print(f"Warning: Private key file {PRIVATE_KEY_PATH} not found.")
        print("Please set GITHUB_PRIVATE_KEY environment variable with the key content or ensure the file exists.")

def verify_signature(payload_body, signature_header):
    secret = WEBHOOK_SECRET.encode()
    expected = 'sha256=' + hmac.new(secret, payload_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header)

def generate_jwt():
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + (10 * 60),
        "iss": GITHUB_APP_ID
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

def get_installation_token(installation_id):
    headers = {
        "Authorization": f"Bearer {generate_jwt()}",
        "Accept": "application/vnd.github+json"
    }
    res = requests.post(f"https://api.github.com/app/installations/{installation_id}/access_tokens", headers=headers)
    return res.json()["token"]

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    if not verify_signature(request.data, signature):
        return "Invalid signature", 401

    event = request.headers.get("X-GitHub-Event")
    payload = request.json

    if event == "issues":
        action = payload["action"]
        issue = payload["issue"]
        installation_id = payload["installation"]["id"]

        if action == "opened":
            handle_new_issue(issue, installation_id)

    return jsonify({"status": "ok"})

def handle_new_issue(issue, installation_id):
    title = issue["title"].lower()
    body = issue["body"].lower() if issue["body"] else ""

    labels = []
    if "bug" in title or "error" in body:
        labels.append("bug")
    elif "feature" in title or "request" in body:
        labels.append("enhancement")
    elif "docs" in title or "documentation" in body:
        labels.append("documentation")

    token = get_installation_token(installation_id)
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}

    if labels:
        requests.post(
            issue["labels_url"],
            headers=headers,
            json={"labels": labels}
        )

    # Example auto assignment
    assignee = "YourGitHubUsername"
    requests.post(
        issue["url"] + "/assignees",
        headers=headers,
        json={"assignees": [assignee]}
    )

    print(f"Labeled & assigned issue #{issue['number']}")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
