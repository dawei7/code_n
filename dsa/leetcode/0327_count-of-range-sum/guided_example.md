# Guided Example: Count of Range Sum

We trace the step-by-step prefix sum inequality transformation, coordinate compression across boundary intervals ($x - \text{upper}$ and $x - \text{lower}$), Binary Indexed Tree (Fenwick tree) range frequency querying, and valid range sum count accumulation on representative sequence instances:

- **Input:**
  $$
  \text{nums} = [-2, 5, -1], \quad \text{lower} = -2, \quad \text{upper} = 2
  $$
- **Required output:** $3$
  - Subarrays and their sums:
    - $\text{nums}[0 \dots 0] = [-2]$, sum $= -2 \in [-2, 2]$ (Valid)
    - $\text{nums}[2 \dots 2] = [-1]$, sum $= -1 \in [-2, 2]$ (Valid)
    - $\text{nums}[0 \dots 2] = [-2, 5, -1]$, sum $= 2 \in [-2, 2]$ (Valid)
    - Other subarrays: $[5] \implies 5$, $[-2, 5] \implies 3$, $[5, -1] \implies 4$ (All outside $[-2, 2]$)
  - Total valid range sums: $\mathbf{3}$
- **Single Element Within Range:** $\text{nums} = [0], \text{lower} = 0, \text{upper} = 0 \implies 1$
- **Large Bound Negative Values:** Range bounds can span negative coordinates; algebraic rearrangement $x - \text{upper} \le s[i] \le x - \text{lower}$ preserves exact interval boundaries

This instance demonstrates counting inversions and range intervals via Fenwick trees, proves how coordinate compression over prefix points and query bounds maps continuous values to rank indices, contrasts $O(N \log N)$ BIT querying against naive $O(N^2)$ pairwise checking, and analyzes $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given array $\text{nums} = [-2, 5, -1]$ ($N = 3$) with target range $[\text{lower}, \text{upper}] = [-2, 2]$:
Count the number of contiguous subarrays $\text{nums}[i \dots j]$ ($0 \le i \le j < N$) whose sum satisfies:
$$
-2 \le \sum_{k=i}^j \text{nums}[k] \le 2
$$

```text
nums: [-2, 5, -1]
Prefix Sums s: [0, -2, 3, 2] (Length N + 1 = 4)

Subarray sums s[j+1] - s[i]:
(0, 0): s[1] - s[0] = -2 - 0 = -2  (in [-2, 2]) -> VALID (1)
(0, 1): s[2] - s[0] =  3 - 0 =  3  (outside)
(0, 2): s[3] - s[0] =  2 - 0 =  2  (in [-2, 2]) -> VALID (2)
(1, 1): s[2] - s[1] =  3 - (-2) = 5 (outside)
(1, 2): s[3] - s[1] =  2 - (-2) = 4 (outside)
(2, 2): s[3] - s[2] =  2 - 3 = -1  (in [-2, 2]) -> VALID (3)

Total Valid Subarrays: 3
```

### The Inequality Inversion
For any subarray from $i$ to $j$:
$$
\text{lower} \le s[j+1] - s[i] \le \text{upper}
$$
Rearranging to isolate the earlier prefix sum $s[i]$:
$$
s[j+1] - \text{upper} \le s[i] \le s[j+1] - \text{lower}
$$
As we iterate through current prefix sum $x = s[j+1]$, we must count how many **previously seen** prefix sums $s[i]$ ($i \le j$) fall into the closed interval:
$$
[x - \text{upper}, \; x - \text{lower}]
$$

---

## 2. Conceptual Foundation & Invariants

### 1. Cumulative Prefix Sum Array
Compute $s$ with initial $0$:
$$
s = [0, \; -2, \; 3, \; 2]
$$

### 2. Coordinate Compression
Because values of $s[i]$, $x - \text{upper}$, and $x - \text{lower}$ can be arbitrary large or negative integers, we compress all possible query and insertion points:
$$
\text{arr} = \text{sorted}(\text{set}(v \text{ for } x \in s \text{ for } v \in (x, \; x - \text{lower}, \; x - \text{upper})))
$$
For our instance, the unique values are:
$$
\text{arr} = [-4, -2, 0, 1, 2, 3, 4, 5] \quad (\text{Length } 8)
$$
1-based ranks via `bisect_left(arr, val) + 1`:
- $-4 \to 1, \quad -2 \to 2, \quad 0 \to 3, \quad 1 \to 4, \quad 2 \to 5, \quad 3 \to 6, \quad 4 \to 7, \quad 5 \to 8$.

