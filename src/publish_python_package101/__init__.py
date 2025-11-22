from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("publish_python_package101")
except PackageNotFoundError:
    __version__ = "0.0.0"
