class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node

        current = head
        while True:
            following = current.next
            normal_gap = current.val <= insertVal <= following.val
            wrap_gap = (
                current.val > following.val
                and (insertVal >= current.val or insertVal <= following.val)
            )
            if normal_gap or wrap_gap:
                break
            current = following
            if current is head:
                break

        node = Node(insertVal)
        node.next = current.next
        current.next = node
        return head
