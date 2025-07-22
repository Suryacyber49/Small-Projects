# 🔐 Web Login Brute Force Tool (Python)

A Python script that performs a brute-force login attack against a web form by testing multiple usernames and a password wordlist. Built for ethical hacking demonstrations and security research.

> ⚠️ **Disclaimer**: This script is for **educational and authorized penetration testing only**. Do **NOT** use it on systems you don't own or have permission to test.

---

## 📄 Description

This tool attempts to log in to a target web application by iterating through a list of usernames and passwords. It's useful for demonstrating insecure login mechanisms and the importance of strong credentials and rate-limiting.

---

## ✅ Features

- Uses Python's `requests` library for POST form submission
- Custom list of usernames and password wordlist support
- Displays real-time attempt feedback in terminal
- Identifies successful login based on keyword matching (e.g., “Logged In Successfully”)

---

## 🚀 Usage
You'll be prompted to enter the target login URL, for example:

website url: http://example.com/login

## 🧪 Example Output
[X] Attempting user:password -> student:123456

[X] Attempting user:password -> student:qwerty

[>>>>>] Valid password 'letmein' found for user 'user'!

## 🔧 Customization
Usernames list is hardcoded in the script:

usernames = ["student", "user", "test"]
Password file path:

password = r'F:\htlm\Hacking python\top100.txt'
Success keyword to match successful login:

needle = "Logged In Successfully"
Modify these variables as needed for your specific target.

### 🧱 Requirements
- Python 3.x
- `requests` module (install using `pip install requests`)

---

### ▶️ Run the Script

```bash
python web_login_bruteforce.py
