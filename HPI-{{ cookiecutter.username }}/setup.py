from typing import Iterator
from setuptools import setup, find_namespace_packages


def subpackages() -> Iterator[str]:
    # filter to only folders starting with my.
    for p in find_namespace_packages("."):
        if p.startswith("my"):
            yield p


def main() -> None:
    # use a unique name, so that egg-link installs have unique filepaths
    pkg = "HPI-{{ cookiecutter.username }}"
    setup(
        name=pkg,
        version="0.1.0",
        author="{{ cookiecutter.username }}",
        license="MIT",
        packages=list(subpackages()),
        package_data={"my": ["py.typed"]},
        zip_safe=False,
        python_requires=">=3.7",
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
