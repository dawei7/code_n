# Guided Example: Path Sum III

We trace the step-by-step tree prefix-sum accumulation ($s = \sum val$), complementary target lookup ($s - targetSum$), hash-map frequency tracking, and backtracking unwinding on representative binary tree paths:

- **Input:**
  - Binary tree: Root $10$, left child $5$, right child $-3$.
    - Node $5$ has children $3$ and $2$.
    - Node $3$ has children $3$ and $-2$.
    - Node $2$ has right child $1$.
    - Node $-3$ has right child $11$.
  - $targetSum = 8$
- **Required output:** `3`
  - Valid downward paths summing to $8$:
    1. Path $5 \to 3$: Sum $= 5 + 3 = 8$
    2. Path $5 \to 2 \to 1$: Sum $= 5 + 2 + 1 = 8$
    3. Path $-3 \to 11$: Sum $= -3 + 11 = 8$
- **Execution trace:**
  - Prefix map initialized: $cnt = \{0: 1\}$ (represents empty prefix before root)
  - **At Root $10$:** Running sum $s = 10$. Lookup $s - 8 = 2$ in $cnt \implies 0$ matches. Register $cnt[10] = 1$.
  - **Descend Left to Node $5$:** $s = 10 + 5 = 15$. Lookup $15 - 8 = 7 \implies 0$ matches. Register $cnt[15] = 1$.
  - **Descend Left to Node $3$:** $s = 15 + 3 = 18$.
    - Lookup $s - 8 = 18 - 8 = 10$ in $cnt$.
    - $cnt[10] = 1$ (from Root $10$!) $\implies$ **Path 1 found ($5 \to 3$)!**
    - Register $cnt[18] = 1$.
    - Explore children of $3$ ($3$ and $-2$), then unwind: decrement $cnt[18] \leftarrow 0$.
  - **Explore Right from Node $5$ to Node $2$:** $s = 15 + 2 = 17$. Lookup $17 - 8 = 9 \implies 0$. Register $cnt[17] = 1$.
  - **Descend Right to Node $1$:** $s = 17 + 1 = 18$.
    - Lookup $18 - 8 = 10$ in $cnt$.
    - $cnt[10] = 1$ $\implies$ **Path 2 found ($5 \to 2 \to 1$)!**
    - Unwind $1$ and $2$.
  - Unwind Node $5$: decrement $cnt[15] \leftarrow 0$.
  - **Descend Right from Root to Node $-3$:** $s = 10 + (-3) = 7$. Lookup $7 - 8 = -1 \implies 0$. Register $cnt[7] = 1$.
  - **Descend Right to Node $11$:** $s = 7 + 11 = 18$.
    - Lookup $18 - 8 = 10$ in $cnt$.
    - $cnt[10] = 1$ $\implies$ **Path 3 found ($-3 \to 11$)!**
  - Traversal completes. Total valid paths: $\mathbf{3}$.
- **Empty Tree Instance:** $root = \text{None} \implies \mathbf{0}$
- **All Values Match Target:** Single node with $val = targetSum \implies 1$ match ($s - targetSum = 0 \in cnt$).

This instance demonstrates tree prefix-sum indexing, mathematically proves why hash-map backtracking isolates independent branches, and achieves $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree and an integer $targetSum = 8$:
Find the number of paths that sum to $targetSum$.
The path does not need to start or end at the root or a leaf, but it must go **downwards** (traveling only from parent nodes to child nodes).

```text
Tree Hierarchy:
           10
          /  \
        5     -3
       / \      \
      3   2      11
     / \   \
    3  -2   1

Three Valid Paths Summing to 8:
  Path 1:  5 -> 3          (5 + 3 = 8)
  Path 2:  5 -> 2 -> 1     (5 + 2 + 1 = 8)
  Path 3: -3 -> 11         (-3 + 11 = 8)
```

