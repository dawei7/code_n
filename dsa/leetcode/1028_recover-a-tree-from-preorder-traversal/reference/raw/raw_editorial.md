## Solution

---

### Overview

We are given a string representation of a preorder traversal of a binary tree, where each node is represented as `D` dashes followed by its value. The number of dashes `D` indicates the depth of the node in the tree, with the root having depth `0`. Each node may have one or two children, and if a node has only one child, it is always the left child. Our task is to reconstruct the original binary tree from this traversal string.  

Since preorder traversal follows the **root → left → right** order, we process the nodes in sequence and assign them to their correct positions.

For example, given `traversal = "1-2--3--4-5--6--7"`, we can break it down as follows:  

```css
1  (Root)
|- 2  (Depth 1, Left child of 1)
|  |- 3  (Depth 2, Left child of 2)
|  |- 4  (Depth 2, Right child of 2)
|- 5  (Depth 1, Right child of 1)
   |- 6  (Depth 2, Left child of 5)
   |- 7  (Depth 2, Right child of 5)
```

This means the tree structure is:  

```css
       1
      / \
     2   5
    / \  / \
   3   4 6  7
```

The output should be: `[1, 2, 5, 3, 4, 6, 7]`.

Before diving into specific approaches, let’s first build a high-level strategy that applies to all the approaches.  

1. **Depth determines hierarchy**

Each node’s position in the tree is determined by the number of dashes (`-`) before its value:  
- A node with depth `D` is the child of the last node with depth `D - 1`.  
- If a node has a sibling, it appears immediately after its left sibling in the traversal.  
- If a node does not have a sibling, it is the only child of its parent.  

This means that the structure of the tree is fully determined by depth information, without requiring additional information like explicit left/right indicators. Because nodes appear before their children in preorder, we can sequentially assign them to their parents without needing to look ahead or backtrack significantly.  

2. **Maintaining a Structure to Track Parent-Child Relationships**

To efficiently determine the correct parent for each node, we need a mechanism to track nodes at different depths. There are two main ways to do this:  
- Using Recursion: We can recursively parse the string and build the tree.
- Using Stack: We maintain a stack where each node is pushed when encountered. When we process a new node, we find its correct parent by checking the stack for the most recent node with `depth - 1`.  

Regardless of the approach, the core idea is the same: When we encounter a new node, we determine its depth. We find the last node at `depth - 1` and attach the new node as its child. Then we ensure that the first child assigned to a parent is the left child, and the second (if present) is the right child.

---

### Approach 1: Brute Force (Recursive with String Manipulation)

#### Intuition

The simplest way to reconstruct a tree from a string is to process the input step by step as the input is in the format of preorder traversal. We know that each number in the string represents a node in the tree, and the number of dashes before it tells us how deep it should be.

To build the tree, first, we count the number of dashes (-). The more dashes we see, the deeper the node is in the tree. After counting the dashes, we extract the number that follows. This number becomes the value of a new node.

Once we have a node, we need to figure out where to place it in the tree. Since the nodes appear in depth-first (preorder) order in the string, we know that every new node belongs as a child of the most recently encountered node that has space for a child. If a node is at a greater depth than the previous one, it must be its left child. If it's at the same depth as the last node, it means we have moved to a new subtree, and it should be attached as a right child instead.

To implement this, we use recursion. A helper function takes the string and the current index, processes the node at that position, and then calls itself to construct the left and right children. This recursion follows the same logic as a depth-first traversal of a tree. If the function encounters a node at the wrong depth, it stops and returns, ensuring that nodes are placed correctly.

