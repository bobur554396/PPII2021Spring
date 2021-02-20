# RegEx - Regular Expression
import re


txt = "The          rain     in      Spain"
x = re.split("in", txt)
x = re.split(" ", txt)
x = re.split("\s+", txt)
x = re.split("\s+", txt, 2)

print(x)
