class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder, in_start, in_end, post_start, post_end, index_map):
    if in_start > in_end or post_start > post_end:
        return None
    root_val = postorder[post_end]
    root = Node(root_val)
    in_root_index = index_map[root_val]
    left_tree_size = in_root_index - in_start
    root.left = build_tree(inorder, postorder, in_start, in_root_index - 1, post_start, post_start + left_tree_size - 1, index_map)
    root.right = build_tree(inorder, postorder, in_root_index + 1, in_end, post_start + left_tree_size, post_end - 1, index_map)
    return root

def preorder_traversal(root, res):
    if root:
        res.append(root.val)
        preorder_traversal(root.left, res)
        preorder_traversal(root.right, res)

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        inorder = list(map(int, data[index:index + n]))
        index += n
        postorder = list(map(int, data[index:index + n]))
        index += n
        index_map = {val: idx for idx, val in enumerate(inorder)}
        root = build_tree(inorder, postorder, 0, n - 1, 0, n - 1, index_map)
        res = []
        preorder_traversal(root, res)
        output_lines.append(' '.join(map(str, res)))
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
