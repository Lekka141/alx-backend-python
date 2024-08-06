#!/usr/bin/env python3

import asyncio
import sys
from os.path import dirname, abspath

# Add the parent directory to the path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await measure_runtime()

print(asyncio.run(main()))
