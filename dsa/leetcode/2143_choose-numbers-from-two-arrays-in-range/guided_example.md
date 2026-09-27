# Guided Example: Choose Numbers From Two Arrays in Range

We analyze and execute the rolling balance Dynamic Programming algorithm on a representative problem instance, demonstrating how signed algebraic transformation converts range partition matching into zero-sum prefix path counting.

- **Input:** `nums1 = [1, 2, 5]`, `nums2 = [2, 6, 3]`
- **Output:** `3`

This instance illustrates active range spawning, branch extension via signed delta transitions, and cumulative zero-balance collection.

---

## 1. Problem Overview & Representative Instance

Given two integer arrays `nums1` and `nums2` of length $n$, we consider every contiguous subarray range $[l, r]$ with $0 \le l \le r < n$. For each index $i \in [l, r]$, we must choose exactly one value:
- Choose from `nums1`: contributes $\text{nums1}[i]$ to the sum of array 1.
- Choose from `nums2`: contributes $\text{nums2}[i]$ to the sum of array 2.

A range $[l, r]$ together with a specific choice assignment across its indices is called **balanced** if:
$$\sum_{i \in \text{chosen from nums1}} \text{nums1}[i] = \sum_{i \in \text{chosen from nums2}} \text{nums2}[i]$$

Two selections are considered distinct if:
1. The left endpoint $l$ differs,
2. The right endpoint $r$ differs, or
3. At least one index $i \in [l, r]$ chooses a different source array.

The task is to compute the total number of distinct balanced configurations modulo $10^9 + 7$.

In our representative instance:
- `nums1 = [1, 2, 5]`
- `nums2 = [2, 6, 3]`
- Length $n = 3$.

---

## 2. Mathematical & Algorithmic Principles

### Signed Delta Algebraic Transformation

Rather than maintaining two independent running sums $\sum_{1}$ and $\sum_{2}$, we define a single signed balance variable $\Delta$:
$$\Delta = \sum_{1} - \sum_{2}$$

A range selection is balanced if and only if:
$$\Delta = 0$$

At each index $i$:
- Selecting $\text{nums1}[i]$ contributes $+\text{nums1}[i]$ to $\Delta$.
- Selecting $\text{nums2}[i]$ contributes $-\text{nums2}[i]$ to $\Delta$.

### Rolling Subarray DP with Dual Actions

At each index $i \in [0, n - 1]$, two independent mechanisms generate ranges ending at $i$:
1. **Spawn New Range Starting at $i$ ($l = i$):**
   - Option A: Pick $\text{nums1}[i] \implies \text{delta} = +\text{nums1}[i]$.
   - Option B: Pick $\text{nums2}[i] \implies \text{delta} = -\text{nums2}[i]$.
2. **Extend Existing Ranges Ending at $i - 1$ ($l < i$):**
   - For every existing balance $b$ with frequency $\text{count}(b)$ ending at index $i - 1$:
     - Extend by choosing $\text{nums1}[i] \implies \text{new delta} = b + \text{nums1}[i]$, with frequency $\text{count}(b)$.
     - Extend by choosing $\text{nums2}[i] \implies \text{new delta} = b - \text{nums2}[i]$, with frequency $\text{count}(b)$.

### Accumulation of Zero-Balance Configurations

After computing the frequency table $\text{DP}_i[\Delta]$ of all active selections ending at index $i$:
$$\text{Total Balanced} = \sum_{i=0}^{n-1} \text{DP}_i[0] \pmod{10^9 + 7}$$

| Parameter | Algebraic Definition | Concrete Role in Problem |
|---|---|---|
| State $\Delta$ | $\sum \text{nums1} - \sum \text{nums2}$ | Net signed balance for a contiguous choice sequence |
| $\text{DP}_i[\Delta]$ | Number of choice sequences ending at $i$ with net balance $\Delta$ | Rolling dynamic programming frequency state |
| Target State $\Delta = 0$ | Perfect equality between array 1 and array 2 sums | Balanced configurations contributing to final answer |
| Spawn Step | $+\text{nums1}[i]$ and $-\text{nums2}[i]$ | Starts a new candidate subarray at left index $l = i$ |
| Extension Step | $b + \text{nums1}[i]$ and $b - \text{nums2}[i]$ | Continues candidate subarrays from $l < i$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the algorithm on `nums1 = [1, 2, 5]` and `nums2 = [2, 6, 3]` across indices $0, 1, 2$.

```
Index 0: nums1[0] = 1, nums2[0] = 2
Index 1: nums1[1] = 2, nums2[1] = 6
Index 2: nums1[2] = 5, nums2[2] = 3
```

