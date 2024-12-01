from pathlib import Path
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

text_processed.scan_file("example_email.txt")

list_types = ["phones", "emails", "websites"]

for type in list_types:
    text_processed.create_file(type=type)


