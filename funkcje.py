import re

def findFunctions(file):
    fileContent = open(file).read()
    regex = r"def[\s]+([a-zA-Z_0-9]+)\(.*\)[ ]*\:"
    matches = re.findall(regex, fileContent, re.MULTILINE)
    return matches
