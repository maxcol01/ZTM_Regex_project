from pathlib import Path
import shutil as sh
import re 
import os
from helper import copy_file, ProcessText

path_name = os.path.join(
    "/Users/maximecollet/Desktop/Bureau - iMac de Maxime",
    "DOC MAX/Courses/ZTM_AUTOMATION_BOOTCAMP",
    "0 - Course Resources/5 - Regular Expressions/16 - Project Intro"
)


ORIGIN_FOLDER = Path(path_name)
ORIGIN_FOLDER = Path.cwd()
to_copy = False

if to_copy:
    copy_file(origin_folder=ORIGIN_FOLDER,
            target_folder=ORIGIN_FOLDER)


text_processed = ProcessText()

list_phone, list_email, list_website = text_processed.scan_file("example_email.txt")

text_processed.create_file(list_phone, type="phones")
text_processed.create_file(list_email, type="emails")
text_processed.create_file(list_website, type="websites")

