class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = None
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()

    def peek(self):
        return self.next_val

    def next(self):
        res = self.next_val
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
        else:
            self.next_val = None
        return res

    def hasNext(self):
        return self.next_val is not None

def solve(iterator_data, operations):
    """
    This function acts as a driver to demonstrate the PeekingIterator logic.
    'iterator_data' is the list to iterate over.
    'operations' is a list of method names to call.
    """
    class Iterator:
        def __init__(self, nums):
            self.nums = nums
            self.idx = 0
        def next(self):
            val = self.nums[self.idx]
            self.idx += 1
            return val
        def hasNext(self):
            return self.idx < len(self.nums)

    it = Iterator(iterator_data)
    peeking_it = PeekingIterator(it)
    results = [None]
    
    for op in operations[1:]:
        if op == "next":
            results.append(peeking_it.next())
        elif op == "peek":
            results.append(peeking_it.peek())
        elif op == "hasNext":
            results.append(peeking_it.hasNext())
            
    return results
