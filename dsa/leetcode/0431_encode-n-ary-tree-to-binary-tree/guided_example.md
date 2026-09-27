# Guided Example: Encode N-ary Tree to Binary Tree

We trace the step-by-step Left-Child Right-Sibling (LCRS) tree transformation, first-child leftward descent, sibling rightward horizontal chaining, and exact inverse decoding on representative $N$-ary hierarchical structures:

- **Input:** $N$-ary tree with root $1$, children $3, 2, 4$, where node $3$ has children $5, 6$:
  ```text
        1
      / | \
     3  2  4
    / \
   5   6
  ```
- **Required output:** Binary tree where `left` points to first child and `right` points to next sibling:
  ```text
        1
       /
      3
     / \
    5   2
     \   \
      6   4
  ```
- **Encoding trace:**
  - Root $1$: has children $[3, 2, 4]$.
    - First child is $3 \implies 1.left = \text{encode}(3)$.
    - Root has no siblings $\implies 1.right = \text{None}$.
  - Node $3$:
    - First child is $5 \implies 3.left = \text{encode}(5)$.
    - Next sibling is $2 \implies 3.right = \text{encode}(2)$.
  - Node $5$:
    - No children $\implies 5.left = \text{None}$.
    - Next sibling is $6 \implies 5.right = \text{encode}(6)$.
  - Node $6$:
    - No children $\implies 6.left = \text{None}$, no next sibling $\implies 6.right = \text{None}$.
  - Node $2$:
    - No children $\implies 2.left = \text{None}$.
    - Next sibling is $4 \implies 2.right = \text{encode}(4)$.
  - Node $4$:
    - No children $\implies 4.left = \text{None}$, no next sibling $\implies 4.right = \text{None}$.
- **Decoding trace:**
  - Read binary root $1$: instantiate $N$-ary Node $1$.
  - Inspect $1.left = 3$:
    - Traverse right-sibling chain from $3$: $3 \to 2 \to 4$.
    - Child 1 ($3$): decode $3.left = 5$ with right sibling $6 \implies$ children $[5, 6]$.
    - Child 2 ($2$): decode $2.left = \text{None} \implies$ children $[]$.
    - Child 3 ($4$): decode $4.left = \text{None} \implies$ children $[]$.
    - Children of $1$ assembled: $[3, 2, 4]$.
  - Reconstructed $N$-ary tree matches the original input with 100% fidelity.
- **Empty Tree Instance:** $root = \text{None} \implies$ Binary tree is `None` $\implies$ Decodes to `None`
- **Single Node Instance:** $root = \text{Node}(7) \implies \text{TreeNode}(7)$ with `left = right = None`

This instance demonstrates Knuth's canonical Left-Child Right-Sibling (LCRS) tree bijection, mathematically proves the invertibility of sibling-chain projection, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of an $N$-ary tree:
Design an encoding algorithm to convert the $N$-ary tree into a binary tree, and a decoding algorithm to convert that binary tree back into the original $N$-ary tree.

```text
N-ary Tree Representation:              Equivalent Binary Tree (LCRS):
        1                                           1
      / | \                                        /
     3  2  4                                      3
    / \                                          / \
   5   6                                        5   2
                                                 \   \
                                                  6   4
(Node 1 has 3 children)                    (left = first child, right = next sibling)
```

### The Left-Child Right-Sibling (LCRS) Representation
An $N$-ary node can possess an arbitrary number of children, but a binary tree node has strictly two pointers: `left` and `right`.
Knuth's **Left-Child Right-Sibling** isomorphism solves this cleanly:
- **`left` pointer:** Points to the node's **first child** (primary offspring).
- **`right` pointer:** Points to the node's **next immediate sibling** (the next child belonging to the same parent).
This establishes an exact bijective correspondence between the set of all $N$-ary trees and the set of all binary trees whose root has no right child.

---

## 2. Conceptual Foundation & Invariants

### 1. Encoding Rules:
Given an $N$-ary node $u$:
1. If $u$ is `None`, return `None`.
2. Create binary node $B = \text{TreeNode}(u.val)$.
3. If $u.children$ is empty, return $B$.
4. Recursively encode the first child:
   $$
   B.left \leftarrow \text{encode}(u.children[0])
   $$
5. Chain all remaining children $u.children[1 \dots k-1]$ along the `right` pointer of the previous child:
   $$
   curr \leftarrow B.left
   $$
   $$
   curr.right \leftarrow \text{encode}(u.children[i]), \quad curr \leftarrow curr.right \quad \forall i \in [1, k-1]
   $$
6. Return $B$.

### 2. Decoding Rules:
Given a binary node $B$:
1. If $B$ is `None`, return `None`.
2. Create $N$-ary node $u = \text{Node}(B.val, [])$.
3. Walk along the sibling chain starting at $B.left$:
   $$
   curr \leftarrow B.left
   $$
   $$
   \text{While } curr \ne \text{None}: \quad u.children.\text{append}(\text{decode}(curr)), \quad curr \leftarrow curr.right
   $$
4. Return $u$.

> **Bijection Invariant.** For every node $u$, $u.left$ is the head of the linked list of $u$'s children, threaded together horizontally via their `right` pointers.

---

## 3. Step-by-Step Worked Execution

We trace the representative tree with root $1$:

---

