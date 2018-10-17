import os
import shutil
import tempfile
from contextlib import contextmanager


def create_dir(path, rewrite=False):
    try:
        os.mkdir(path)
    except FileExistsError:
        if rewrite:
            remove_dir_tree(path)
            os.mkdir(path)


def create_temp_dir(path, prefix=""):
    return tempfile.mkdtemp(prefix=prefix, dir=path)


def remove_dir_tree(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def remove_file(path):
    os.remove(path)


def which(file):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, file)):
            return os.path.join(path, file)
    return ''


@contextmanager
def write_to_tempfile(content):
    with tempfile.NamedTemporaryFile() as file:
        with open(file.name, 'w') as f:
            f.write(content)
        yield file.name
