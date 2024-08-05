#!/usr/bin/env python3

import sys
from os.path import dirname, abspath

# Add the parent directory to the path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
