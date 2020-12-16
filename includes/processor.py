import os
from pathlib import Path

from plugins.datasee.includes import engine

def getTypeClassMapping():
    classMap = {}
    processors = os.listdir(Path("plugins/datasee/includes/processors"))
    for processor in processors:
        if processor.endswith(".py"):
            processor = processor[:-3]
            mod = __import__("plugins.datasee.includes.processors.{0}".format(processor), fromlist=["_{0}".format(processor)])
            class_ = getattr(mod, "_{0}".format(processor))
            for fileType in class_().supportedFileTypes:
                classMap[fileType] = class_()
    return classMap

class processItem():
    def __init__(self,processType,content):
        self.processType = processType
        self.content = content

class processor():

    def processHandler(self,dsFile):
        result = {}
        self.dsFile = dsFile
        try:
            for checkContent in self.process():
                if checkContent:
                    # File processing
                    if checkContent.processType == 0:
                        matches = engine.process(checkContent.content)
                    # String processing
                    elif checkContent.processType == 1:
                        matches = engine.process(data=checkContent.content)
                    elif checkContent.processType == -1:
                        matches = checkContent.content
                    elif checkContent.processType == -2:
                        matches = { "passwordProtected" : { "data" : ["Password Protected / Cant Read"], "count" : 1 } }
                    elif checkContent.processType == -3:
                        matches = { "unsupportedFileType" : { "data" : ["Unsupported file type"], "count" : 1 } }
                    elif checkContent.processType == -4:
                        matches = { "largeFile" : { "data" : ["Large file is over max size"], "count" : 1 } }
                    for key in matches.keys():
                        if key not in result:
                            result[key] = matches[key]
                        else:
                            result[key]["count"] += matches[key]["count"]
        except Exception as e:
            result["errorProcessing"] = { "errorText" : str(e) }
        return result

    def process(self):
        return []

