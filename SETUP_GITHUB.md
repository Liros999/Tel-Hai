# Setup Instructions for GitHub Repository

## Current Status
✅ Files created locally  
❌ Not yet in GitHub repository  
❌ Git repository not initialized  

## Step-by-Step Setup

### Option 1: Initialize Git and Push to Existing Repository

1. **Initialize Git Repository**
```bash
cd "C:\Users\lirdi\Desktop\Tel-Hai\Linux\linux_assignment 2"
git init
git add .
git commit -m "Add Python container assignment with Docker volumes example"
```

2. **Connect to GitHub Repository**
```bash
git remote add origin https://github.com/Liros999/Tel-Hai.git
git branch -M main
git push -u origin main
```

### Option 2: Use GitHub Codespaces (Recommended)

1. **Go to GitHub Repository**
   - Visit: https://github.com/Liros999/Tel-Hai
   - Click "Code" → "Codespaces" → "Create codespace on main"

2. **Upload Files in Codespaces**
   - In Codespaces, create the files:
     - `generate.py`
     - `data/` folder
     - `DOCKER_COMMAND.md`
   - Or use: File → Upload to upload from your local machine

3. **Run the Command**
   - Open terminal in Codespaces
   - Navigate to repository root
   - Run the Docker command

### Option 3: Manual Upload via GitHub Web Interface

1. Go to https://github.com/Liros999/Tel-Hai
2. Click "Add file" → "Upload files"
3. Upload:
   - `generate.py`
   - All files from `linux_assignment 2/` folder
4. Create `data` folder and add `.gitkeep` file

## Files Needed for the Screenshot

### Required Files:
- ✅ `generate.py` - The Python script
- ✅ `data/` folder - Output directory
- ✅ `DOCKER_COMMAND.md` - Command documentation

### The Command to Run:
```bash
docker run --rm \
-v $(pwd):/app \
-v $(pwd)/data:/data \
python:3.11-slim \
bash -c "pip install pandas numpy && python /app/generate.py"
```

## After Setup

Once files are in GitHub:
1. Open Codespaces
2. Run the Docker command
3. Take screenshot showing:
   - File structure (generate.py, data folder)
   - Command execution
   - Output (pandas installing, result.csv created)