### 3. Binary Indexed Tree (Fenwick Tree) Operations:
Initialize Fenwick tree of size $\text{len}(\text{arr})$:
For each $x \in s$:
1. $l = \text{rank}(x - \text{upper})$
2. $r = \text{rank}(x - \text{lower})$
3. Count valid prior prefixes:
   $$
   \text{ans} \mathrel{+}= \text{tree.query}(r) - \text{tree.query}(l - 1)
   $$
4. Insert current prefix $x$ into the tree:
   $$
   \text{tree.update}(\text{rank}(x), \; 1)
   $$

> **Invariant.** Before inserting $x = s[j+1]$, the Fenwick tree holds the frequencies of all prefix sums $s[0 \dots j]$. Querying $[l, r]$ counts precisely the prefixes $s[i]$ satisfying $s[j+1] - \text{upper} \le s[i] \le s[j+1] - \text{lower}$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $s = [0, -2, 3, 2]$ with $\text{lower} = -2, \text{upper} = 2$:
Sorted points: $\text{arr} = [-4, -2, 0, 1, 2, 3, 4, 5]$.
Tree initialized to all zeros.

---

### Step 1: Process $x = 0$ (Initial Prefix $s[0]$)
- Interval bounds:
  - $x - \text{upper} = 0 - 2 = -2 \implies l = \text{rank}(-2) = 2$.
  - $x - \text{lower} = 0 - (-2) = 2 \implies r = \text{rank}(2) = 5$.
- Query range $[2, 5]$:
  - Tree is empty $\implies \text{query}(5) - \text{query}(1) = 0$.
  - $\text{ans} \mathrel{+}= 0$.
- Insert $x = 0$ ($\text{rank}(0) = 3$):
  - $\text{tree.update}(3, 1)$.
- Active tree multiset: $\{0\}$.

---

### Step 2: Process $x = -2$ (Prefix $s[1]$, Subarray End 0)
- Interval bounds:
  - $x - \text{upper} = -2 - 2 = -4 \implies l = \text{rank}(-4) = 1$.
  - $x - \text{lower} = -2 - (-2) = 0 \implies r = \text{rank}(0) = 3$.
- Query range $[1, 3]$:
  - Ranks present: rank $3$ ($0$) has frequency 1.
  - $\text{query}(3) - \text{query}(0) = \mathbf{1}$.
  - $\text{ans} \mathrel{+}= 1 \implies \text{ans} = \mathbf{1}$ (Subarray $\text{nums}[0 \dots 0] = [-2]$).
- Insert $x = -2$ ($\text{rank}(-2) = 2$):
  - $\text{tree.update}(2, 1)$.
- Active tree multiset: $\{-2, 0\}$.

---

### Step 3: Process $x = 3$ (Prefix $s[2]$, Subarray End 1)
- Interval bounds:
  - $x - \text{upper} = 3 - 2 = 1 \implies l = \text{rank}(1) = 4$.
  - $x - \text{lower} = 3 - (-2) = 5 \implies r = \text{rank}(5) = 8$.
- Query range $[4, 8]$:
  - Ranks in tree: $\{2, 3\}$. None fall in $[4, 8]$.
  - Count: $0$.
  - $\text{ans} \mathrel{+}= 0 \implies \text{ans} = 1$.
- Insert $x = 3$ ($\text{rank}(3) = 6$):
  - $\text{tree.update}(6, 1)$.
- Active tree multiset: $\{-2, 0, 3\}$.

---

### Step 4: Process $x = 2$ (Prefix $s[3]$, Subarray End 2)
- Interval bounds:
  - $x - \text{upper} = 2 - 2 = 0 \implies l = \text{rank}(0) = 3$.
  - $x - \text{lower} = 2 - (-2) = 4 \implies r = \text{rank}(4) = 7$.
