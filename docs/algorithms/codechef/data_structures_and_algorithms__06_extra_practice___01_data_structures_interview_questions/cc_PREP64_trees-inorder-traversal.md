# Trees - Inorder Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP64 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [PREP64](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/PREP64) |

---

## Problem Statement

You are given the root of a [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree) consisting of $N$ nodes, rooted at node $1$.

Your task is to return the *Inorder Traversal* of the given tree.

### Input:

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains single lines of input.
- The first line contains the Binary Tree representation in the order of level order Traversal where, numbers denote node values, and a character $N$ denotes NULL child.

- For Java language, you need to:

Complete the function in the submit solution tab:
```
ArrayList inOrder(Node root){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
vector inOrder(Node* root){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def InOrder(self,root):
```
### Output:
The function you complete should return the required answer.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 5\cdot 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
1 3 2 N N N N
1 2 3 N N 4 6 N 5 N N 7 N N N
1 2 3 4 N 5 N N N N N
```

**Output**

```text
3 1 2 
2 1 4 7 5 3 6 
4 2 1 5 3
```

**Explanation**

Test case $1$: The inorder traversal of the given tree is $[3, 1, 2]$.

Test case $2$: The inorder traversal of the given tree is $[2, 1, 4, 7, 5, 3, 6]$.

Test case $3$: The inorder traversal of the given tree is $[4, 2, 1, 5, 3]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3 2 N N N N
```

**Output for this case**

```text
3 1 2
```



#### Test case 2

**Input for this case**

```text
1 2 3 N N 4 6 N 5 N N 7 N N N
```

**Output for this case**

```text
2 1 4 7 5 3 6
```



#### Test case 3

**Input for this case**

```text
1 2 3 4 N 5 N N N N N
```

**Output for this case**

```text
4 2 1 5 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Inorder Traversal Editorial

In this problem, our objective is to perform an **inorder traversal** of a binary tree. In an inorder traversal, we visit the nodes in the following order:
$$
\text{Left Subtree} \rightarrow \text{Node} \rightarrow \text{Right Subtree}
$$
This traversal order is especially important because if the tree is a Binary Search Tree (BST), then the inorder traversal will produce the node values in sorted order.

We will discuss **three approaches** to solve this problem. Each approach has its merits and trade-offs, which will help you understand how to solve similar problems in different ways.

---

#### **Approach 1: Recursive Method**

**Explanation:**

The recursive approach is the most intuitive method for inorder traversal. The idea is to call the function recursively to:
1. Visit all nodes in the left subtree.
2. Process the current node (add its value to the result list).
3. Visit all nodes in the right subtree.

The recursive pattern follows the order:
$$
\text{inOrder}(node) = \text{inOrder}(node.\text{left}) \quad \text{(process current)} \quad \text{inOrder}(node.\text{right})
$$

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes.
- **Space Complexity:** $O(h)$, where $h$ is the height of the tree (used by the recursion stack).

**C++ Implementation:**
```cpp
class Solution {
  public:
    void inOrderTraversal(Node* node, vector& result) {
        if (node == NULL) return;
        inOrderTraversal(node->left, result);
        result.push_back(node->data);
        inOrderTraversal(node->right, result);
    }

    vector inOrder(Node* root) {
        vector result;
        inOrderTraversal(root, result);
        return result;
    }
};
```

**Python Implementation:**
```python
class Solution:
    def InOrder(self, root):
        def inOrderTraversal(node, res):
            if node is None:
                return
            inOrderTraversal(node.left, res)
            res.append(node.data)
            inOrderTraversal(node.right, res)
        result = []
        inOrderTraversal(root, result)
        return result
```

---

#### **Approach 2: Iterative Method Using a Stack**

**Explanation:**

The iterative method uses a stack to simulate the recursion process. Here’s how it works:
1. Start at the root and push all left children onto the stack.
2. When you reach a node with no left child, pop from the stack (this is the current node), add its value to the result, and then shift to its right child.
3. Repeat until there are no nodes left to process.

This approach is particularly useful when you want to avoid potential issues with deep recursion.

- **Time Complexity:** $O(N)$.
- **Space Complexity:** $O(N)$ in the worst case.

**C++ Implementation:**
```cpp
class Solution {
  public:
    vector inOrder(Node* root) {
        vector result;
        stack st;
        Node* current = root;
        while (current != NULL || !st.empty()) {
            while (current != NULL) {
                st.push(current);
                current = current->left;
            }
            current = st.top();
            st.pop();
            result.push_back(current->data);
            current = current->right;
        }
        return result;
    }
};
```

**Python Implementation:**
```python
class Solution:
    def InOrder(self, root):
        result = []
        stack = []
        current = root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.data)
            current = current.right
        return result
```

---

#### **Approach 3: Morris Traversal**

**Explanation:**

Morris Traversal is a space-optimized way to perform an inorder traversal without using a recursion stack or an explicit stack. The algorithm temporarily modifies the tree by establishing a threaded pointer to the inorder predecessor. Once the left subtree is processed, the algorithm removes the temporary link.

**Steps:**
1. If the current node has no left child, add its value and move to the right child.
2. If a left child exists, find the inorder predecessor (the rightmost node in the left subtree).
3. If the predecessor’s right pointer is `NULL`, make it point to the current node and move to the left child.
4. If the predecessor’s right pointer already points to the current node, revert the change (set it back to `NULL`), add the current node’s value, and move to the right child.

- **Time Complexity:** $O(N)$.
- **Space Complexity:** $O(1)$.

**C++ Implementation:**
```cpp
class Solution {
  public:
    vector inOrder(Node* root) {
        vector result;
        Node* current = root;
        while(current != NULL) {
            if(current->left == NULL) {
                result.push_back(current->data);
                current = current->right;
            } else {
                Node* pre = current->left;
                while(pre->right != NULL && pre->right != current) {
                    pre = pre->right;
                }
                if(pre->right == NULL) {
                    pre->right = current;
                    current = current->left;
                } else {
                    pre->right = NULL;
                    result.push_back(current->data);
                    current = current->right;
                }
            }
        }
        return result;
    }
};
```

**Python Implementation:**
```python
class Solution:
    def InOrder(self, root):
        result = []
        current = root
        while current:
            if current.left is None:
                result.append(current.data)
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    result.append(current.data)
                    current = current.right
        return result
```

---

### Summary

We explored three methods for performing an inorder traversal of a binary tree:

1. **Recursive Approach:** Easy and intuitive with a simple implementation.
2. **Iterative Approach:** Uses a stack to simulate recursion and avoids potential recursion depth limits.
3. **Morris Traversal:** Achieves the traversal in $O(1)$ space by temporarily altering the tree structure.

Each approach efficiently visits every node in the tree with a time complexity of $O(N)$ while differing mainly in space usage and implementation style. Selecting an approach depends on the constraints of the problem and the specific requirements regarding space and recursion.

Happy coding, and best of luck with your DSA interview preparation!

</details>
