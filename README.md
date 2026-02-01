# 🤖 JARVIS iOS Shortcuts

**One-click installer for JARVIS voice commands, photo analysis, and Apple Watch integration.**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://senpai-sama7.github.io/iphone-shortcuts)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

### Live Installation

**Your installer is already live at:**
👉 **[https://senpai-sama7.github.io/iphone-shortcuts](https://senpai-sama7.github.io/iphone-shortcuts)**

1. Open the URL above on your iPhone in Safari
2. Update the IP address to match your JARVIS server
3. Tap **"Install Shortcut"** for each shortcut you want
4. Allow installation when prompted

---

## 📱 What's Included

| Shortcut | Purpose | How to Use |
|----------|---------|------------|
| **🎤 Ask JARVIS** | Voice commands via Siri | "Hey Siri, Ask JARVIS what's the weather?" |
| **📸 Send to JARVIS** | Ray-Ban photo analysis | Take photo → Share → "Send to JARVIS" |
| **⌚ JARVIS Status** | Apple Watch complication | Tap complication for instant status |

---

## 🔧 Configuration

### Find Your JARVIS Server IP

On your JARVIS server (HP 845 G8), run:

```bash
hostname -I
```

Or check your router's DHCP leases for the device.

### Update Shortcuts

**Method 1: Via Web Interface (Easiest)**
1. Open [https://senpai-sama7.github.io/iphone-shortcuts](https://senpai-sama7.github.io/iphone-shortcuts) on iPhone
2. Enter your server IP in the configuration box
3. Click "Update Install Links"
4. Install shortcuts with updated IP

**Method 2: Edit After Installation**
1. Install shortcuts from the web page
2. Open Shortcuts app on iPhone
3. Find each JARVIS shortcut
4. Edit the "Get URL" action
5. Update IP address from `172.20.1.30` to your server IP

### Security Token

The default token in the shortcuts is:
```
ab25e2ddac40ff2ebb7f4594cf286b1fbda31c06f48ccc57
```

**🔒 For production use, generate a new token on your JARVIS server and update the shortcuts.**

---

## 🛠️ Repository Setup (For Developers)

### Forking and Customization

1. **Fork this repository**
   ```bash
   # Or click "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/iphone-shortcuts.git
   cd iphone-shortcuts
   ```

3. **Customize settings**
   - Edit `index.html` to update default IP and token
   - Modify shortcut files in `shortcuts/` directory
   - Update branding and styling as needed

4. **Enable GitHub Pages**
   - Go to **Settings** → **Pages**
   - Source: **GitHub Actions**
   - GitHub will automatically deploy on push to `main`

5. **Your site will be live at:**
   ```
   https://YOUR-USERNAME.github.io/iphone-shortcuts
   ```

### GitHub Actions Workflow

This repository includes automated deployment via GitHub Actions (`.github/workflows/deploy.yml`):

- ✅ Automatic deployment on push to `main` branch
- ✅ Manual deployment via workflow_dispatch
- ✅ GitHub Pages hosting with HTTPS
- ✅ No build step required (static files)

---

## 📧 Alternative: Email Method

**Don't want to use GitHub Pages?** Email the shortcuts to yourself:

1. Download shortcut files:
   - [`ask-jarvis.shortcut`](shortcuts/ask-jarvis.shortcut)
   - [`send-to-jarvis.shortcut`](shortcuts/send-to-jarvis.shortcut)
   - [`jarvis-status.shortcut`](shortcuts/jarvis-status.shortcut)

2. Attach to an email and send to yourself

3. On iPhone:
   - Open email
   - Tap attachment
   - Select **"Open in Shortcuts"**
   - Edit IP address and token in each shortcut

---

## 🎯 After Installation

### Voice Commands
```
Hey Siri, Ask JARVIS what's the weather?
Hey Siri, Ask JARVIS to turn on the lights
Hey Siri, Ask JARVIS what time is it?
```

### Ray-Ban Photo Analysis
1. Take photo with Ray-Ban Meta glasses
2. Photo appears on iPhone
3. Tap Share button
4. Select **"Send to JARVIS"**
5. Wait for AI analysis

### Apple Watch
1. Add JARVIS Status shortcut to watch face as complication
2. Tap complication anytime for instant server status
3. See uptime, temperature, load average, etc.

---

## 🐛 Troubleshooting

### "Can't connect to server"

**Cause:** iPhone and JARVIS server not on same network, or IP address incorrect.

**Solutions:**
- Verify iPhone and server on same WiFi network
- Run `hostname -I` on server to confirm IP
- Update IP in shortcuts using web interface or Shortcuts app
- Check firewall rules allow port 18790

### "Untrusted shortcut"

**Cause:** iOS security settings block third-party shortcuts.

**Solution:**
1. Go to **Settings** → **Shortcuts**
2. Enable **"Allow Untrusted Shortcuts"**
3. You may need to run a shortcut once first for this option to appear

### "Shortcut not found"

**Cause:** Shortcut wasn't installed properly.

**Solution:**
- Re-install from the web page
- Make sure you tapped "Add Untrusted Shortcut" when prompted
- Check Shortcuts app to verify installation

### "Invalid response from server"

**Cause:** JARVIS server not running or wrong endpoint.

**Solution:**
- Verify JARVIS server is running: `systemctl status jarvis`
- Check server logs: `journalctl -u jarvis -f`
- Confirm API endpoint is correct in shortcut
- Test endpoint manually: `curl http://YOUR-IP:18790/api/v1/webhook/rayban`

---

## 📂 Repository Structure

```
iphone-shortcuts/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions auto-deploy
├── shortcuts/
│   ├── ask-jarvis.shortcut     # Voice command shortcut
│   ├── send-to-jarvis.shortcut # Photo analysis shortcut
│   ├── jarvis-status.shortcut  # Status check shortcut
│   └── .env                    # Environment placeholder
├── index.html                  # Web installer interface
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git exclusions
```

---

## 🔐 Security Considerations

1. **Change the default token** in production
2. **Use HTTPS** for all API calls (configure reverse proxy)
3. **Limit API access** to trusted networks (firewall rules)
4. **Don't commit** real tokens to public repositories
5. **Regenerate tokens** regularly for security

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built for integration with custom JARVIS AI server
- Designed for Ray-Ban Meta glasses and Apple Watch
- Powered by iOS Shortcuts automation

---

## 📞 Support

**Issues?** Open an issue on [GitHub Issues](https://github.com/Senpai-Sama7/iphone-shortcuts/issues)

**Questions?** Check the [Troubleshooting](#-troubleshooting) section first

---

Made with 🤖 for JARVIS • [Houston Oil Airs](https://houstonoilairs.org)
