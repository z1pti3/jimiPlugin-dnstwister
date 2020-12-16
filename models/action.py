import time
from core import settings, helpers, db
from core.models import action

from plugins.datasee.includes import dataseeMain
from plugins.datasee.models import datasee

class _dataSeeFileScan(action._action):
    scanName = str()
    filename = str()
    customProperties = dict()
    keepHistory = bool()
    overrideFilename = bool()
    customFilename = str()

    def run(self,data,persistentData,actionResult):
        scanName = helpers.evalString(self.scanName,{"data" : data})
        filename = helpers.evalString(self.filename,{"data" : data})
        customFilename = filename
        if self.overrideFilename:
            customFilename = helpers.evalString(self.filename,{"data" : data})
        customProperties = helpers.evalDict(self.customProperties,{"data" : data})

        f, result = dataseeMain.fileProcess(customFilename)

        try:
            record = datasee._dataSee().getAsClass(query={ "name" : scanName, "filename" : filename })[0]
            actionResult["rc"] = 202
        except IndexError:
            datasee._dataSee().new(self.acl,scanName,filename,customProperties,f.sha265,f.size)
            record = datasee._dataSee().getAsClass(query={ "name" : scanName, "filename" : filename })[0]
            actionResult["rc"] = 201

        record.updateRecord(result,customProperties,f.sha265,f.size,self.keepHistory)

        if result:
            actionResult["data"] = result
            actionResult["hash"] = f.sha265
            actionResult["size"] = f.size
            actionResult["result"] = True
        else:
            actionResult["result"] = False
            actionResult["rc"] = 901
        return actionResult

class _dataSeeAddRecord(action._action):
    scanName = str()
    filename = str()
    customProperties = dict()

    def run(self,data,persistentData,actionResult):
        scanName = helpers.evalString(self.scanName,{"data" : data})
        filename = helpers.evalString(self.filename,{"data" : data})
        customProperties = helpers.evalDict(self.customProperties,{"data" : data})

        try:
            datasee._dataSee().getAsClass(query={ "name" : scanName, "filename" : filename })[0]
            actionResult["result"] = False
            actionResult["rc"] = 302
        except IndexError:
            datasee._dataSee().new(self.acl,scanName,filename,customProperties)
            actionResult["result"] = True
            actionResult["rc"] = 201

        return actionResult

class _dataSeeAddRecords(action._action):
    scanName = str()
    filenames = str()
    customProperties = dict()

    def run(self,data,persistentData,actionResult):
        scanName = helpers.evalString(self.scanName,{"data" : data})
        filenames = helpers.evalString(self.filenames,{"data" : data})
        customProperties = helpers.evalDict(self.customProperties,{"data" : data})

        actionResult["result"] = True
        actionResult["rc"] = 201

        try:
            existingFiles = [x["filename"] for x in datasee._dataSee().query(query={ "name" : scanName, "filename" : {"$in" : [filename for filename in filenames]} },fields=["filename"])["results"]]
        except KeyError:
            existingFiles = []
        filenames = [filename for filename in filenames if filename not in existingFiles]

        bulkClass = db._bulk()
        for filename in filenames:
            datasee._dataSee().bulkNew(self.acl,scanName,filename,customProperties,bulkClass)
        if len(filenames) == 0:
            actionResult["rc"] = 302
        return actionResult

class _dataSeeGetRecord(action._action):
    scanName = str()
    filename = str()

    def run(self,data,persistentData,actionResult):
        scanName = helpers.evalString(self.scanName,{"data" : data})
        filename = helpers.evalString(self.filename,{"data" : data})

        try:
            record = datasee._dataSee().getAsClass(query={ "name" : scanName, "filename" : filename })[0]
            actionResult["filename"] = record.filename
            actionResult["hash"] = record.filename
            actionResult["size"] = record.size
            actionResult["properties"] = record.properties
            actionResult["result"] = True
            actionResult["rc"] = 0
        except IndexError:
            actionResult["result"] = False
            actionResult["rc"] = 404

        return actionResult

class _dataSeeGetRecords(action._action):
    scanName = str()
    limit = int()
    excludeComplete = bool()

    def run(self,data,persistentData,actionResult):
        scanName = helpers.evalString(self.scanName,{"data" : data})

        limit = 10
        if self.limit:
            limit = self.limit

        try:
            if self.excludeComplete:
                tempRecords = datasee._dataSee().getAsClass(query={ "name" : scanName, "lastScan" : 0 },limit=limit)
            else:
                tempRecords = datasee._dataSee().getAsClass(query={ "name" : scanName },limit=limit,sort=[( "lastScan", 1 )])
            records = []
            for record in tempRecords:
                records.append({ "name" : record.name, "filename" : record.filename, "filehash" : record.filehash, "filesize" : record.filesize, "properties" : record.properties, "lastscan" : record.lastScan })
            actionResult["records"] = records
            actionResult["result"] = True
            actionResult["rc"] = 0
        except IndexError:
            actionResult["result"] = False
            actionResult["rc"] = 404

        return actionResult

