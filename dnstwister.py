from core import plugin, model

class _dnstwister(plugin._plugin):
    version = 0.2

    def install(self):
        # Register models
        model.registerModel("dnstwisterIPResolution","_dnstwisterIPResolution","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterParkedCheck","_dnstwisterParkedCheck","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterWhois","_dnstwisterWhois","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterGoogleSafeBrowsing","_dnstwisterGoogleSafeBrowsing","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterFuzz","_dnstwisterFuzz","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterReport","_dnstwisterReport","_action","plugins.dnstwister.models.action")
        model.registerModel("dnstwisterObserve","_dnstwisterObserve","_trigger","plugins.dnstwister.models.trigger")
        model.registerModel("dnstwister","_dnstwister","_document","plugins.dnstwister.models.dnstwister",True)
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("dnstwisterIPResolution","_dnstwisterIPResolution","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterParkedCheck","_dnstwisterParkedCheck","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterWhois","_dnstwisterWhois","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterGoogleSafeBrowsing","_dnstwisterGoogleSafeBrowsing","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterFuzz","_dnstwisterFuzz","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterReport","_dnstwisterReport","_action","plugins.dnstwister.models.action")
        model.deregisterModel("dnstwisterObserve","_dnstwisterObserve","_trigger","plugins.dnstwister.models.trigger")
        model.deregisterModel("dnstwister","_dnstwister","_document","plugins.dnstwister.models.dnstwister")
        return True
    
    def upgrade(self,LatestPluginVersion):
        if self.version < 0.2:
            model.registerModel("dnstwister","_dnstwister","_document","plugins.dnstwister.models.dnstwister",True)