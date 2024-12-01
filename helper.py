from pathlib import Path
import shutil as sh
import re

# Building the REGEX for the type of files: phone numbers, email , website

# Phone numbers to match: 123-456-7890 or 123 456 7890 or (123)-456-7890
# Email to match to match: name@something.com|net|org
# Website to find: 

class ProcessText:
    
    def __init__(self):
        self.list_phone = list()
        self.list_email = list()
        self.list_website = list()
        
    def scan_file(self, text):
        regex_pn = r"\(?\d{3}\)?[- ]\d{3}[- ]\d{4}"
        regex_email = r"([\w\.]+@\w+\.(com|net|org))"
        regex_ws = r"(^|\s)(\w+\.(com|net|org))"
        with open(text, mode="r") as file:
            content = file.readlines()
            for line in content:
                if re.search(regex_pn, line):
                    self.list_phone.append(re.search(regex_pn, line).group())
                elif re.search(regex_email, line):
                   self.list_email.append(re.search(regex_email, line).group())
                elif re.search(regex_ws, line):
                    self.list_website.append(re.search(regex_ws, line).group())
        return self.list_phone, self.list_email, self.list_website
    

    
    def create_file(self, list_file, type):
        for item in list_file:
            with open(f"{type}.txt", mode="a") as storage_file:
                storage_file.write(f"{item}\n")


def copy_file(origin_folder, target_folder):
    wanted_files = [".pdf", ".txt"]
    for file in origin_folder.iterdir():
        if file.suffix in wanted_files:
            sh.copy(file, target_folder)
    print("Files copied !") 

