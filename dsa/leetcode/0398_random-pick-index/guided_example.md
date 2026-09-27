# Guided Example: Random Pick Index

We trace the step-by-step inverted index table construction (`self.pos[num].append(i)`), constant-time uniform index sampling (`random.choice(self.pos[target])`), contrast with streaming Reservoir Sampling ($O(1)$ space trade-off), and probability guarantees on representative duplicate arrays:

- **Input:** $nums = [1, 2, 3, 3, 3]$, queries: `pick(3)`, `pick(1)`, `pick(3)`
- **Required output:** `[2, 0, 4]` (any valid random selection from matching index sets)
  - Precomputation trace:
    - Index $0$ ($num = 1$): $pos[1] = [0]$
    - Index $1$ ($num = 2$): $pos[2] = [1]$
    - Index $2$ ($num = 3$): $pos[3] = [2]$
    - Index $3$ ($num = 3$): $pos[3] = [2, 3]$
    - Index $4$ ($num = 3$): $pos[3] = [2, 3, 4]$
  - Query 1: `pick(3)` $\implies$ samples from $[2, 3, 4]$ with equal probability $\frac{1}{3}$ each (e.g. returns $2$)
  - Query 2: `pick(1)` $\implies$ samples from $[0]$ with probability $1$ (returns $0$)
  - Query 3: `pick(3)` $\implies$ samples from $[2, 3, 4]$ with equal probability $\frac{1}{3}$ each (e.g. returns $4$)
- **Single Unique Occurrence:** $nums = [10], target = 10 \implies pos[10] = [0] \implies 0$
- **All Duplicates:** $nums = [5, 5, 5, 5], target = 5 \implies pos[5] = [0, 1, 2, 3] \implies$ each returned with probability $\frac{1}{4}$

This instance demonstrates amortized query optimization using inverted hash maps, mathematically proves why sampling from precomputed index buckets ensures uniform probability, explores the memory-constrained Reservoir Sampling alternative, and derives $O(1)$ query time and $O(N)$ preprocessing space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 2, 3, 3, 3]$ with duplicate values:
Implement the `Solution` class:
- `Solution(int[] nums)`: Initializes the object with the array `nums`.
- `pick(int target)`: Randomly returns an index $i$ such that $nums[i] == target$. Each matching index must have **equal probability** of being chosen.

```text
Array:   [ 1,   2,   3,   3,   3 ]
Indices:   0    1    2    3    4

Inverted Index Map:
  1 -> [0]
  2 -> [1]
  3 -> [2, 3, 4]  (Size 3)

Query pick(3):
  Sample uniformly from {2, 3, 4}
  P(idx = 2) = 1/3
  P(idx = 3) = 1/3
  P(idx = 4) = 1/3
```

### The Architectural Trade-off: Inverted Index vs Reservoir Sampling
1. **Inverted Index Map (Optimal for Multiple Queries):**
   - Precompute a map `pos = {val: [indices]}` in $O(N)$ time.
   - Each `pick(target)` selects a random index from `pos[target]` in strictly $O(1)$ time.
   - Uses $O(N)$ extra memory.
2. **Reservoir Sampling (Optimal for Extreme Memory Constraints):**
   - Do not store index lists.
   - Scan $nums$ on each query: count matches $k$ and replace candidate with probability $1/k$.
   - Uses $O(1)$ extra memory, but takes $O(N)$ time per query.

---

## 2. Conceptual Foundation & Invariants

### 1. Inverted Index Map Structure:
- Construct a hash map `self.pos = defaultdict(list)`:
  For each $(i, num) \in \text{enumerate}(nums)$:
  $$
  self.pos[num].\text{append}(i)
  $$

### 2. Method Invariant:
For any query `pick(target)`:
- Look up precomputed index bucket: $indices = self.pos[target]$.
- Return `random.choice(indices)`.
- If the bucket has size $K = \text{len}(indices)$, each index $i \in indices$ is chosen with probability:
  $$
  P(i) = \frac{1}{K}
  $$

> **Invariant.** For every integer $v \in nums$, `self.pos[v]` contains all indices where $v$ appears in ascending order. Calling `random.choice` on this list guarantees an exact discrete uniform distribution over all occurrences.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3, 3, 3]$:

---

