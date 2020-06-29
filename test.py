import re
text_to_search = '''
abcdefghijklmopqurstuvwxyz1234567890
ABCDEFGHIJKLMOPQURSTUVWXYZ1234567890

words
dragon
cool
nikecl5
'''

pattern = re.compile(r'z\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)




