import random
import time

def expensive_function():
    execution_time = random.random() / 100
    time.sleep(execution_time)
    
if __name__ == '__main__':
    for _ in range(1000):
        expensive_function()