#!/usr/bin/env python3

import os
from test_ia import main  # Import the main function from the submodule
import logging

if __name__ == "__main__":
    os.chdir("test_ia")  # Change directory to the submodule
    log = logging.getLogger(__name__)
    log.info('hello')
