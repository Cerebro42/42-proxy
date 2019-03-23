import re
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

VERSION_RE = re.compile(r"__version__\s*=\s*\"(.*?)\"")

current_path = abspath(dirname(__file__))

with open(join(current_path, "42proxy", "__init__.py")) as file:
    result = VERSION_RE.search(file.read())
    if result is None:
        raise Exception("could not find package version")
    __version__ = result.group(1)

setup(
    name="42proxy",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    description=open("README.md").read(),
    author="Charles Labourier`",
    author_email="clabouri@student.42.fr",
    zip_safe=True,
)
