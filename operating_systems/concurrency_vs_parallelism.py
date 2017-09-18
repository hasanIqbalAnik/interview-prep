"""
Concurrency issues are critical in a multi-threading environment.

"Concurrency is about dealing with lots of things at once, parallelism is about doing lots of things at once."

For example: mouse, keyboard, display drivers do not necessarily run parallely but concurrently.
On the other hand, an image can be converted from colored to black and white parallely, but converting a portion of the
image in a different processor.

parallel is the opposite of serial,
concurrent is the opposite of sequential.
"""


from multiprocessing.dummy import Pool as ThreadPool
import timeit


"""
locks
The broad definition of the methods used to prevent multiple threads from accessing a resource at the same time. 
Semaphores are examples of locks. 

"""
"""
semaphores
Semaphores are general purpose locks. The difference with mutexes is, a lock by mutex can only be released by the program 
which acquired it. But a semaphore can be signaled to be unlocked. So it's more suitable than mutexes for problems like
producer consumer. 
A semaphore is just a counter. 
"""
"""
mutexes
a mutex is a simple binary semaphore, allowing only one thread at a time. For example, a file handling mutex 
would allow only one program to access it at the same time. These two are used for different purposes. While mutex 
ensures exclusive access to a resource, semaphores provides a way to control a number of processes. 
For example, one toilet with one key is like mutex, 4 toilets with 4 keys are like semaphores. if all 4 toilets are busy
the semaphore count is 0, if one person leaves, it's increased to one.   
"""
"""
monitors
semaphores provide a foundation for implementing solutions to synchronization problems. But it's not enough.
Monitors is an object, designed to be accessed from multiple threads. A monitor can allow n threads with conditional
variables. In some cases, only mutual exclusion is not enough. Threads may need to wait until some condition is true. 

"""
"""
dining philosopher problem
"""
"""
scheduling
"""
"""
how context switching works
"""

"""
the following code is taken from https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
"""


def cuber(x):
    return x * x * x


inp_arr = [x for x in range(10000)]
pool = ThreadPool(5)
result = pool.map(cuber, inp_arr)
start_time = timeit.default_timer()
# result = map(cuber, inp_arr)
print('elapsed: {}', timeit.default_timer() - start_time)  # 0.0000014 in case of threads, .0015 without threads

print result
