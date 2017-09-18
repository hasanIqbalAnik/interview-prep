"""
https://en.wikipedia.org/wiki/Thread_(computing)

Multi Programming:
More than one program, like excel and access is active at the same time. If one program is waiting for an I/O
then the other can be loaded in the cpu to keep it busy.

Multi Processing:
While multi-programming refers to softwares, multi-processing refers to hardwares. In this case, a computer
system would have multiple processors available. A system can perform multiprogramming on multiple processors.

Multi Tasking:
Task and process is used interchangeably nowadays. In this case, multiple process can be executed at the same time.

Multi Threading:
A process can have a number of threads, depending on the actual programming. Each thread can run in parallel.


Threads are the smallest sequence of programmed instructions that can be managed independently by a scheduler.
In most cases, a thread is part of a process. Multiple threads can be of the same process and share the
same resources such as memory, while different processes don't share them.

a very good reference link:
https://www.youtube.com/watch?v=EvbA3qVMGaw
"""

"""
the following examples are taken from : 
https://en.wikibooks.org/wiki/Python_Programming/Threading
"""
import threading
import time


def loop_1_to_10():
    for i in range(1, 11, 1):
        time.sleep(0.5)
        print(i)

# threading.Thread(target=loop_1_to_10).start()


"""object based example of threads"""


class MyThread(threading.Thread):
    def run(self):
        print('{} started!'.format(self.getName()))
        time.sleep(.7)
        print('{} finished!'.format(self.getName()))


for x in range(4):
    my_thread = MyThread()
    my_thread.start()  # individual threads should be started with this call.
    # else it would be a sequential execution anyways
    time.sleep(.3)  # a smaller time in the main thread.