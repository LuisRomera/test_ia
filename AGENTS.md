# Job Documentation

## Purpose
This job runs a simple Python script that logs an informational message. It uses the MinIO library to interact with MinIO servers.

## Entry Point
The entry point of the job is `main.py`. This script is executed when the job runs in the Kubernetes pod.

## CLI Arguments
The current script does not accept any command-line arguments. All configuration and credentials should be passed via environment variables.

## Module Structure
- **`main.py`**: The main module that contains the entry point of the job.
- **`requirements.txt`**: Contains the list of third-party packages required by the job.
- **`.gitignore`**: Specifies files to be ignored by Git.

## External Dependencies in `requirements.txt`
The following package is listed in `requirements.txt`:
- `minio==7.2.12`: A Python client for interacting with MinIO servers.

## Coding/Logging Conventions
- Logging is configured by the platform, and the job should use the provided logger.
- The logging format is set to `%(asctime)s %(levelname)s %(name)s: %(message)s` with a level of INFO.
- All printed or logged messages are shown live in the Logs window, colored by level.
- If the last printed line is JSON, it becomes the result of the run.
- Exit with an error (exception or `sys.exit(1)`) when the job fails.
