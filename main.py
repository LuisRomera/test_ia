#!/usr/bin/env python3

import os
from test_ia import main  # Import the main function from the submodule

if __name__ == "__main__":
    os.chdir("test_ia")  # Change directory to the submodule
    main()
