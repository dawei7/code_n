# Trees - Path Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP65 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [PREP65](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/PREP65) |

---

## Problem Statement

You are given the root of a [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree) consisting of $N$ nodes, rooted at node $1$ where value of $i^{th}$ node will be $A_i$.

Your task is to find if the tree has a **root-to-leaf** path such that adding up all the values along the path equals the given sum $K$.

Note: If you return `True` then the output will be $1$ otherwise $0$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains two space-separated integers $N$, $K$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_{N}$ — the elements of array $A$ where $A_i$ will be the value of $i^{th}$ node.
- The third line of each test case contains the Binary Tree representation in the order of level order Traversal where, numbers denote node values, and a character $N$ denotes NULL child.

- For Java language, you need to:

Complete the function in the submit solution tab:
```
boolean hasPathSum(Node root, int K){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
bool hasPathSum(Node* root, int K){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def hasPathSum(self, root, K):
```

---

## Output Format

The function you complete should return the required answer.

---

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 2\cdot 10^4$
- $-10^5 \leq A_i, K \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3 5
1 5 10
1 2 3 N N N N
3 15
5 5 10
1 2 3 N N N N
4 4
1 5 8 -5
1 2 3 N N 4 N N N
```

**Output**

```text
0
1
1
```

**Explanation**

**Test case $1$:** There is no **root-to-leaf** path such that sum will be $5$.

**Test case $2$:** The **root-to-leaf** path will be $1 \rightarrow 3$. So the sum will be $5 + 10 = 15$.

**Test case $3$:** The **root-to-leaf** path will be $1 \rightarrow 3 \rightarrow 4$. So the sum will be $1 + 8 - 5 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 5
1 5 10
1 2 3 N N N N
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 15
5 5 10
1 2 3 N N N N
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 4
1 5 8 -5
1 2 3 N N 4 N N N
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, you are given a binary tree with $N$ nodes and a target sum $K$. Your task is to determine whether there exists a **root-to-leaf** path in the tree such that the sum of the node values along that path equals $K$. In other words, starting from the root and ending at a leaf, if you add the values of all the nodes encountered, the sum should be exactly $K$.

To solve this problem, we will discuss three different approaches:

---

### Approach 1: Recursive Depth-First Search (DFS)

The recursive DFS approach is the most natural method when dealing with tree problems. The idea is to:

1. **Base Case:**
   - If the current node is `NULL`, return `false` because there's no path.
   - If the current node is a leaf (both left and right children are `NULL`), check if its value is equal to the remaining target sum $K$.
2. **Recursive Step:**
   - Otherwise, subtract the current node's value from $K$, and recursively check both the left and right subtrees.
   - If either subtree returns `true`, then a valid path exists.

**Time Complexity:** $O(N)$ in the worst case, where $N$ is the number of nodes.
**Space Complexity:** $O(H)$, where $H$ is the height of the tree due to the recursion stack.

Below are the implementations in C++ and Python:

```cpp
class Solution {
  public:
    bool hasPathSum(Node* root, int K) {
        if (root == NULL)
            return false;
        // Check if it is a leaf node
        if (root->left == NULL && root->right == NULL)
            return (K == root->data);
        // Recursively check for either subtree
        return hasPathSum(root->left, K - root->data) ||
               hasPathSum(root->right, K - root->data);
    }
};
```

```python
class Solution:
    def hasPathSum(self, root, K):
        if not root:
            return False
        # If it's a leaf, check that the remaining sum equals node's value
        if not root.left and not root.right:
            return K == root.data
        # Recursively check for left and right subtree paths
        return self.hasPathSum(root.left, K - root.data) or self.hasPathSum(root.right, K - root.data)
```

---

### Approach 2: Iterative DFS using a Stack

Instead of recursion, you can perform DFS iteratively with an explicit stack. The idea is to:

1. **Initialization:**
   - Use a stack to store pairs of $(\text{node}, \text{remaining sum})$.
   - Initialize the stack with the root node and the target sum $K$.
2. **Iteration:**
   - Pop an element from the stack.
   - If the node is a leaf and its value equals the remaining sum, return `true`.
   - Otherwise, push its non-`NULL` children into the stack with the updated remaining sum (subtract the current node's value).

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ in the worst-case scenario when the tree is skewed.

Below are the implementations in C++ and Python:

```cpp
class Solution {
  public:
    bool hasPathSum(Node* root, int K) {
        if (!root)
            return false;
        stack> st;
        st.push({root, K});
        while (!st.empty()){
            auto [node, remain] = st.top();
            st.pop();
            // Check if this is a leaf node and the required sum is met.
            if (!node->left && !node->right && remain == node->data)
                return true;
            if (node->right)
                st.push({node->right, remain - node->data});
            if (node->left)
                st.push({node->left, remain - node->data});
        }
        return false;
    }
};
```

```python
class Solution:
    def hasPathSum(self, root, K):
        if not root:
            return False
        stack = [(root, K)]
        while stack:
            node, remain = stack.pop()
            # Check if it's a leaf and the remaining sum is achieved
            if not node.left and not node.right and node.data == remain:
                return True
            if node.right:
                stack.append((node.right, remain - node.data))
            if node.left:
                stack.append((node.left, remain - node.data))
        return False
```

---

### Approach 3: Breadth-First Search (BFS) using a Queue

A BFS approach processes nodes level-by-level and can be implemented using a queue. The steps are similar to the DFS strategy:

1. **Initialization:**
   - Use a queue to store pairs of $(\text{node}, \text{remaining sum})$.
   - Start by enqueueing the root with the target sum $K$.
2. **Iteration:**
   - Dequeue an element.
   - If the node is a leaf and its value equals the remaining sum, return `true`.
   - Otherwise, enqueue its children with the updated remaining sum.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ due to the storage of nodes in the queue.

Below are the implementations in C++ and Python:

```cpp
class Solution {
  public:
    bool hasPathSum(Node* root, int K) {
        if (!root)
            return false;
        queue> q;
        q.push({root, K});
        while(!q.empty()){
            auto [node, remain] = q.front();
            q.pop();
            // Check if it is a leaf and the condition is satisfied.
            if (!node->left && !node->right && node->data == remain)
                return true;
            if (node->left)
                q.push({node->left, remain - node->data});
            if (node->right)
                q.push({node->right, remain - node->data});
        }
        return false;
    }
};
```

```python
class Solution:
    def hasPathSum(self, root, K):
        if not root:
            return False
        from collections import deque
        q = deque([(root, K)])
        while q:
            node, remain = q.popleft()
            # If at a leaf, check for the matching sum.
            if not node.left and not node.right and node.data == remain:
                return True
            if node.left:
                q.append((node.left, remain - node.data))
            if node.right:
                q.append((node.right, remain - node.data))
        return False
```

---

**Summary:**
- **Approach 1 (Recursive DFS)** is intuitive and mirrors the problem statement directly by subtracting the node value from the remaining sum during recursion.
- **Approach 2 (Iterative DFS using Stack)** achieves the same goal as recursion but avoids the function call overhead by maintaining an explicit stack.
- **Approach 3 (BFS using Queue)** processes the tree level-by-level, which can be a more natural fit in some scenarios, especially when the tree is balanced.

Each method correctly identifies if there exists a root-to-leaf path with the sum $K$. Choose the approach that best suits your style and the constraints of your specific problem instance.

</details>
