import os

from plugins.datasee.includes import processor

maxMemorySize = 65535

class _default(processor.processor):
    supportedFileTypes = ["*"]

    def process(self):
        if self.dsFile.extension not in ["pdf","vsd","ppt","pptx","rar","accdb","jpg","png","db","img","iso","exe","dll","com","cab","pub","pubx","jpeg","cad","gif","pst","lnk","msg","vmdk","ova"]:
            return [processor.processItem(0,self.dsFile.path)]
        else:
            return [processor.processItem(-3,None)]
