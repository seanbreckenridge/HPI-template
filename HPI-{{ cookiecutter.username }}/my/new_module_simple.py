"""
An basic example of a new module. If this is just a personal
module, you might be fine hardcoding inputs or not using caching

These no requirement to import anything from my.core, it just has
a lot of helper functions for logging/caching etc.

see the _complex.py file for a more complete example
"""

from typing import Iterator
from pathlib import Path


# can use 'hpi query my.new_module_simple' to test

def results() -> Iterator[float]:
    # get modification time
    for f in Path("~/Downloads").expanduser().glob("*"):
        yield f.stat().st_mtime
