# SC0039_final_project

Final project for course SC0039

The final_project_1.py contains the script to change the paths in the test.cara file to the new one where your .ft3 files (files needed for further analysis) are located.

In command line write:
python final_project_1.py -in test.cara -out new_test.cara -p /new_path/

Where -in is the name of the .cara file you want to modify, -out is the name of the modified cara file (extension has to be .cara for further use) and -p is the new path where your .ft3 file are located.

A new file called new_test.cara will be created with your new path.

Python used:
Python 3.12.4

Packages:
os
re
argparse
