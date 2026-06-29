


def solve():
    class Heap:
        def __init__(self):
            self.arr = []

        def insert(self, val):
            self.arr.append(val)
            cur_index = len(self.arr)-1
            while(cur_index!=0):
                parent_index = (cur_index-1)//2
                if(self.arr[parent_index]<self.arr[cur_index]):
                    self.arr[parent_index], self.arr[cur_index] = self.arr[cur_index], self.arr[parent_index]
                cur_index = parent_index


        def heapify(self, index):
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < len(self.arr) and self.arr[left_child] > self.arr[index]:
                self.arr[index], self.arr[left_child] = self.arr[left_child], self.arr[index]
                self.heapify(left_child)

            if right_child < len(self.arr) and self.arr[right_child] > self.arr[index]:
                self.arr[index], self.arr[right_child] = self.arr[right_child], self.arr[index]
                self.heapify(right_child)

        def delete_from_heap(self):
            index = 0
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.arr.pop()
            self.heapify(index)

    if __name__== '__main__':
        h1 = Heap()
        n, k = map(int, input().split())

        values = list(map(int, input().split()))
        for value in values:
            h1.insert(value)

        for _ in range(k - 1):
            h1.delete_from_heap()

        print(h1.arr[0])


if __name__ == "__main__":
    solve()
