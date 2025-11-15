# Analyze Task

## Overview
This project analyzes data using Python and automated CI/CD.

## Files
- `execute.py`: Main analysis script (typo fixed)
- `data.csv`: Data file converted from Excel
- `.github/workflows/ci.yml`: GitHub Actions workflow

## CI/CD Pipeline
The GitHub Actions workflow:
1. Runs ruff linter for code quality
2. Executes `execute.py` to generate `result.json`
3. Deploys `result.json` to GitHub Pages

## Usage
Push to main branch to trigger the CI pipeline.

## Result
View the generated `result.json` on GitHub Pages after CI completes.