### Step 1: Process Index $i = 0$
- Values: $\text{nums1}[0] = 1$, $\text{nums2}[0] = 2$.
- No prior state exists.
- Spawn new ranges at index $0$:
  - Choose `nums1[0]`: $\Delta = +1$ (1 way).
  - Choose `nums2[0]`: $\Delta = -2$ (1 way).
- Active DP table $\text{DP}_0$:
  - $\{+1: 1, -2: 1\}$.
- Count with $\Delta = 0$: $0$.
- Cumulative answer: $0$.

### Step 2: Process Index $i = 1$
- Values: $\text{nums1}[1] = 2$, $\text{nums2}[1] = 6$.
- Spawn new ranges at index $1$:
  - Choose `nums1[1]`: $\Delta = +2$ (1 way).
  - Choose `nums2[1]`: $\Delta = -6$ (1 way).
- Extend existing ranges from $\text{DP}_0$:
  - From balance $+1$ (1 way):
    - Choose `nums1[1]`: $+1 + 2 = +3$ (1 way).
    - Choose `nums2[1]`: $+1 - 6 = -5$ (1 way).
  - From balance $-2$ (1 way):
    - Choose `nums1[1]`: $-2 + 2 = 0$ (1 way). **Balanced!**
    - Choose `nums2[1]`: $-2 - 6 = -8$ (1 way).
- Active DP table $\text{DP}_1$:
  - $\{+3: 1, +2: 1, 0: 1, -5: 1, -6: 1, -8: 1\}$.
- Count with $\Delta = 0$: $1$ (Range $[0, 1]$ choosing `nums2[0]` and `nums1[1]`: $\text{sum}_1 = 2, \text{sum}_2 = 2$).
- Cumulative answer: $0 + 1 = 1$.

### Step 3: Process Index $i = 2$
- Values: $\text{nums1}[2] = 5$, $\text{nums2}[2] = 3$.
- Spawn new ranges at index $2$:
  - Choose `nums1[2]`: $\Delta = +5$ (1 way).
  - Choose `nums2[2]`: $\Delta = -3$ (1 way).
- Extend existing ranges from $\text{DP}_1$:
  - From $+3$ (1 way):
    - $+5 \implies +8$ (1 way).
    - $-3 \implies 0$ (1 way). **Balanced!**
  - From $+2$ (1 way):
    - $+5 \implies +7$ (1 way).
    - $-3 \implies -1$ (1 way).
  - From $0$ (1 way):
    - $+5 \implies +5$ (1 way).
    - $-3 \implies -3$ (1 way).
  - From $-5$ (1 way):
    - $+5 \implies 0$ (1 way). **Balanced!**
    - $-3 \implies -8$ (1 way).
  - From $-6$ (1 way):
    - $+5 \implies -1$ (1 way).
    - $-3 \implies -9$ (1 way).
  - From $-8$ (1 way):
    - $+5 \implies -3$ (1 way).
    - $-3 \implies -11$ (1 way).
- Count with $\Delta = 0$ at index $2$: $2$.
  - First balanced selection: Extended from $+3$ via $-3$. Originates from range $[0, 2]$ with choices `[nums1[0], nums1[1], nums2[2]]` ($\text{sum}_1 = 1 + 2 = 3, \text{sum}_2 = 3$).
  - Second balanced selection: Extended from $-5$ via $+5$. Originates from range $[0, 2]$ with choices `[nums1[0], nums2[1], nums1[2]]` ($\text{sum}_1 = 1 + 5 = 6, \text{sum}_2 = 6$).
- Cumulative answer: $1 + 2 = 3$.

Execution completes. Total balanced selections: $3$.

---

## 4. Comprehensive State Trace

The table below catalogs the progression of active balances and zero-sum detections across all indices:

| Index $i$ | $\text{nums1}[i]$ | $\text{nums2}[i]$ | Spawns Added | Extensions Computed | Zero-Sum Matches ($\Delta = 0$) | Matches Meaning | Total Count |
|---|---|---|---|---|---|---|---|
| $0$ | $1$ | $2$ | $+1, -2$ | None | $0$ | None | $0$ |
| $1$ | $2$ | $6$ | $+2, -6$ | From $+1 \to +3, -5$<br>From $-2 \to 0, -8$ | $1$ | Range $[0, 1]$: `[nums2[0], nums1[1]]` ($2 = 2$) | $1$ |
| $2$ | $5$ | $3$ | $+5, -3$ | From $+3 \to +8, 0$<br>From $+2 \to +7, -1$<br>From $0 \to +5, -3$<br>From $-5 \to 0, -8$<br>From $-6 \to -1, -9$<br>From $-8 \to -3, -11$ | $2$ | Range $[0, 2]$: `[nums1, nums1, nums2]` ($3 = 3$)<br>Range $[0, 2]$: `[nums1, nums2, nums1]` ($6 = 6$) | $3$ |

