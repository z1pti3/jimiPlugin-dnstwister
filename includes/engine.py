import re

from plugins.datasee.includes import yaraProcessor

def process(filename=None,data=None):
    rules = yaraProcessor.loadRules()
    result = {}
    matches = None
    if filename:
        matches = rules.match(filename, timeout=60)
    elif data:
        matches = rules.match(data=data, timeout=60)

    if matches:
        for match in matches:
            result[match.rule] = { "data" : [], "count" : 0, "tags" : match.tags }
            for string in match.strings:
                if result[match.rule]["count"] < 100:
                    result[match.rule]["data"].append({ "offset" : string[0], "id" : string[1], "text" : str(string[2]) })
                result[match.rule]["count"] += 1
        
    return result