- Query range $[3, 7]$:
  - Ranks in tree: rank $3$ ($0$) and rank $6$ ($3$). Both lie in $[3, 7]$!
  - Count: $1 + 1 = \mathbf{2}$.
  - $\text{ans} \mathrel{+}= 2 \implies \text{ans} = 1 + 2 = \mathbf{3}$.
    - Subarray from $s[0]$ to $s[3]$: $\text{nums}[0 \dots 2]$, sum $= 2 - 0 = 2 \in [-2, 2]$.
    - Subarray from $s[2]$ to $s[3]$: $\text{nums}[2 \dots 2]$, sum $= 2 - 3 = -1 \in [-2, 2]$.
- Insert $x = 2$ ($\text{rank}(2) = 5$):
  - $\text{tree.update}(5, 1)$.

---

### Step 5: Final Result
Total range sums within $[-2, 2]$:
$$
\text{ans} = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
nums = [-2, 5, -1], lower = -2, upper = 2
s = [0, -2, 3, 2]
arr = [-4, -2, 0, 1, 2, 3, 4, 5] (ranks 1 to 8)

1. x =  0: query[-2, 2] (ranks 2..5) -> 0 matches -> ans = 0, insert rank 3 (val 0)
2. x = -2: query[-4, 0] (ranks 1..3) -> 1 match (val 0) -> ans = 1, insert rank 2 (val -2)
3. x =  3: query[ 1, 5] (ranks 4..8) -> 0 matches -> ans = 1, insert rank 6 (val 3)
4. x =  2: query[ 0, 4] (ranks 3..7) -> 2 matches (vals 0, 3) -> ans = 3, insert rank 5 (val 2)

Final Result: 3
```

| Step $j+1$ | Prefix $x$ | Lower Query Bound $x - \text{upper}$ | Upper Query Bound $x - \text{lower}$ | Rank Interval $[l, r]$ | Elements Matched in Tree | Increment | Cumulative `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | -2 | 2 | $[2, 5]$ | None | 0 | 0 |
| 1 | -2 | -4 | 0 | $[1, 3]$ | $\{0\}$ | **1** | **1** |
| 2 | 3 | 1 | 5 | $[4, 8]$ | None | 0 | 1 |
| **3** | **2** | **0** | **4** | **$[3, 7]$** | **$\{0, 3\}$** | **2** | **$\mathbf{3}$ (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** A contiguous subarray $\text{nums}[i \dots j]$ has sum $s[j+1] - s[i]$. The condition $\text{lower} \le s[j+1] - s[i] \le \text{upper}$ is algebraically equivalent to $s[j+1] - \text{upper} \le s[i] \le s[j+1] - \text{lower}$. Querying the Fenwick tree counts the exact number of prior prefixes $s[i]$ ($i \le j$) that satisfy this range condition.

**Completeness.** Every prefix sum $s[j+1]$ for $j \in [0, N-1]$ is evaluated. Inserting each prefix into the Fenwick tree only after querying ensures that each valid pair $(i, j)$ with $i \le j$ is counted exactly once without self-matching or future leakage. Coordinate compression preserves all boundary values without truncation.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Suffixes:** Range sums can exceed 32-bit signed integers when summing many values near $2^{31} - 1$. Python automatically promotes integers to arbitrary precision, avoiding overflow.
- **Order of Query vs Update:** Updating the tree with $x$ *before* querying would count the empty subarray $\text{nums}[j+1 \dots j]$ if $0 \in [\text{lower}, \text{upper}]$. Querying *before* updating guarantees $i < j + 1$.
- **Coordinate Compression of Query Bounds:** The compressed array $\text{arr}$ must include not only the prefix values $x$, but also the query bounds $x - \text{lower}$ and $x - \text{upper}$. Omitting query bounds prevents binary search from mapping intervals to exact discrete ranks.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$.
  - Suffix and boundary generation: $3(N + 1)$ elements.
  - Sorting and coordinate compression: $O(N \log N)$.
  - Tree queries and updates: $N + 1$ iterations, each taking $O(\log N)$ time.
  - Total time is $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store prefix array $s$, compressed point array $\text{arr}$, and the Fenwick tree array of size $O(N)$.
