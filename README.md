# 🤖 Automation with Python

This repository contains a collection of Python scripts that automate everyday tasks. Each automation script is organized in its own folder with descriptions and setup instructions.

---

## 📁 Folder Structure

```

automation-with-python/
├── hacker-news-email/
│   ├── hackerNews.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
├── ted-talk-downloader/
│   ├── downloader.py
│   ├── requirements.txt
│   └── README.md

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-with-python.git
cd automation-with-python
````

### 2. Navigate to any script folder

```bash
cd hacker-news-email
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file and add necessary keys (refer to `.env.example` if available).

### 5. Run the script

```bash
python hackerNews.py
```

---
## 🧰 Available Scripts

| Folder               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `hacker-news-email`  | Sends top Hacker News stories to your email daily using the HN API          |
| `table-from-pdf`     | Extracts tables from a PDF using Camelot and visualizes data with Seaborn   |
| `ted-talk-downloader`| Downloads TED Talks using `youtube_dl` by scraping TED video URLs           |


## 🔐 Environment Variables

Some scripts require credentials (e.g., email, phone). Use a `.env` file to store them securely.

Example:

```
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password
```

Make sure to add `.env` to `.gitignore` to avoid pushing secrets.

---

## 👤 Author

**Shagun Gupta**
GitHub: [@Shagungupta7](https://github.com/Shagungupta7)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Contributing

Want to add more scripts? Fork the repo, add your folder, and create a pull request. Contributions are welcome!

```

---

### ✅ What to do next:
- Replace `your-username` with your actual GitHub username.
- Customize/add more folders if needed.
- Create `.env.example` files where applicable.

Let me know if you'd like help setting up one of the script sub-`README.md` files too!
```
