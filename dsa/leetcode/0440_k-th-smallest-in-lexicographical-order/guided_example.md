# Guided Example: K-th Smallest in Lexicographical Order

We trace the step-by-step 10-ary prefix tree (denary trie) traversal, prefix subtree size calculation ($\min(n + 1, next) - curr$), sibling skipping ($k \ge cnt \implies curr + 1$), and child descent ($k < cnt \implies curr \times 10$) on representative numerical instances:

- **Input:** $n = 13, \quad k = 2$
- **Required output:** `10`
  - Lexicographical ordering of numbers $1 \dots 13$:
    $$
    [1, \; \mathbf{10}, \; 11, \; 12, \; 13, \; 2, \; 3, \; 4, \; 5, \; 6, \; 7, \; 8, \; 9]
    $$
  - The 2nd element is `10`.
- **Execution trace:**
  - Start at smallest prefix: $curr = 1$. Steps needed: $k = 2 - 1 = 1$.
  - **Iteration 1 (At prefix $curr = 1$):**
    - Count numbers in $[1, 13]$ with prefix $1$:
      - Level 1: $[1, 2) \implies$ numbers $\{1\} \implies \text{count} = 1$
      - Level 2: $[10, 20) \cap [10, 13] \implies \{10, 11, 12, 13\} \implies \text{count} = 4$
      - Level 3: $[100, 200) > 13 \implies 0$
      - Total steps in subtree of $1$: $cnt = 1 + 4 = \mathbf{5}$.
    - Compare $k = 1$ against $cnt = 5$:
      - Since $k = 1 < 5$, the $k$-th smallest number lies **inside** the subtree rooted at $1$!
      - Consume prefix $1$: $k \leftarrow 1 - 1 = 0$.
      - Descend to first child: $curr \leftarrow 1 \times 10 = \mathbf{10}$.
  - Loop terminates because $k = 0$.
  - Emitted result: **`10`**.
- **Sibling Skipping Instance ($n = 13, k = 6$):**
  - Prefix $1$ has $cnt = 5$. Since $k = 5 \ge cnt (5)$, skip subtree $1$: $k \leftarrow 5 - 5 = 0, curr \leftarrow 1 + 1 = \mathbf{2}$ (the 6th element is $2$).
- **Single Element Instance:** $n = 1, k = 1 \implies \mathbf{1}$

This instance demonstrates navigating a virtual 10-ary prefix trie without materializing tree nodes, mathematically proves how interval differences compute subtree cardinalities in $O(\log_{10} n)$ time, and derives $O((\log_{10} n)^2)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two integers $n = 13$ and $k = 2$:
Find the $k$-th lexicographically smallest integer in the range $[1, n]$.

```text
The Virtual 10-ary Trie over [1 .. 13]:
           (Root)
          /  |  \   \
        (1) (2) (3) ... (9)
       / | \ \
     10 11 12 13

Lexicographical Preorder Sequence:
  1st: 1
  2nd: 10  <- Target (k = 2)
  3rd: 11
  4th: 12
  5th: 13
  6th: 2
  ...
```

### The Lexicographical Skip Challenge
Generating and sorting all $n$ numbers takes $O(n \log n)$ time and $O(n)$ space. For $n = 10^9$, this is completely infeasible.
However:
- The numbers $1 \dots n$ form an implicit **10-ary tree** where node $u$ has children $u \cdot 10 + 0, \dots, u \cdot 10 + 9$.
- A lexicographical traversal is precisely a **preorder DFS** on this tree.
- If we can count how many nodes exist in the subtree rooted at $curr$ in $O(\log_{10} n)$ time:
  - If $k$ exceeds the subtree size, we can **skip the entire subtree in a single step**, jumping to the right sibling $curr + 1$.
  - If $k$ falls within the subtree, we step into the leftmost child $curr \cdot 10$.

---

## 2. Conceptual Foundation & Invariants

### 1. Subtree Node Count Formula:
How many integers $\le n$ have prefix $curr$?
At depth $0$, the range of values is $[curr, curr + 1)$.
At depth $1$, the range of values is $[curr \cdot 10, (curr + 1) \cdot 10)$.
At depth $d$, the range of values is $[first, last)$ where $first = curr \cdot 10^d$ and $last = (curr + 1) \cdot 10^d$.
The number of valid integers in $[first, last)$ that are $\le n$ is:
$$
\Delta = \min(n + 1, last) - first
$$
Summing $\Delta$ across all levels until $first > n$ yields the exact total size of $curr$'s subtree:
$$
\text{count}(curr, n) = \sum_{d=0}^{\lfloor \log_{10} n \rfloor} \max(0, \; \min(n + 1, (curr + 1) \cdot 10^d) - curr \cdot 10^d)
$$

