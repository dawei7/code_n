# Guided Example: Sum Root to Leaf Numbers

We trace the step-by-step base-10 positional digit accumulation and leaf path summation on a representative binary tree:

- **Input:** $\text{root} = [4, 9, 0, 5, 1]$
- **Required output:** $1026$ (Numbers: $495 + 491 + 40 = 1026$)
- **Base Instance:** $\text{root} = [1, 2, 3] \implies 25$ ($12 + 13 = 25$)

This instance demonstrates decimal place-value shifting ($\text{curr} \times 10 + \text{digit}$), distinguishing leaf node terminal returns from internal branch summations, avoiding string conversions via direct integer arithmetic, and achieving linear $O(N)$ runtime.

---

## 1. Instance & Teaching Goal

You are given the root of a binary tree containing digits from $0$ to $9$ only:
$$
\begin{gathered}
4 \\
\swarrow \quad \searrow \\
9 \qquad\quad 0 \\
\swarrow \;\; \searrow \qquad\qquad \\
5 \quad\;\; 1 \qquad\qquad
\end{gathered}
$$
Each root-to-leaf path represents a multi-digit number where the root is the most significant digit.
Calculate the total sum of all root-to-leaf numbers.

The tree contains three distinct root-to-leaf paths:
1. Path $4 \to 9 \to 5$: evaluates to number $495$.
2. Path $4 \to 9 \to 1$: evaluates to number $491$.
3. Path $4 \to 0$: evaluates to number $40$ (notice the trailing zero is preserved).
The required total sum is:
$$
495 + 491 + 40 = 1026
$$

Converting paths to strings and parsing them with `int()` allocates unnecessary objects.
By passing a running integer $\text{curr}$ down the recursion stack and updating it as $\text{curr} \times 10 + \text{node.val}$, each number is constructed directly via positional arithmetic in $O(1)$ operations per step.

---

## 2. Conceptual Foundation & Invariants

### Positional Decimal DFS Protocol
Define recursive function $\text{dfs}(\text{node}, \text{curr})$:

1. **Null Guard:**
   If $\text{node} == \emptyset$: return $0$.
2. **Shift and Add Current Digit:**
   Multiply the accumulated prefix by $10$ to shift existing digits left by one decimal place, then add the current node's value:
   $$
   \text{curr}' = \text{curr} \times 10 + \text{node.val}
   $$
3. **Leaf Node Base Case:**
   If $\text{node.left} == \emptyset$ and $\text{node.right} == \emptyset$:
   - The path has reached a true leaf.
   - Return the completed number directly:
     $$
     \text{return } \text{curr}'
     $$
4. **Internal Node Branching:**
   Recursively evaluate both subtrees and return their sum:
   $$
   \text{return } \text{dfs}(\text{node.left}, \, \text{curr}') + \text{dfs}(\text{node.right}, \, \text{curr}')
   $$

> **Invariant.** When visiting `node`, `curr` stores the exact decimal integer represented by the path from `root` down through `node`'s parent.

---

## 3. Step-by-Step Worked Execution

We trace the recursive calls on $\text{root} = [4, 9, 0, 5, 1]$ starting with $\text{curr} = 0$:

### Step 1: Root Node 4
- Incoming $\text{curr} = 0$.
- Update: $\text{curr}' = 0 \times 10 + 4 = 4$.
- Not a leaf (children $9$ and $0$).
- Recurse left: $\text{dfs}(\text{Node}(9), 4)$.
- Recurse right: $\text{dfs}(\text{Node}(0), 4)$.

---

### Step 2: Left Subtree at Node 9
- Incoming $\text{curr} = 4$.
- Update: $\text{curr}' = 4 \times 10 + 9 = 49$.
- Not a leaf (children $5$ and $1$).
  - **Left Child Node 5:**
    - Incoming $\text{curr} = 49$.
    - Update: $\text{curr}' = 49 \times 10 + 5 = \mathbf{495}$.
    - Node 5 is a leaf ($\text{left} = \text{right} = \emptyset$).
    - Returns number $\mathbf{495}$.
  - **Right Child Node 1:**
    - Incoming $\text{curr} = 49$.
    - Update: $\text{curr}' = 49 \times 10 + 1 = \mathbf{491}$.
    - Node 1 is a leaf ($\text{left} = \text{right} = \emptyset$).
    - Returns number $\mathbf{491}$.
- Node 9 aggregates both leaf returns:
  $$
  495 + 491 = 986
  $$
- Node 9 returns $986$ to Root.

---

### Step 3: Right Subtree at Node 0
- Incoming $\text{curr} = 4$.
- Update: $\text{curr}' = 4 \times 10 + 0 = \mathbf{40}$.
- Node 0 has no children ($\text{left} = \text{right} = \emptyset$).
- **Leaf Detected!**
- Returns number $\mathbf{40}$.

---

### Step 4: Root Node Aggregation
- Root combines left and right subtree results:
  $$
  \text{Total Sum} = 986 + 40 = \mathbf{1026}
  $$

