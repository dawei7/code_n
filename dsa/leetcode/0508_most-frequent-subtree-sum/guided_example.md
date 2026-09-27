# Guided Example: Most Frequent Subtree Sum

We trace the step-by-step bottom-up post-order DFS subtree aggregation ($s = l + r + root.val$), frequency counter population ($cnt[s] += 1$), peak multiplicity extraction ($mx = \max(cnt.values())$), and mode collection on representative binary trees:

- **Input:** $root = [5, 2, -5]$
  - Tree structure:
    - Root: $5$
    - Left child: $2$
    - Right child: $-5$
- **Required output:** `[2]`
  - Subtree sum definition: For any node $u$, its subtree sum is the sum of all node values in the subtree rooted at $u$:
    $$
    S(u) = \text{val}(u) + \sum_{v \in \text{Left}(u)} \text{val}(v) + \sum_{w \in \text{Right}(u)} \text{val}(w)
    $$
- **Bottom-up DFS execution trace:**
  - Initialize frequency dictionary: $cnt = \{\}$
  - Post-order traversal rule ($Left \to Right \to Root$):
  - **Step 1 (Visit Left Leaf $2$):**
    - Left child is `None` $\implies 0$
    - Right child is `None` $\implies 0$
    - Subtree sum:
      $$
      s_{left} = 0 + 0 + 2 = \mathbf{2}
      $$
    - Record frequency: $cnt[2] \leftarrow 1$
    - Return $2$ to parent.
  - **Step 2 (Visit Right Leaf $-5$):**
    - Left child is `None` $\implies 0$
    - Right child is `None` $\implies 0$
    - Subtree sum:
      $$
      s_{right} = 0 + 0 + (-5) = \mathbf{-5}
      $$
    - Record frequency: $cnt[-5] \leftarrow 1$
    - Return $-5$ to parent.
  - **Step 3 (Visit Root Node $5$):**
    - Left subtree returned: $l = 2$
    - Right subtree returned: $r = -5$
    - Node value: $5$
    - Subtree sum:
      $$
      s_{root} = l + r + \text{val} = 2 + (-5) + 5 = \mathbf{2}
      $$
    - Record frequency: $cnt[2] \leftarrow 1 + 1 = \mathbf{2}$
    - Return $2$.
  - **Step 4: Find Peak Frequencies:**
    - Frequencies recorded:
      $$
      cnt = \{2: \mathbf{2}, \; -5: 1\}
      $$
    - Maximum frequency:
      $$
      mx = \max(2, 1) = \mathbf{2}
      $$
    - All sums achieving frequency $mx = 2$:
      $$
      ans = \mathbf{[2]}
      $$
- **All Distinct Sums Instance ($root = [5, 2, -3]$):**
  - Left sum: $2$ (count 1)
  - Right sum: $-3$ (count 1)
  - Root sum: $2 + (-3) + 5 = 4$ (count 1)
  - Max frequency is 1 $\implies$ All sums tied $\implies \mathbf{[2, -3, 4]}$
- **Single Node Tree ($root = [10]$):**
  - Only one subtree sum: $10 \implies \mathbf{[10]}$

This instance demonstrates bottom-up tree recursion and multi-modal frequency counting, mathematically proves why post-order traversal computes all subtree sums in linear time, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree $root = [5, 2, -5]$:
The **subtree sum** of a node is the sum of all values in the subtree rooted at that node (including itself).
Find the **most frequent subtree sum**. If there is a tie, return all values with the highest frequency in any order.

```text
Tree:
        5
       / \
      2  -5

Subtree Sums:
  Node (2):   Sum = 2
  Node (-5):  Sum = -5
  Node (5):   Sum = 2 + (-5) + 5 = 2

Frequencies:
  Sum  2: Count = 2  <- Mode!
  Sum -5: Count = 1

Result: [2]
```

### Bottom-Up Subtree Aggregation
To compute the sum of any subtree:
$$
S(u) = u.\text{val} + S(u.\text{left}) + S(u.\text{right})
$$
- A top-down approach that recomputes subtree sums from scratch at each node would take $O(N^2)$ time.
- A **post-order traversal** visits the left and right children first, computes their sums, and then combines them with the parent node in $O(1)$ operations!
- Every node's subtree sum is computed exactly once during the bottom-up return.

---

## 2. Conceptual Foundation & Invariants

### 1. The Post-Order DFS Function:
Define function $dfs(node) \to \text{int}$:
- If $node$ is `None`: return $0$.
- Recurse:
  $$
  l = dfs(node.\text{left}), \quad r = dfs(node.\text{right})
  $$
- Combine:
  $$
  s = l + r + node.\text{val}
  $$
- Increment frequency:
  $$
  cnt[s] \leftarrow cnt[s] + 1
  $$
- Return $s$ to parent.

### 2. Multi-Modal Peak Filtering:
After the traversal visits all $N$ nodes:
1. Identify the maximum frequency:
   $$
   mx = \max_{k \in cnt} cnt[k]
   $$
2. Collect all keys achieving this frequency:
   $$
   ans = [k \text{ for } k, v \in cnt \text{ if } v == mx]
   $$

> **Post-Order Subtree Invariant.** When $dfs(node)$ returns, the exact sum of all descendants of $node$ has been computed and recorded in $cnt$ without redundant subtree traversals.

---

## 3. Step-by-Step Worked Execution

We trace $root = [5, 2, -5]$:

---

### Step 1: Initialize Frequency Counter
$$
cnt = \{\}
$$

---

### Step 2: Post-Order Recursive Traversal

1. **Visit Node 2 (Left child of 5):**
   - $dfs(\text{None}) = 0$, $dfs(\text{None}) = 0$.
   - $s = 0 + 0 + 2 = \mathbf{2}$.
   - Update: $cnt[2] = 1$.
   - Return $2$.

2. **Visit Node -5 (Right child of 5):**
   - $dfs(\text{None}) = 0$, $dfs(\text{None}) = 0$.
   - $s = 0 + 0 + (-5) = \mathbf{-5}$.
   - Update: $cnt[-5] = 1$.
   - Return $-5$.

3. **Visit Node 5 (Root):**
   - Left subtree sum: $l = 2$.
   - Right subtree sum: $r = -5$.
   - $s = 2 + (-5) + 5 = \mathbf{2}$.
   - Update: $cnt[2] \leftarrow 1 + 1 = \mathbf{2}$.
   - Return $2$.

---

### Step 3: Extract Modes
- Counter state:
  $$
  cnt = \{2: 2, \; -5: 1\}
  $$
- Maximum count:
  $$
  mx = \max(2, 1) = \mathbf{2}
  $$
- Filter keys:
  $$
  ans = \mathbf{[2]}
  $$

---

## 4. Complete Execution Trace

| Node Visited | Left Child Sum $l$ | Right Child Sum $r$ | Node Value | Subtree Sum $s = l + r + \text{val}$ | Frequency Count $cnt[s]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Node $2$** | $0$ | $0$ | $2$ | **$2$** | $1$ |
| **Node $-5$** | $0$ | $0$ | $-5$ | **$-5$** | $1$ |
| **Node $5$** | $2$ | $-5$ | $5$ | **$2$** | **$2$** |
| **Peak Selection** | — | — | — | Max Frequency $= 2$ | **Result: `[2]`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($root = [1]$):** Returns `[1]`.
- **All Subtree Sums Tied ($[5, 2, -3]$):** Sums $\{2, -3, 4\}$ each appear once ($mx = 1$) $\implies$ returns all three `[2, -3, 4]`.
- **Degenerate Linked-List Tree ($1 \to 2 \to 3$):** Correctly handles unbalanced linear trees up to recursion stack limit.
- **Negative and Zero Node Values ($[0, 0, 0]$):** All subtree sums evaluate to $0 \implies \mathbf{[0]}$.

---

## 6. Traps & Common Anti-Patterns

- **Recomputing Subtree Sums from Every Node ($O(N^2)$):** Calling a separate helper `sum_tree(node)` from every node revisits nodes repeatedly. Returning the sum directly from the post-order DFS computes all subtree sums in a single pass.
- **Returning Only a Single Mode:** When multiple sums tie for the maximum frequency, returning just one violates the problem specification. All tied keys must be returned in the list.
- **Confusing Path Sum with Subtree Sum:** Subtree sum includes ALL descendants in the entire subtree, not just a path from root to leaf.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Post-order DFS visits each of the $N$ nodes exactly once.
  - At each node, computing the sum and updating the hash map takes $O(1)$ amortized time.
  - Finding the maximum frequency among at most $N$ unique sums takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the frequency hash map $cnt$ and recursion stack ($O(H)$).
