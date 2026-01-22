# Docker Practice Assignment

## Files

- `plotgen.py` - Python script that generates graphs
- `Dockerfile` - Instructions for building Docker image

## Usage

### Build Docker Image
```bash
docker build -t imgplotgen .
```

### Run Container
```bash
docker run --rm -v "$(pwd)/output:/app/output" imgplotgen 10
```

### Verify Output
```bash
ls output/
```
