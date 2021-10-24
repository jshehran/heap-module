# heap-module
Write generator merge(…) which accepts as arguments an arbitrary number of iterables, each of which
generates sorted numbers, not necessarily one after another. merge() must merge the outputs of the
iterables, i.e. give a sorted queue of all the numbers from the input iterables. merge() must correctly stop if
all of the input iterables have stopped. Please supply unit tests for your solution.
E.g., the input iterables are three generators giving the following numbers:
Iterable 1: 1, 5, 9
Iterable 2: 2, 5
Iterable 3: 1, 6, 10, 11
The sequence generated by merge(…) in this case must be: 1, 1, 2, 5, 5, 6, 9, 10, 11
NOTE: There exists a standard python solution based on heapq.merge, but we would like that you write
your solution from scratch without using heapq module.
Once Finished
Share the link to a public online repository containing the solution implemented.
NOTE: If not finished, but running out of time, please share your implementation anyway. We will be glad to
evaluate it anyway.