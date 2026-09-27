# Guided Example: Range Sum Query - Mutable

We trace the step-by-step Binary Indexed Tree (Fenwick tree) construction, least-significant bit isolation (`lowbit(x) = x & -x`), point update delta propagation, and $O(\log N)$ prefix sum queries on representative mutable array instances:

- **Input:**
  $$
  \text{nums} = [1, 3, 5]
  $$
  $$
  \text{operations} = [\text{sumRange}(0, 2), \; \text{update}(1, 2), \; \text{sumRange}(0, 2)]
  $$
- **Required outputs:**
  - Initial $\text{sumRange}(0, 2) = 1 + 3 + 5 = 9$
  - After $\text{update}(1, 2)$, array becomes $[1, 2, 5]$
  - Subsequent $\text{sumRange}(0, 2) = 1 + 2 + 5 = 8$
- **Single Element Point Query:** $\text{sumRange}(i, i) = \text{query}(i + 1) - \text{query}(i) = \text{nums}[i]$
- **Arbitrary Point Update:** $\text{update}(i, v)$ computes $\Delta = v - \text{current}$ and applies $\Delta$ to all ancestor tree nodes
- **All-Zero Initial Array:** Tree initializes with all zeros; updates accumulate point values identically

This instance demonstrates Fenwick tree binary interval decomposition, mathematically proves why `x & -x` identifies node range coverage, explains why point updates and range queries each execute in strictly $O(\log N)$ time, and achieves $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a mutable integer array $\text{nums} = [1, 3, 5]$ ($N = 3$):
We need to support two operations dynamically:
1. `update(index, val)`: Set $\text{nums}[index] = val$.
2. `sumRange(left, right)`: Compute $\sum_{i=left}^{right} \text{nums}[i]$.

```text
Initial Array: [1, 3, 5]
Query (0, 2):  1 + 3 + 5 = 9

Update(1, 2):  nums[1] modified from 3 to 2 -> nums = [1, 2, 5]
Query (0, 2):  1 + 2 + 5 = 8
```

### The Mutable Range Sum Dilemma
- An unaugmented array gives $O(1)$ updates, but queries take $O(N)$ linear time.
- A static prefix sum array gives $O(1)$ queries, but updating a single element takes $O(N)$ time to rebuild the prefix table.
- A **Binary Indexed Tree (Fenwick Tree)** balances both operations:
  - Both `update` and `sumRange` execute in **$O(\log N)$ time** using bitwise power-of-two interval decomposition!

---

## 2. Conceptual Foundation & Invariants

### Lowbit and Interval Coverage
For any 1-based index $x \ge 1$:
$$
\operatorname{lowbit}(x) = x \ \& \ (-x)
$$
`lowbit(x)` extracts the value of the lowest set bit in $x$ (e.g. $\operatorname{lowbit}(6) = 6 \ \& \ (-6) = 0\text{b}110 \ \& \ 0\text{b}010 = 2$).

In a Fenwick tree array $c$ of size $N + 1$:
$c[x]$ stores the sum of elements in the 1-based half-open interval:
$$
(x - \operatorname{lowbit}(x), \; x] = [x - \operatorname{lowbit}(x) + 1, \; x]
$$

```text
x = 1 (001): lowbit = 1 -> covers [1, 1] (nums[0])
x = 2 (010): lowbit = 2 -> covers [1, 2] (nums[0] + nums[1])
x = 3 (011): lowbit = 1 -> covers [3, 3] (nums[2])
x = 4 (100): lowbit = 4 -> covers [1, 4] (nums[0] + nums[1] + nums[2] + nums[3])
```

For the traced array $[1, 3, 5]$ only nodes $0 \dots 3$ exist, and their
coverage is fixed before any operation runs. The final column tracks how each
node reacts to the single replacement in the trace:

| Node $x$ | Binary | $\operatorname{lowbit}(x)$ | Interval covered | Array elements held | $c[x]$ after the build | $c[x]$ after `update(1, 2)` |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | 000 | 0 | none — the empty prefix | none | 0 | 0 |
| 1 | 001 | 1 | $[1, 1]$ | nums[0] = 1 | 1 | 1 |
| 2 | 010 | 2 | $[1, 2]$ | nums[0] + nums[1] | 4 | **3** |
| 3 | 011 | 1 | $[3, 3]$ | nums[2] = 5 | 5 | 5 |

