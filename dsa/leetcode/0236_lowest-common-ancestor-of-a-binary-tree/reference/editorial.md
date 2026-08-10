
## Solution

First the given nodes `p` and `q` are to be searched in a binary tree and then their lowest common ancestor is to be found. We can resort to a normal tree traversal to search for the two nodes. Once we reach the desired nodes `p` and `q`, we can backtrack and find the lowest common ancestor.

<center>
<img src="images/236_LCA_Binary_1.png" width="600"/>
</center>

### Approach 1: Recursive Approach

**Intuition**

The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of the nodes `p` or `q`, return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a `True` flag. It can also be the node which itself is one of `p` or `q` and for which one of the subtree recursions returns a `True` flag.

Let us look at the formal algorithm based on this idea.

**Algorithm**

1. Start traversing the tree from the root node.
2. If the current node itself is one of `p` or `q`, we would mark a variable `mid` as `True` and continue the search for the other node in the left and right branches.
3. If either of the left or the right branch returns `True`, this means one of the two nodes was found below.
4. If at any point in the traversal, any two of the three flags `left`, `right` or `mid` become `True`, this means we have found the lowest common ancestor for the nodes `p` and `q`.

Let us look at a sample tree and we search for the lowest common ancestor of two nodes `9` and `11` in the tree.

<center>

![Slide 1](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_2.png)

![Slide 2](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_3.png)

![Slide 3](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_4.png)

![Slide 4](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_5.png)

![Slide 5](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_6.png)

![Slide 6](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_7.png)

![Slide 7](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_8.png)

![Slide 8](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_9.png)

![Slide 9](images/slideshow_236_LCA_Binary_Tree_1_236_LCA_Binary_10.png)

</center>

Following is the sequence of nodes that are followed in the recursion:

<pre>
1 --> 2 --> 4 --> 8
BACKTRACK 8 --> 4
4 --> 9 (ONE NODE FOUND, return True)
BACKTRACK 9 --> 4 --> 2
2 --> 5 --> 10
BACKTRACK 10 --> 5
5 --> 11 (ANOTHER NODE FOUND, return True)
BACKTRACK 11 --> 5 --> 2

2 is the node where we have left = True and right = True and hence it is the lowest common ancestor.
</pre>

```python
class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

* Space Complexity: $O(N)$. This is because the maximum amount of space utilized by the recursion stack would be $N$ since the height of a skewed binary tree could be $N$.
<br/>
<br/>

---

### Approach 2: Iterative using parent pointers

**Intuition**

If we have parent pointers for each node we can traverse back from `p` and `q` to get their ancestors. The first common node we get during this traversal would be the LCA node. We can save the parent pointers in a dictionary as we traverse the tree.

**Algorithm**

1. Start from the root node and traverse the tree.
2. Until we find `p` and `q` both, keep storing the parent pointers in a dictionary.
3. Once we have found both `p` and `q`, we get all the ancestors for `p` using the parent dictionary and add to a set called `ancestors`.
4. Similarly, we traverse through ancestors for node `q`. If the ancestor is present in the ancestors set for `p`, this means this is the first ancestor common between `p` and `q` (while traversing upwards) and hence this is the LCA node.

```python
class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
```

**Complexity Analysis**

* Time Complexity : $O(N)$, where $N$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

* Space Complexity : $O(N)$. In the worst case space utilized by the stack, the parent pointer dictionary and the ancestor set, would be $N$ each, since the height of a skewed binary tree could be $N$.
<br>
<br>

---

### Approach 3: Iterative without parent pointers

**Intuition**

In the previous approach, we come across the LCA during the backtracking process. We can get rid of the backtracking process itself. In this approach we always have a pointer to the probable LCA and the moment we find both the nodes we return the pointer as the answer.

**Algorithm**

1. Start with root node.
2. Put the $(root, \text{root}_{state})$ on to the stack. $\text{root}_{state}$ defines whether one of the children or both children of `root` are left for traversal.
3. While the stack is not empty, peek into the top element of the stack represented as $(\text{parent}_{node}, \text{parent}_{state})$.
4. Before traversing any of the child nodes of $\text{parent}_{node}$ we check if the $\text{parent}_{node}$ itself is one of `p` or `q`.
5. First time we find either of `p` or `q`, set a boolean flag called `one_node_found` to `True`. Also start keeping track of the lowest common ancestors by keeping a note of the top index of the stack in the variable $\text{LCA}_{index}$. Since all the current elements of the stack are ancestors of the node we just found.
6. The second time $\text{parent}_{node} = p or \text{parent}_{node} = q$ it means we have found both the nodes and we can return the `LCA node`.
7. Whenever we visit a child of a $\text{parent}_{node}$ we push the $(\text{parent}_{node}, updated_parent_state)$ onto the stack. We update the state of the parent since a child/branch has been visited/processed and accordingly the state changes.
8. A node finally gets popped off from the stack when the state becomes $\text{BOTH}_{DONE}$ implying both left and right subtrees have been pushed onto the stack and processed. If `one_node_found` is `True` then we need to check if the top node being popped could be one of the ancestors of the found node. In that case we need to reduce $\text{LCA}_{index}$ by one. Since one of the ancestors was popped off.

> Whenever both `p` and `q` are found, $\text{LCA}_{index}$ would be pointing to an index in the stack which would contain all the common ancestors between `p` and `q`. And the $\text{LCA}_{index}$ element has the `lowest` ancestor common between p and q.

<center>

![Slide 1](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_11.png)

![Slide 2](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_12.png)

![Slide 3](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_13.png)

![Slide 4](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_14.png)

![Slide 5](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_15.png)

![Slide 6](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_16.png)

![Slide 7](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_17.png)

![Slide 8](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_18.png)

![Slide 9](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_19.png)

![Slide 10](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_20.png)

![Slide 11](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_21.png)

![Slide 12](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_22.png)

![Slide 13](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_23.png)

![Slide 14](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_24.png)

![Slide 15](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_25.png)

![Slide 16](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_26.png)

![Slide 17](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_27.png)

![Slide 18](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_28.png)

![Slide 19](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_29.png)

![Slide 20](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_30.png)

![Slide 21](images/slideshow_236_LCA_Binary_Tree_2_236_LCA_Binary_31.png)

</center>

The animation above shows how a stack is used to traverse the binary tree and keep track of the common ancestors between nodes `p` and `q`.

```python
class Solution:

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None
```

**Complexity Analysis**

* Time Complexity : $O(N)$, where $N$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree. The advantage of this approach is that we can prune backtracking. We simply return once both the nodes are found.

* Space Complexity : $O(N)$. In the worst case the space utilized by stack would be $N$ since the height of a skewed binary tree could be $N$.

<br/>