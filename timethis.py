import time
from contextlib import contextmanager
import random
import string


random_strings = [''.join(random.choices(string.digits, k=10)) for _ in range(int(1e7))]


@contextmanager
def timethis(snippet):
    start = time.time()
    yield
    print(f'Duration of {snippet}: {(time.time() - start):.2f}')


print('starting')

with timethis('add strings'):
    final_string = ''
    for rs in random_strings:
        final_string += rs

with timethis('use join'):
    ''.join(random_strings)
