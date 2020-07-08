#!/usr/bin/env python3
from pathlib import Path

# Tworzymy śmietnik
for i in range(3000000):
    Path('./tmp/'+str(i) ).touch()
