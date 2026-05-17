# Task Manager API

This project is a Flask-based Task Management application containerized with Docker and automated using a 4-stage GitHub Actions CI Pipeline.

## CI/CD Pipeline Stages
1. **Build:** Verifies application imports and setup.
2. **Unit Tests:** Runs pytest suite.
3. **Lint (flake8):** Ensures code quality checks.
4. **Package:** Builds the final Docker image.

# Task Manager API
![CI Pipeline Status](https://github.com/asadniyazov/docker-lahiye/actions/workflows/ci.yml/badge.svg)