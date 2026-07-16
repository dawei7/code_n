def solve(nums: list[int]) -> int:
    modulus = 1_000_000_007
    size = len(nums)

    factorial = [1] * (size + 1)
    for value in range(1, size + 1):
        factorial[value] = factorial[value - 1] * value % modulus

    inverse_factorial = [1] * (size + 1)
    inverse_factorial[size] = pow(factorial[size], modulus - 2, modulus)
    for value in range(size, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

    insertion_time = [0] * size
    for time, key in enumerate(nums):
        insertion_time[key - 1] = time

    left_child = [-1] * size
    right_child = [-1] * size
    stack: list[int] = []

    for key in range(size):
        last_popped = -1
        while stack and insertion_time[stack[-1]] > insertion_time[key]:
            last_popped = stack.pop()
        if stack:
            right_child[stack[-1]] = key
        if last_popped != -1:
            left_child[key] = last_popped
        stack.append(key)

    root = stack[0]
    traversal = [root]
    order: list[int] = []
    while traversal:
        node = traversal.pop()
        order.append(node)
        if left_child[node] != -1:
            traversal.append(left_child[node])
        if right_child[node] != -1:
            traversal.append(right_child[node])

    subtree_size = [0] * size
    ways = [1] * size

    for node in reversed(order):
        left = left_child[node]
        right = right_child[node]
        left_size = subtree_size[left] if left != -1 else 0
        right_size = subtree_size[right] if right != -1 else 0
        interleavings = (
            factorial[left_size + right_size]
            * inverse_factorial[left_size]
            * inverse_factorial[right_size]
        ) % modulus

        subtree_size[node] = left_size + right_size + 1
        ways[node] = interleavings
        if left != -1:
            ways[node] = ways[node] * ways[left] % modulus
        if right != -1:
            ways[node] = ways[node] * ways[right] % modulus

    return (ways[root] - 1) % modulus
