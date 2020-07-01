#!/usr/bin/python3

import os
import re
import sys

input_fh = open('/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/application.xml', 'r')
output_fh = open('/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/application_new.xml', 'w')

for line in input_fh.readlines():
    if 'TrialSerialNumber' in line:

        match = re.search('TrialSerialNumber">(\d+)<', line)
        if match:
            id = match.group(1)
            id = int(id) + 1
            print("New TrialSerialNumber ID is %s." % id)
        else:
            print("Error: Found TrialSerialNumber but not matching ID.")
            sys.exit(1)

        line = re.sub('TrialSerialNumber">\d+<', 'TrialSerialNumber">%s<' % id, line)

    output_fh.write(line)
os.remove('/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/application.xml')
os.rename('/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/application_new.xml', '/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/application.xml')

