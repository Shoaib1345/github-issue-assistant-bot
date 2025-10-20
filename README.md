```markdown
# 🤖 GitHub Issue Assistant Bot

An intelligent GitHub App built with **Flask + GitHub Webhooks** that automatically labels, assigns, and manages issues in your repositories.

---

## 🚀 Features

✅ Automatically detects keywords in issue titles/descriptions  
✅ Adds relevant labels (`bug`, `enhancement`, `documentation`)  
✅ Assigns issues to a default user (``)  
✅ Uses **GitHub App authentication (JWT + installation tokens)**  
✅ Easy to deploy on Render, Railway, or GCP  

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Flask**
- **GitHub REST API**
- **GitHub Webhooks**
- **PyJWT**
- **Dotenv**

---

## 📦 Project Structure

```

github-issue-assistant-bot/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── private-key.pem           # Private key from GitHub App
└── README.md                 # Documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shoaib1345/github-issue-assistant-bot.git
cd github-issue-assistant-bot
````

---

### 2️⃣ Create a GitHub App

1. Go to [https://github.com/settings/apps](https://github.com/settings/apps)
2. Click **"New GitHub App"**
3. Fill in:

   * **GitHub App name:** `github-issue-assistant-bot`
   * **Homepage URL:** `https://example.com`
   * **Webhook URL:** `http://localhost:5000/webhook`
   * **Webhook Secret:** choose a random string (e.g. `mysecret123`)
4. Under **Repository permissions:**

   * Issues → Read and Write
   * Metadata → Read-only
5. Subscribe to events:

   * `Issues`
   * `Meta`
6. Click **Create GitHub App**
7. Scroll down and **Generate a Private Key**

---

### 3️⃣ Save the Private Key

Download the `.pem` file from your GitHub App and rename it:

```
private-key.pem
```

Then move it inside your project folder.

---

### 4️⃣ Create `.env` File

Create a `.env` file in your project directory and fill in:

```env
GITHUB_APP_ID=
WEBHOOK_SECRET=
REPO_OWNER=
REPO_NAME=
GITHUB_PRIVATE_KEY_PATH=
```
---

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
Flask
python-dotenv
PyJWT
requests
```

---

### 6️⃣ Run the Flask App

```bash
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000/
```

---

### 7️⃣ Expose Local Server to GitHub

Since GitHub can’t reach localhost directly, use **ngrok**:

```bash
ngrok http 5000
```

Copy the **Forwarding URL** (e.g. `https://abcd1234.ngrok.io`)
→ Go back to your GitHub App settings and update the **Webhook URL**:

```
https://abcd1234.ngrok.io/webhook
```

---

### 8️⃣ Install Your App

On your GitHub App’s page:

* Click **Install App**
* Choose your account (``)
* Install it on your test repository

---

### 9️⃣ Test It 🚀

1. Open a new **Issue** in your test repository.
2. Try titles like:

   * `Bug: API returning 500`
   * `Feature request: add AI mode`
3. Your bot will:

   * Add labels (e.g. `bug`, `enhancement`)
   * Assign it to ``

Terminal output:

```
Labeled & assigned issue #1
```

---

## 🧩 Example Output

**Issue title:** “Feature request: add dark mode”
✅ Label added: `enhancement`
✅ Assigned to: ``

---

## 🛠️ Deployment (Optional)

You can deploy easily on:

* [Render](https://render.com/)
* [Railway](https://railway.app/)
* [Google Cloud Run](https://cloud.google.com/run)

Just set the same environment variables in your hosting dashboard.

---

## 📜 License

MIT License — free to use and modify.

---

## 👨‍💻 Author

**Shoaib Ahmed**
📧 Email: [shoaibahmedprogramming@gmail.com](mailto:shoaibahmedprogramming@gmail.com)
🌐 GitHub: [@shoaib1345](https://github.com/shoaib1345)

---

## 💡 Future Improvements

* Auto-close stale issues
* Reply with helpful comments
* Support multiple assignees
* Add slash-command support

---

**Made with ❤️ by [Shoaib Ahmed](https://github.com/shoaib1345)**



Would you like me to generate the **matching `requirements.txt`** and **`.env.example`** files too, so your repository is 100% ready to push to GitHub?
```
