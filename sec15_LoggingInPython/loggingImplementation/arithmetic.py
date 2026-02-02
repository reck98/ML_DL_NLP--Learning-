from logger import getLogger

logger_ = getLogger(__name__)


def add(*args : int):
    logger_.info("The function is called")
    sum = 0
    
    try:
        for i in args:
            sum += i
        logger_.info("The function calculates the sum properly and returns the value ")
        return sum
    except Exception as err:
        logger_.error(f"An error occurred as {err}")
    
    return None


