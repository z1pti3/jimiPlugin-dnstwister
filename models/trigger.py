from core import settings, helpers
from core.models import trigger

from plugins.dnstwister.includes import dnstwister
from plugins.dnstwister.models import dnstwister as dnstwisterDB

class _dnstwisterObserve(trigger._trigger):
    domains = list()

    def check(self):
        if "ca" in dnstwisterSettings:
            dns = dnstwister._dnstwister(dnstwisterSettings["ca"],requestTimeout=dnstwisterSettings["requestTimeout"])
        else:
            dns = dnstwister._dnstwister(requestTimeout=dnstwisterSettings["requestTimeout"])

        events = []
        update=False
        for domain in self.domains:
            fuzzDomains = dns.fuzz(domain)
            for fuzzDomain in fuzzDomains:
                dnstwisterObj = dnstwisterDB._dnstwister().getAsClass(query={ "domain" : fuzzDomain["domain"] })
                if len(dnstwisterObj) > 0:
                    dnstwisterObj = dnstwisterObj[0]
                    update = True
                elif len(dnstwisterObj) == 0:
                    dnstwisterObj = dnstwisterDB._dnstwister().new(fuzzDomain["domain"], self.acl).inserted_id
                    dnstwisterObj = dnstwisterDB._dnstwister().getAsClass(id=dnstwisterObj)
                    dnstwisterObj = dnstwisterObj[0]

                domainReport = dns.report(fuzzDomain["domain"])
                
                if type(domainReport["ip"]) is bool:
                    domainReport["ip"] = ""

                if dnstwisterObj.ip != domainReport["ip"] or dnstwisterObj.mx != domainReport["mx"]:
                    dnstwisterObj.updateRecord(fuzzDomain["domain"],domainReport["ip"],domainReport["mx"],domainReport["when"],fuzzDomain["fuzzer"])
                    domainReport["domain"] = fuzzDomain["domain"]
                    if update:
                        domainReport["type"] = "update"
                    else:
                        domainReport["type"] = "created"
                    events.append(domainReport)
                    
        self.result["events"] = events


dnstwisterSettings = settings.config["dnstwister"]
