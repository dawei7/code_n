


def solve():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def removeDuplicates(head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def buildLinkedList(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for num in arr[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def printLinkedList(head):
        current = head
        res = []
        while current:
            res.append(str(current.val))
            current = current.next
        print(" ".join(res))

    if __name__ == "__main__":
        import sys
        data = sys.stdin.read().strip().split()
        if not data:
            exit()
        t = int(data[0])
        index = 1
        for _ in range(t):
            n = int(data[index])
            index += 1
            arr = list(map(int, data[index:index+n]))
            index += n
            head = buildLinkedList(arr)
            new_head = removeDuplicates(head)
            printLinkedList(new_head)


if __name__ == "__main__":
    solve()