Node 0 is a sentinel, not storage: `query` stops there immediately because
$0 > 0$ is already false, while an update launched from node 0 would spin
forever since $0 + \operatorname{lowbit}(0) = 0$. Only node 2 changes, because
element index 1 lives in the 1-based block $[1, 2]$ and in no other block that
this tree materialises; nodes 1 and 3 cover elements that the update never
touched, which is exactly why their values stay put.

### Operations Protocol:

#### 1. Prefix Sum `query(x)`: $\sum_{i=1}^x \text{nums}[i-1]$
Accumulate $c[x]$ and peel off trailing bits:
- While $x > 0$:
  $$
  s \leftarrow s + c[x]
  $$
  $$
  x \leftarrow x - (x \ \& \ -x)
  $$
- Returns the prefix sum of the first $x$ elements.

#### 2. Point Delta `update(x, delta)`:
Propagate $\Delta$ upward to all containing ancestor blocks:
- While $x \le N$:
  $$
  c[x] \leftarrow c[x] + \Delta
  $$
  $$
  x \leftarrow x + (x \ \& \ -x)
  $$

#### 3. Range Sum `sumRange(left, right)`:
$$
\text{sumRange}(left, right) = \text{query}(right + 1) - \text{query}(left)
$$

#### 4. Value Replacement `update(index, val)`:
Find current value at index: $\text{prev} = \text{sumRange}(index, index)$.
Compute difference: $\Delta = val - \text{prev}$.
Apply: $\text{tree.update}(index + 1, \Delta)$.

> **Invariant.** For every $x$, $c[x]$ stores the exact sum of a power-of-two slice. Any prefix $[1, x]$ is partitioned into at most $\lfloor \log_2 x \rfloor + 1$ disjoint power-of-two intervals.

---

## 3. Step-by-Step Worked Execution

We trace the operations on $\text{nums} = [1, 3, 5]$ ($N = 3$):
Fenwick tree size: $N + 1 = 4$, initialized to $c = [0, 0, 0, 0]$.

---

### Step 1: Fenwick Tree Construction
Insert each value $v \in [1, 3, 5]$ at 1-based index $i \in [1, 2, 3]$:
1. **Insert $v = 1$ at $x = 1$:**
   - $x = 1$: $c[1] \mathrel{+}= 1 \implies c[1] = 1$. Next $x = 1 + 1 = 2$.
   - $x = 2$: $c[2] \mathrel{+}= 1 \implies c[2] = 1$. Next $x = 2 + 2 = 4 > 3$. Stop.
2. **Insert $v = 3$ at $x = 2$:**
   - $x = 2$: $c[2] \mathrel{+}= 3 \implies c[2] = 1 + 3 = 4$. Next $x = 2 + 2 = 4 > 3$. Stop.
3. **Insert $v = 5$ at $x = 3$:**
   - $x = 3$: $c[3] \mathrel{+}= 5 \implies c[3] = 5$. Next $x = 3 + 1 = 4 > 3$. Stop.

Tree state:
$$
c = [0, \; 1, \; 4, \; 5]
$$

---

### Step 2: Evaluate $\text{sumRange}(0, 2)$
- Query formula: $\text{query}(2 + 1) - \text{query}(0) = \text{query}(3) - \text{query}(0)$.
- **Evaluate $\text{query}(3)$:**
  - $x = 3$: $s \mathrel{+}= c[3] = 5$. Next $x = 3 - (3 \ \& \ -3) = 3 - 1 = 2$.
  - $x = 2$: $s \mathrel{+}= c[2] = 5 + 4 = 9$. Next $x = 2 - (2 \ \& \ -2) = 2 - 2 = 0$. Stop.
  - $\text{query}(3) = \mathbf{9}$.
- **Evaluate $\text{query}(0)$:**
  - $x = 0 \implies \text{query}(0) = 0$.
- Result: $9 - 0 = \mathbf{9}$.

---

### Step 3: Execute $\text{update}(1, 2)$
- Replace element at index 1 with value $2$.
- Find current value:
  $$
  \text{prev} = \text{sumRange}(1, 1) = \text{query}(2) - \text{query}(1)
  $$
  - $\text{query}(2) = c[2] = 4$.
  - $\text{query}(1) = c[1] = 1$.
  - $\text{prev} = 4 - 1 = 3$.
- Compute delta:
  $$
  \Delta = val - \text{prev} = 2 - 3 = \mathbf{-1}
  $$
