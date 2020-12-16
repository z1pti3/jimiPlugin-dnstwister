import os
from pathlib import Path

from plugins.datasee.includes import processor, hash

class dsFile:

    def __init__(self,dir,filename):
        self.dir = dir
        self.name = filename
        self.extension = ""
        if "." in filename:
            self.extension = filename.split(".")[-1]
        self.path = "{0}/{1}".format(dir,filename)
        self.sha265 = hash.fileHashSHA256(Path(self.path))
        self.size = os.path.getsize(Path(self.path))

def fileProcess(filename):
    result = None
    f = dsFile("/".join(filename.split("/")[:-1]),filename.split("/")[-1])
    fileTypeClassMap = processor.getTypeClassMapping()
    if f.extension in fileTypeClassMap:
        result = fileTypeClassMap[f.extension].processHandler(f)
    elif "*" in fileTypeClassMap:
        result = fileTypeClassMap["*"].processHandler(f)
    return (f, result)