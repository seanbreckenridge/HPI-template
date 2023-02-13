"""
An extensive example module file with the common structure for a module

You may not need all of this for every module; this includes:

- user config using 'get_files'
- typical result NamedTuple w/ TypeVar/parse functions
- logging using the core module, allows overriding with --debug/HPI_LOGS environment variable
- optional caching using mcachew (https://github.com/karlicoss/cachew)
"""

# TODO: uncomment this once you've defined something in your config file
# from my.config import new_module_complex as user_config

from typing import Sequence, Iterator, NamedTuple

from my.core import dataclass, Paths, Path, get_files, LazyLogger
from my.core.common import mcachew


# stub example config, can remove this if you add something to 'my.config'
class user_config:
    export_path: Paths = "~/Downloads/*"


logger = LazyLogger(__name__, level="info")


@dataclass
class config(user_config):
    # path[s]/glob to the export files
    export_paths: Paths


def inputs() -> Sequence[Path]:
    # uses 'get_files' to resolve globs/paths
    return get_files(config.export_path)


# the output of this module
class Result(NamedTuple):
    path: str


# shorthand variable for the output of this module
Results = Iterator[Result]

# can use 'hpi --debug query my.new_module_complex' to test


# cache refreshes whenever items are added/removed from inputs(); pass logger to cachew
@mcachew(depends_on=lambda: [str(f) for f in inputs()], logger=logger)
def results() -> Results:
    for file in inputs():
        for result in _parse_file(file):
            yield result


def _parse_file(input_file: Path) -> Results:
    # TODO: handle parsing this input file
    logger.info(f"Parsing {input_file}")
    yield Result(path=str(input_file.absolute()))
