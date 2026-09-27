# Guided Example: Split Linked List in Parts

We trace the step-by-step linked list total node count traversal ($N$), integer division quotient-remainder partition ($cnt = \lfloor N/k \rfloor, mod = N \pmod k$), front-loaded extra element distribution ($m = cnt + [i < mod]$), sub-list pointer severance ($cur.next \leftarrow \text{null}$), and trailing null-part padding on representative linked structures:

- **Input:** $head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], \quad k = 3$
- **Required output:**
  $$
  [[1, 2, 3, 4], \; [5, 6, 7], \; [8, 9, 10]]
  $$
  - Partitioning criteria:
    - Split a singly linked list of length $N$ into exactly $k$ consecutive parts.
    - **Balanced Lengths:** No two parts may differ in size by more than 1.
    - **Monotone Ordering:** Earlier parts must have size greater than or equal to later parts.
    - **Empty Padding:** If $k > N$, surplus parts must be null/empty `[]`.
    - Each returned part must be a cleanly terminated linked list (`tail.next = null`).
    - For $N = 10$ nodes and $k = 3$:
      - $10 = 4 + 3 + 3$.
      - Part sizes: 4, 3, 3 (maximum difference $4 - 3 = 1$).
      - Parts are $[1, 2, 3, 4]$, $[5, 6, 7]$, and $[8, 9, 10]$.
- **Quotient-Remainder Integer Partition Invariant:**
  - **The Arithmetic Decomposition:**
    - By the Euclidean Division Algorithm, for any non-negative integer $N$ and divisor $k \ge 1$:
      $$
      N = cnt \times k + mod \quad (0 \le mod < k)
      $$
      - $cnt = \lfloor N / k \rfloor$: base minimum capacity of each part.
      - $mod = N \pmod k$: surplus nodes to be distributed.
  - **Front-Loading Distribution Rule:**
    - To satisfy the monotone non-increasing size requirement:
      - The first $mod$ parts receive size $cnt + 1$.
      - The remaining $k - mod$ parts receive size $cnt$.
    - Formula for the size $m_i$ of the $i$-th part ($0 \le i < k$):
      $$
      m_i = cnt + \begin{cases} 1 & \text{if } i < mod \\ 0 & \text{if } i \ge mod \end{cases}
      $$
    - Total verification:
      $$
      \sum_{i=0}^{k-1} m_i = mod \times (cnt + 1) + (k - mod) \times cnt = k \cdot cnt + mod = N
      $$
  - **Sub-list Pointer Severance:**
    - For each part $i$:
      1. Anchor the part head: $ans[i] \leftarrow cur$.
      2. Step forward $m_i - 1$ times to reach the tail node of this part.
      3. Save next part's head: $nxt \leftarrow cur.next$.
      4. Sever link to terminate sub-list cleanly: $cur.next \leftarrow \text{null}$.
      5. Advance active pointer: $cur \leftarrow nxt$.
- **Step-by-Step Worked Execution Trace on $N = 10, k = 3$:**
  - **Phase 0: Measure List Length:**
    - Traverse $head \to 1 \to 2 \dots \to 10 \implies N = 10$.
  - **Phase 1: Compute Part Sizes:**
    - Base size:
      $$
      cnt = \lfloor 10 / 3 \rfloor = \mathbf{3}
      $$
    - Remainder:
      $$
      mod = 10 \pmod 3 = \mathbf{1}
      $$
    - Part 0 ($i = 0 < 1$): size $m_0 = 3 + 1 = \mathbf{4}$.
    - Part 1 ($i = 1 \ge 1$): size $m_1 = 3 + 0 = \mathbf{3}$.
    - Part 2 ($i = 2 \ge 1$): size $m_2 = 3 + 0 = \mathbf{3}$.
    - Size schedule: $[4, 3, 3]$.
  - **Phase 2: Segment the Linked List:**
    - **Part 0 ($i = 0$, target size $m_0 = 4$):**
      - Set head: $ans[0] = Node(1)$.
      - Traverse $m_0 - 1 = 3$ steps to find tail:
        - Step 1: $Node(2)$.
        - Step 2: $Node(3)$.
        - Step 3: $Node(4)$ (Tail).
      - Save next head: $nxt = Node(4).next = Node(5)$.
      - Sever link:
        $$
        Node(4).next \leftarrow \mathbf{null}
        $$
      - Advance: $cur \leftarrow Node(5)$.
      - Resulting sublist: $1 \to 2 \to 3 \to 4 \to \text{null}$.
    - **Part 1 ($i = 1$, target size $m_1 = 3$):**
      - Set head: $ans[1] = Node(5)$.
      - Traverse $m_1 - 1 = 2$ steps to find tail:
        - Step 1: $Node(6)$.
        - Step 2: $Node(7)$ (Tail).
      - Save next head: $nxt = Node(7).next = Node(8)$.
      - Sever link:
        $$
        Node(7).next \leftarrow \mathbf{null}
        $$
      - Advance: $cur \leftarrow Node(8)$.
      - Resulting sublist: $5 \to 6 \to 7 \to \text{null}$.
    - **Part 2 ($i = 2$, target size $m_2 = 3$):**
      - Set head: $ans[2] = Node(8)$.
      - Traverse $m_2 - 1 = 2$ steps to find tail:
        - Step 1: $Node(9)$.
        - Step 2: $Node(10)$ (Tail).
      - Save next head: $nxt = Node(10).next = \text{null}$.
      - Sever link:
        $$
        Node(10).next \leftarrow \mathbf{null}
        $$
      - Advance: $cur \leftarrow \text{null}$.
      - Resulting sublist: $8 \to 9 \to 10 \to \text{null}$.
  - **Phase 3: Output Compilation:**
    $$
    ans = [[1 \to 2 \to 3 \to 4], \; [5 \to 6 \to 7], \; [8 \to 9 \to 10]]
    $$
