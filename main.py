#!/usr/bin/env python3

import logging

log = logging.getLogger(__name__)

def greet(name):
    log.info(f'Hello, {name}!')

if __name__ == '__main__':
    greet('World')
