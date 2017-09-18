"""
Deadlock is a situation when multiple threads or processes enters in a waiting state because a resource
it requested is being held by other thread or process. Example of a deadlock: Dining philosopher problem.
It occurs when all the following four conditions are held true(Coffman Conditions):

1. mutual exclusion: resources must be unsharable.
2. hold and wait: a thread is holding a resource and waiting for another
3. no-preemption: a resource may only be released voluntarily by a thread
4. circular wait: each process or thread is waiting for each of the other processes.

ostrich algorithm: ignoring deadlock like an ostrich, sticking it's head in the sand.
banker's algorithm: each process must declare it's maximum wanted resource before it is allocated any. the algorithm
checks whether this is ok or not.


Livelock:

"""