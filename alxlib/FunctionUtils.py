import time


def time_this_function(fn, times, *args):
    """
    Measure the time it takes to execute a function multiple times.

    Parameters:
        fn (callable): The function to be timed.
        times (int): The number of times to execute the function.
        *args: Variable number of arguments to be passed to the function.

    Returns:
        float: The total time taken to execute the function `times` times.

    Example:
        time_this_function(my_function, 100, arg1, arg2) returns the total time taken to execute my_function 100 times.
    """
    # Record the start time
    tic = time.perf_counter()

    # Execute the function 'times' number of times
    for _ in range(0, times):
        fn(*args)

    # Record the end time
    toc = time.perf_counter()

    # Return the total time taken
    return toc - tic
