"""
Module providing ANSI color escape codes for terminal output formatting
for cross-platform CLI feedback.
"""

import os

# Enable ANSI escape codes on Windows
if os.name == 'nt':
    os.system('')

class Colors:
    """Contains standard ANSI color escape code constants."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
