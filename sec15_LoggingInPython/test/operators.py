from utils.logger import getLogger

logger_ = getLogger(__name__)

def addFunc(*args : int) -> int:
    sum = 0
    logger_.info("The function is called")

    try:
        for i in args:
            sum += i
        logger_.info("The function calculates sum")
        return sum
    except Exception as err:
        logger_.error(f"An error occured as {err}")
    
    return None
        
