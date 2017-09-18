"""
https://en.wikipedia.org/wiki/Process_(computing)

A process is an instance of a computer program in execution. It contains
* an image of the executable machine code
* memory(executable code, process specific data including input and output, call stack, heap to hold intermediate
    data generated during the execution.
* OS system descriptors of resources allocated to this process, such as file descriptors or handles.
* security attributes such as the process owner and set of permissions.
* context, such as the registers and physical memory addressing. it's typically stored in the registers when
    the process is executing.


A process can be in any of the following states:
created -> waiting -> running -> blocked -> terminated.

A few examples of working with processes is given below:

"""

import psutil

import multiprocess
import os
import time


def list_process():
    return [(proc.name(), proc.pid, proc.memory_full_info()) for proc in psutil.process_iter() if proc.name().__contains__('python')]

for item in list_process():
    print item

print multiprocess.Process()