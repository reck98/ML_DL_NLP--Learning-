from utils.logger import getLogger
from test.operators import addFunc

logger_ = getLogger(__name__)

sum = addFunc(2555, "hye")
print(sum)

logger_.info("The main function completed")