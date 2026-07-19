def solve(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    rows = height(root)
    columns = (1 << rows) - 1
    result = [[""] * columns for _ in range(rows)]

    def place(node, row, left, right):
        if node is None:
            return
        middle = (left + right) // 2
        result[row][middle] = str(node.val)
        place(node.left, row + 1, left, middle - 1)
        place(node.right, row + 1, middle + 1, right)

    place(root, 0, 0, columns - 1)
    return result
