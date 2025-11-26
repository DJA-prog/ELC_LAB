#!/usr/bin/env python3
"""
Launcher script for Component Manager
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the application
from component_manager import main

if __name__ == '__main__':
    main()