- Call $\text{update}(1 + 1 = 2, \; \Delta = -1)$:
  - $x = 2$: $c[2] \mathrel{+}= (-1) \implies c[2] = 4 - 1 = \mathbf{3}$. Next $x = 2 + 2 = 4 > 3$. Stop.
- Updated tree state:
  $$
  c = [0, \; 1, \; 3, \; 5]
  $$

---

### Step 4: Evaluate $\text{sumRange}(0, 2)$ After Update
- Query: $\text{query}(3) - \text{query}(0)$.
- **Evaluate $\text{query}(3)$:**
  - $x = 3$: $s \mathrel{+}= c[3] = 5$. Next $x = 2$.
  - $x = 2$: $s \mathrel{+}= c[2] = 5 + 3 = \mathbf{8}$. Next $x = 0$.
- Result: $8 - 0 = \mathbf{8}$.

---

## 4. Complete Execution Trace

```text
nums = [1, 3, 5], N = 3
c    = [0, 1, 4, 5]

Query 1: sumRange(0, 2) = query(3) - query(0) = (c[3] + c[2]) - 0 = 5 + 4 = 9

Update: update(index=1, val=2):
  prev = sumRange(1, 1) = query(2) - query(1) = 4 - 1 = 3
  delta = 2 - 3 = -1
  c[2] += -1 -> c[2] becomes 3
  c is now [0, 1, 3, 5]

Query 2: sumRange(0, 2) = query(3) - query(0) = (c[3] + c[2]) - 0 = 5 + 3 = 8

Results: [9, 8]
```

| Step | Operation Called | Parameter State | Active Tree Traversal | Tree Array $c$ After Step | Output |
|:---:|:---:|:---:|:---|:---:|:---:|
| Build | `init([1, 3, 5])` | $N = 3$ | Points $1, 2, 3$ initialized | `[0, 1, 4, 5]` | - |
| **1** | **`sumRange(0, 2)`** | $L=0, R=2$ | $\text{query}(3) - \text{query}(0) = 9 - 0$ | `[0, 1, 4, 5]` | **9** |
| 2 | `update(1, 2)` | $\text{idx}=1, v=2$ | $\Delta = 2 - 3 = -1$; update node 2 | **`[0, 1, 3, 5]`** | - |
| **3** | **`sumRange(0, 2)`** | $L=0, R=2$ | $\text{query}(3) - \text{query}(0) = 8 - 0$ | `[0, 1, 3, 5]` | **8** |

Every operation above is one while-loop over node indices, so the whole trace
can be written as the individual pointer walks. Each row is one loop iteration;
the "next" column shows where the peel-off or climb-up rule sends the pointer,
and `s` is the running sum inside a query.

| Called operation | Phase | $x$ | $\operatorname{lowbit}(x)$ | Value read or added | Accumulator or node state | Next $x$ |
|:---|:---|:---:|:---:|:---:|:---|:---|
| Build, insert 1 | climb | 1 | 1 | $+1$ | $c[1] = 1$ | 2 |
| Build, insert 1 | climb | 2 | 2 | $+1$ | $c[2] = 1$ | $4 > 3$, stop |
| Build, insert 3 | climb | 2 | 2 | $+3$ | $c[2] = 4$ | $4 > 3$, stop |
| Build, insert 5 | climb | 3 | 1 | $+5$ | $c[3] = 5$ | $4 > 3$, stop |
| `sumRange(0, 2)` | query(3) | 3 | 1 | $c[3] = 5$ | $s = 5$ | 2 |
| `sumRange(0, 2)` | query(3) | 2 | 2 | $c[2] = 4$ | $s = 9$ | $0$, stop |
| `sumRange(0, 2)` | query(0) | 0 | — | none | $s = 0$, loop never entered | — |
| `update(1, 2)` | query(2) | 2 | 2 | $c[2] = 4$ | $s = 4$ | $0$, stop |
| `update(1, 2)` | query(1) | 1 | 1 | $c[1] = 1$ | $s = 1$ | $0$, stop |
| `update(1, 2)` | climb | 2 | 2 | $\Delta = -1$ | $c[2]: 4 \to 3$ | $4 > 3$, stop |
| `sumRange(0, 2)` after | query(3) | 3 | 1 | $c[3] = 5$ | $s = 5$ | 2 |
| `sumRange(0, 2)` after | query(3) | 2 | 2 | $c[2] = 3$ | $s = 8$ | $0$, stop |

