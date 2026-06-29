


def solve():
    class Heap:
        def __init__(self):
            self.arr = []

        def insert(self, val):
            self.arr.append(val)
            cur_index = len(self.arr)-1
            while(cur_index!=0):
                parent_index = (cur_index-1)//2
                if(self.arr[parent_index]>self.arr[cur_index]):
                    self.arr[parent_index], self.arr[cur_index] = self.arr[cur_index], self.arr[parent_index]
                cur_index = parent_index


        def heapify(self, index):
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < len(self.arr) and self.arr[left_child] < self.arr[index]:
                self.arr[index], self.arr[left_child] = self.arr[left_child], self.arr[index]
                self.heapify(left_child)

            if right_child < len(self.arr) and self.arr[right_child] < self.arr[index]:
                self.arr[index], self.arr[right_child] = self.arr[right_child], self.arr[index]
                self.heapify(right_child)

        def delete_from_heap(self):
            index = 0
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.arr.pop()
            self.heapify(index)

    if __name__== '__main__':
        h1 = Heap()
        n = int(input())
        for _ in range(n):
            command = list(map(str, input().split()))
            if(command[0]=="insert"):
                value = int(command[1])
                h1.insert(value)
            elif(command[0]=="delete"):
                h1.delete_from_heap()
            elif(command[0=="print"]):
                print(*h1.arr)


if __name__ == "__main__":
    solve()
