
import re

string = str(input("Input your string:"))
parser = re.compile(r'\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.'
                    r'([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])')
for_print = "не валідний"

for el in parser.finditer(string):
    if el.group() == string:
        for_print = "валідний"

print(for_print)
print(string)
