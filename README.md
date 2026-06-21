<div align="center">
  <img src="https://raw.githubusercontent.com/imramflow/Tchekly/master/src/tchekly/web/static/img/logo.svg" width="80" alt="Tchekly Logo">
  <h1 align="center">⚡ Tchekly</h1>
  <p align="center"><strong>Email Checker & Management Tool — Windows Desktop App</strong></p>
  <p align="center">
    <a href="#-download"><img src="https://img.shields.io/badge/Download-Latest%20Build-00d4ff?style=for-the-badge&logo=windows&logoColor=white"></a>
    <a href="#-features"><img src="https://img.shields.io/badge/Features-Overview-a78bfa?style=for-the-badge"></a>
  </p>
  <br>
</div>

---

## 📥 Download

| Version | Link | Size |
|---------|------|------|
| **Latest Build** | [⬇️ Download tchekly.exe](https://github.com/imramflow/Tchekly-Download/releases/latest/download/tchekly.exe) | ~50 MB |
| All Releases | [View All Releases →](https://github.com/imramflow/Tchekly-Download/releases) | |

> 💡 **Note:** Windows might show SmartScreen warning — click **"More info" → "Run anyway"**. This is normal for unsigned apps.

### System Requirements

| Component | Requirement |
|-----------|-------------|
| OS | Windows 10 / Windows 11 (64-bit) |
| RAM | 2 GB minimum |
| Storage | 200 MB free |
| WebView2 | Auto-installs if missing (requires internet) |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Email Validation** | Check IMAP credentials with proxy support (SOCKS4/5, HTTP) |
| **Bulk Checker** | Validate thousands of emails with multi-threading + stop/resume |
| **Clean List** | Deduplicate, format validation, remove invalid formats |
| **Read Emails** | Preview last 10 emails from any inbox |
| **DOB Detection** | Extract date of birth from email headers & content |
| **Profile Intel** | Extract name, phone, address, social accounts, financial data |
| **SMTP Detect** | Auto-detect SMTP settings per email domain |
| **Keyword Search** | Search inbox for specific keywords + save matches |
| **Free Proxy Fetcher** | Built-in tool to fetch free proxies from 20+ sources |
| **Dark Desktop UI** | Native frameless window with custom titlebar, glass effects |
| **In-App Tabs** | Browse external links inside the app without leaving |
| **Remote Config** | Banners, announcements, settings update without reinstalling |

---

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

### 🧹 How to Clean a List

```
Step 1: Click "Clean List" from the sidebar
Step 2: Upload your email list file
Step 3: Choose options (remove duplicates, validate format)
Step 4: Click "Clean"
Step 5: Download the cleaned result file
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
| **Permissions** | 🔐 `results/` = `700`, files = `600` |
| **Network** | 🚫 Web GUI binds to `127.0.0.1` only (localhost) |
| **Remote config** | 🌐 Fetches banners/config from GitHub only (no tracking) |

---

## ❓ FAQ

**Q: Does it work on Linux or Mac?**
A: No. This is a Windows-only desktop application (pywebview frameless window).

**Q: Can I use it offline?**
A: Some features work offline (cleaning lists, formatting). Email checking requires internet.

**Q: Why does SmartScreen block the .exe?**
A: The .exe uses PyArmor obfuscation + PyInstaller bundling. It's not code-signed. Click **"More info" → "Run anyway"** — it's safe.

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

<div align="center">
  <br>
  <p>Developed by <strong>Ramflow</strong></p>
  <p>Built with Python · PyArmor · PyInstaller · pywebview · Flask</p>
  <br>
  <p>
    <a href="https://github.com/imramflow/Tchekly-Download/releases"><img src="https://img.shields.io/github/v/release/imramflow/Tchekly-Download?color=00d4ff&label=Latest&logo=github"></a>
    <a href="https://github.com/imramflow/Tchekly-Download/releases/latest/download/tchekly.exe"><img src="https://img.shields.io/badge/Download-.exe-22c55e?logo=windows&logoColor=white"></a>
  </p>
  <br>
</div>
