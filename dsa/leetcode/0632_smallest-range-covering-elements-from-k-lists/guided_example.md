# Guided Example: Smallest Range Covering Elements from K Lists

We trace the step-by-step multi-list tuple projection ($(value, list\_id)$), global coordinate sorting, variable-width sliding window expansion ($right$), multi-category frequency coverage tracking ($|cnt| == k$), left boundary contraction ($left$), and minimal range interval minimization ($b - a < span$) on representative sorted list collections:

- **Input:**
  ```text
  nums = [
    [4, 10, 15, 24, 26],   (List 0)
    [0, 9, 12, 20],        (List 1)
    [5, 18, 22, 30]        (List 2)
  ]
  ```
- **Required output:** `[20, 24]`
  - Problem objective: Find an interval $[a, b]$ such that:
    1. Every list contains at least one number in $[a, b]$:
       $$
       \forall i \in [0, k - 1]: \exists x \in nums[i] \text{ such that } a \le x \le b
       $$
    2. The width $b - a$ is **minimized**.
    3. Tie-breaker: If multiple ranges have the same minimal width, choose the one with the smallest starting coordinate $a$.
- **Tagged Tuple Flattening & Sliding Window Equivalence:**
  - Instead of juggling $k$ separate pointers simultaneously, transform the multi-list problem into a standard **sliding window over tagged coordinates**:
    - Tag every number with its source list ID: $(x, list\_id)$.
    - Merge all $N$ numbers into a single list $T$ and sort by value $x$:
      $$
      T = [(0, 1), (4, 0), (5, 2), (9, 1), (10, 0), (12, 1), (15, 0), (18, 2), (20, 1), (22, 2), (24, 0), (26, 0), (30, 2)]
      $$
  - **The Sliding Window Condition:**
    - A subarray $T[j \dots i]$ represents a valid interval $[T[j].val, \; T[i].val]$ if and only if the distinct list IDs in the window equals $k$:
      $$
      |cnt| == k
      $$
    - Maintain a frequency map $cnt$ of active list IDs in the window.
    - Expand $i$: Add $T[i].list\_id$ to $cnt$.
    - Whenever $|cnt| == k$ (all $k$ lists covered):
      - Update best interval with $[T[j].val, T[i].val]$.
      - Shrink from the left by advancing $j$ and decrementing $cnt$ until coverage drops below $k$.
- **Step-by-Step Worked Execution Trace on the Merged Sequence:**
  - Total lists: $k = 3$.
  - Initialize $ans = [-\infty, \infty]$, width $= \infty$, left pointer $j = 0$, map $cnt = \{\}$.
  - **Expand Window with Right Pointer $i$:**
    - Insert $(0, 1) \implies cnt = \{1: 1\}$.
    - Insert $(4, 0) \implies cnt = \{1: 1, 0: 1\}$.
    - Insert $(5, 2) \implies cnt = \{1: 1, 0: 1, 2: 1\}$ (**All 3 covered!**).
  - **First Feasible Window ($j = 0 \dots 2$, values $0 \dots 5$):**
    - Range: $[0, 5]$, width $5 - 0 = \mathbf{5}$.
    - Best range: $[0, 5]$.
    - Shrink $j$: Remove $(0, 1) \implies cnt = \{0: 1, 2: 1\}$ (List 1 dropped).
    - Advance $j \leftarrow 1$.
  - **Continue Expanding $i$:**
    - Insert $(9, 1) \implies cnt = \{0: 1, 2: 1, 1: 1\}$ (**All 3 covered!**).
    - Window $j = 1 \dots 3$, values $4 \dots 9$:
      - Range: $[4, 9]$, width $9 - 4 = \mathbf{5}$ (Tied with 5, but start 4 > 0, so keep $[0, 5]$).
      - Shrink $j$: Remove $(4, 0) \implies j \leftarrow 2$.
    - Insert $(10, 0) \implies$ Covers all 3! Range $[5, 10]$, width $5$.
    - Insert $(12, 1) \implies$ Covers all 3! Range $[5, 12]$, width $7$.
    - Insert $(15, 0) \implies$ Range $[10, 15]$, width $5$.
    - Insert $(18, 2) \implies$ Range $[12, 18]$, width $6$.
  - **Crucial Tightening Phase at $i = 8 \dots 10$:**
    - At $i = 8$, insert $(20, 1)$.
    - At $i = 9$, insert $(22, 2)$.
    - At $i = 10$, insert $(24, 0)$.
    - Active window has right endpoint at $24$ (from List 0).
    - Active window contains:
      - $(20, 1)$ from List 1
      - $(22, 2)$ from List 2
      - $(24, 0)$ from List 0
    - Left pointer $j$ shrinks forward until the earliest required element:
      - $T[j] = (20, 1)$.
      - All three lists $\{0, 1, 2\}$ are covered!
      - Candidate range:
        $$
        [a, b] = [20, \; 24]
        $$
      - Width:
        $$
        b - a = 24 - 20 = \mathbf{4}
        $$
      - Compare with previous best width ($5$):
        $$
        4 < 5 \implies \mathbf{Strictly\ smaller\ width\ found!}
        $$
      - Update global best:
        $$
        ans \leftarrow [\mathbf{20}, \; \mathbf{24}]
        $$
    - Shrink $j$: Remove $(20, 1) \implies$ List 1 is lost ($|cnt| = 2 < 3$).
  - **Subsequent Elements ($26, 30$):**
    - Adding $(26, 0)$ and $(30, 2)$ cannot achieve a width $\le 4$.
  - **Final Output:**
    $$
    ans = \mathbf{[20, 24]}
    $$
    - Verification:
      - List 0 contains $24 \in [20, 24]$.
      - List 1 contains $20 \in [20, 24]$.
      - List 2 contains $22 \in [20, 24]$.
      - All $3$ lists are represented in an interval of width $4$.

