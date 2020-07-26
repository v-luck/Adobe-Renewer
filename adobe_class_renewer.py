#!/usr/bin/python3

import os
import re
import sys

class adobe_locations():
    def __init__(self, programLocation, programName):
        self.programLocation = programLocation + "application.xml"
        self.newXml = programLocation + "application_new.xml"
        self.programName = programName
    def renewTrial(self):
        input_fh = open(self.programLocation, 'r')
        output_fh = open(self.newXml, 'w')
        for line in input_fh.readlines():
            if 'TrialSerialNumber' in line:
                match = re.search('TrialSerialNumber">(\d+)<', line)
                if match:
                    id = match.group(1)
                    id = int(id) + 1
                    print("New TrialSerialNumber ID  for " + self.programName + " is %s." % id)
                else:
                    print("Error: Found TrialSerialNumber but not matching ID.")
                    sys.exit(1)

                line = re.sub('TrialSerialNumber">\d+<', 'TrialSerialNumber">%s<' % id, line)

            output_fh.write(line)
        os.remove(self.programLocation)
        os.rename(self.newXml, self.programLocation)

adobe_illustrator = adobe_locations('/mnt/c/Program Files/Adobe/Adobe Illustrator CC 2018/Support Files/Contents/Windows/AMT/', "Adobe Illustrator")
adobe_photoshop = adobe_locations('/mnt/c/Program Files/Adobe/Adobe Photoshop CC 2018/AMT/', "Photoshop")
adobe_after_effects = adobe_locations('/mnt/c/Program Files/Adobe/Adobe After Effects CC 2018/Support Files/AMT/', "After Effects")
adobe_premiere_pro= adobe_locations('/mnt/c/Program Files/Adobe/Adobe Premiere Pro CC 2018/AMT/', "Premiere Pro")
test = adobe_locations('/mnt/c/users/Bobba/Downloads/test/', "Test")
test.renewTrial()
