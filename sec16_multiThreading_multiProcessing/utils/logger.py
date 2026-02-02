import logging
from pathlib import Path


PATH = Path('./logs/debug.log')
PATH.parent.mkdir(exist_ok=True, parents=True)
PATH.touch(exist_ok=True)


logging.basicConfig(
    filemode='w',
    filename=str(PATH),
    level=logging.DEBUG,
    format="%(asctime)s || %(name)s || %(levelname)s || %(message)s",
    force=True
)

def getLogger(name : str):
    return logging.getLogger(name)

