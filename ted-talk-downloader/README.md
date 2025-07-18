# 🎥 TED Talk Downloader

A Python script to download TED Talk videos by parsing their embedded video URLs.

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
🚀 Usage
bash
Copy
Edit
python ted_downloader.py "https://www.ted.com/talks/nada_majdalani_the_power_of_youth_in_palestine"
The video will be downloaded and saved in the current directory.

🛑 Note
If the video fails to download (403 or Access Denied), it's likely due to TED's temporary restrictions or requiring signed URLs. In such cases, try again later.

📁 Output
The script downloads the highest-quality .mp4 file it can find.

Filename is automatically extracted from the URL.

🧪 Tested With
Python 3.8+

TED Talk video URLs

⭐ Feel free to fork or contribute!

yaml
Copy
Edit

---

### ✅ Steps to Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: TED Talk downloader script"
gh repo create ted-downloader --public --source=. --remote=origin --push