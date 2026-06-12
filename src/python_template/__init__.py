from importlib import metadata

__all__ = ["__version__"]
# TIP: Change it to the name of your repository
# NOTE: It has to match what you've written in pyproject.toml
PACKAGE_NAME = "python-template"

try:
    __version__ = metadata.version(PACKAGE_NAME)
except metadata.PackageNotFoundError:
    __version__ = "0.1.dev1+UNKNOWN"
