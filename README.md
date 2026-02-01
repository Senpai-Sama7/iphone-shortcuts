# JARVIS iOS Shortcuts

One-click installer for JARVIS voice commands, photo analysis, and Apple Watch integration.

## 🚀 Deploy to GitHub Pages (Free HTTPS)

### Step 1: Create GitHub Repo
1. Go to https://github.com/new
2. Name: `jarvis-shortcuts`
3. Make it **Public**
4. Click **Create repository**

### Step 2: Upload These Files
Upload all files from this folder to your new repo:
- `index.html`
- `shortcuts/` folder
- `.github/workflows/` folder

### Step 3: Enable GitHub Pages
1. In your repo, go to **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **root**
4. Click **Save**

### Step 4: Wait 2 Minutes
- GitHub will build and deploy
- Your URL: `https://yourusername.github.io/jarvis-shortcuts`

### Step 5: Open on iPhone
- Open the GitHub Pages URL in Safari
- Tap **"Install Shortcut"** buttons
- Works with HTTPS-Only enabled!

---

## 📱 What's Included

| Shortcut | Purpose |
|----------|---------|
| **Ask JARVIS** | Voice commands via Siri |
| **Send to JARVIS** | Ray-Ban photo analysis |
| **JARVIS Status** | Apple Watch complication |

---

## 🔧 Configuration

Edit these values in `index.html` before deploying:

```javascript
const JARVIS_IP = '172.20.1.30';  // Your 845 G8 IP
const JARVIS_TOKEN = 'ab25e2ddac40ff2ebb7f4594cf286b1fbda31c06f48ccc57';
```

Find your IP:
```bash
hostname -I
```

---

## 📧 Alternative: Email Method

Don't want GitHub? Email the files:

1. Attach these files to an email:
   - `shortcuts/ask-jarvis.shortcut`
   - `shortcuts/send-to-jarvis.shortcut`
   - `shortcuts/jarvis-status.shortcut`

2. Send to yourself

3. On iPhone, open email → tap attachment → "Open in Shortcuts"

---

## 🎯 After Installation

**Voice Commands:**
- "Hey Siri, Ask JARVIS what's the weather?"

**Ray-Ban Photos:**
- Take photo → Share → "Send to JARVIS"

**Apple Watch:**
- Tap JARVIS complication for instant status

---

## 🛠️ Troubleshooting

**"Can't connect to server"**
→ Your iPhone and 845 G8 must be on same WiFi
→ Update IP in index.html to match `hostname -I`

**"Untrusted shortcut"**
→ Settings → Shortcuts → Allow Untrusted Shortcuts

---

## 📝 Files in This Repo

```
jarvis-shortcuts/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Pages auto-deploy
├── shortcuts/
│   ├── ask-jarvis.shortcut
│   ├── send-to-jarvis.shortcut
│   └── jarvis-status.shortcut
├── index.html              # Main installer page
└── README.md               # This file
```

---

Made with 🤖 for JARVIS