### Verification of All Three Balanced Selections

1. **Selection A:** Range $[0, 1]$
   - Index $0$: choose `nums2[0] = 2`.
   - Index $1$: choose `nums1[1] = 2`.
   - Sum array 1: $2$. Sum array 2: $2$. Balance: $2 - 2 = 0$.
2. **Selection B:** Range $[0, 2]$
   - Index $0$: choose `nums1[0] = 1`.
   - Index $1$: choose `nums1[1] = 2`.
   - Index $2$: choose `nums2[2] = 3`.
   - Sum array 1: $1 + 2 = 3$. Sum array 2: $3$. Balance: $3 - 3 = 0$.
3. **Selection C:** Range $[0, 2]$
   - Index $0$: choose `nums1[0] = 1`.
   - Index $1$: choose `nums2[1] = 6`.
   - Index $2$: choose `nums1[2] = 5`.
   - Sum array 1: $1 + 5 = 6$. Sum array 2: $6$. Balance: $6 - 6 = 0$.

All three configurations are mathematically valid and mutually distinct.

---

## 5. Algorithmic Correctness & Soundness

### Completeness by Subarray Construction
Every valid balanced selection corresponds to a unique contiguous range $[l, r]$ and a unique sequence of binary decisions. 
- Spawning a new range at each index $l$ guarantees that all possible left boundaries are seeded.
- Propagating forward through indices $l+1, \dots, r$ by trying both choices guarantees that all $2^{r - l + 1}$ decision paths are explored.
- Aggregating at the moment the right boundary reaches $r$ ensures every balanced range $[l, r]$ is counted exactly once when its balance evaluates to $0$.

### Soundness by Additive Independence
The balance update $\Delta' = \Delta \pm \text{val}$ depends only on the current cumulative delta $\Delta$ and the newly chosen element. The history of which specific earlier elements produced $\Delta$ does not affect future delta transitions. Therefore, merging equal deltas via frequency aggregation $\text{count}(\Delta)$ is completely sound and preserves exact combinatorial multiplicity.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Zero-Valued Elements ($\text{nums1}[i] = 0$ or $\text{nums2}[i] = 0$):** If an element has value $0$, selecting it produces $\Delta = 0$ immediately for a singleton range $[i, i]$. The algorithm correctly adds $+0$ or $-0$, producing valid zero-balance counts.
2. **Both Elements Zero at the Same Index:** If $\text{nums1}[i] = 0$ and $\text{nums2}[i] = 0$, both choices are distinct according to the problem contract. Spawning adds two separate ways with delta $0$, both counted.
3. **Large Balances with Maximum Constraints:** With $n \le 100$ and values up to $100$, the maximum possible balance is $100 \times 100 = 10000$, and the minimum is $-10000$. The range $[-10000, 10000]$ contains at most $20001$ states, perfectly manageable in a flat array or hash table.
4. **Modulo Arithmetic:** Frequency additions must be performed modulo $10^9 + 7$ at every step to prevent integer overflow.

### Common Anti-Patterns
- **Brute Force Subarray Recursion:** Enumerating all $O(n^2)$ ranges and testing all $2^{r-l+1}$ assignments requires $O(n^2 \cdot 2^n)$ time, which is impossible for $n = 100$.
- **Collapsing Identical Value Choices:** If $\text{nums1}[i] = \text{nums2}[i]$, choosing from `nums1` versus `nums2` are distinct configurations. Treating them as identical produces undercounts.
- **Forgetting Range Spawning:** Extending only from index $0$ restricts evaluation to prefixes $[0, r]$, omitting valid subsegments $[l, r]$ with $l > 0$.

---

## 7. Complexity Analysis

### Time Complexity
- Let $n$ be the array length, and let $M = \max(\text{nums1}[i], \text{nums2}[i])$.
- The maximum possible balance is $S = n \cdot M \le 100 \times 100 = 10000$.
- The number of distinct possible delta states at any index is at most $2S + 1 \le 20001$.
- At each index $i \in [0, n - 1]$:
  - Iterating over all active states in the previous table and making two transitions takes $O(\min(2^i, S))$ time.
- Across $n$ steps, the total time complexity is $O(n \cdot (n \cdot M)) = O(n^2 \cdot M)$.
- For $n = 100$ and $M = 100$, the number of inner loop operations is at most $100 \times 20001 \approx 2 \times 10^6$, which runs in less than $0.05$ seconds.

### Auxiliary Space Complexity
- A rolling DP approach requires storing only the state frequencies for the current index and the previous index.
- Each frequency table stores at most $2S + 1$ integers.
- Total auxiliary space complexity is $O(n \cdot M)$, requiring approximately $20000 \times 4$ bytes $\approx 80$ KB of memory.
