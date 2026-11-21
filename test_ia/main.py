"""test ia: a job of the PMO platform.

Runs as `python main.py [arguments]` in its own pod. Everything printed or logged
(log.info, log.warning, log.error...) appears live in the Logs window of the job.
"""
import argparse
import json
import logging

log = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description="test ia")
    parser.add_argument("--dry-run", action="store_true", help="Do not write anything")
    parser.add_argument("--data-file", required=True, help="Path to the data file")
    args = parser.parse_args()

    log.info("Starting (dry_run=%s, data_file=%s)", args.dry_run, args.data_file)
    processed = 0
    # TODO: read from args.data_file and process the data
    log.info("Done: %s items processed", processed)
    print(json.dumps({"processed": processed}))  # the last JSON line is the result of the run


if __name__ == "__main__":
    main()
