class Class:
    def __init__(self, name: str, dir: str, parent=None):
        self.name = name
        self.dir = dir
        self.parent = parent
        self.used_in = []

    def __repr__(self) -> str:
        res = f'{self.name}'
        if self.parent:
            res += f' : {self.parent}'
        res += f'\nDirectory: {self.dir}\n'
        return res