### The Linear Prefix Sum Analogy
On an array, finding contiguous subarrays that sum to $K$ uses running prefix sums:
$$
\text{sum}(i \dots j) = \text{prefix}[j] - \text{prefix}[i - 1] = K \iff \text{prefix}[i - 1] = \text{prefix}[j] - K
$$
By storing seen prefix sums in a hash map, each ending position checks for matching start positions in $O(1)$ time.
On a binary tree, the "array" is the path from the root down to the current node.
However, because trees branch:
**When backtracking up out of a subtree, we must remove the current node's prefix sum from the hash map** so it does not falsely leak into sibling subtrees.

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative Path Sum State:
Let $s$ be the sum of all node values along the path from the root down to the current node $u$:
$$
s = \sum_{v \in \text{path}(root \dots u)} v.val
$$
Any downward subsegment ending at $u$ that sums to $targetSum$ begins at some ancestor $w$ such that:
$$
s - \text{prefix}(w) = targetSum \iff \text{prefix}(w) = s - targetSum
$$
Looking up $cnt[s - targetSum]$ yields the exact number of valid paths ending at $u$.

### 2. Backtracking Invariant:
Let $cnt$ be a frequency map of prefix sums:
- Before exploring $u$'s children: increment $cnt[s] \leftarrow cnt[s] + 1$.
- After exploring both left and right subtrees of $u$: decrement $cnt[s] \leftarrow cnt[s] - 1$.
- This guarantees that when examining any node $v$, the map $cnt$ contains *only* prefix sums from ancestors of $v$ along the direct path to the root.

> **Path Isolation Invariant.** At any point during DFS, the hash map $cnt$ reflects the multiset of prefix sums along the unique path from the root to the current node, preventing horizontal cross-talk between sibling branches.

---

## 3. Step-by-Step Worked Execution

We trace $targetSum = 8$ with $cnt = \{0: 1\}$:

---

### Step 1: Root Node 10
- Running sum: $s = 0 + 10 = \mathbf{10}$.
- Target prefix query: $s - targetSum = 10 - 8 = \mathbf{2}$.
- $cnt[2] = 0 \implies$ No path ending at 10.
- Register current prefix: $cnt[10] \leftarrow cnt[10] + 1 = 1$.
- Active ancestor prefixes in $cnt$: $\{0: 1, 10: 1\}$.

---

### Step 2: Traverse Left Subtree (Node 5)
- Running sum: $s = 10 + 5 = \mathbf{15}$.
- Target prefix query: $15 - 8 = \mathbf{7}$.
- $cnt[7] = 0 \implies$ No path ending at 5.
- Register prefix: $cnt[15] \leftarrow 1$.
- Active prefixes: $\{0: 1, 10: 1, 15: 1\}$.

---

### Step 3: Traverse Node 3 (under 5)
- Running sum: $s = 15 + 3 = \mathbf{18}$.
- Target prefix query: $18 - 8 = \mathbf{10}$.
- Lookup: $cnt[10] = \mathbf{1}$!
  - Ancestor with prefix 10 is Root 10.
  - Subpath: from child of Root (5) down to Node 3.
  - Subpath sum: $18 - 10 = 8$ (**Path 1 confirmed: $5 \to 3$**).
  - Global paths count: $ans \leftarrow ans + 1 = \mathbf{1}$.
- Register prefix $cnt[18] \leftarrow 1$.
- Explore children of 3 (subpaths sum to $21$ and $16$, yielding 0 matches).
- **Backtrack from 3:** Decrement $cnt[18] \leftarrow 0$.

---

### Step 4: Traverse Node 2 (under 5)
- Running sum: $s = 15 + 2 = \mathbf{17}$.
- Target prefix query: $17 - 8 = \mathbf{9} \implies cnt[9] = 0$.
- Register prefix: $cnt[17] \leftarrow 1$.
- Descend to Right Child (Node 1):
  - Running sum: $s = 17 + 1 = \mathbf{18}$.
  - Target prefix query: $18 - 8 = \mathbf{10}$.
  - Lookup: $cnt[10] = \mathbf{1}$!
  - Subpath from child of Root (5) down to Node 1: $5 + 2 + 1 = 8$ (**Path 2 confirmed: $5 \to 2 \to 1$**).
  - Global paths count: $ans \leftarrow 1 + 1 = \mathbf{2}$.
- Unwind 1 ($cnt[18] \leftarrow 0$) and 2 ($cnt[17] \leftarrow 0$).
- **Backtrack from Node 5:** Decrement $cnt[15] \leftarrow 0$.

---