### Step 1: Initialization Phase `__init__(nums)`
Iterate through $nums$ with $(i, num)$:
- $i = 0, num = 1 \implies self.pos[1] = [0]$
- $i = 1, num = 2 \implies self.pos[2] = [1]$
- $i = 2, num = 3 \implies self.pos[3] = [2]$
- $i = 3, num = 3 \implies self.pos[3] = [2, 3]$
- $i = 4, num = 3 \implies self.pos[3] = [2, 3, 4]$
Completed inverted map:
$$
self.pos = \{1: [0], \; 2: [1], \; 3: [2, 3, 4]\}
$$

---

### Step 2: Query 1 — `pick(3)`
- Target: $3$.
- Retrieve index bucket: $indices = self.pos[3] = [2, 3, 4]$.
- Length: $K = 3$.
- Draw discrete uniform random sample:
  $$
  idx \in \{2, 3, 4\} \quad \text{with } P = \frac{1}{3}
  $$
- Candidate chosen: **`2`** (or $3$ or $4$).

---

### Step 3: Query 2 — `pick(1)`
- Target: $1$.
- Retrieve index bucket: $indices = self.pos[1] = [0]$.
- Length: $K = 1$.
- Draw sample:
  $$
  idx = 0 \quad \text{with } P = 1.0
  $$
- Returned index: **`0`**.

---

### Step 4: Query 3 — `pick(3)`
- Target: $3$.
- Retrieve index bucket: $[2, 3, 4]$.
- Independent random draw:
  $$
  idx \in \{2, 3, 4\}
  $$
- Candidate chosen: **`4`**.

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3, 3, 3]

Init:
  pos = {1: [0], 2: [1], 3: [2, 3, 4]}

Call pick(3):
  sample from [2, 3, 4] -> returns 2 (P = 1/3)
Call pick(1):
  sample from [0]       -> returns 0 (P = 1)
Call pick(3):
  sample from [2, 3, 4] -> returns 4 (P = 1/3)

Output Stream: [2, 0, 4]
```

| Operation | Target | Matching Index Bucket $self.pos[target]$ | Bucket Size $K$ | Selection Probability Per Index | Sampled Outcome |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `Init` | All | $\{1: [0], \; 2: [1], \; 3: [2, 3, 4]\}$ | $N = 5$ | - | Table Built |
| `pick` | 3 | $[2, 3, 4]$ | 3 | $\frac{1}{3}$ ($33.3\%$) | **`2`** |
| `pick` | 1 | $[0]$ | 1 | $1$ ($100\%$) | **`0`** |
| **`pick`** | **3** | **$[2, 3, 4]$** | **3** | **$\frac{1}{3}$ ($33.3\%$)** | **`4`** |

---

## 5. Algorithmic Correctness

**Soundness.** Precomputing the inverted index map partitions the set of indices $\{0, 1, \dots, N - 1\}$ into disjoint lists indexed by element value. The list `self.pos[target]` contains all and only the indices where $nums[i] == target$. Calling `random.choice` on this list generates an integer index uniformly in $[0, K - 1]$, giving each index probability exactly $1 / K$.

**Completeness.** By problem guarantee, `target` always exists in $nums$. Thus, `self.pos[target]` is guaranteed to be non-empty, and `random.choice` will never raise an `IndexError` on an empty sequence.

---

## 6. Traps This Instance Exposes

- **Linear Re-Scanning on Every Pick:** Re-scanning the entire array `nums` inside `pick(target)` without a hash map costs $O(N)$ time per query. When $Q = 10^4$ queries are executed on an array of length $N = 10^4$, total runtime is $O(N \cdot Q) = 10^8$ operations, causing TLE.
- **Rejection Sampling Degeneracy:** Generating a random index $r \in [0, N - 1]$ and checking if $nums[r] == target$ takes expected time $N / K$. If $target$ appears only once in an array of $10^5$ elements, each pick takes on average $10^5$ attempts.
- **Memory vs Time Trade-off:** The inverted index map achieves $O(1)$ query time at the cost of $O(N)$ extra space. If memory is strictly constrained to $O(1)$, Reservoir Sampling provides the $O(1)$ space alternative.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `__init__(nums)`: $O(N)$, where $N = \text{len}(nums)$, scanning the array once to build the hash map.
  - `pick(target)`: $O(1)$ time to access the bucket in the hash table and sample an element.
  - Across $Q$ queries, total runtime is $O(N + Q)$, optimal for repeated querying.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space to store all $N$ indices across the buckets of `self.pos`.
