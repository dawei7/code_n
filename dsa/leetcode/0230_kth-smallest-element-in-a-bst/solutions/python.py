def solve(root, k: int) -> int:
    stack = []
    current = root
    while True:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right