### Step 5: Traverse Right Subtree (Node -3)
- Active ancestor prefixes: $\{0: 1, 10: 1\}$.
- Running sum: $s = 10 + (-3) = \mathbf{7}$.
- Target prefix query: $7 - 8 = \mathbf{-1} \implies cnt[-1] = 0$.
- Register prefix: $cnt[7] \leftarrow 1$.
- Descend to Right Child (Node 11):
  - Running sum: $s = 7 + 11 = \mathbf{18}$.
  - Target prefix query: $18 - 8 = \mathbf{10}$.
  - Lookup: $cnt[10] = \mathbf{1}$!
  - Subpath from child of Root (-3) down to Node 11: $-3 + 11 = 8$ (**Path 3 confirmed: $-3 \to 11$**).
  - Global paths count: $ans \leftarrow 2 + 1 = \mathbf{3}$.
- Unwind 11 and -3.
- Unwind Root 10.

---

### Termination:
DFS complete. Total paths discovered: **`3`**.

---

## 4. Complete Execution Trace

| Node Visited | Node Val | Running Sum $s$ | Query $s - 8$ | Query Count in $cnt$ | Paths Found Here | Backtracking Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$10$** | $10$ | $10$ | $2$ | $0$ | None | Push $cnt[10] = 1$ |
| **$5$** | $5$ | $15$ | $7$ | $0$ | None | Push $cnt[15] = 1$ |
| **$3$** | $3$ | $18$ | $10$ | **$1$** | **Path 1: $5 \to 3$** | Push $cnt[18]=1 \to$ Pop $cnt[18]=0$ |
| **$2$** | $2$ | $17$ | $9$ | $0$ | None | Push $cnt[17] = 1$ |
| **$1$** | $1$ | $18$ | $10$ | **$1$** | **Path 2: $5 \to 2 \to 1$** | Push $cnt[18]=1 \to$ Pop $cnt[18]=0$ |
| — | — | — | — | — | — | Pop $cnt[17]=0$, Pop $cnt[15]=0$ |
| **$-3$** | $-3$ | $7$ | $-1$ | $0$ | None | Push $cnt[7] = 1$ |
| **$11$** | $11$ | $18$ | $10$ | **$1$** | **Path 3: $-3 \to 11$** | Push $cnt[18]=1 \to$ Pop $cnt[18]=0$ |
| **Final** | — | — | — | — | **Total: 3** | All nodes unwound cleanly |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** Guard returns `0` immediately.
- **Paths Starting at Root:** When a path starts at the root, $s = targetSum$, so $s - targetSum = 0$. The base prefix $\{0: 1\}$ in the map matches and correctly counts root-originating paths.
- **Negative Node Values and Zero Target:** Prefix sums are not monotonic when negative values exist. The hash map handles negative numbers and non-monotonic sums without degradation.
- **Single Node Tree Matching Target ($root = [8], targetSum = 8$):** $s = 8, s - 8 = 0$. Lookup finds $\{0: 1\} \implies$ returns `1`.

---

## 6. Traps & Common Anti-Patterns

- **Omitting the Backtracking Decrement (`cnt[s] -= 1`):** Failing to decrement $cnt[s]$ when unwinding leaves left-subtree prefix sums in the map while searching the right subtree, creating ghost paths that cross unrelated branches.
- **Double-DFS Brute Force ($O(N^2)$):** Running a separate DFS from every single node takes $O(N^2)$ time in skewed trees. Prefix sum with hash map achieves strictly $O(N)$ linear time in a single pass.
- **Forgetting Sentinel Count $\{0: 1\}$:** Omitting $\{0: 1\}$ causes the algorithm to miss any valid path that begins at the root node.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard DFS visits each of the $N$ tree nodes exactly once.
  - Hash map lookups, insertions, and decrements take $O(1)$ average time.
  - Total Time: $\mathcal{O}(N)$. For $N = 1000$, completes in under 3 ms.
- **Auxiliary Space Complexity:**
  - The recursion stack takes $O(H)$ space, where $H$ is the tree height.
  - The prefix map $cnt$ contains at most $H + 1$ entries at any moment (corresponding to the ancestors of the current node).
  - Total Auxiliary Space: $\mathcal{O}(H)$ ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees).