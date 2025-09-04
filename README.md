# PHISH_SOUP 🚨

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![CLI Tool](https://img.shields.io/badge/cli-interactive-brightgreen)
![For Training Only](https://img.shields.io/badge/for%20training%20only-red)

> **Advanced tool for generating simulated phishing landing pages and email templates, with SMTP sending support.**

---

## 🚀 Features
- Custom HTML landing pages
- Password reset clones for:
  - Instagram
  - Facebook
  - Twitter
  - LinkedIn
  - TikTok
- Email template generator
- Send emails via SMTP (local/external)
- Interactive ASCII CLI menu

---

## 📋 Usage
1. Configure your SMTP service (`.env.example`)
2. Generate a landing page or email template from the CLI menu
3. Send test emails via SMTP

---

## 🕵️‍♂️ Available Landing Page Clones
| Social    | Type           | Output Suffix         |
|-----------|----------------|----------------------|
| Instagram | Login          | `_insta.html`        |
| Instagram | Password Reset | `_insta_pwreset.html`|
| Facebook  | Login          | `_fb.html`           |
| Facebook  | Password Reset | `_fb_pwreset.html`   |
| Twitter   | Password Reset | `_twitter_pwreset.html`|
| LinkedIn  | Password Reset | `_linkedin_pwreset.html`|
| TikTok    | Password Reset | `_tiktok_pwreset.html`|

---

## 📧 Example: Send Email via Gmail
1. Select "Send email" from the menu
2. Enter:
   - SMTP host: `smtp.gmail.com`
   - SMTP port: `465` (SSL) or `587` (TLS)
   - Sender: `your@gmail.com`
   - Recipient: `your@gmail.com` (or any target)
   - Subject/Body: as you wish
   - Use SMTP authentication: `y`
   - SMTP username: `your@gmail.com`
   - SMTP password: (App password recommended)
   - Use SSL/TLS: `y`

---

## ⚠️ Disclaimer
**For educational and simulation purposes only (HackTheBox, awareness, etc.)**

---

## 📚 License
MIT
