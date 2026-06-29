# Find the Subtree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBTCH |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [SUBTCH](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/SUBTCH) |

---

## Problem Statement

Given two undirected binary trees $T_1$ and $T_2$ , check if the second tree $T_2$ exists as a **subtree** in the first tree $T_1$.

A **binary tree** is a tree in which each node has at most two children.

A **subtree** of a node $x$ in a tree $T$ is a tree consisting of the node $x$ and all of its **descendants** in $T$. A **descendant** of a node $x$ is any node reachable from it by repeated proceeding from a parent to its child.

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $M$ — the number of nodes in the two binary trees.
- Next $N - 1$ lines contain three space separated characters $p1_i, c1_i, R_i$, describing the first tree with edge informations - $p1_i$ is an integer denoting the parent node of the $i$th edge, $c1_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c1_i$ is left child of $p1_i$, else `R`.
- Similarly, next $M - 1$ lines contain three space separated characters $p2_i, c2_i, R_i$, describing the second tree with edge informations - $p2_i$ is an integer denoting the parent node of the $i$th edge, $c2_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c2_i$ is left child of $p2_i$, else `R`.

---

## Output Format

- Complete the given function whic should return a single integer $1$ if the binary tree $T_2$ exists as a subtree in the binary tree $T_1$ and $0$ otherwise.

---

## Constraints

- $1 \leq N, M \leq 1000$
- $1 \leq p1_i, p2_i, c1_i, c2_i \leq 10000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.

---

## Examples

**Example 1**

**Input**

```text
5 5
1 2 L
1 3 R
3 4 L
3 5 R
1 2 L
1 3 R
3 4 L
3 5 R
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore two primary approaches to determine whether a binary tree \( T_2 \) exists as a subtree of another binary tree \( T_1 \). Both approaches leverage classic tree algorithms and recursion concepts to compare the structure and values of the trees.

---

### **Approach 1: Recursive Tree Comparison**

#### **Idea:**

The intuition behind this approach is that if \( T_2 \) is a subtree of \( T_1 \), then there exists a node in \( T_1 \) where the subtree rooted at that node is **identical** to \( T_2 \).

To achieve this, we define a helper function, which we call \( I(a, b) \), to check if the subtree rooted at node \( a \) is identical to the subtree rooted at node \( b \). Formally, the function is defined as:

$$
I(a, b) =
\begin{cases}
\text{true} & \text{if } a = b = \text{NULL} \\
\text{false} & \text{if } a = \text{NULL} \text{ or } b = \text{NULL} \\
\left(a.\text{val} = b.\text{val}\right) \land I(a.\text{left}, b.\text{left}) \land I(a.\text{right}, b.\text{right}) & \text{otherwise}
\end{cases}
$$

The main function recursively checks every node in \( T_1 \). If at any point \( I(\text{node}, T_2) \) is true, then \( T_2 \) is a subtree of \( T_1 \).

#### **Complexity:**

The worst-case time complexity is \( O(|T_1| \times |T_2|) \) because, in the worst-case scenario, we might need to inspect every node of \( T_1 \) and for each such node, compare a whole subtree of \( T_2 \).

#### **C++ Implementation:**

```cpp
class Solution {
  public:
    int findSubtree(Node* root1, Node* root2){
        if(root2 == NULL) return 1; // An empty tree is always a subtree.
        if(root1 == NULL) return 0;

        // Lambda to check if two trees are identical.
        function isIdentical = [&](Node* a, Node* b) -> bool {
            if(a == NULL && b == NULL) return true;
            if(a == NULL || b == NULL) return false;
            return (a->val == b->val) &&
                   isIdentical(a->left, b->left) &&
                   isIdentical(a->right, b->right);
        };

        // Check if the trees match starting at the current node.
        if(isIdentical(root1, root2)) return 1;

        // Recursively check left and right subtrees.
        return findSubtree(root1->left, root2) || findSubtree(root1->right, root2);
    }
};
```

#### **Python Implementation:**

```python
class Solution:
    def findSubtree(self, root1, root2):
        if root2 is None:
            return 1  # An empty tree is always a subtree.
        if root1 is None:
            return 0

        def isIdentical(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (node1.val == node2.val and
                    isIdentical(node1.left, node2.left) and
                    isIdentical(node1.right, node2.right))

        if isIdentical(root1, root2):
            return 1
        return self.findSubtree(root1.left, root2) or self.findSubtree(root1.right, root2)
```

---

### **Approach 2: Tree Serialization**

#### **Idea:**

In this approach, we convert each binary tree into a serialized string using a preorder traversal. It is **crucial** to include a special marker (e.g., "X") for null nodes to ensure that the tree structure is captured uniquely. Let \( S(T) \) be the serialization of tree \( T \).

For example, consider a tree with root value 1:
- Its serialization might look like:
  $$
  S(T) = "\#1,\#2,X,\#,X,\#3,\#4,X,\#,X,\#5,X,\#"
  $$

Once both \( T_1 \) and \( T_2 \) are serialized, we check if \( S(T_2) \) is a substring of \( S(T_1) \). If it is, \( T_2 \) exists as a subtree of \( T_1 \).

#### **Complexity:**

- **Serialization:** Takes \( O(n) \) time for \( T_1 \) and \( O(m) \) time for \( T_2 \).
- **Substring Check:** Typically, the search can be performed in \( O(n + m) \) time using efficient algorithms.

Thus, the overall approach is efficient for the given constraints.

#### **C++ Implementation:**

```cpp
class Solution {
  public:
    int findSubtree(Node* root1, Node* root2){
        // Helper lambda to serialize the tree using preorder traversal.
        function serialize = [&](Node* node) -> string {
            if(node == NULL) return "X,";
            return "#" + to_string(node->val) + "," + serialize(node->left) + serialize(node->right);
        };

        string s1 = serialize(root1);
        string s2 = serialize(root2);

        // Check if the serialization of T2 is a substring of the serialization of T1.
        if(s1.find(s2) != string::npos)
            return 1;
        return 0;
    }
};
```

#### **Python Implementation:**

```python
class Solution:
    def findSubtree(self, root1, root2):
        def serialize(node):
            if node is None:
                return "X,"
            return "#" + str(node.val) + "," + serialize(node.left) + serialize(node.right)

        s1 = serialize(root1)
        s2 = serialize(root2)

        # Check if the serialized string of T2 is found within that of T1.
        return 1 if s2 in s1 else 0
```

---

Both approaches effectively solve the problem, and the choice of method can depend on considerations such as ease of implementation and handling of edge cases. The recursive comparison approach is more direct, while the serialization method leverages string search, which might be advantageous in some scenarios. As you practice these techniques, you will improve your understanding of tree traversals and recursion—essential tools for many DSA interviews.

</details>
