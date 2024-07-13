import time
import logging

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function {func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def task(n):
    result = 0
    for i in range(n):
        result +=1
    return result

logging.basicConfig(level=logging.INFO)
task(1000000)
