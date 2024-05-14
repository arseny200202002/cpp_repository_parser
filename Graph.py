from inspect_repository import *

from collections import defaultdict
from typing import Dict, List, Tuple, Optional

from Class import Class
from File import File

class Graph:
    def __init__(self, root_path: str):
        self.root: str = root_path

        self.graph: Dict[File, List[File]] =defaultdict(list)
        self.files: Dict[str, List[File]] =       defaultdict(list)
        self.classes: Dict[str, Class] =    dict()

        self.other_headers: List[str] =         []
        self.vertexes: List[Tuple[File, File]] =[]

    def process_file(self, file: File):
        for class_ in file.classes:
            if class_ not in self.classes.values():
                self.classes[class_.name] = class_
            class_.used_in.append(file)
        headers = file.get_headers()
        for header in headers:
            try:
                self.graph[file].append(self.files[header])
            except Exception as e:
                self.other_headers.append(header)
    
    def build_graph(self):
        files = get_all_files(self.root)
        self.files = {file.name: file for file in files}

        [self.process_file(file) for file in files]
            
        for header, used_files in self.graph.items():
            for used_file in used_files:
                used_file: File
                used_file.used_in.append(header)

        self.build_vertexes()

    def build_vertexes(self):
        for destination, sources in self.graph.items():
            vertexes = [(source, destination) for source in sources]
            self.vertexes += vertexes
    
    def get_vertexes(self) -> List[Tuple[File, File]]:
        return self.vertexes

    def __repr__(self):
        representation = ""
        for node, includes in zip(self.graph.keys(), self.graph.values()):
            representation += f'{node}:\n'
            representation += f'{includes}\n'
        
        return representation
    

if __name__ == "__main__":
    import os
    cwd = os.getcwd()
    ROOT = cwd + "\\CuraEngine"

    graph = Graph(ROOT)
    graph.build_graph()