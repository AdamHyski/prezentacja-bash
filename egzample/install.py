#!/usr/bin/env python3
from pathlib import Path

# Tworzymy śmietnik
# getconf ARG_MAX + 1
for i in range(2097152+1):
    Path('./tmp/'+str(i)+'.tmp').touch()
    if i % 100000 == 0 :
        print ( i )
