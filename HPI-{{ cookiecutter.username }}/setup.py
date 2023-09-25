from typing import Iterator
from setuptools import setup, find_namespace_packages


def subpackages() -> Iterator[str]:
    # filter to only folders starting with my.
    for p in find_namespace_packages("."):
        if p.startswith("my"):
            yield p


def main() -> None:
    setup(
        # use a unique name, so that egg-link installs have unique filepaths
        name="HPI-{{ cookiecutter.username }}",
        packages=list(subpackages()),
        # reminder: should use mypy's --namespace-packages flag
        # when importing from my/ so it can discover the py.typed properly
        package_data={"my": ["py.typed"]},
        # dependencies
        install_requires=[],
        extras_require={
            "testing": [
                "pytest",
                "mypy",
            ]
        },
    )


if __name__ == "__main__":
    main()
