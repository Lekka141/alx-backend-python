#!/usr/bin/env python3

import asyncio
import sys
from os.path import dirname, abspath

# Add the parent directory to the path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
