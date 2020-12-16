import os
#yara-python !yara
import yara
import glob

def getRuleFiles():
    ruleFiles = {}
    files = glob.glob("plugins/datasee/rules" "/**/*.rule", recursive=True)
    for f in files:
        ruleFiles["namespace{0}".format(len(ruleFiles))] = f
    return ruleFiles

def loadRules():
    if os.path.isfile("plugins/datasee/rules.complied"):
        rules = yara.load('plugins/datasee/rules.complied')
    else:
        rules = yara.compile(filepaths=getRuleFiles())
        rules.save("plugins/datasee/rules.complied")
    return rules