### 2. Transition Rules:
Let $k$ be the remaining 0-indexed step budget ($k \leftarrow k - 1$ initially):
Let $cnt = \text{count}(curr, n)$.
1. **Case $k \ge cnt$ (Target is not in this subtree):**
   - Skip the entire subtree of $curr$.
   - Deduct the skipped count: $k \leftarrow k - cnt$.
   - Advance to horizontal right sibling: $curr \leftarrow curr + 1$.
2. **Case $k < cnt$ (Target is inside this subtree):**
   - The root of this subtree ($curr$) accounts for 1 rank.
   - Deduct 1 rank: $k \leftarrow k - 1$.
   - Descend to first vertical child: $curr \leftarrow curr \cdot 10$.

> **Frontier Invariant.** The active prefix $curr$ always corresponds to the root of a candidate subtree known to contain the $k$-th element, and $k$ represents the exact rank of the target within $curr$'s remaining preorder traversal.

---

## 3. Step-by-Step Worked Execution

We trace $n = 13, k = 2$:
Initialize $curr = 1$. Convert $k$ to 0-indexed offset:
$$
k = 2 - 1 = \mathbf{1}
$$

---

### Step 1: Evaluate Subtree of $curr = 1$
Calculate $cnt = \text{count}(1, 13)$:
- Level 0:
  - $first = 1, last = 2$.
  - Contribution: $\min(13 + 1, 2) - 1 = 2 - 1 = \mathbf{1}$ (Value: $1$).
- Level 1:
  - $first = 10, last = 20$.
  - Contribution: $\min(13 + 1, 20) - 10 = 14 - 10 = \mathbf{4}$ (Values: $10, 11, 12, 13$).
- Level 2:
  - $first = 100 > 13$. Loop terminates.
- Total subtree size:
  $$
  cnt = 1 + 4 = \mathbf{5}
  $$

---

### Step 2: Compare Budget $k$ with Subtree Size $cnt$
- Current state: $k = 1, cnt = 5$.
- Condition test:
  $$
  k < cnt \quad (1 < 5)
  $$
- Meaning: The target element is located **within** the subtree rooted at $1$.
- Actions:
  - Consume root $1$: $k \leftarrow 1 - 1 = \mathbf{0}$.
  - Descend to first child:
    $$
    curr \leftarrow 1 \times 10 = \mathbf{10}
    $$

---

### Step 3: Termination Check
- Budget is fully consumed: $k = \mathbf{0}$.
- While-loop terminates.
- Output: $curr = \mathbf{10}$.

---

## 4. Complete Execution Trace

| Step | Prefix $curr$ | Subtree Levels $[first, last)$ | Valid Count at Level | Total Subtree $cnt$ | Budget $k$ | Branch Decision | Next State |
|:---:|:---:|:---|:---:|:---:|:---:|:---|:---|
| **Init** | $1$ | — | — | — | $k = 2 - 1 = 1$ | — | — |
| **1** | $1$ | Level 0: $[1, 2)$<br>Level 1: $[10, 20) \to [10, 14)$ | $1$<br>$4$ | **$5$** | $1$ | $k < 5 \implies$ **Descend Child** | $k = 0, \; curr = 10$ |
| **End** | $10$ | — | — | — | $0$ | Terminate ($k = 0$) | **Result: $10$** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$ (First Element):** $k \leftarrow 0$. Loop does not execute $\implies$ returns $curr = 1$.
- **$k = n$ (Last Element in Range):** Skips subtrees for $1, \dots, 8$ if they do not reach $n$, descends into prefix $9$, finding the lexicographically largest element.
- **Large Bounds ($n = 10^9$):** Each subtree count executes at most $9$ level additions. The traversal depth is at most $9$. Total loop iterations $\le 9 \times 9 = 81$ steps, avoiding memory limits and running in $< 1$ ms.
- **Power of Ten Boundaries ($n = 100, k = 10$):** Correctly traverses through $1, 10, 100, 11, \dots$.

---

## 6. Traps & Common Anti-Patterns

- **Integer Overflow in Sibling Multiplication:** Multiplying $next \times 10$ can exceed 32-bit signed integers when $n \approx 2 \times 10^9$. In languages like C++ or Java, `next` and `curr` must be typed as 64-bit integers (`long long`).
- **Off-By-One in Upper Bound Clamping:** Using $\min(n, next)$ instead of $\min(n + 1, next)$ misses the upper boundary number $n$ itself, causing the count to be short by 1.
- **Converting to Strings for Comparison ($O(n \log n)$):** Stringifying integers takes excessive memory and time for $n = 10^9$. Pure arithmetic tree stepping uses $O(1)$ memory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The height of the 10-ary tree is at most $\log_{10} n \le 10$.
  - Calculating `count(curr)` performs at most $\log_{10} n$ iterations.
  - At each tree depth, we examine at most 9 sibling branches before either descending or concluding.
  - Total Time: $\mathcal{O}((\log_{10} n)^2)$. For $n = 10^9$, at most $\approx 100$ basic arithmetic operations (executes in $< 1$ ms).
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. Requires only a few integer scalar variables for interval endpoints and counters.
