import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')

def add(a, b):
    q = a + b
    return q

a = 1
b = 2

add = add(a, b)
logging.debug(add)