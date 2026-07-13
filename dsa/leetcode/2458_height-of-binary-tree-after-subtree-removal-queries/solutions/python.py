class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, queries: list[int]) -> list[int]:
    node_height = {}

    def get_height(node):
        if not node:
            return -1

        h = 1 + max(get_height(node.left), get_height(node.right))
        node_height[node.val] = h
        return h

    get_height(root)

    ans = {}

    def compute_results(node, depth, best_without_subtree):
        if not node:
            return

        ans[node.val] = best_without_subtree

        left_h = node_height[node.left.val] if node.left else -1
        right_h = node_height[node.right.val] if node.right else -1

        compute_results(node.left, depth + 1, max(best_without_subtree, depth + 1 + right_h))
        compute_results(node.right, depth + 1, max(best_without_subtree, depth + 1 + left_h))

    compute_results(root, 0, 0)
    return [ans[q] for q in queries]
