from os import mkdir
from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest + '/' + path.relative_to(self.source)
        mkdir(directory,parents=True, exists_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exists_ok=True)
        for path in self.source.rglob('*'):
            if isinstance(path, Path):
                Site.create_dir(path)
