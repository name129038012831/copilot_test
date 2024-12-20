
"""
This script performs the following tasks:
1. Imports the datetime module to get the current date.
2. Prints the current date.
3. Prints the Python version.
4. Writes the versions of the loaded modules to a file.

Usage:
    Run the script to print the current date, Python version, and save the
    loaded modules' versions to a file.

Modules:
    - datetime: To get the current date.
    - sys: To get the Python version.
    - pkg_resources: To get the versions of the loaded modules.

Functions:
    None

Variables:
    - current_date: Stores the current date.

File Output:
    - module_versions.txt: Contains the names and versions of the loaded
     modules.
"""
from datetime import datetime
import sys
import pkg_resources
# This script imports the datetime module to get the current date and prints
# it. It also prints the Python version and writes the versions of the loaded
# modules
# to a file.
# Usage:
#     Run the script to print the current date, Python version, and save the
#     loaded modules' versions to a file.

# Get the current date

current_date = datetime.now().date()

# Print the current date
print("Current date:", current_date)
# Print the Python version
print("Python version:", sys.version)

# Write the versions of the loaded modules to a file
with open('/home/david/vscode/copilot_test/module_versions.txt', 'w',
          encoding='utf-8') as file:

    file.write("Loaded modules and their versions:\n")
    for dist in pkg_resources.working_set:
        file.write(f"{dist.project_name} ({dist.version})\n")
