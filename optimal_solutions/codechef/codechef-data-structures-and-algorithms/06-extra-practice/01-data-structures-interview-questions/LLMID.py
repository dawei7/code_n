


def solve():
    def getMiddleElement(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data


if __name__ == "__main__":
    solve()
