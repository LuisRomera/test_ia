#!/usr/bin/env python3

import os
import logging

if __name__ == "__main__":
    os.chdir("test_ia")  # Change directory to the submodule
    log = logging.getLogger(__name__)
    log.info('hello')
