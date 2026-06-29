# Counting Nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTND |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [CNTND](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/CNTND) |

---

## Problem Statement

You are given the root of a **binary tree** with $N$ nodes numbered from $1$ to $N$. You need to count the number of nodes in each node's **subtree**.

A **binary tree** is a tree in which each node has at most two children.

A **subtree** of a node $x$ in a tree $T$ is a tree consisting of the node $x$ and all of its **descendants** in $T$. A **descendant** of a node $x$ is any node reachable from it by repeated proceeding from a parent to its child.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

- The second line contains $N$ space-separated integers $p_1,p_2, \ldots, p_N$ - the parents of each node. If $p_i<0$ then the node $i$ is the **left child** of the node $|p_i|$. If $p_i>0$ then the node $i$ is the **right child** of the node $|p_i|$.

**Note:**
- For Java language, you need to:

Complete the function in the submit solution tab:
```
ArrayList(Integer) countNodes(Node root){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
vector(int) countNodes(struct Node* root){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def countNodes(root):
```

---

## Output Format

- For each test case, the function you complete should return a list of $N$ integers in which the $i$-th ($1$-based indexing) number should be the number of nodes in the subtree of the node which is labeled with $i$.

---

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le |p_i| \le N$ for each valid $i$ except the root of the tree
- $p_i=0$ holds only for the root of the tree
- The undirected graph described on the input is guaranteed to be a binary tree
- The sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5
0 1 2 3 4
6
-2 0 2 -1 1 3
```

**Output**

```text
5 4 3 2 1
3 6 2 1 1 1
```

**Explanation**

**Example case 1:** The root of this binary tree is the node $1$. There are $5$ nodes in the subtree of node $1$, $4$ nodes in the subtree of node $2$, $3$ nodes in the subtree of node $3$, $2$ nodes in the subtree of node $2$ and only one node in the subtree of node $5$ - itself.

**Example case 2:** The root of this binary tree is the node $2$. The node $1$ has $3$ nodes in its subtree, node $2$ has all $6$ nodes in its subtree, node $3$ has $2$ nodes in its subtree, while nodes $4$, $5$, and $6$ all have a single node in their subtrees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
0 1 2 3 4
```

**Output for this case**

```text
5 4 3 2 1
```



#### Test case 2

**Input for this case**

```text
6
-2 0 2 -1 1 3
```

**Output for this case**

```text
3 6 2 1 1 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on Counting Subtree Nodes in a Binary Tree

In this lesson, we tackle the problem of calculating the number of nodes in the subtree of every node in a binary tree. The goal is to compute, for each node, the total count of nodes in the subtree that has that node as its root. A node's subtree includes the node itself and all of its descendants.

## Approaches to the Problem

We will discuss two primary approaches:

### Approach 1: Recursive Depth-First Search (DFS)

This is a natural and straightforward method to solve the problem:
- We perform a DFS traversal in a postorder fashion.
- For each node, we recursively compute the size of its left subtree and right subtree.
- The subtree size for any given node is computed as

$$
\text{SubtreeSize}(x) = 1 + \text{SubtreeSize}(\text{left child of } x) + \text{SubtreeSize}(\text{right child of } x)
$$

- This solution visits every node once.
- **Time Complexity:** $O(N)$ because each node is visited exactly once.
- **Space Complexity:** $O(H)$, where $H$ is the height of the tree.

### Approach 2: Iterative DFS Using Postorder Traversal

An alternative is to simulate the DFS traversal iteratively:
- We simulate a postorder DFS traversal using a stack to build the postorder sequence.
- Once the nodes are in postorder (i.e. the children are processed before their parent), we compute the subtree sizes.
- **Time Complexity:** $O(N)$.
- **Space Complexity:** $O(N)$ due to the extra space used for the stack and auxiliary storage.

Both approaches are valid; the recursive method is simpler and more intuitive, while the iterative version can be useful in environments that restrict recursion depth.

## Code Implementation

Below, we present the implementation in both C++ and Python for each approach.

### Approach 1: Recursive DFS

#### C++ Code:
```cpp
vector countNodes(Node* root){
    // Create a vector to store the subtree sizes for each node.
    vector count(100001, 0); // Assumes maximum N is 10^5

    // Define a recursive lambda function for DFS.
    function dfs = [&](Node* node) -> int {
        if (node == NULL) return 0;

        // Recursively compute sizes of left and right subtrees.
        int leftCount = dfs(node->left);
        int rightCount = dfs(node->right);

        // Compute current node's subtree size.
        count[node->label] = 1 + leftCount + rightCount;
        return count[node->label];
    };

    dfs(root);

    // Prepare result vector in order of node labels.
    vector result;
    // Nodes are labeled from 1. We extract until we have non-zero values.
    for (int i = 1; i < count.size(); i++){
        if(count[i] != 0){
            result.push_back(count[i]);
        }
        else break;
    }

    return result;
}
```

#### Python Code:
```python
def countNodes(root):
    # Dictionary to store subtree sizes for each node.
    count = {}

    def dfs(node):
        if node is None:
            return 0
        # Recursively compute the sizes of left and right subtrees.
        left = dfs(node.left)
        right = dfs(node.right)
        # Calculate current node's subtree size.
        count[node.label] = 1 + left + right
        return count[node.label]

    dfs(root)
    # The nodes are labeled from 1 to N.
    n = max(count.keys())
    # Return the subtree sizes in order.
    return [count[i] for i in range(1, n+1)]
```

### Approach 2: Iterative DFS Using Postorder Traversal

#### C++ Code:
```cpp
vector countNodes(Node* root){
    vector count(100001, 0); // Array to hold subtree sizes.
    if (root == NULL) return {};

    // Use a stack to perform iterative DFS.
    stack s;
    vector postorder;

    s.push(root);
    // Build postorder traversal.
    while(!s.empty()){
        Node* node = s.top();
        s.pop();
        postorder.push_back(node);
        if (node->left) s.push(node->left);
        if (node->right) s.push(node->right);
    }
    // Reverse the vector to get the correct postorder.
    reverse(postorder.begin(), postorder.end());

    // Compute subtree sizes in postorder.
    for(auto node : postorder){
        int leftCount = (node->left ? count[node->left->label] : 0);
        int rightCount = (node->right ? count[node->right->label] : 0);
        count[node->label] = 1 + leftCount + rightCount;
    }

    // Prepare the result vector.
    vector result;
    for (int i = 1; i < count.size(); i++){
        if(count[i] != 0)
            result.push_back(count[i]);
        else break;
    }
    return result;
}
```

#### Python Code:
```python
def countNodes(root):
    if root is None:
        return []

    count = {}
    stack = [root]
    postorder = []

    # Build postorder traversal using an iterative DFS.
    while stack:
        node = stack.pop()
        postorder.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    postorder.reverse()

    # Compute subtree sizes in postorder.
    for node in postorder:
        leftCount = count[node.left.label] if node.left else 0
        rightCount = count[node.right.label] if node.right else 0
        count[node.label] = 1 + leftCount + rightCount

    n = max(count.keys())
    return [count[i] for i in range(1, n+1)]
```

In both approaches, the key idea is to guarantee that we compute the subtree sizes only after the sizes for the child nodes have been computed. This ensures that each node's count is correctly calculated.

</details>
