#!/usr/bin/env python3

class CountedIterator:
    """Define a class CountedIterator that extends the built-in iterator"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count
