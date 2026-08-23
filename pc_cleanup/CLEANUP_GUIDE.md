# 🧹 PC & WSL Quick Maintenance Guide

This guide provides fast, copy-paste commands and procedures to instantly reclaim 15–30+ GB whenever your `C:` drive runs low on space.

---

## ⚡ 1. The 2-Minute Quick Cleanup (Reclaims 5–15 GB)

Whenever your `C:` drive starts filling up, run these two quick sections.

### Part A: Inside WSL / Linux Terminal
Run this single command block to clean all developer caches:

```bash
# 1. Clean Docker dangling images & build caches
docker builder prune -f 2>/dev/null
docker image prune -f 2>/dev/null

# 2. Clean package manager caches (NPM, UV, Pip)
npm cache clean --force 2>/dev/null
uv cache clean 2>/dev/null
pip cache purge 2>/dev/null

# 3. Clean system journal logs older than 3 days
sudo journalctl --vacuum-time=3d 2>/dev/null

echo "✅ WSL caches cleaned!"
```

---

### Part B: In Windows PowerShell (Run as Administrator)
Open **PowerShell (Admin)** and paste this block:

```powershell
# 1. Clean Windows User & System Temp files
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$env:LOCALAPPDATA\CrashDumps\*" -Recurse -Force -ErrorAction SilentlyContinue

# 2. Clean Windows Update download cache & Empty Recycle Bin
Remove-Item -Path "C:\Windows\SoftwareDistribution\Download\*" -Recurse -Force -ErrorAction SilentlyContinue
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

# 3. Clean Windows-side dev caches (if any)
Remove-Item -Path "$env:LOCALAPPDATA\npm-cache", "$env:LOCALAPPDATA\uv", "$env:APPDATA\uv" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "✅ Windows Temp and System caches cleaned!" -ForegroundColor Green
```

---

## 📦 2. Shrinking the WSL Virtual Disk (Reclaims 5–15 GB)

> [!NOTE]
> When you delete files inside WSL, Linux frees the space, but Windows holds the `.vhdx` file at its maximum size until you compact it. Do this once a month or after deleting large Docker images / virtual environments.

### Steps:
1. Close your WSL terminals / VS Code.
2. Open **PowerShell** in Windows and run:
   ```powershell
   wsl --shutdown
   diskpart
   ```
3. Inside the `DISKPART>` prompt, paste these lines:
   ```text
   select vdisk file="C:\Users\Arun Yadav\AppData\Local\wsl\{7d4ad266-3c37-42f7-b091-71278d1a8a8a}\ext4.vhdx"
   compact vdisk
   exit
   ```
4. Done! The `.vhdx` file will physically shrink back down on `C:`.

---

## 🛠️ 3. Deep System Cleaning (Run Every 2–3 Months)

### A. Windows Component Store Cleanup (Reclaims 2–5 GB)
In **PowerShell (Admin)**:
```powershell
dism /online /cleanup-image /startcomponentcleanup
```
*(Removes old, superseded Windows Update backup files).*

---

### B. Ensure Reduced Hibernation is Active (Reclaims ~11 GB)
In **PowerShell (Admin)**:
```powershell
powercfg /h /type reduced
```
*(Or `powercfg /h off` if you want to completely disable hibernation for maximum space).*

---

### C. Clean Browser Caches (Reclaims 1–3 GB)
* **Brave / Chrome:** Press `Ctrl + Shift + Delete` ➔ Select **"Cached images and files"** (keep Cookies unchecked so you stay logged in) ➔ Click **Clear data**.

---

## 🛡️ 4. Safety Guardrails (What NOT to Delete)

| Path | Why Keep It |
| :--- | :--- |
| `C:\Users\Arun Yadav\.gitconfig` | Contains your global Git name and email. |
| `C:\Users\Arun Yadav\.wslconfig` | Contains your WSL networking & memory configuration. |
| `C:\Users\Arun Yadav\.vscode` | Contains your Windows VS Code settings. |
| `/home/arun/projects/*` | Your active codebases and git repositories. |

---

## 💾 5. Rule of Thumb for Your Storage Setup

* **`C:` Drive (163 GB):** Keep exclusively for Windows OS, installed software, and the WSL virtual disk. Maintain at least **35–50 GB free** for optimal SSD performance.
* **`D:` Drive (314 GB):** Use for all large media (Videos, Pictures, raw datasets, courses, and zip downloads).