> For a more comprehensive understanding of recursion, check out the [Recursion Explore Card 🔗](https://leetcode.com/explore/learn/card/recursion-i/).

#### Algorithm

- Start with `index = 0` and call the recursive `helper` function with `depth = 0`.

- In `helper` function:
  - If `index` exceeds the length of `traversal`, return `nullptr`.

  - Count the number of dashes (`dashCount`) at `index`:
    - Iterate while the character at `index + dashCount` is `'-'`.
    - Increase `dashCount` accordingly.

  - If `dashCount` does not match `depth`, return `nullptr` (ensures correct tree structure).

  - Move `index` past the dashes.

  - Extract the numeric value for the node:
    - Initialize `value = 0`.
    - While `index` points to a digit, update `value` using `value * 10 + (digit)`.
    - Increment `index` for each digit processed.

  - Create a new `TreeNode` with the extracted value.

  - Recursively construct left and right children:
    - Call `helper` with `depth + 1` for the left subtree.
    - Call `helper` with `depth + 1` for the right subtree.

  - Return the constructed `TreeNode`.

#### Implementation


```python
class Solution:
    def __init__(self):
        self.index = 0

    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        return self.helper(traversal, 0)

    def helper(self, traversal, depth):
        if self.index >= len(traversal):
            return None

        dash_count = 0
        while (
            self.index + dash_count < len(traversal)
            and traversal[self.index + dash_count] == "-"
        ):
            dash_count += 1

        # If the number of dashes doesn't match the current depth, return null
        if dash_count != depth:
            return None

        self.index += dash_count

        # Extract the node value
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = value * 10 + int(traversal[self.index])
            self.index += 1

        # Create the current node
        node = TreeNode(value)

        # Recursively build the left and right subtrees
        node.left = self.helper(traversal, depth + 1)
        node.right = self.helper(traversal, depth + 1)

        return node
```


#### Complexity Analysis

Let $n$ be the number of nodes in the tree.  

- Time complexity: $O(n)$  

    The string index advances monotonically and is shared across all recursive calls. Each character is processed a constant number of times — dashes at a given position are counted at most twice (once for a failed left-child attempt and once when the right-child is tried), and each digit is read exactly once. Thus the total work is proportional to the string length, giving $O(n)$ time.

- Space complexity: $O(n)$  

    The recursion depth is determined by the depth of the tree, which in the worst case (a skewed tree) can be $O(n)$, leading to an $O(n)$ recursive call stack space. Additionally, we allocate $O(n)$ new `TreeNode` objects, contributing to an extra $O(n)$ memory usage.  

    Thus, the overall space complexity is $O(n)$.
 
---

### Approach 2: Iterative Approach with Stack (Single Pass)

#### Intuition

Recursion is useful, but it can be slow because it involves extra function calls and memory overhead. A more efficient way to process the string is to use a stack to keep track of nodes as we build the tree.

Think of the stack as a way to remember where we are in the tree. Each time we find a new node, we check how deep it should be by counting dashes. If the stack already has more nodes than this depth, it means we have finished processing a subtree, so we remove nodes from the stack until we reach the correct depth. The node left at the top of the stack is the parent of the new node.

Since the stack always holds the path from the root to the current node, its length at any point represents how deep we are in the tree. When we encounter a new node, we count the dashes to determine its depth. If the stack is longer than the depth, it means we need to move up in the tree, so we remove nodes from the stack until it matches the correct depth.

Once we identify the parent, we decide whether to attach the new node as its left or right child. If the left child doesn’t exist, we set it as the left child. Otherwise, it must be the right child. Finally, we push the new node onto the stack because it might have its own children in later steps.

The algorithm is visualized below: 

![approach__4](images/approach__4.png)

> For a more comprehensive understanding of stacks, check out the [Stack Explore Card 🔗](https://leetcode.com/explore/learn/card/queue-stack/). 

#### Algorithm

- Initialize a `stack` to keep track of nodes at different depths.
- Initialize `index` to 0 for traversing the `traversal` string.

- Iterate while `index` is within the bounds of `traversal`:
  - Count the number of dashes (`-`) to determine the `depth` of the current node.
  - Extract the numerical value of the node by iterating through the digits.
  - Create a new `TreeNode` with the extracted value.
  - Adjust the `stack` to ensure it aligns with the correct depth by popping elements if necessary.
  - Attach the newly created node to its parent:
    - If the top node of the stack has no left child, assign the new node as the left child.
    - Otherwise, assign it as the right child.
  - Push the new node onto the stack.

- Ensure the root node is correctly identified by popping extra elements from the stack until only one remains.
- Return the remaining node in the stack as the root of the reconstructed tree.

#### Implementation


```python
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0

        while index < len(traversal):
            # Count the number of dashes
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract the node value
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the current node
            node = TreeNode(value)

            # Adjust the stack to the correct depth
            while len(stack) > depth:
                stack.pop()

            # Attach the node to the parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # Push the current node onto the stack
            stack.append(node)

        return stack[0]
```


#### Complexity Analysis

Let $n$ be the number of nodes in the tree.   

- Time complexity: $O(n)$  

    We traverse the input string exactly once; each character is processed a constant number of times, contributing $O(n)$.  

    While a single iteration may pop multiple nodes from the stack, each node is pushed exactly once and popped at most once. The total number of push and pop operations across the entire traversal is therefore $O(n)$, giving an amortized $O(1)$ stack cost per node. Combined, the overall time complexity is $O(n)$.

- Space complexity: $O(n)$  

    The maximum depth of the tree determines the maximum size of the stack. In the worst case (a skewed tree), the depth can be $O(n)$, leading to an $O(n)$ stack size.  

    Additionally, we allocate $O(n)$ `TreeNode` objects, contributing to an extra $O(n)$ memory usage.  

    Thus, the overall space complexity is $O(n)$.
 
---

### Approach 3: Iterative Approach with List

#### Intuition

Instead of using a stack, we can implement the solution using a list, as some may find list operations more intuitive. Both a stack and a list perform similar operations, such as appending elements to the end and removing them in a last-in, first-out (LIFO) manner. As a result, the overall time and space complexity remain the same. The choice between the two is mainly a matter of readability and personal preference rather than performance. In fact, in Python 3, there will be negligible difference between the two approaches since both utilize a list for storage.

We traverse the input while keeping track of depth using dashes. Whenever we encounter a digit, we extract the node value directly and create a new node. Instead of using a stack, we maintain a `levels` list where `levels[depth]` always holds the last node at that depth. 

After extracting a node’s value, we update `levels` to ensure that the new node is correctly positioned. If a node at the same depth already exists, we replace it; otherwise, we append the new node. The parent of the new node is always stored at `levels[depth - 1]`, ensuring that the tree structure remains correct as we attach nodes to their left or right children.

#### Algorithm

- Initialize `levels` array to track the last node at each depth level.
- Set `index` to 0 and `n` to the length of `traversal`.

- Iterate while `index < n`:
  - Count `depth` by counting consecutive dashes (`-`).
  - Extract `value` by reading digits until a non-digit character is encountered.
  - Create a new `TreeNode` with the extracted `value`.

  - If `depth` is smaller than `levels.size()`, replace `levels[depth]` with the new node.
  - Otherwise, append the new node to `levels`.

  - If `depth > 0`, attach the new node as a child:
    - Retrieve its `parent` from `levels[depth - 1]`.
    - If `parent->left` is null, assign the new node to `parent->left`.
    - Otherwise, assign the new node to `parent->right`.

- Return `levels[0]` as the root of the reconstructed tree.

#### Implementation


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []  # List to track the last node at each depth
        index, n = 0, len(traversal)

        while index < n:
            # Count depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract node value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the new node
            node = TreeNode(value)

            # Adjust levels list to match the current depth
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            # Attach the node to its parent
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        # The root node is always at index 0
        return levels[0]
```


#### Complexity Analysis

Let $n$ be the number of nodes in the tree.   

- Time complexity: $O(n)$  

    We traverse the input string exactly once; each character is processed a constant number of times. Parent lookup uses direct indexing into the levels list at position `depth`, which is an $O(1)$ operation. Thus the overall time complexity is $O(n)$.

- Space complexity: $O(n)$  

    The levels list keeps track of at most $O(h)$ nodes, where the tree height $h$ can be at most $O(n)$ in the worst case. Additionally, we allocate $O(n)$ `TreeNode` objects for the tree itself.  

    Thus, the overall space complexity is $O(n)$.
 
---