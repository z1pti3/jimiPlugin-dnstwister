from core import plugin, model

class _datasee(plugin._plugin):
    version = 0.21

    def install(self):
        # Register models
        model.registerModel("dataSee","_dataSee","_document","plugins.datasee.models.datasee")
        model.registerModel("dataSeeFileScan","_dataSeeFileScan","_action","plugins.datasee.models.action")
        model.registerModel("dataSeeAddRecord","_dataSeeAddRecord","_action","plugins.datasee.models.action")
        model.registerModel("dataSeeAddRecords","_dataSeeAddRecords","_action","plugins.datasee.models.action")
        model.registerModel("dataSeeGetRecord","_dataSeeGetRecord","_action","plugins.datasee.models.action")
        model.registerModel("dataSeeGetRecords","_dataSeeGetRecords","_action","plugins.datasee.models.action")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("dataSee","_dataSee","_document","plugins.datasee.models.datasee")
        model.deregisterModel("dataSeeFileScan","_dataSeeFileScan","_action","plugins.datasee.models.action")
        model.deregisterModel("dataSeeAddRecord","_dataSeeAddRecord","_action","plugins.datasee.models.action")
        model.deregisterModel("dataSeeAddRecords","_dataSeeAddRecords","_action","plugins.datasee.models.action")
        model.deregisterModel("dataSeeGetRecord","_dataSeeGetRecord","_action","plugins.datasee.models.action")
        model.deregisterModel("dataSeeGetRecords","_dataSeeGetRecords","_action","plugins.datasee.models.action")
        return True
    
    def upgrade(self,LatestPluginVersion):
        if self.version < 0.2:
            model.registerModel("dataSeeGetRecord","_dataSeeGetRecord","_action","plugins.datasee.models.action")
            model.registerModel("dataSeeGetRecords","_dataSeeGetRecords","_action","plugins.datasee.models.action")

        #Added adding multiple records
        if self.version < 0.21:
            model.registerModel("dataSeeAddRecords","_dataSeeAddRecords","_action","plugins.datasee.models.action")


