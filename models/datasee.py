import time

from core import db, helpers, logging, audit


class _dataSee(db._document):
    name = str()
    filehash = str()
    filesize = int()
    filename = str()
    createdDate = int()
    lastScan = int()
    properties = dict()

    _dbCollection = db.db["dataSee"]

    def new(self, acl, name, filename, properties, filehash="", filesize=0):
        self.name = name
        self.filehash = filehash
        self.filesize = filesize
        self.filename = filename
        self.properties = properties
        self.createdDate = int(time.time())
        self.acl = acl
        return super(_dataSee, self).new()

    def bulkNew(self, acl, name, filename, properties, bulkClass, filehash="", filesize=0):
        self.name = name
        self.filehash = filehash
        self.filesize = filesize
        self.filename = filename
        self.properties = properties
        self.createdDate = int(time.time())
        self.acl = acl
        return super(_dataSee, self).bulkNew(bulkClass)

    def updateRecord(self, output, properties, filehash, filesize, auditLog=False):
        self.lastScan = int(time.time())
        self.output = output
        self.properties = properties
        self.update(["lastScan","output","properties"])
        if auditLog:
            audit._audit().add("datasee","file scan",{ "name" : self.name, "filehash" : self.filename, "filename" : self.filename, "createdDate" : self.createdDate, "lastScan" : self.lastScan, "properties" : self.properties, "output" : self.output })
        

