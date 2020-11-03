from pathlib import Path
import os.path


def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()
