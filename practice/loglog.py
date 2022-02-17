import logging
import time

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')

def add(a, b):
    q = a + b
    return q

a = 1
b = 2

