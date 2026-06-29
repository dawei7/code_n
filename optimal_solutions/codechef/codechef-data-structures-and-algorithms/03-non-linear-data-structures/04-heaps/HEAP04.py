


def solve():
    class Heap:
        def __init__(self):
            self.arr = []

        def insert(self, val): # Define a method to insert a value into the heap
            self.arr.append(val) # Append the value to the end of the list
            cur_index = len(self.arr) - 1 # Index of the newly inserted element

            # Perform heapify-up operation
            while cur_index != 0: # Continue until reaching the root (index 0)
                parent_index = (cur_index - 1) // 2 # Calculate the index of the parent node
                if self.arr[parent_index] > self.arr[cur_index]: # If the parent node is greater than the current node
                    # Swap the parent node with the current node
                    self.arr[parent_index], self.arr[cur_index] = self.arr[cur_index], self.arr[parent_index]
                cur_index = parent_index # Move up to the parent node

    if __name__== '__main__':
        n = int(input())
        h1 = Heap()
        nums = list(map(int, input().split()))
        for i in nums:
            h1.insert(i)
        print(*h1.arr)


if __name__ == "__main__":
    solve()
