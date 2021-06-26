import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter =  r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls,string):
        _, fm, content = re.split(cls.__regex, string, depth=2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata,content)

    
    def __init__(self,metadata, content):
        self.data = metadata
        self.data['content'] = content

    @property
    def body(self):
        return self.data['content']

    @property
    def type(self, type):
        return self.data['type'] if type in self.data else None

    @type.setter
    def type(self,type):
        type = self.data['type']

    def __getitem__(self, k):
        return self.data[k]

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        data  = {}
        for key, value in self.data.items():
            if key != 'content':
                value = data[key]
        return str(data)


    