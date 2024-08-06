#!/usr/bin/env python3

import asyncio
import sys
from os.path import dirname, abspath

# Add the parent directory to the path
sys.path.insert(0, dirname(dirname(abspath(__file__))))

async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
