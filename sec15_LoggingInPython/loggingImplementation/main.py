from logging import getLogger
from arithmetic import add


logger_ = getLogger(__name__)

sum = add(37,392, "HEy this is error making")
print(sum)
# logger_.info('Executed')