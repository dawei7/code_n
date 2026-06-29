


def solve():
    class Solution:
        def next_smaller_value(self, head):
            if head is None:
                return None
            nodes = []
            curr = head
            while curr:
                nodes.append(curr)
                curr = curr.next
            n = len(nodes)
            result = [-1] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and stack[-1] >= nodes[i].val:
                    stack.pop()
                result[i] = stack[-1] if stack else -1
                stack.append(nodes[i].val)
            for i in range(n):
                nodes[i].val = result[i]
            return head


if __name__ == "__main__":
    solve()
