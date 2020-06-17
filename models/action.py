from core import settings, helpers
from core.models import action
from plugins.dnstwister.includes import dnstwister

class _dnstwisterIPResolution(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["ip"] = dns.IPResolution(domain)
        if actionResult["data"]["ip"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

class _dnstwisterParkedCheck(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["parked"] = dns.parkedCheck(domain)
        if actionResult["data"]["parked"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

class _dnstwisterWhois(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["whois"] = dns.whois(domain)
        if actionResult["data"]["whois"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

class _dnstwisterGoogleSafeBrowsing(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["googleSafeBrowsing"] = dns.googleSafeBrowsing(domain)
        if actionResult["data"]["googleSafeBrowsing"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

class _dnstwisterFuzz(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["fuzz"] = dns.fuzz(domain)
        if actionResult["data"]["fuzz"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

class _dnstwisterReport(action._action):
    domain = str()

    def run(self,data,persistentData,actionResult):
        domain = helpers.evalString(self.domain,{"data" : data})

        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],timeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(timeout=dnstwisterSettings["requestTimeout"])

        actionResult["data"]["report"] = dns.report(domain)
        if actionResult["data"]["report"]:
            actionResult["result"] = True
            actionResult["rc"] = 0
        else:
            actionResult["result"] = False
            actionResult["rc"] = 404
        return actionResult

dnstwisterSettings = settings.config["dnstwister"]
