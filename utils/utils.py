import os
import sys
from termcolor import colored, cprint


def log_info(msg: str, color: str):
    print(colored(msg, color, attrs=['reverse', 'blink']))

def serialize_text_into_list(file: str):
    f = open(file, "r")
    text = [word for line in f for word in line.split()]
    f.close()
    print(text)
    return text

def serialize_text_into_set(file: str):
    f = open(file, "r")
    text = set(word for line in f for word in line.split())
    f.close()
    return text

def list_files_in_directory(directory: str):
    files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                # path = f"{root}/{file}"
                # files.append(path)
                # files.append(f"{root}/{file}")
                print(os.path.join(root, file))