### Phase 1: Encoding to Binary Tree

#### Step 1: Root Node 1
- Create `TreeNode(1)`.
- Children: $[3, 2, 4]$.
- First child: Node $3$. Set $1.left = \text{encode}(3)$.
- Root has no siblings $\implies 1.right = \text{None}$.

#### Step 2: Node 3
- Create `TreeNode(3)`.
- Children: $[5, 6]$.
- First child: Node $5$. Set $3.left = \text{encode}(5)$.
- Node $3$ is child index 0 of Root 1. Next sibling is Node $2$.
- Set $3.right = \text{encode}(2)$.

#### Step 3: Node 5
- Create `TreeNode(5)`.
- Children: none $\implies 5.left = \text{None}$.
- Next sibling is Node $6 \implies 5.right = \text{encode}(6)$.

#### Step 4: Node 6
- Create `TreeNode(6)`.
- Children: none $\implies 6.left = \text{None}$.
- No further siblings $\implies 6.right = \text{None}$.
- Subtree at $5$ finishes: $5 \to 5.right = 6$.

#### Step 5: Node 2
- Create `TreeNode(2)`.
- Children: none $\implies 2.left = \text{None}$.
- Next sibling of Node $2$ is Node $4 \implies 2.right = \text{encode}(4)$.

#### Step 6: Node 4
- Create `TreeNode(4)`.
- Children: none $\implies 4.left = \text{None}$.
- No further siblings $\implies 4.right = \text{None}$.
- Binary tree encoding is complete!

---

### Phase 2: Decoding to N-ary Tree

1. **Decode Root 1:**
   - Create `Node(1)`.
   - Inspect $1.left = \text{TreeNode}(3)$.
2. **Collect Children of 1 by traversing right pointers:**
   - Sibling 1: $\text{TreeNode}(3)$.
     - Decode 3: $3.left = \text{TreeNode}(5)$.
     - Collect children of 3 by traversing right pointers:
       - $5$ (has no left $\implies$ leaf).
       - $5.right = 6$ (has no left $\implies$ leaf).
       - Reconstructed children of 3: $[5, 6]$.
     - Reconstructed Node 3: `Node(3, [5, 6])`.
   - Sibling 2 ($3.right = \text{TreeNode}(2)$):
     - Decode 2: $2.left = \text{None} \implies$ leaf.
     - Reconstructed Node 2: `Node(2, [])`.
   - Sibling 3 ($2.right = \text{TreeNode}(4)$):
     - Decode 4: $4.left = \text{None} \implies$ leaf.
     - Reconstructed Node 4: `Node(4, [])`.
   - $4.right = \text{None}$. Sibling chain ends.
3. **Assemble Children into Root 1:**
   - `Node(1).children = [Node(3), Node(2), Node(4)]`.
4. Reconstructed tree is completely identical to input.

---

## 4. Complete Execution Trace

| N-ary Node | Children in N-ary Tree | Binary `left` Pointer (First Child) | Binary `right` Pointer (Next Sibling) | Binary Role |
|:---:|:---:|:---:|:---:|:---|
| **$1$** | $[3, 2, 4]$ | **Node $3$** | `None` | Binary Root |
| **$3$** | $[5, 6]$ | **Node $5$** | **Node $2$** | First child of $1$, points right to sibling $2$ |
| **$2$** | $[]$ | `None` | **Node $4$** | Second child of $1$, points right to sibling $4$ |
| **$4$** | $[]$ | `None` | `None` | Third child of $1$, end of sibling list |
| **$5$** | $[]$ | `None` | **Node $6$** | First child of $3$, points right to sibling $6$ |
| **$6$** | $[]$ | `None` | `None` | Second child of $3$, end of sibling list |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** `encode` returns `None`. `decode` with `None` returns `None`.
- **Single Node Without Children ($root = \text{Node}(10)$):** Encodes to `TreeNode(10)` with `left = right = None`. Decodes to `Node(10, [])`.
- **Unary Tree ($1 \to 2 \to 3$, 1 child each):** Every node has exactly one child. All binary nodes have `left` set and `right = None` (left-skewed binary tree).
- **Single Parent with 100 Children:** The root has 1 child on `left`. That child and all subsequent 99 siblings form a linear right-spine chain of length 100.

---

## 6. Traps & Common Anti-Patterns

- **Interchanging Left and Right Semantic Roles:** Setting `right` as the first child and `left` as the sibling is technically possible, but mixing the two arbitrarily creates an un-invertible structure. Consistently maintaining `left` = first child and `right` = sibling is required.
- **Root Sibling Leak:** The root of the $N$-ary tree has no parent and therefore no siblings. A valid binary tree encoding must always have `binary_root.right == None`.
- **Quadratic Sibling Traversal:** Appending to a sibling list by repeatedly traversing from the start takes $O(K^2)$ time where $K$ is the degree. Keeping a pointer to the current sibling advances in $O(1)$ per child.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Encoding:** Visits each $N$-ary node and its edges once. Every pointer update is $O(1)$. Total time: $\mathcal{O}(N)$.
  - **Decoding:** Visits each binary tree node once, converting right-spine chains into lists in $O(1)$ amortized time per node. Total time: $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ recursion stack depth, where $H$ is the height of the $N$-ary tree (bounded by $N$).
  - The generated binary tree contains exactly $N$ nodes.