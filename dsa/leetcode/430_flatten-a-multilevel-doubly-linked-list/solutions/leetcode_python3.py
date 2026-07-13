class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        stack = [head]
        previous = None
        while stack:
            current = stack.pop()
            if current.next is not None:
                stack.append(current.next)
            if current.child is not None:
                stack.append(current.child)
            if previous is not None:
                previous.next = current
                current.prev = previous
            current.child = None
            previous = current
        return head