Final answer: $\mathbf{1026}$.

---

## 4. Complete Execution Trace

```text
                     Node 4 (curr=4)
                     /             \
             Node 9 (curr=49)     Node 0 (curr=40) [LEAF -> 40]
             /              \
     Node 5 (curr=495)     Node 1 (curr=491)
       [LEAF -> 495]         [LEAF -> 491]
```

| Recursion Step | Node Visited | Node Digit | Incoming $\text{curr}$ | Computed $\text{curr}' = \text{curr} \times 10 + V$ | Node Type | Value Returned to Caller |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $\text{Node}(4)$ | 4 | 0 | 4 | Internal | Sum of children: $986 + 40 = 1026$ |
| 1.1 | $\text{Node}(9)$ | 9 | 4 | 49 | Internal | Sum of children: $495 + 491 = 986$ |
| 1.1.1 | $\text{Node}(5)$ | 5 | 49 | 495 | **Leaf** | **495** |
| 1.1.2 | $\text{Node}(1)$ | 1 | 49 | 491 | **Leaf** | **491** |
| 1.2 | $\text{Node}(0)$ | 0 | 4 | 40 | **Leaf** | **40** |
| **Result** | - | - | - | - | - | **1026** |

---

## 5. Algorithmic Correctness

**Soundness.** In positional base-10 representation, appending digit $d$ to a number $N$ yields $10 \times N + d$. By multiplying by 10 at every level of descent, the root digit is multiplied by $10^{H-1}$, exactly matching its place value in the root-to-leaf integer.

**Completeness.** Traversal visits every root-to-leaf path. Because leaf values are returned directly and summed at all internal branches, every valid path number is included in the final sum without omission or double counting.

---

## 6. Traps This Instance Exposes

- **Premature Summing on Single Null Children:** If a node has only one child (e.g. left child exists but right is null), treating the null child as a leaf returning `curr` would count the incomplete prefix number! The leaf condition must strictly require `not node.left and not node.right`.
- **Handling Zero Digits:** Trailing zeroes (like node $0$ in path $4 \to 0 = 40$) are fully preserved by the multiplication $\text{curr} \times 10 + 0 = 40$. String conversions can sometimes drop leading or trailing zeroes if parsed carelessly.
- **Empty Tree:** An empty tree $\text{root} == \emptyset$ returns $0$.

### Boundary and Degenerate Instances

| Instance | Input condition | Expected | Why the arithmetic produces it |
|:---|:---|:---:|:---|
| $\text{root} = [1, 2, 3]$ | Both children of the root are leaves | $25$ | One shift builds $12$ and the other builds $13$; the root then returns their sum. |
| $\text{root} = [4, 9, 0, 5, 1]$ | Two 3-digit paths and one 2-digit path | $1026$ | The shorter path stops shifting at $4$ and $0$, contributing $40$ rather than a third 3-digit number. |
| $\text{root} = [0]$ | A single node whose digit is $0$ | $0$ | The only path is the one-digit number $0$; the same value a null child returns, so both the leaf base case and the null guard agree. |
| $\text{root} = [1, \text{null}, 2, \text{null}, 3]$ | Every internal node has exactly one child | $123$ | There is one leaf, so the single number $1 \to 2 \to 3$ is returned instead of three partial prefixes. |
| $\text{root} = [0, 1, 2]$ | The root digit is $0$ and both children are leaves | $3$ | The leading zero adds nothing: $0 \times 10 + 1 = 1$ and $0 \times 10 + 2 = 2$, so the total is $3$ rather than $12$. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited once and performs $O(1)$ arithmetic.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the tree height ($O(\log N)$ balanced, $O(N)$ skewed), to maintain the call stack.

### Alternative Implementations and Their Costs

With $N \le 1000$ nodes and depth $H \le 10$, the arithmetic route is the only one that keeps both the work per node and the live state constant.

| Approach | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| **String concatenation per path** | Append each node's digit to a string and parse the completed string at every leaf. | $\mathcal{O}(N \cdot H)$ worst case | $\mathcal{O}(H)$ live strings plus one string per completed path | Each leaf pays a parse proportional to its depth, and correct zero handling depends on the parser rather than on positional arithmetic. |
| **Positional integer accumulation** (used here) | Pass `curr * 10 + node.val` down the recursion and return that value at a leaf. | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ call stack | Demands the exact leaf test `not node.left and not node.right`; a null child must return $0$ instead of the accumulated prefix. |
| **Breadth-first queue of node-value pairs** | Enqueue each child together with its accumulated value and add to the total when a leaf is dequeued. | $\mathcal{O}(N)$ | $\mathcal{O}(W)$, where $W$ is the widest level (up to roughly $500$ here) | Level order keeps a whole level alive at once, which on this tree is far more state than a depth-3 recursion stack. |
| **Explicit-stack depth-first traversal** | Push (node, value) pairs onto a list and add the value when a leaf is popped. | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ | Matches the recursion in cost and avoids any call-depth limit, but here $H \le 10$, so the call stack is already safe. |