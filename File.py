import io, re, os

cwd = os.getcwd()
FIND_CLASSES_EXAMPLE_FILE = cwd + "\\CuraEngine\\include\\FffGcodeWriter.h"

from typing import List
from regex_strings import   line_contains_class,\
                            get_filename,\
                            get_header,\
                            is_correct_header

from Class import Class

class File:
    def __init__(self, path):
        self.path = path
        self.name = get_filename(self.path)

        self.classes = []
        self.file_content = []
        self.used_in = []

        self.get_file_content()
        self.find_classes()

    def add_class(self, class_: Class):
        self.classes.append(class_)

    def get_file_content(self):
        with io.open(self.path, "r", errors='ignore') as file:
            lines = file.readlines()
        self.file_content = lines

    def find_classes(self):
        for i, line in enumerate(self.file_content[:-1]):
            if line_contains_class(line) and self.file_content[i+1] == "{\n":
                words = line.split()
                class_name = words[words.index('class') + 1]
                if ':' in words:
                    if words[words.index(':') + 1] in ['public', 'protected', 'private']:
                        index = words.index(':') + 2
                    else: 
                        index = words.index(':') + 1
                    class_parent = words[index]
                else:
                    class_parent = None
                class_ = Class(class_name, self.path, class_parent)
                self.add_class(class_)

    def get_headers(self) -> List[str]:
        headers = [
                get_header(line)
                for line in self.file_content 
                if is_correct_header(line)
        ]
        return headers

    def has_class(self, classname: Class) -> bool:
        return classname in self.classes
    
    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return f'name: {self.name}, path: {self.path}' 
    

if __name__ == "__main__":
    file = File(FIND_CLASSES_EXAMPLE_FILE)
    file.find_classes()
    print(file.get_headers())