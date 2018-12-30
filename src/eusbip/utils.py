import functools
import subprocess


@functools.wraps(subprocess.run)
def run(*args, **kwarg):
    return subprocess.run(*args, **kwargs)
