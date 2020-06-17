import requests
import json
import binascii
from pathlib import Path

class _dnstwister():
    url = "http://dnstwister.report/api/"

    def __init__(self,ca=None,requestTimeout=30):
        self.requestTimeout = requestTimeout
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def getAPI(self,url):
        try:
            if self.ca:
                response = requests.get(url, verify=self.ca, timeout=self.requestTimeout)
            else:
                response = requests.get(url, timeout=self.requestTimeout)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"

        if response.status_code == 200:
            return response.text

        return None

    def IPResolution(self,domain):
        url = "{0}{1}/{2}".format(self.url,"ip",binascii.hexlify(domain.encode()).decode())
        response = self.getAPI(url)
        if response:
            return json.loads(response)["ip"]
        return None

    def parkedCheck(self,domain):
        url = "{0}{1}/{2}".format(self.url,"parked",binascii.hexlify(domain.encode()).decode())
        response = self.getAPI(url)
        if response:
            response = json.loads(response)
            return { "dressed" : response["dressed"], "redirects" : response["redirects"], "redirects_to" : response["redirects_to"], "score" : response["score"], "score_text" : response["score_text"] }
        return None

    def whois(self,domain):
        url = "{0}{1}/{2}".format(self.url,"whois",binascii.hexlify(domain.encode()).decode())
        response = self.getAPI(url)
        if response:
            return json.loads(response)["whois_text"]
        return None

    def googleSafeBrowsing(self,domain):
        url = "{0}{1}/{2}".format(self.url,"safebrowsing",binascii.hexlify(domain.encode()).decode())
        response = self.getAPI(url)
        if response:
            return json.loads(response)["issue_detected"]
        return None

    def fuzz(self,domain):
        url = "{0}{1}/{2}".format(self.url,"fuzz",binascii.hexlify(domain.encode()).decode())
        response = self.getAPI(url)
        if response:
            response = json.loads(response)
            result = []
            for domain in response["fuzzy_domains"]:
                result.append({ "domain": domain["domain"], "fuzzer" : domain["fuzzer"] })
            return result
        return None

    def report(self,domain):
        url = "{0}{1}?pd={2}".format(self.url,"webui",domain)
        response = self.getAPI(url)
        if response:
            response = json.loads(response)
            return { "ip" : response["a"]["ip"], "when" : response["a"]["when"], "mx" : response["mx"] }
        return None

