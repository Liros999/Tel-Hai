# Tel-Hai

## Linux Assignment 2: Python Container - Manual Installation & Run

### Assignment Overview

This assignment demonstrates manual Python container creation and usage in GitHub Codespaces, without using Dockerfile or DevContainer configurations.

## Repository Structure

```
.
├── README.md                    # This file
├── python_container_tutorial.md # Complete tutorial guide
├── instructor_notes.md          # Notes for instructors
├── generate.py                  # Docker volumes example script
├── EXACT_COMMAND.txt            # The Docker command to run
├── examples/                   # Example Python scripts
│   ├── main.py
│   └── experiment.py
├── exercises/                  # Mandatory exercises
│   ├── README.md
│   ├── plot_example.py
│   ├── save_csv.py
│   ├── read_csv.py
│   ├── create_json.py
│   └── seaborn_example.py
└── data/                       # Output directory for results
    └── .gitkeep
```

## Quick Start

1. Open GitHub Codespaces
2. Follow the tutorial in `python_container_tutorial.md`
3. Complete all exercises in the `exercises/` directory

## Key Concepts

- **Container**: Isolated Linux environment
- **Manual Installation**: Full control without automation
- **Reproducibility**: Consistent environment for scientific work
- **Container vs Image**: Understanding the difference

## Prerequisites

- GitHub account with Codespaces access
- Basic Linux command line knowledge
- Basic Python knowledge

## Assignment Steps

See `python_container_tutorial.md` for detailed step-by-step instructions.

## Mandatory Exercises

All exercises are located in the `exercises/` directory:

1. Add matplotlib and plot a graph
2. Save CSV file
3. Read CSV file
4. Create JSON file
5. Install and use seaborn package

See `exercises/README.md` for detailed exercise instructions.

## Docker Volumes Example

Run the Docker command with volume mounting:

```bash
docker run --rm \
-v $(pwd):/app \
-v $(pwd)/data:/data \
python:3.11-slim \
bash -c "pip install pandas numpy && python /app/generate.py"
```

This creates `result.csv` in the `data/` folder. See `DOCKER_COMMAND.md` for detailed explanation.

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Python Docker Images](https://hub.docker.com/_/python)
- [GitHub Codespaces](https://github.com/features/codespaces)


