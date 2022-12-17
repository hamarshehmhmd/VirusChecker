# Import the necessary libraries
import os
import antivirus

# Define a function to scan the phone for viruses
def scan_for_viruses():
  # Get a list of all files on the phone
  file_list = os.listdir()

  # Scan each file using the antivirus library
  for file in file_list:
    result = antivirus.scan(file)
    if result:
      print(f"Virus found: {result}")
    else:
      print("No viruses found")

# Call the function to start the scan
scan_for_viruses()

