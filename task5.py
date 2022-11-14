import string
from random import sample
def get_random_password() -> str:
    alfabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = sample(alfabet, 8)
    return ''.join(password)
print(get_random_password())
