import logging 
from pathlib import Path

FILEPATH = Path('./utils/debug.log')
FILEPATH.parent.mkdir(parents=True, exist_ok=True)
FILEPATH.touch(exist_ok=True)

logging.basicConfig(
    filename=str(FILEPATH),
    filemode='a',
    level=logging.DEBUG,
    format="%(asctime)s || %(name)s || %(levelname)s || %(message)s",
    force=True
)


def getLogger(name : str) -> logging.Logger:
    return logging.getLogger(name)




