# RegEx - Regular Expression
import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
x = re.search("in", txt)

print(x.start())
print(x.endpos)
print(x.span())
print(x.group())


