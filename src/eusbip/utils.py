import functools
import subprocess


@functools.wraps(subprocess.run)
def run(*args, **kwargs):
    return subprocess.run(*args, **kwargs)
