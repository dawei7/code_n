import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, queries: list[int]) -> list[int]:
    # Stores the height of the subtree rooted at each node
    node_height = {}
    # Stores the two largest heights found at each depth
    # depth_max_heights[depth] = [max1, max2]
    depth_max_heights = collections.defaultdict(list)
    
    def get_height(node, depth):
        if not node:
            return -1
        
        h = 1 + max(get_height(node.left, depth + 1), get_height(node.right, depth + 1))
        node_height[node.val] = h
        
        # Keep track of the two largest heights at this depth
        depth_max_heights[depth].append(h)
        depth_max_heights[depth].sort(reverse=True)
        if len(depth_max_heights[depth]) > 2:
            depth_max_heights[depth].pop()
            
        return h

    # Pre-calculate heights and depths
    get_height(root, 0)
    
    # Map node values to their depths
    node_depth = {}
    def get_depths(node, depth):
        if not node:
            return
        node_depth[node.val] = depth
        get_depths(node.left, depth + 1)
        get_depths(node.right, depth + 1)
        
    get_depths(root, 0)
    
    results = []
    for q in queries:
        d = node_depth[q]
        h = node_height[q]
        
        # If the removed node's height is the max at its depth, 
        # the new height is the second max at that depth.
        # Otherwise, it's the current max.
        max_h_at_depth = depth_max_heights[d]
        
        if len(max_h_at_depth) > 1 and max_h_at_depth[0] == h:
            new_height = d + max_h_at_depth[1]
        else:
            new_height = d + (max_h_at_depth[0] - 1 if max_h_at_depth[0] == h else max_h_at_depth[0])
            
        # The height of the tree is the max depth reached by any remaining node
        # We calculate the max height across all depths, excluding the removed branch
        # A simpler way: the height is max(depth + (second_max if max == h else max))
        # We need to find the max height of the tree after removal.
        # The height is max over all depths d' of (d' + max_height_at_d')
        # If we remove a node at depth d with height h, we only affect depth d.
        
        res = 0
        # We can optimize this by pre-calculating the max height for each depth
        # but for simplicity and correctness:
        # The height of the tree is max(depth + max_height_at_depth)
        # We pre-calculate the global max height for each depth
        pass

    # Refined approach for query processing:
    # Pre-calculate the max height of the tree if we remove the subtree at node
    ans = {}
    def compute_results(node, depth, current_max_height):
        if not node:
            return
        
        # If we remove this node, the height of the tree is current_max_height
        ans[node.val] = current_max_height
        
        # To compute the next max_height, we look at siblings
        left_h = node_height[node.left.val] if node.left else -1
        right_h = node_height[node.right.val] if node.right else -1
        
        compute_results(node.left, depth + 1, max(current_max_height, depth + 1 + right_h))
        compute_results(node.right, depth + 1, max(current_max_height, depth + 1 + left_h))

    compute_results(root, 0, 0)
    return [ans[q] for q in queries]
