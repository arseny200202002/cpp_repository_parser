import re
from os import listdir
from os.path import isfile, join


from typing import List
from File import File
from regex_strings import get_filename


def is_correct_extention(filename, extentions: list) -> bool:
    for extention in extentions:
        pattern = re.compile(f'.*\.{extention}')
        if re.match(pattern, filename):
            return True
    return False


def isfolder(filename: str) -> bool:
    return (not isfile(filename) and "." not in filename)


def get_files(path: str) -> list:
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files


def get_folders(path: str) -> list:
    #files = [path + "\\" + file for file in listdir(path) if isfolder(file)]
    files = []
    for file in listdir(path):
        if isfolder(path + "\\" + file):
            files.append(path + "\\" + file)
    return files


def get_some_files(path: str, extentions: list) -> List[File]:
    files = [
        File(path + "\\" + file) 
        for file in listdir(path) 
        if is_correct_extention(file, extentions)
    ]
    return files


def get_headers(path) -> list:
    return get_some_files(path, ["h", "hpp"])


def get_source_files(path) -> list:
    return get_some_files(path, ["cpp"])


def get_all_files(root: str) -> List[File]:
    visited_folders = set()
    all_files = []

    def dfs(folder_path, all_files):
        folder_name = get_filename(folder_path)
        visited_folders.add(folder_name)
        current_folders = get_folders(folder_path)

        all_files += get_headers(folder_path) 
        all_files += get_source_files(folder_path)

        for folder in current_folders:
            dfs(folder, all_files)

    dfs(root, all_files)

    return all_files