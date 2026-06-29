# Reconstruct the Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECTREE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [RECTREE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/RECTREE) |

---

## Problem Statement

You are given a **level order traversal** of a **complete binary tree** which has $N$ nodes numbered from $1$ to $N$. The label of the $i$-th node in the traversal is $A_i$. You need to reconstruct that tree.

A **binary tree** is a tree in which each node has at most two children.

A **complete binary tree** is a **binary tree** in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

A **level order traversal** of a complete binary tree is a sequence in which each node's label appears exactly once and where the nodes are arranged in increasing order of their distance to the root of the tree. Nodes that have the same distance to the root are arranged in order from left to right.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - the level order traversal of the tree.

**Note:**
- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node reconstruct(Vector(Integer) traversal){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* reconstruct(vector(int) traversal){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def reconstruct(traversal: List):
```

---

## Output Format

- For each test case, the function you complete should return the root of the complete binary tree. After the function is called, the validity of the reconstructed tree is checked in the hidden part of the submitted code rather than in the checker. Therefore, the output of your solution will always either be $1$ if the reconstructed tree returned by your function is valid or $0$ if the reconstructed tree returned by your function is invalid. The checker simply verifies that the output of the solution is $1$ on each test case.

---

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \leq A_i \le N$
- each node's label appears exactly once in the sequence $A$
- The sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
1
5
1 2 3 4 5
```

**Output**

```text
1
```

**Explanation**

**Example case 1:** The level order traversal of the complete binary tree whose root is node $1$ and which has edges $(1,2),(1,3),(2,4)$ and $(2,5)$ is exactly $[1,2,3,4,5]$. Note that the output field only contains a single integer $1$ which indicates that the reconstructed tree is valid. A single integer $0$ in the output field would indicate that the reconstructed tree is invalid which would result in the 'Wrong answer' verdict.

**Example 2**

**Input**

```text
1
7
2 1 3 5 7 6 4
```

**Output**

```text
1
```

**Explanation**

**Example case 1:** The level order traversal the complete binary tree whose root is node $2$ and which has edges $(2,1),(2,3),(1,5),(1,7),(3,6)$ and $(3,4)$ is exactly $[2,1,3,5,7,6,4]$. Note that the output field only contains a single integer $1$ which indicates that the reconstructed tree is valid. A single integer $0$ in the output field would indicate that the reconstructed tree is invalid which would result in the 'Wrong answer' verdict.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial for Reconstructing a Complete Binary Tree from Level-Order Traversal

In this lesson, we learn how to reconstruct a complete binary tree when given its level order traversal. A complete binary tree is defined such that every level, except possibly the last, is completely filled and all nodes in the last level are as far left as possible. The input is a list of node labels arranged in the order of a level order traversal, and our goal is to reconstruct the structure of the tree.

## Approaches to the Problem

We discuss three approaches to solve this problem:

### Approach 1: Queue-Based Iterative Reconstruction
In this approach, we use a queue to simulate the level order construction:
- **Idea:**
  - Create the root using the first element of the traversal.
  - Enqueue the root.
  - Iteratively remove a node from the queue and assign its left and right children using the next elements from the traversal.
- **Mathematical Insight:**
  For a node from the traversal, if the number of nodes processed so far is less than $ {n}$, then we can assign:
  - Left child if $ {i < n}$
  - Right child if $ {i+1 < n}$
- **Time Complexity:** $ {O(n)}$
- **Space Complexity:** $ {O(n)}$

Below is the implementation for Approach 1.

#### C++ Code:
```cpp
Node* reconstruct(vector  traversal){
    int n = traversal.size();
    if(n == 0) return NULL;
    Node* root = new Node(traversal[0]);
    queue q;
    q.push(root);
    int i = 1;
    while(!q.empty() && i < n){
        Node* current = q.front();
        q.pop();
        if(i < n){
            current->left = new Node(traversal[i++]);
            q.push(current->left);
        }
        if(i < n){
            current->right = new Node(traversal[i++]);
            q.push(current->right);
        }
    }
    return root;
}
```

#### Python Code:
```python
def reconstruct(traversal: list):
    n = len(traversal)
    if n == 0:
        return None
    root = Node(traversal[0])
    q = [root]
    i = 1
    while q and i < n:
        current = q.pop(0)
        if i < n:
            current.left = Node(traversal[i])
            q.append(current.left)
            i += 1
        if i < n:
            current.right = Node(traversal[i])
            q.append(current.right)
            i += 1
    return root
```

### Approach 2: Recursive Reconstruction Using Index Arithmetic
This method leverages the fact that in a complete binary tree stored in an array (0-indexed), the following relationships hold:
- The left child of a node at index $ {i}$ is at index $ {2*i + 1}$.
- The right child is at index $ {2*i + 2}$.

- **Idea:**
  We create a recursive function that builds the tree from the traversal list using the above indices.
- **Recursive Formula:**
  $$
  \text{buildTree}(i)=
  \begin{cases}
  \text{NULL} & \text{if } i \geq n \\
  \text{new Node(traversal}[i]\text{) with } \text{left}=\text{buildTree}(2*i+1) \text{ and } \text{right}=\text{buildTree}(2*i+2) & \text{otherwise.}
  \end{cases}
  $$
- **Time Complexity:** $ {O(n)}$
- **Space Complexity:** $ {O(n)}$ in the worst-case recursion (but practically, the depth is $ {O(\log n)}$).

Below is the implementation for Approach 2.

#### C++ Code:
```cpp
Node* buildTree(const vector &traversal, int index) {
    if(index >= traversal.size()) return NULL;
    Node* node = new Node(traversal[index]);
    node->left = buildTree(traversal, 2 * index + 1);
    node->right = buildTree(traversal, 2 * index + 2);
    return node;
}

Node* reconstruct(vector  traversal){
    return buildTree(traversal, 0);
}
```

#### Python Code:
```python
def build_tree(traversal, index):
    if index >= len(traversal):
        return None
    node = Node(traversal[index])
    node.left = build_tree(traversal, 2 * index + 1)
    node.right = build_tree(traversal, 2 * index + 2)
    return node

def reconstruct(traversal: list):
    return build_tree(traversal, 0)
```

### Approach 3: Iterative Array Indexing Method
Here, we create an auxiliary array (or vector) of node pointers corresponding to each element in the traversal list and then assign children by taking advantage of the complete binary tree’s indexing:
- **Idea:**
  - Create a list of nodes from the traversal.
  - For each node at index $ {i}$, assign:
    - Left child at index $ {2*i+1}$ if it exists.
    - Right child at index $ {2*i+2}$ if it exists.
- **Time Complexity:** $ {O(n)}$
- **Space Complexity:** $ {O(n)}$

Below is the implementation for Approach 3.

#### C++ Code:
```cpp
Node* reconstruct(vector  traversal){
    int n = traversal.size();
    if(n == 0) return NULL;
    vector nodes(n, NULL);
    for(int i = 0; i < n; i++){
        nodes[i] = new Node(traversal[i]);
    }
    for(int i = 0; i < n; i++){
        int leftIdx = 2 * i + 1;
        int rightIdx = 2 * i + 2;
        if(leftIdx < n) nodes[i]->left = nodes[leftIdx];
        if(rightIdx < n) nodes[i]->right = nodes[rightIdx];
    }
    return nodes[0];
}
```

#### Python Code:
```python
def reconstruct(traversal: list):
    n = len(traversal)
    if n == 0:
        return None
    nodes = [Node(x) for x in traversal]
    for i in range(n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        if right_idx < n:
            nodes[i].right = nodes[right_idx]
    return nodes[0]
```

## Summary
- **Approach 1** uses a queue to process nodes in level order and assign children sequentially.
- **Approach 2** takes advantage of the complete binary tree property by using recursion with index arithmetic.
- **Approach 3** creates an auxiliary array of nodes and iteratively assigns left and right children based on computed indices.

Each approach runs in $ {O(n)}$ time and is efficient for handling large inputs within the problem constraints.

</details>
