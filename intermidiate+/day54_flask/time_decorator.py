import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    function()
    ttime = time.time()
    running_time = ttime - current_time
    print(running_time)
    return function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()