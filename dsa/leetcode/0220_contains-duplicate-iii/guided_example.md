# Guided Example: Contains Duplicate III

We trace the step-by-step bucket partitioning algorithm, sliding window eviction, and adjacent bucket proximity tests on representative value-and-index constrained arrays:

- **Input:** $\text{nums} = [1, 2, 3, 1], \quad \text{indexDiff} = 3, \quad \text{valueDiff} = 0$
- **Required output:** `true` (Indices $0$ and $3$ have $|0 - 3| = 3 \le 3$ and $|1 - 1| = 0 \le 0$)
- **Exceeded Value Gap Instance:** $\text{nums} = [1, 5, 9, 1, 5, 9], \quad \text{indexDiff} = 2, \quad \text{valueDiff} = 3 \implies \text{false}$ (Gaps between adjacent elements are $4 > 3$)
- **Adjacent Match Instance:** $\text{nums} = [1, 3, 6, 2], \quad \text{indexDiff} = 1, \quad \text{valueDiff} = 2 \implies \text{true}$ (Pair at indices 0 and 1 has difference $|1 - 3| = 2 \le 2$)
- **Negative Integer Support:** Correctly handles signed values across bucket boundaries using floor division

This instance demonstrates linear-time proximity search via dynamic bucket sort, proves why bucket width $W = \text{valueDiff} + 1$ guarantees at most 3 bucket queries per element, evicts out-of-window elements ($i - \text{indexDiff}$), and achieves strictly $O(N)$ runtime.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3, 1]$ and thresholds $\text{indexDiff} = 3$ and $\text{valueDiff} = 0$:
Determine whether there exists any pair of distinct indices $(i, j)$ satisfying both:
1. **Index Proximity:** $|i - j| \le \text{indexDiff}$
2. **Value Proximity:** $|\text{nums}[i] - \text{nums}[j]| \le \text{valueDiff}$

A balanced binary search tree (or ordered set) maintains a window of size $\text{indexDiff}$ and queries the predecessor and successor in $O(\log k)$ time, yielding $O(N \log k)$ total time.
The **Bucket Sort** method maps values into discrete intervals of width:
$$
W = \text{valueDiff} + 1
$$
Because the interval width is $\text{valueDiff} + 1$:
- Any two numbers placed into the **same bucket** are guaranteed to have absolute difference $\le \text{valueDiff}$!
- Any number close enough to $\text{nums}[i]$ can reside **only in the same bucket $b$ or the two immediate neighbors $b - 1$ and $b + 1$**!
Testing at most 3 buckets per step achieves optimal **$O(N)$ linear time**.

---

## 2. Conceptual Foundation & Invariants

### Bucket Sizing and Floor Division
For any integer $x$, assign bucket ID:
$$
b = \lfloor x / W \rfloor = x // W \quad \text{where } W = \text{valueDiff} + 1
$$
- Positive integers: $0, 1, \dots, W-1 \implies b = 0$.
- Negative integers: $-1, -2, \dots, -W \implies b = -1$.
Python's integer floor division `//` naturally preserves uniform intervals across zero.

### Sliding Window Bucket Protocol:
Maintain hash map $\text{buckets} = \{\text{bucket\_id}: \text{value}\}$:
For index $i$ from $0$ to $N - 1$:
1. Let $x = \text{nums}[i]$ and $b = x // W$.
2. **Same Bucket Collision:**
   If $b \in \text{buckets}$:
   Return `true`! (Two elements in the same bucket differ by at most $W - 1 = \text{valueDiff}$).
3. **Neighboring Bucket Checks:**
   - If $(b - 1) \in \text{buckets}$ and $|x - \text{buckets}[b - 1]| \le \text{valueDiff}$:
     Return `true`.
   - If $(b + 1) \in \text{buckets}$ and $|x - \text{buckets}[b + 1]| \le \text{valueDiff}$:
     Return `true`.
4. **Register Element:**
   $\text{buckets}[b] = x$.