The two directions are visible side by side: a query clears the lowest set bit
and therefore only ever moves to a smaller index, while an update adds it and
only ever moves to a larger one. Neither walk performs more than
$\lfloor \log_2 N \rfloor + 1 = 2$ iterations at $N = 3$, and the update visits
just the single node whose block contains element index 1.

---

## 5. Algorithmic Correctness

**Soundness.** A Fenwick tree organizes partial sums such that every index $x$ is covered by a telescoping sequence of power-of-two intervals. Because $x - (x \ \& \ -x)$ removes the lowest set bit, the intervals are strictly disjoint and sum to the prefix $[1, x]$. Propagating $\Delta$ via $x + (x \ \& \ -x)$ visits all ancestor nodes whose range includes $x$, ensuring every subsequent prefix query reflects the updated value.

**Completeness.** Any query interval $[left, right]$ is expressed as $\text{query}(right + 1) - \text{query}(left)$. The 1-based indexing maps $0$-based index $0$ to empty prefix $\text{query}(0) = 0$, guaranteeing uniform prefix cancellation for all $0 \le left \le right < N$.

---

## 6. Traps This Instance Exposes

- **Replacing vs Adding Delta:** The Fenwick tree `update` adds `delta` to existing node values. Passing `val` directly would compute $\text{old} + \text{val}$ instead of setting the cell to `val`. The difference $\Delta = val - \text{prev}$ must be computed.
- **Zero-Based Indexing Trap:** Calling `update(0, val)` or `lowbit(0)` fails because $0 \ \& \ (-0) = 0$, creating an infinite loop. Fenwick trees must use 1-based indexing ($1$ to $N$).
- **Single Element Query ($left == right$):** Evaluating $\text{sumRange}(i, i)$ returns $\text{query}(i + 1) - \text{query}(i) = \text{nums}[i]$, isolating the exact current value without a separate tracking array.

### Structures this instance rules out

The trace above needs two operations to stay fast at the same time: `update`
must not touch more than a few nodes, and `sumRange` must not walk the array.
Only one of the structures below satisfies both, and the stated limits make the
difference decisive — up to $3 \cdot 10^4$ calls over an array of up to
$3 \cdot 10^4$ elements.

| Structure or strategy | `update(index, val)` | `sumRange(left, right)` | Auxiliary space | Consequence for this problem |
|:---|:---:|:---:|:---:|:---|
| Plain array | $O(1)$: overwrite the cell | $O(N)$: add the slice | $O(N)$ | Correct, but one full-range query costs $3 \cdot 10^4$ additions, and tens of thousands of such queries are permitted |
| Prefix sums, rebuilt on every update | $O(N)$: rewrite the table | $O(1)$ | $O(N)$ plus the array | The mirror image: cheap queries become expensive updates, because a single cell change invalidates every later prefix |
| Fenwick tree (the structure used here) | $O(\log N)$ | $O(\log N)$ | $O(N)$ for $c$ | Each operation stays within $\lfloor \log_2 N \rfloor + 1$ iterations — at most 2 for $[1, 3, 5]$ — and negative deltas such as $\Delta = -1$ need no special case |
| Segment tree | $O(\log N)$ | $O(\log N)$ | about $4N$ nodes | The same two bounds with a larger constant and a recursive descent; it also answers range minimum or maximum, which this problem never asks for |
| Square-root decomposition | $O(1)$ cell plus its block | $O(\sqrt N)$ | $O(N)$ | Cheaper updates than the Fenwick tree at the cost of $\sqrt{N} \approx 173$ block-boundary work per query at the limit, against 15 bit steps |
| A mirror copy of the array for `prev` | $O(1)$ read plus the same climb | unchanged | $O(N)$ extra | Removes the two extra queries that `sumRange(index, index)` performs, but duplicates state that the Fenwick query already reconstructs exactly |

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: $O(N \log N)$ using repeated insertions.
  - `update(index, val)`: $O(\log N)$ logarithmic time, visiting at most $\lceil \log_2 N \rceil$ ancestor nodes.
  - `sumRange(left, right)`: $O(\log N)$ logarithmic time, visiting at most $\lceil \log_2 N \rceil$ bit-cleared nodes.
  - Total time for $Q$ operations: $O(N \log N + Q \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the Fenwick tree array $c$ of size $N + 1$.
