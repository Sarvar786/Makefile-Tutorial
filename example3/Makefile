PYTHON = python3
VENV = venv

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip

# Generate raw data file
generate:
	$(PYTHON) generate.py

# Process raw data and create processed file
process: generate
	$(PYTHON) process.py

# Summarize processed data
summary: process
	$(PYTHON) summary.py

# Run everything sequentially
run: summary

# Clean generated files
clean:
	rm -f data.txt processed.txt summary.txt

