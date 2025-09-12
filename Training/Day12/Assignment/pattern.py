"""
Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
Write a script to:
- Find all .txt files in a folder.
- Check if any file contains the word "Python".
- Print the file name if the word is found
 
 
Assignment 2: Match File Names Using re.match
List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 
 
Assignment 3: Validate Phone Numbers with re.match
Given a list of phone numbers, print only the ones that match this format:
(123) 456-7890
"""

import glob
import re
import os
# Assignment 1: List All .txt Files and Check for a Word using glob + re.search

files = glob.glob("Assignment/Pattern/*.txt")
for file in files:
    with open(file, 'r') as f:
        content =  f.read()
        match = re.search(r"Python",content)
        if match:
            print (f"Python test found in file: {file}")
        f.close()

#Assignment 2: Match File Names Using re.match
print("Assignment 2 ***************************************")
files = glob.glob("Assignment/Pattern/*.*")
print(files)
for file in files:
        filename = os.path.basename(file)
        #match = re.match(r"data_",filename) and re.match(r"vsc.",filename[::-1])
        match = re.match(r"^(data_).*(\.csv)$",filename) #and re.match(r"vsc.",filename[::-1])
        if match:
            print (f"This is a csv file and starts with data_: {file}")

print("Assignment 3 ***************************************")
# Assignment 3: Validate Phone Numbers with re.match
listofphones = ["(123) 450-7890" , "(919) 456-8760", "(56) 57-8668"]
for phone in listofphones:
     match = re.match(r"\([1-9]{3}\)\s[0-9]{3}-[0-9]{4}",phone)
     if match:
        print (f"This is a valid phone Number: {phone}")
     else:
        print (f"Invalid phone Number: {phone}")

     