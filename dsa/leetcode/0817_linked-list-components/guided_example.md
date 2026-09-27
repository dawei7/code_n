# Guided Example: Linked List Components

We trace the step-by-step linked list sequential traversal, subset membership verification ($val \in S$), contiguous connected component segmentation, run-length block skipping, and total connected component count accumulation on representative singly-linked lists:

- **Input:**
  $$
  head = [0 \to 1 \to 2 \to 3], \quad nums = [0, 1, 3]
  $$
- **Required output:** `2`
  - Linked list connectivity definitions:
    - We have a singly linked list where every node has a unique integer value.
    - We are given a subset $nums$ of these values.
    - Two nodes in $nums$ belong to the same **connected component** if they appear consecutively (adjacent via $next$ pointers) in the linked list.
    - Objective: Count the total number of connected components formed by elements of $nums$.
    - For $head = [0 \to 1 \to 2 \to 3]$ with $nums = [0, 1, 3]$:
      - Node 0 is in $nums$, Node 1 is in $nums$, and $0 \to 1$ are adjacent $\implies$ Component 1: $\{0, 1\}$.
      - Node 2 is **NOT** in $nums$ $\implies$ Breaks the connected run!
      - Node 3 is in $nums$ $\implies$ Component 2: $\{3\}$.
      - Total connected components: **2**.
- **Run-Length Membership & Component Boundary Invariant:**
  - **Fast Hash Set Membership ($S$):**
    - Convert $nums$ into a hash set $S$ for $\mathcal{O}(1)$ membership queries:
      $$
      S = \{ x \mid x \in nums \}
      $$
  - **Contiguous Run Compression:**
    - Traverse the linked list from $head$ to tail:
      1. **Skip Non-Members:** Advance $head$ while $head \ne \text{null}$ and $head.val \notin S$.
      2. **Detect Component Start:**
         - If $head \ne \text{null}$: A new connected component has begun!
           $$
           ans \leftarrow ans + 1
           $$
      3. **Consume Connected Run:**
         - Advance $head$ while $head \ne \text{null}$ and $head.val \in S$. All these nodes belong to this exact same component.
    - Repeat until the end of the linked list is reached.
  - **Alternative Right-Endpoint Invariant:**
    - A node marks the **terminal tail** of a connected component if:
      $$
      curr.val \in S \quad \text{and} \quad (curr.next = \text{null} \lor curr.next.val \notin S)
      $$
    - Summing all terminal tails yields the exact same count in a single pointer sweep.
- **Step-by-Step Worked Execution Trace on $[0 \to 1 \to 2 \to 3]$:**
  - Hash set: $S = \{0, 1, 3\}$.
  - Initialize: $ans = 0, curr = head$.
  - **Node 0 ($val = 0$):**
    - Is $0 \in S$? $\implies \mathbf{Yes.}$
    - Start of new component!
      $$
      ans \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Advance through consecutive members in $S$:
      - Node 0: $0 \in S \implies$ advance to Node 1.
      - Node 1: $1 \in S \implies$ advance to Node 2.
    - Consecutive segment $\{0, 1\}$ consumed.
  - **Node 2 ($val = 2$):**
    - Is $2 \in S$? $\implies \mathbf{No.}$
    - Advance past non-members:
      - Node 2: $2 \notin S \implies$ advance to Node 3.
  - **Node 3 ($val = 3$):**
    - Is $3 \in S$? $\implies \mathbf{Yes.}$
    - Start of new component!
      $$
      ans \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Advance through consecutive members in $S$:
      - Node 3: $3 \in S \implies$ advance to `null`.
    - Consecutive segment $\{3\}$ consumed.
  - **End of List Reached ($curr = \text{null}$):**
    - Total components:
      $$
      ans = \mathbf{2}
      $$
- **Two Disjoint Pairs Trace ($head = [0 \to 1 \to 2 \to 3 \to 4], nums = [0, 3, 1, 4]$):**
  - Node 0 and 1 $\in S \implies$ Component 1 ($\{0, 1\}$).
  - Node 2 $\notin S \implies$ Split.
  - Node 3 and 4 $\in S \implies$ Component 2 ($\{3, 4\}$).
  - Total components: **2**.
