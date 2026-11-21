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
    args = parser.parse_args()

    log.info("Starting (dry_run=%s)", args.dry_run)
    processed = 0
    # TODO: the work of the job
    log.info("Done: %s items processed", processed)
    print(json.dumps({"processed": processed}))  # the last JSON line is the result of the run


if __name__ == "__main__":
    main()
