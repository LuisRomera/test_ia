# Project Documentation: Data Platform Job

## Purpose
This job is designed to interact with a MinIO object storage service to retrieve metadata about files. It loads configuration parameters (like credentials and bucket paths) from a YAML file, initializes a MinIO client, and identifies the latest file in a specific directory.

## Entry Point
The main entry point for this job is `main.py`. The platform executes it using:
`python main.py <arguments>`

## CLI Arguments & Configuration
- **Configuration**: Primary configuration is stored in `resources/config.yaml`.
- **Arguments**: While the current implementation primarily uses the YAML config, any additional parameters should be passed via `argparse` in `main.py`.
- **Environment Variables**: Credentials or overrides can be provided via environment variables and accessed using `os.environ`.

## Module Structure
- `main.py`: Orchestrates the job execution flow.
- `config_loader.py`: Handles loading and parsing of the YAML configuration file.
- `minio_client.py`: Provides a wrapper for interacting with the MinIO service (listing buckets, getting latest files).
- `resources/`: Contains static configuration files.

## External Dependencies
The following third-party packages are required (defined in `requirements.txt`):
- `PyYAML`: For parsing configuration files.
- `minio`: For interacting with the MinIO object storage.

## Coding & Logging Conventions
- **Logging**: Use the platform's pre-configured logging. 
    - Initialize: `log = logging.getLogger(__name__)`
    - Methods: Use `log.info()`, `log.warning()`, `log.error()`, and `log.exception()`.
    - Do not call `logging.basicConfig()`.
- **Error Handling**: Catch exceptions at the top level in `main.py`, log them using `log.exception()`, and exit with `sys.exit(1)`.
- **Type Hinting**: Use Python type hints for all function signatures to ensure maintainability.
- **Style**: Follow PEP 8 guidelines for naming conventions and code structure.
