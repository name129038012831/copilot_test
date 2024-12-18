from datetime import datetime
import sys
import pkg_resources
"""
This script imports the datetime module to get the current date and prints it.

Functions:
    None

Variables:
    current_date (datetime.date): The current date obtained using datetime.now().date()

Usage:
    Run the script to print the current date in the format "Current date: YYYY-MM-DD".
"""

# Get the current date
current_date = datetime.now().date()

# Print the current date
print("Current date:", current_date)
# Print the Python version
print("Python version:", sys.version)

# Write the versions of the loaded modules to a file
with open('/home/david/vscode/copilot_test/module_versions.txt', 'w') as file:
    file.write("Loaded modules and their versions:\n")
    for dist in pkg_resources.working_set:
        file.write(f"{dist.project_name} ({dist.version})\n")