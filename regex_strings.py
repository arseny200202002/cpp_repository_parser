import re

def line_contains_class(line: str) -> bool:
    words = line.split()
    if len(words) < 1: 
        return False
    if words[0] == "class":
        return True
    else:
        return False


def get_filename(path: str) -> str:
    units = path.split("\\")
    filename = units[-1]
    return filename


def get_header(line: str) -> str:
    line = line[:-2].split()[1]
    line = line.split('/')[-1]
    header = line.strip('\"')
    return header


def is_correct_header(header: str) -> bool:
    return re.match(r'#include', header) and not "<" in header

