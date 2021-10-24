#!/usr/bin/env python3
"""
Program generates an iterable of sorted numbers from input iterables.
We use Heap data structure for improved performance over the list type
"""

from heapq import heapify, heappush, heappop
from itertools import repeat
import argparse




def merge(*args):
    """ Generate an iterable of sorted numbers from iterables passed as input arguments """

    # Convert the arguments into a list of iterators
    itrs = [iter(i) for i in args]
    remaining_itr_count = len(itrs)

    # Check corner case
    if not remaining_itr_count:
        return

    # Create a heap to store checked values
    checked_values = []
    heapify(checked_values)

    while True:
        for i, it in enumerate(itrs):
            try:
                value = next(it)
                if value is not None:
                    heappush(checked_values, value)
                    if i >= remaining_itr_count - 1:
                        # pop the min value from checked_values
                        yield heappop(checked_values)
            except StopIteration:
                remaining_itr_count -= 1
                itrs[i] = repeat(None)
                if not remaining_itr_count:
                    while len(checked_values) > 0:
                        # Yield the remaining checked_values
                        yield heappop(checked_values)
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    merge(args)