


def solve():
    class Solution:
        def copyRandomList(self, head):
            if not head:
                return None
            # Create a mapping from original node to copied node
            node_map = {}
            curr = head
            # First pass: copy all nodes
            while curr:
                node_map[curr] = Node(curr.data)
                curr = curr.next

            curr = head
            # Second pass: assign next and random pointers
            while curr:
                copy_node = node_map[curr]
                copy_node.next = node_map[curr.next] if curr.next else None
                copy_node.random = node_map[curr.random] if curr.random else None
                curr = curr.next
            return node_map[head]


if __name__ == "__main__":
    solve()