- **All Elements in $nums$ ($nums == head$):**
  - All nodes form a single uninterrupted chain $\implies ans = \mathbf{1}$.
- **Isolated Alternating Singletons ($nums = [0, 2, 4]$):**
  - Separators at nodes 1 and 3 $\implies ans = \mathbf{3}$.

This instance demonstrates 1D connectivity on directed line graphs and binary run-length compression under boolean characteristic functions, mathematically proves why contiguous runs partition linear posets into maximal connected subgraphs, and derives $O(N + M)$ execution time and $O(M)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a linked list and subset $nums$:
Count how many **connected components** exist (nodes in $nums$ that are directly adjacent in the list).

```text
List: 0 -> 1 -> 2 -> 3
nums: { 0, 1, 3 }

Segment 1: [ 0 -> 1 ] (both in nums) -> Component 1
Separator:   2        (not in nums)   -> Break
Segment 2:   3        (in nums)       -> Component 2

Total components = 2
Result: 2
```

### The Invariant of Contiguous Run Counting
- Store $nums$ in a hash set for $O(1)$ lookup.
- Skip nodes not in $nums$.
- When a node in $nums$ is encountered, increment count by 1 and skip all consecutive nodes that are in $nums$.

---

## 2. Conceptual Foundation & Invariants

### 1. Characteristic Function:
$$
\chi_S(v) = \begin{cases} 1 & v \in nums \\ 0 & v \notin nums \end{cases}
$$

### 2. Component Boundary Condition:
$$
ans = \sum_{u \in List} \Big[ \chi_S(u) = 1 \;\land\; \big( u.next = null \lor \chi_S(u.next) = 0 \big) \Big]
$$

> **Linear Poset Induced Subgraph Invariant.** The linked list is a directed tree of maximum in/out degree 1. The induced subgraph $G[S]$ is a collection of disjoint path graphs. The number of paths equals the number of sinks in $G[S]$.

---

## 3. Step-by-Step Worked Execution

We trace $head = [0 \to 1 \to 2 \to 3], nums = [0, 1, 3]$:

---

### Step 1: Initialize
- $S = \{0, 1, 3\}, ans = 0$.

---

### Step 2: Node 0
- $0 \in S \implies$ new component! $ans = 1$.
- Skip 0 and 1 (both $\in S$).

---

### Step 3: Node 2
- $2 \notin S \implies$ skip.

---

### Step 4: Node 3
- $3 \in S \implies$ new component! $ans = 2$.
- Skip 3 ($\in S$).

---

### Step 5: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Node Value | In Set $S$? | Action | Run Type | Running Component Count $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | Yes | **New Component Started** | Member Run | $1$ |
| $1$ | Yes | Continue Run | Member Run | $1$ |
| $2$ | No | **Break / Disconnect** | Non-member Gap | $1$ |
| **$3$** | **Yes** | **New Component Started** | **Member Run** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node List:** $nums = [0] \implies 1$; $nums = [] \implies 0$.
- **Entire List in $nums$:** Continuous unbroken run $\implies 1$.
- **No Two Consecutive Nodes in $nums$:** Every element is an isolated component $\implies |nums|$.
- **Subsets of Length 1:** Returns 1.

---

## 6. Traps & Common Anti-Patterns

- **Searching `nums` as a List ($O(N \cdot M)$):** Checking `head.val in nums` on a Python list takes linear time per node, resulting in $O(N^2)$ quadratic slowdown. A hash set `set(nums)` provides strictly $O(1)$ lookups.
- **Incrementing on Every Matching Node:** Do NOT increment for every node in $nums$; only increment when starting a new contiguous run.
- **Null Pointer Exceptions on Inner While Loops:** Always check `head is not None` before accessing `head.val` or `head.next`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructing hash set from $nums$ of size $M$: $\mathcal{O}(M)$.
  - Single pass through linked list of length $N$: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N + M)$ where $N, M \le 10^4$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M)$ memory for the hash set $S$.
