


def solve():
    def inorder_traverse(root, val, min_dif):
        if root is None:
            return min_dif
        min_dif = inorder_traverse(root.left, val, min_dif)
        if val[0] >= 0:
            min_dif = min(min_dif, root.val - val[0])
        val[0] = root.val
        min_dif = inorder_traverse(root.right, val, min_dif)
        return min_dif

    def print_min_difference(root):
        min_dif = float('inf')
        val = [-1]
        ans = inorder_traverse(root, val, min_dif)
        print(ans)


if __name__ == "__main__":
    solve()
