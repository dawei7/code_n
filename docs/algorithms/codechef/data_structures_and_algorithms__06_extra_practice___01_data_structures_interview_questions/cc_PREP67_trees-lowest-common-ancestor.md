# Trees - Lowest Common Ancestor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP67 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [PREP67](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/PREP67) |

---

## Problem Statement

You are given the root of a [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree) consisting of $N$ nodes, rooted at node $1$.

Your task is to return the [lowest common ancestor (LCA)](https://en.wikipedia.org/wiki/Lowest_common_ancestor) of two given nodes $A$, $B$ in the tree.

Note: The lowest common ancestor is defined between two nodes $A$ and $B$ as the lowest node in tree that has both $A$ and $B$ as descendants (where we allow **a node to be a descendant of itself**).

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains three space-separated integers $N$, $A$, $B$.
- The second line of each test case contains the Binary Tree representation in the order of level order Traversal where, numbers denote node values, and a character $N$ denotes NULL child.

- For Java language, you need to:

Complete the function in the submit solution tab:
```
int lowestCommonAncestor(Node root, int A, int B){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
int lowestCommonAncestor(Node* root, int A, int B){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def lowestCommonAncestor(self,root, A, B):
```

---

## Output Format

The function you complete should return the required answer.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 5\cdot 10^4$
- $1 \leq A, B \leq N$
- $A \neq B$

---

## Examples

**Example 1**

**Input**

```text
3
3 2 3
1 2 3 N N N N
3 2 3
1 2 N N 3 N N
6 3 5
1 6 N 2 N 4 5 3 N N N N N
```

**Output**

```text
1
2
2
```

**Explanation**

**Test case $1$:** The LCA of $2$, $3$ will be $1$.

**Test case $2$:** The LCA of $2$, $3$ will be $1$ as a node can be a descendant of itself according to the LCA definition.

**Test case $3$:** The LCA of $3$, $5$ will be $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 3
1 2 3 N N N N
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 2 3
1 2 N N 3 N N
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
6 3 5
1 6 N 2 N 4 5 3 N N N N N
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we discuss how to solve the Lowest Common Ancestor (LCA) problem in a binary tree. Recall that the LCA of two nodes $A$ and $B$ is the lowest node in the tree that has both $A$ and $B$ as descendants (a node can be a descendant of itself). In our discussion, we will explore two different approaches.

---

### Approach 1: Path Finding Approach

#### **Idea:**

In this method, we find the path from the root node to each of the target nodes (i.e., $A$ and $B$). Once we have the two paths (say, $\textbf{pathA}$ and $\textbf{pathB}$), we compare them element by element. The last common element in the two paths is the lowest common ancestor.

- **Steps:**
  1. Traverse the tree to find the path from the root to $A$. Store this path in an array (or list).
  2. Traverse the tree to find the path from the root to $B$. Store this path in another array (or list).
  3. Compare these two paths from the beginning. The node where the paths diverge is just after the LCA. Therefore, the last common node before divergence is the LCA.

#### **Complexity:**
- **Time Complexity:** In the worst-case scenario, you might traverse the entire tree for each node, leading to a complexity of $O(n)$ per path. Overall, it is approximately $O(n)$.
- **Space Complexity:** You use extra space to store the paths, which in the worst case takes $O(n)$ space.

#### **Example:**
Suppose the tree is as follows:
$$
\begin{array}{c}
    1 \\
   / \ \backslash \\
  2 \quad 3 \\
 / \\
4
\end{array}
$$
For $A=4$ and $B=3$, the paths would be:
- $\textbf{pathA} = [1, 2, 4]$
- $\textbf{pathB} = [1, 3]$
The last common node is $1$, so the LCA is $1$.

#### **Code Implementation:**

Below is the C++ and Python implementation using the path-based approach.

**C++ Code (Approach 1):**
```cpp
class Solution {
  public:
    bool findPath(Node* root, int target, vector& path) {
        if(root == NULL)
            return false;
        path.push_back(root->data);
        if(root->data == target)
            return true;
        if(findPath(root->left, target, path) || findPath(root->right, target, path))
            return true;
        path.pop_back();
        return false;
    }

    int lowestCommonAncestor(Node* root, int A, int B) {
        vector pathA, pathB;
        if (!findPath(root, A, pathA) || !findPath(root, B, pathB))
            return -1;
        int i = 0;
        while(i < pathA.size() && i < pathB.size() && pathA[i] == pathB[i])
            i++;
        return pathA[i-1];
    }
};
```

**Python Code (Approach 1):**
```python
class Solution:
    def lowestCommonAncestor(self, root, A, B):
        def findPath(node, target, path):
            if node is None:
                return False
            path.append(node.data)
            if node.data == target:
                return True
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            path.pop()
            return False

        pathA, pathB = [], []
        if not findPath(root, A, pathA) or not findPath(root, B, pathB):
            return -1

        i = 0
        while i < len(pathA) and i < len(pathB) and pathA[i] == pathB[i]:
            i += 1
        return pathA[i-1]
```

---

### Approach 2: Direct Recursive Approach

#### **Idea:**

This method uses recursion directly to find the LCA without constructing the full paths. The idea is based on the following:
- If the current node is `NULL`, return `NULL`.
- If the current node is equal to $A$ or $B$, return the current node.
- Recursively search for $A$ and $B$ in the left and right subtrees.
- If both subtrees return non-`NULL` values, it means one target is found in the left subtree and the other in the right subtree. In that case, the current node is the LCA.
- Otherwise, if only one subtree returns a non-`NULL` value, return that value.

#### **Complexity:**
- **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree because every node is visited once.
- **Space Complexity:** $O(h)$ in the worst case, where $h$ is the height of the tree (due to recursion stack).

#### **Example:**
Using our previous tree:
$$
\begin{array}{c}
    1 \\
   / \ \backslash \\
  2 \quad 3 \\
 / \\
4
\end{array}
$$
If $A=4$ and $B=3$, the recursion will discover:
- $4$ in the left subtree of node $2$.
- $3$ in the right subtree of node $1$.
Since both are found separately, the LCA is $1$.

#### **Code Implementation:**

Below is the C++ and Python implementation using the direct recursive approach.

**C++ Code (Approach 2):**
```cpp
class Solution {
  public:
    Node* lca(Node* root, int A, int B) {
        if(root == NULL)
            return NULL;
        if(root->data == A || root->data == B)
            return root;

        Node* left = lca(root->left, A, B);
        Node* right = lca(root->right, A, B);

        if(left && right)
            return root;
        return left ? left : right;
    }

    int lowestCommonAncestor(Node* root, int A, int B) {
        Node* node = lca(root, A, B);
        return node ? node->data : -1;
    }
};
```

**Python Code (Approach 2):**
```python
class Solution:
    def lowestCommonAncestor(self, root, A, B):
        def lca(node, A, B):
            if node is None:
                return None
            if node.data == A or node.data == B:
                return node

            left = lca(node.left, A, B)
            right = lca(node.right, A, B)

            if left and right:
                return node
            return left if left is not None else right

        node = lca(root, A, B)
        return node.data if node is not None else -1
```

---

### Summary

- **Approach 1 (Path Finding):** This method involves finding paths from the root to each node and then comparing these paths. It is intuitive and easy to understand, especially if you are just getting started with tree problems.

- **Approach 2 (Direct Recursive):** This method uses recursion directly to identify the LCA and is more optimized in terms of space, as it does not require storing the entire path.

Both approaches have a time complexity of $O(n)$, but the direct recursive approach typically uses less space. Choose the approach that best suits your needs and understanding.

Happy Coding!

</details>
