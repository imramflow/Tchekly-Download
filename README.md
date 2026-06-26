<div align="center">
  <img src="https://raw.githubusercontent.com/imramflow/Tchekly-Download/main/docs/logo.svg" width="80" alt="Tchekly Logo">
  <h1 align="center">⚡ Tchekly</h1>
  <p align="center"><strong>Email Checker & Management Tool — Windows & Android App</strong></p>
  <p align="center">
    <a href="#-download"><img src="https://img.shields.io/badge/Download-Latest%20Build-00d4ff?style=for-the-badge&logo=windows&logoColor=white"></a>
    <a href="#-features"><img src="https://img.shields.io/badge/Features-Overview-a78bfa?style=for-the-badge"></a>
  </p>
  <br>
</div>

---

## 📥 Download

| Version | Link | Size | SHA-256 Checksum |
|---------|------|------|------------------|
| **Windows** | [⬇️ Download tchekly.exe](https://github.com/imramflow/Tchekly-Download/releases/latest/download/tchekly.exe) | ~26 MB | `6d3e87845b061642fc2df826fc4832a4d98ce528893c14be920393f7fd0de345` |
| **Android** | [⬇️ Download Tchekly.apk](https://github.com/imramflow/Tchekly-Download/releases/latest/download/Tchekly.apk) | ~48 MB | `e6170dbd3dfb8dbf82f0a550f706e553fd7723f157cc303c146d3f479a86625d` |

> 💡 **Verification:** After downloading, verify the file with:
> - **Windows:** `certutil -hashfile tchekly.exe SHA256`
> - **Android/Linux:** `sha256sum Tchekly.apk`
> 
> Compare the output with the checksum above. If they match, the file is intact.
> 
> ⚠️ **Note:** Windows might show SmartScreen warning for unsigned apps — this is normal. Verify the SHA-256 checksum above before running, then click **"More info" → "Run anyway"**.

### System Requirements

| Component | Requirement |
|-----------|-------------|
| **Windows** | Windows 10/11 (64-bit), 2 GB RAM, 200 MB free |
| **Android** | Android 8+ (API 26+), arm64-v8a, 100 MB free |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Email Validation** | Check IMAP credentials with proxy support (SOCKS4/5, HTTP) |
| **Bulk Checker** | Validate thousands of emails with multi-threading + pause/resume/stop |
| **Read Emails** | Preview last 10 emails from any inbox |
| **DOB Detection** | Extract date of birth from email headers & content |
| **Profile Intel** | Extract name, phone, address, social accounts, financial data |
| **SMTP Detect** | Auto-detect SMTP settings per email domain |
| **Keyword Search** | Search inbox for specific keywords + save matches |
| **Free Proxy Fetcher** | Built-in tool to fetch free proxies from 20+ sources |
| **Pro Settings** | Configurable performance, filters, network, notifications & security |
| **Dark Desktop UI** | Native frameless window with custom titlebar, glass effects |


## 🚀 Quick Start Guide

### ▶️ First Run

1. **Download** the latest `tchekly.exe` from the table above
2. **Double-click** to run — the app opens in a native desktop window
3. **Splash screen** appears briefly, then the dashboard loads
4. You get **3 days free trial** to test all features

### 📧 How to Check Emails

```
Step 1: Click "Check Emails" from the sidebar
Step 2: Upload a .txt file with emails (format: email:password, one per line)
Step 3: (Optional) Upload a proxy list or use auto-fetch
Step 4: (Optional) Enter keywords to search inside inboxes
Step 5: Click "Start Checking"
─────────────────────────────────────────────────
Results save automatically to:
  → results/good_emails/valid_emails.txt
  → results/keyword_matches/matches.txt
```

### 📨 How to Read Emails

```
Step 1: Click "Read Email" from the sidebar
Step 2: Enter email:password
Step 3: (Optional) Add a proxy
Step 4: Click "Read"
Step 5: Browse the last 10 emails in the built-in email reader
```

### 🧠 How to Use Profile Intel

```
Step 1: Click "Profile Intel" from the sidebar
Step 2: Enter email:password
Step 3: (Optional) Add a proxy
Step 4: Click "Extract Intelligence"
Step 5: View extracted data: name, phone, address, accounts, social links
         → Full report saved in results/intel/
```

### 🔑 License

| Period | Price | Payment |
|--------|-------|---------|
| Trial | **Free** — 3 days | Automatic on first run |
| License | **$8 USDT/month** | NOWPayments (USDT BSC/BEP20) |

Buy/Renew from the **License** page inside the app.

---

## ⚙️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+I` | Open DevTools (for debugging) |
| `Ctrl+W` | Close active in-app tab |
| `Ctrl+Tab` | Switch between open tabs |

---

## 🔧 Proxy Support

| Type | Format Example |
|------|---------------|
| HTTP | `http://user:pass@1.2.3.4:8080` |
| SOCKS4 | `socks4://1.2.3.4:1080` |
| SOCKS5 | `socks5://user:pass@1.2.3.4:1080` |

**Auto-fetch:** Leave proxy field empty and check "Fetch free proxies" to get working proxies automatically.

---

## 📁 Output Files

All results are saved in the `results/` folder (next to the .exe):

| File | Contents |
|------|----------|
| `results/good_emails/valid_emails.txt` | ✅ Valid email:password pairs |
| `results/keyword_matches/matches.txt` | 🔍 Emails matching your keywords |
| `results/intel/*.txt` | 🧠 Full intelligence reports |
| `results/.secret_key` | 🔐 Auto-generated Flask secret key |

> 🔒 All result files: permission `600` (owner read/write only)

---

## 🛡️ Privacy & Security

| Feature | Detail |
|---------|--------|
| **Data collection** | ❌ None — the app does not phone home |
| **Processing** | 💻 100% local — nothing leaves your machine |
| **Logging** | 📝 Email addresses only — passwords never logged |
| **Network** | 🚫 Web GUI binds to `127.0.0.1` only (localhost) |

---

## ❓ FAQ

**Q: Does it work on Linux, Mac, or Android?**
A: Tchekly runs on Windows 10/11 (64-bit) and **Android 8+**. Linux and Mac are not supported.

**Q: Can I use it offline?**
A: Some features work offline (cleaning lists, formatting). Email checking requires internet.

**Q: Why does SmartScreen block the .exe?**
A: The app is not code-signed. Verify the SHA-256 checksum from the download table, then click **"More info" → "Run anyway"**.

**Q: How do I update?**
A: Just download the latest `.exe` and replace your old one. Your license and config are preserved.

**Q: My license expired, how do I renew?**
A: Open the License page in the app and click "Renew License" — pay with USDT.

**Q: Where are my results saved?**
A: In the `results/` folder next to `tchekly.exe`.

**Q: Can I run multiple instances?**
A: Yes, but they share the same results folder.

---

## 📞 Support & Contact

| Channel | Link |
|---------|------|
| 💬 Telegram | [@tcheklyy](https://t.me/tcheklyy) |
| 🐛 Report Issues | [GitHub Issues](https://github.com/imramflow/Tchekly-Download/issues) |

---

---

> **Tchekly** is proprietary software. All rights reserved © 2026 Ramflow.
> You may download and use the compiled `.exe` for personal use only.
> Redistribution, modification, or reverse engineering is prohibited.

<div align="center">
  <br>
  <p>Developed by <strong><a href="https://github.com/imramflow">Ramflow</a></strong></p>

  <br>
  <p>
    <a href="https://imramflow.github.io/Tchekly-Download/"><img src="https://img.shields.io/badge/Website-Visit-00d4ff?logo=github-pages&logoColor=white"></a>
    <a href="https://github.com/imramflow/Tchekly-Download/releases/latest/download/tchekly.exe"><img src="https://img.shields.io/badge/Download-.exe-22c55e?logo=windows&logoColor=white"></a>
    <a href="https://github.com/imramflow/Tchekly-Download/releases/latest/download/Tchekly.apk"><img src="https://img.shields.io/badge/Download-.apk-22c55e?logo=android&logoColor=white"></a>
  </p>
  <br>
</div>
