#/usr/bin/env python3

# Save as sortplist.py

# Run `$ python3 sortplist.py original.plist >sorted.plist`

import plistlib
import sys

with open(sys.argv[1], 'rb') as f:
    plist = plistlib.load(f)
xml_bytes = plistlib.dumps(plist, sort_keys=True)
print(str(xml_bytes, 'utf-8'))