5. **Window Eviction:**
   If $i \ge \text{indexDiff}$:
   Remove the expired element's bucket:
   $$
   \text{del buckets}[\text{nums}[i - \text{indexDiff}] // W]
   $$

If no match is found after processing all elements, return `false`.

> **Invariant.** At each step $i$, $\text{buckets}$ contains only elements from the sliding window $[i - \text{indexDiff}, i - 1]$. Each bucket contains at most one element (since a second element immediately triggers a return).

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [1, 2, 3, 1]$ with $\text{indexDiff} = 3$ and $\text{valueDiff} = 0$:
- Bucket width $W = \text{valueDiff} + 1 = 0 + 1 = 1$.
- Bucket assignment: $b = x // 1 = x$.
- $\text{buckets} = \{\}$.

---

### Step 1: Index $i = 0$ ($x = 1$)
- Bucket $b = 1 // 1 = 1$.
- Check $b=1$: Not in $\text{buckets}$.
- Check $b-1=0$: Not in $\text{buckets}$.
- Check $b+1=2$: Not in $\text{buckets}$.
- Register: $\text{buckets}[1] = 1$.
- Eviction: $i = 0 \not\ge 3$. No eviction.
- State: $\text{buckets} = \{1: 1\}$.

---

### Step 2: Index $i = 1$ ($x = 2$)
- Bucket $b = 2 // 1 = 2$.
- Check $b=2$: Not in $\text{buckets}$.
- Check $b-1=1$: Present! Value is $1$.
  Check difference:
  $$
  |2 - 1| = 1 \not\le \text{valueDiff} \ (0)
  $$
- Check $b+1=3$: Not in $\text{buckets}$.
- Register: $\text{buckets}[2] = 2$.
- Eviction: $i = 1 \not\ge 3$. No eviction.
- State: $\text{buckets} = \{1: 1, 2: 2\}$.

---

### Step 3: Index $i = 2$ ($x = 3$)
- Bucket $b = 3 // 1 = 3$.
- Check $b=3$: Not in $\text{buckets}$.
- Check $b-1=2$: Present! Value is $2$.
  Check difference:
  $$
  |3 - 2| = 1 \not\le 0
  $$
- Check $b+1=4$: Not in $\text{buckets}$.
- Register: $\text{buckets}[3] = 3$.
- Eviction: $i = 2 \not\ge 3$. No eviction.
- State: $\text{buckets} = \{1: 1, 2: 2, 3: 3\}$.

---

### Step 4: Index $i = 3$ ($x = 1$, Match Found!)
- Bucket $b = 1 // 1 = 1$.
- Check $b=1$: **Present in buckets!** ($\text{buckets}[1] = 1$).
- Two elements occupy bucket $1$.
  Check difference:
  $$
  |1 - 1| = 0 \le \text{valueDiff} \ (0)
  $$
- Index difference: $|3 - 0| = 3 \le \text{indexDiff} \ (3)$.
- **Return `true`!**

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0
Bucket Width W = 0 + 1 = 1

i = 0: x = 1 -> bucket 1 -> Add buckets[1] = 1
i = 1: x = 2 -> bucket 2 -> b-1 (1) diff=1 > 0 -> Add buckets[2] = 2
i = 2: x = 3 -> bucket 3 -> b-1 (2) diff=1 > 0 -> Add buckets[3] = 3
i = 3: x = 1 -> bucket 1 -> BUCKET 1 ALREADY OCCUPIED! (|1 - 1| <= 0) -> RETURN TRUE
```

| Index $i$ | Element $x$ | Bucket ID $b = x // W$ | Proximity Check $(b, b \pm 1)$ | Evicted Bucket ($i \ge \text{indexDiff}$) | Active Buckets Map |
|:---:|:---:|:---:|:---|:---:|:---|
| 0 | 1 | 1 | None | None | `{1: 1}` |
| 1 | 2 | 2 | Neighbor $b-1=1$ (diff 1 > 0) | None | `{1: 1, 2: 2}` |
| 2 | 3 | 3 | Neighbor $b-1=2$ (diff 1 > 0) | None | `{1: 1, 2: 2, 3: 3}` |
| **3** | **1** | **1** | **Same bucket $1$ collision!** | - | **`true` (Match at index 0)** |

### Contrast: Negative Numbers Example $[-3, 3], \text{indexDiff}=2, \text{valueDiff}=4$
- $W = 4 + 1 = 5$.
- $x = -3 \implies b = -3 // 5 = -1$.
- $x = 3 \implies b = 3 // 5 = 0$.
- $b=0$ checks neighbor $b-1=-1$: difference is $|3 - (-3)| = 6 > 4$.
- Correctly returns `false` without negative arithmetic errors.

---

## 5. Algorithmic Correctness

**Soundness.** If a match is found in bucket $b$, both elements fall in the range $[b \cdot W, (b+1) \cdot W - 1]$, guaranteeing difference $\le W - 1 = \text{valueDiff}$. If a match is found in $b \pm 1$, the explicit distance condition $|x - \text{buckets}[b \pm 1]| \le \text{valueDiff}$ is verified. Since buckets are maintained for elements within the last $\text{indexDiff}$ steps, all conditions are guaranteed to hold.

**Completeness.** Any pair $(i, j)$ with $|\text{nums}[i] - \text{nums}[j]| \le \text{valueDiff}$ must either fall into the exact same bucket or into adjacent buckets. Since all elements in the current window are stored in $\text{buckets}$, any valid pair within the sliding window will be tested and accepted.

---

## 6. Traps This Instance Exposes

- **Integer Division with Negatives:** In C++ / Java, integer division truncates toward zero (e.g. $-3 / 5 = 0$, grouping $-3$ with $+3$). In Python, floor division `//` rounds toward $-\infty$ (e.g. $-3 // 5 = -1$), which correctly preserves uniform bucket widths of size $W$.
- **Bucket Size $W = \text{valueDiff}$ vs $W = \text{valueDiff} + 1$:** If $\text{valueDiff} = 0$, dividing by $\text{valueDiff}$ causes a division-by-zero error! Setting $W = \text{valueDiff} + 1$ handles $\text{valueDiff} = 0$ safely.
- **Multiple Elements in Same Bucket:** Because any second element in the same bucket immediately terminates the algorithm with `true`, each bucket key in the dictionary maps to at most one value.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Each element performs at most 3 hash map lookups, 1 insertion, and at most 1 deletion, all taking $O(1)$ amortized time. Total runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(\min(N, \text{indexDiff}))$ auxiliary space to store at most $\text{indexDiff}$ bucket entries.