# Docker Command for Professor - Complete Setup

## The Exact Command

```bash
docker run --rm \
-v $(pwd):/app \
-v $(pwd)/data:/data \
python:3.11-slim \
bash -c "pip install pandas numpy && python /app/generate.py"
```

## What This Does

1. **Creates a temporary container** (`--rm` removes it after completion)
2. **Mounts current directory** to `/app` inside container (access to `generate.py`)
3. **Mounts data folder** to `/data` inside container (where `result.csv` will be saved)
4. **Installs packages** pandas and numpy
5. **Runs the script** `generate.py` which creates `result.csv` in the `data/` folder

## File Structure Required

```
.
├── generate.py          # Python script that generates result.csv
├── data/                # Output folder (will contain result.csv after running)
└── README.md            # Documentation
```

## How to Run in GitHub Codespaces

1. Open your repository in GitHub Codespaces
2. Navigate to the repository root
3. Run the command above
4. Check `data/result.csv` - it should be created!

## Expected Output

The command will:
- Download and install pandas and numpy
- Run generate.py
- Create result.csv in the data/ folder
- Show data preview and statistics
- Exit and remove the container

## Verification

After running, verify the output:
```bash
ls -la data/
cat data/result.csv | head
```

