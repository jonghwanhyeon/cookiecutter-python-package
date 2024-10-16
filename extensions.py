from typing import List, Tuple

from cookiecutter.utils import simple_filter


def parse_version(version: str) -> Tuple[int, int]:
    major, minor = version.split(".", maxsplit=1)
    return (int(major), int(minor))


@simple_filter
def python_requires(python_versions: List[str], python_requires: str) -> str:
    matches = []

    for python_version in python_versions:
        if parse_version(python_version) >= parse_version(python_requires):
            matches.append('"{}"'.format(python_version))

    return ", ".join(matches)