This instance demonstrates multi-stream coordinate projection and category-covering sliding window intervals, mathematically proves why sorting transformed tuples reduces $k$-list boundary search to linear two-pointer contraction, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $k$ sorted lists:
Find the **smallest range $[a, b]$** that contains at least one number from every list.

```text
Lists:
  0: [4, 10, 15, 24, 26]
  1: [0, 9, 12, 20]
  2: [5, 18, 22, 30]

Sorted merged tuples:
  (0, L1), (4, L0), (5, L2), (9, L1), ... (20, L1), (22, L2), (24, L0) ...

Optimal Window:
  [20, 24] contains:
    24 from List 0
    20 from List 1
    22 from List 2
  Width = 24 - 20 = 4 (Smallest possible!)
```

### The Invariant of the Tagged Stream
- Merging all elements into a single list tagged with their origin list ID transforms this complex multidimensional problem into the classic **Smallest Subarray Containing All Categories** problem.
- A standard two-pointer sliding window finds the optimal boundary in a single linear pass over the sorted stream.

---

## 2. Conceptual Foundation & Invariants

### 1. The Tuple Transformation:
$$
T = \text{sorted}([(x, i) \text{ for each list } i \text{ and each } x \in nums[i]])
$$

### 2. Sliding Window Invariant:
- Maintain frequency map $cnt$ of list IDs within window $T[j \dots i]$.
- While $\text{len}(cnt) == k$:
  - Current interval is $[T[j].val, T[i].val]$.
  - If $T[i].val - T[j].val < ans[1] - ans[0]$:
    $$
    ans \leftarrow [T[j].val, \; T[i].val]
    $$
  - Evict $T[j]$: decrement $cnt[T[j].id]$, advance $j$.

> **Category Coverage Invariant.** A contiguous subsegment of the sorted stream spans at least one element from each of the $k$ lists if and only if the support size of its origin histogram equals $k$.

---

## 3. Step-by-Step Worked Execution

We trace the candidate intervals:

---

### Step 1: Flatten and Sort
- Sorted stream has 13 tuples.

---

### Step 2: First Full Coverage at Index 2
- Window $[0, 5]$ (values 0, 4, 5).
- Covers lists 1, 0, 2.
- Width $= 5 - 0 = 5$.
- Best $= [0, 5]$.

---

### Step 3: Evolution to Window $[20, 24]$
- At $i = 10$, elements in active window include 20 (L1), 22 (L2), 24 (L0).
- Left pointer $j$ advances to 20.
- Width $= 24 - 20 = 4$.
- $4 < 5 \implies$ New best: $[20, 24]$.

---

### Step 4: Final Answer
$$
\mathbf{[20, 24]}
$$

---

## 4. Complete Execution Trace

| Step Event | Stream Token $(val, list)$ | Window $[j \dots i]$ | Distinct Lists Covered | Span $[a, b]$ | Active Width | Best Range So Far |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Add $(0, 1)$ | $0$ (L1) | $[0 \dots 0]$ | $1$ | — | — | $[-\infty, \infty]$ |
| Add $(4, 0)$ | $4$ (L0) | $[0 \dots 1]$ | $2$ | — | — | $[-\infty, \infty]$ |
| Add $(5, 2)$ | $5$ (L2) | $[0 \dots 2]$ | **$3$ (Full)** | $[0, 5]$ | $5$ | $[0, 5]$ |
| ... | ... | ... | ... | ... | ... | ... |
| Add $(24, 0)$ | $24$ (L0) | $[8 \dots 10]$ | **$3$ (Full)** | $[20, 24]$ | **$4$** | **`[20, 24]`** |
| **Output** | — | — | — | — | — | **`[20, 24]`** |

---

## 5. Boundary Cases & Failure Modes

- **Single List ($k = 1$):** Every element covers all lists $\implies$ width 0: $[x, x]$.
- **All Lists Identical ($[[1], [1], [1]]$):** Window $[1, 1]$ covers all 3 lists with width $0 \implies [1, 1]$.
- **Lists with Duplicate Values:** Handled seamlessly by origin ID tagging.
- **Large Lists ($N = 3500$):** Sorting $3500$ elements takes $< 5$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Using a Priority Queue Without Tracking the Window Max:** A min-heap approach requires tracking the current max of the $k$ elements; forgetting to update the max when pushing breaks the range width calculation.
- **Tie-Breaking Misunderstanding:** If two ranges have equal width ($b - a == d - c$), the problem specifies choosing the one with the smaller starting point ($a < c$).
- **Shrinking Too Late:** The left pointer must shrink immediately while $\text{len}(cnt) == k$ to uncover the tightest possible left boundary.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the total number of elements across all $k$ lists.
  - Sorting all $N$ tagged pairs: $\mathcal{O}(N \log N)$ (or $\mathcal{O}(N \log k)$ using a $k$-way heap merge).
  - Two-pointer sliding window visits each pair at most twice: $\mathcal{O}(N)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the merged tagged array.
