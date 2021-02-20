# RegEx - Regular Expression
import re


txt = "The          rain     in      Spain"
x = re.sub("in", '**', txt)
x = re.sub("\s+", ' ', txt)

print(x)