- **More Parts Than Nodes ($N = 3, k = 5$):**
  - $cnt = 0, mod = 3$.
  - Part sizes: $[1, 1, 1, 0, 0]$.
  - First three parts contain single nodes $[1], [2], [3]$.
  - Trailing two parts receive $\text{null}$ pointers (`[]`, `[]`).
  - Output: $[[1], [2], [3], [], []]$.
- **Empty Initial List ($head = \text{null}, k = 3$):**
  - $N = 0 \implies$ all 3 parts are $\text{null}$.
  - Returns `[[], [], []]`.

This instance demonstrates discrete integer partitioning and singly linked list in-place edge dissection, mathematically proves why front-loading modular remainders minimizes adjacent block variance, and derives $O(N + k)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a linked list of length $N$ and integer $k$:
Split the list into $k$ consecutive parts.
Lengths must differ by at most 1, with earlier parts $\ge$ later parts.
Pad with empty lists if $k > N$.

```text
head = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], k = 3
N = 10

Divmod: 10 // 3 = 3, remainder = 1
First 1 part gets 3 + 1 = 4 nodes: [ 1, 2, 3, 4 ]
Next 2 parts get 3 nodes each:     [ 5, 6, 7 ], [ 8, 9, 10 ]

Sever links between parts:
  4.next = null
  7.next = null
  10.next = null

Result: [ [1, 2, 3, 4], [5, 6, 7], [8, 9, 10] ]
```

### The Invariant of Front-Loaded Remainders
- Distributing $N$ elements into $k$ buckets with size difference $\le 1$ requires giving size $\lfloor N/k \rfloor + 1$ to the first $N \pmod k$ buckets, and $\lfloor N/k \rfloor$ to the remaining buckets.
- Traversal steps $m - 1$ times to locate the sublist tail, breaks the `.next` link, and advances.

---

## 2. Conceptual Foundation & Invariants

### 1. Integer Division Schedule:
$$
cnt = \lfloor N / k \rfloor, \quad mod = N \pmod k
$$
$$
m_i = cnt + \mathbf{1}_{i < mod}
$$

### 2. Pointer Severance Invariant:
For each part $i \in [0, k - 1]$:
$$
ans[i] \leftarrow cur
$$
$$
cur \leftarrow \text{walk}(cur, \; m_i - 1)
$$
$$
nxt \leftarrow cur.next, \quad cur.next \leftarrow \text{null}, \quad cur \leftarrow nxt
$$

> **Equipartition Majorization Invariant.** The partition vector $(m_0, \dots, m_{k-1})$ lexicographically minimizes the $L_2$ norm $\sum m_i^2$ over all non-negative integer vectors summing to $n$, uniquely achieving $\max_i m_i - \min_i m_i \le 1$.

---

## 3. Step-by-Step Worked Execution

We trace $N = 10, k = 3$:

---

### Step 1: Count
- $N = 10$.

---

### Step 2: Schedule
- $cnt = 3, mod = 1$.
- Sizes: $m = [4, 3, 3]$.

---

### Step 3: Part 0 (Size 4)
- Head at 1, walk to 4.
- $4.next \leftarrow \text{null}$. Next head is 5.

---

### Step 4: Part 1 (Size 3)
- Head at 5, walk to 7.
- $7.next \leftarrow \text{null}$. Next head is 8.

---

### Step 5: Part 2 (Size 3)
- Head at 8, walk to 10.
- $10.next \leftarrow \text{null}$.

---

### Step 6: Output
$$
[[1, 2, 3, 4], \; [5, 6, 7], \; [8, 9, 10]]
$$

---

## 4. Complete Execution Trace

| Part Index $i$ | Target Size $m_i$ | Head Node | Tail Node Walked | Severed Pointer | Surviving Next Head |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $4$ ($3 + 1$) | $Node(1)$ | $Node(4)$ | $Node(4).next \leftarrow \text{null}$ | $Node(5)$ |
| $1$ | $3$ ($3 + 0$) | $Node(5)$ | $Node(7)$ | $Node(7).next \leftarrow \text{null}$ | $Node(8)$ |
| **$2$** | **$3$ ($3 + 0$)** | **$Node(8)$** | **$Node(10)$** | **$Node(10).next \leftarrow \text{null}$** | **$\text{null}$** |

---

## 5. Boundary Cases & Failure Modes

- **$k > N$ (More Parts Than Nodes):** First $N$ parts have 1 node each, remaining $k - N$ parts are $\text{null}$.
- **Empty List ($head = \text{null}$):** All $k$ parts are $\text{null}$.
- **$k = 1$:** Single part containing the entire list unchanged.
- **$N$ Evenly Divisible by $k$ ($mod = 0$):** All parts have identical size $cnt$.

---

## 6. Traps & Common Anti-Patterns

- **Not Severing the `.next` Pointer:** Leaving $tail.next$ pointing to the subsequent node leaves all parts connected as one giant list, failing test assertions. Always set `tail.next = null`.
- **Stepping $m$ Times Instead of $m - 1$:** Stepping $m$ times overshoots the tail node onto the start of the next part. Step exactly $m - 1$ times from the head.
- **Null Pointer Dereference When $cur$ is Null:** When $k > N$, check `if cur is None: break` before attempting to access `.next`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to count $N$ nodes: $\mathcal{O}(N)$.
  - One pass to traverse and partition the $N$ nodes into $k$ sublists: $\mathcal{O}(N)$.
  - Initializing output array of size $k$: $\mathcal{O}(k)$.
  - Total Time: strictly linear $\mathcal{O}(N + k)$. Completes in $< 1$ ms for $N = 1000, k = 50$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond the output array of $k$ head pointers.
