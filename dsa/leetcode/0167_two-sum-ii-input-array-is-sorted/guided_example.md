# Guided Example: Two Sum II - Input Array Is Sorted

We trace the step-by-step inward two-pointer convergence and monotonic sum pruning on representative sorted integer arrays:

- **Input:** $\text{numbers} = [2, 7, 11, 15], \quad \text{target} = 9$
- **Required output:** `[1, 2]` (1-indexed positions of $2$ and $7$, since $2 + 7 = 9$)
- **Span Pruning Instance:** $\text{numbers} = [2, 3, 4], \quad \text{target} = 6 \implies [1, 3]$ ($2 + 4 = 6$)
- **Negative Integer Instance:** $\text{numbers} = [-1, 0], \quad \text{target} = -1 \implies [1, 2]$

This instance demonstrates two-pointer boundary pruning on non-decreasing arrays, proves why $\text{sum} < \text{target}$ strictly disqualifies the left element and $\text{sum} > \text{target}$ strictly disqualifies the right element, converts 0-indexed pointers to 1-indexed answers, and achieves optimal $O(N)$ time with strictly $O(1)$ auxiliary memory.

---

## 1. Instance & Teaching Goal

Given a 1-indexed array of integers $\text{numbers} = [2, 7, 11, 15]$ sorted in non-decreasing order and a target sum $9$:
Find two distinct indices $1 \le \text{index}_1 < \text{index}_2 \le |\text{numbers}|$ such that $\text{numbers}[\text{index}_1] + \text{numbers}[\text{index}_2] == \text{target}$.

In this instance:
- At 0-indexed positions 0 and 1: $\text{numbers}[0] + \text{numbers}[1] = 2 + 7 = 9$.
- Converting to 1-indexed format: $[0 + 1, 1 + 1] = [1, 2]$.

In LeetCode 1 (unsorted array), a hash table finds complements in $O(N)$ time but requires $O(N)$ auxiliary heap memory.
Here, because the array is **already sorted**:
- Placing pointers at the extreme ends ($L = 0, R = N - 1$) allows us to evaluate the current sum.
- If the sum is too small, no element can pair with $\text{numbers}[L]$ to reach the target, so $L$ advances.
- If the sum is too large, no element can pair with $\text{numbers}[R]$ to reach the target, so $R$ decrements.
This eliminates candidate pairs in $O(1)$ operations per step, yielding strictly $O(N)$ time and $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### The Monotonic Inward Pruning Theorem
Initialize $L = 0$ and $R = N - 1$.
At each iteration, compute $\text{curr\_sum} = \text{numbers}[L] + \text{numbers}[R]$.

1. **Exact Match ($\text{curr\_sum} == \text{target}$):**
   The unique solution is found. Return $[L + 1, R + 1]$.
2. **Sum Too Small ($\text{curr\_sum} < \text{target}$):**
   Because the array is sorted, $\text{numbers}[R]$ is the maximum available element in the active range $[L, R]$.
   For any $k \le R$:
   $$
   \text{numbers}[L] + \text{numbers}[k] \le \text{numbers}[L] + \text{numbers}[R] = \text{curr\_sum} < \text{target}
   $$
   Therefore, $\text{numbers}[L]$ cannot pair with **any** remaining element to reach $\text{target}$. Discarding index $L$ is mathematically sound:
   $$
   L \leftarrow L + 1
   $$
3. **Sum Too Large ($\text{curr\_sum} > \text{target}$):**
   Because the array is sorted, $\text{numbers}[L]$ is the minimum available element in the active range $[L, R]$.
   For any $k \ge L$:
   $$
   \text{numbers}[k] + \text{numbers}[R] \ge \text{numbers}[L] + \text{numbers}[R] = \text{curr\_sum} > \text{target}
   $$
   Therefore, $\text{numbers}[R]$ cannot pair with **any** remaining element to reach $\text{target}$. Discarding index $R$ is mathematically sound:
   $$
   R \leftarrow R - 1
   $$

> **Invariant.** The unique solution pair $(\text{index}_1, \text{index}_2)$ is always contained within the remaining index range $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We trace the two pointers on $\text{numbers} = [2, 7, 11, 15]$ with $\text{target} = 9$:

### Initialization
- $L = 0, \quad R = 3$.
- $\text{numbers}[L] = 2, \quad \text{numbers}[R] = 15$.

---

### Step 1: Active Interval $[0, 3]$
- Evaluate sum:
  $$
  \text{curr\_sum} = 2 + 15 = 17
  $$
- Compare against target:
  $$
  17 > 9 \quad (\text{Sum Too Large})
  $$
- Since $17 > 9$, 15 cannot pair with any valid element (even the smallest element 2 produces a sum $> 9$).
- Discard right boundary:
  $$
  R \leftarrow R - 1 = 3 - 1 = \mathbf{2}
  $$
- New interval: $[0, 2]$.

---

### Step 2: Active Interval $[0, 2]$
- Evaluate sum:
  $$
  \text{numbers}[0] + \text{numbers}[2] = 2 + 11 = 13
  $$
- Compare against target:
  $$
  13 > 9 \quad (\text{Sum Too Large})
  $$
- 11 is too large to pair with any remaining candidate.
- Discard right boundary:
  $$
  R \leftarrow R - 1 = 2 - 1 = \mathbf{1}
  $$
- New interval: $[0, 1]$.

---

### Step 3: Active Interval $[0, 1]$
- Evaluate sum:
  $$
  \text{numbers}[0] + \text{numbers}[1] = 2 + 7 = \mathbf{9}
  $$
- Compare against target:
  $$
  9 == 9 \quad (\text{Target Match Found!})
  $$
- Convert to 1-indexed:
  $$
  [L + 1, \, R + 1] = [0 + 1, \, 1 + 1] = \mathbf{[1, 2]}
  $$

Return `[1, 2]`.

---

## 4. Complete Execution Trace

```text
Array:        [ 2,    7,   11,   15 ], target = 9
Indices:        0     1     2     3

Step 1:        [L                 R]   2 + 15 = 17 > 9 -> R moves left (R=2)
Step 2:        [L           R]         2 + 11 = 13 > 9 -> R moves left (R=1)
Step 3:        [L     R]               2 +  7 =  9 == 9 -> MATCH!

1-Indexed Result: [0+1, 1+1] = [1, 2]
```

| Step | Left Index $L$ | Right Index $R$ | Value $\text{numbers}[L]$ | Value $\text{numbers}[R]$ | $\text{curr\_sum}$ | Comparison with Target (9) | Decision Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 3 | 2 | 15 | 17 | $17 > 9$ | $R \leftarrow R - 1$ |
| 2 | 0 | 2 | 2 | 11 | 13 | $13 > 9$ | $R \leftarrow R - 1$ |
| **3** | **0** | **1** | **2** | **7** | **9** | **$9 == 9$** | **Return $[L+1, R+1] = [1, 2]$** |

### Every Pair the Two Steps Eliminate

With $N = 4$ there are only $\binom{4}{2} = 6$ unordered pairs. Listing all of them shows exactly why one pointer move can retire a whole family of candidates at once:

| Pair (1-indexed) | Values | Sum | Compared with target $9$ | Status after the step |
|:---:|:---:|:---:|:---|:---|
| $(1, 4)$ | $2 + 15$ | 17 | Too large | Eliminated at Step 1 by moving $R$ from index $4$ to index $3$ |
| $(2, 4)$ | $7 + 15$ | 22 | Too large | Eliminated by the same move: every pair containing $15$ exceeds the target |
| $(3, 4)$ | $11 + 15$ | 26 | Too large | Eliminated by the same move, since $11$ only pushes the sum higher |
| $(1, 3)$ | $2 + 11$ | 13 | Too large | Eliminated at Step 2 by moving $R$ from index $3$ to index $2$ |
| $(2, 3)$ | $7 + 11$ | 18 | Too large | Eliminated by the same move |
| $(1, 2)$ | $2 + 7$ | **9** | **Exact match** | **Survives as the answer $[1, 2]$** |

The two pointer moves retire $3 + 2 = 5$ candidate pairs without ever evaluating them individually, and the surviving pair is the one the invariant promised could not be pruned.

### Boundary Scenarios This Instance Sits Next To

| Scenario | Input condition | Expected | What the pointer walk does | Trap if handled naively |
|:---|:---|:---:|:---|:---|
| Array shorter than two elements | a single element, e.g. $[2]$ with target $9$ | No pair exists | The walk never runs, because $L = 0$ already equals $R$ and the loop requires $L < R$ | A naive inner loop can index past the end of the array instead of recognising that no valid pair can exist |
| Pair uses both extremes | $[2, 3, 4]$ with target $6$ | $[1, 3]$ | Step 1 computes $2 + 4 = 6$ and returns immediately | Reporting $[2, 3]$ (the middle pair $3 + 3$) would reuse one element twice, which the distinct-index rule forbids |
| Negative values | $[-1, 0]$ with target $-1$ | $[1, 2]$ | $-1 + 0 = -1$ matches; target sign never enters the comparison | Assuming the target is positive, or clamping values to non-negative, breaks the very first comparison |
| Equal values at distinct positions | $[1, 2, 2, 3]$ with target $4$ | $[1, 4]$ | The extremes $1 + 3 = 4$ already match, so the walk stops before the duplicate middle pair is ever considered | Returning the two copies of $2$ is tempting but wrong: their 0-indexed positions are $1$ and $2$, and the guarantee names the unique pair |
| Both extremes must be discarded | $[-10, -4, 1, 4, 8, 20]$ with target $5$ | $[3, 4]$ | Too-large sums shrink $R$ twice down to index $3$, then a too-small sum advances $L$ twice up to index $2$, and $1 + 4 = 5$ matches | A walk that moves only one pointer, or that resets the interval each step, loses the $O(N)$ bound |
| Large range, all values distinct | e.g. $[1, 2, \dots, 10^{4}]$ with a fixed target inside the range | One pair near the middle | Each iteration removes exactly one index, so at most $N - 1$ iterations are ever needed | A nested scan over all pairs is $O(N^{2})$ and times out well before the pointer walk would finish |

---

## 5. Algorithmic Correctness

**Soundness.** Because the array is sorted, any element paired with $\text{numbers}[L]$ when $\text{sum} < \text{target}$ produces a sum $\le \text{sum} < \text{target}$. Similarly, any element paired with $\text{numbers}[R]$ when $\text{sum} > \text{target}$ produces a sum $\ge \text{sum} > \text{target}$. No valid solution element can ever be eliminated.

**Completeness.** In each step, the distance $R - L$ strictly decreases by 1. Since the problem guarantees that exactly one solution exists, the two pointers are guaranteed to intersect at the unique solution pair before $L \ge R$.

---

## 6. Traps This Instance Exposes

- **Zero-Indexed vs One-Indexed:** Returning `[0, 1]` results in a wrong answer. The problem explicitly specifies a 1-indexed output: `[L + 1, R + 1]`.
- **Using Hash Map (Space Violation):** While a hash table solves this in $O(N)$ time, it requires $O(N)$ auxiliary memory. The problem explicitly mandates constant $O(1)$ extra space.
- **Using Binary Search ($O(N \log N)$):** Searching for `target - nums[i]` with binary search for each element takes $O(N \log N)$ time, which is strictly inferior to two-pointer $O(N)$ time.

### Alternative Approaches on This Array

| Approach | Iterations on $[2, 7, 11, 15]$ with target $9$ | Time | Auxiliary space | Tradeoff for this contract |
|:---|:---|:---:|:---:|:---|
| Brute-force pair enumeration | Evaluates all $6$ pairs and finds $(1, 2)$ last | $O(N^{2})$ | $O(1)$ | Correct but quadratic; the sortedness that the problem hands you is thrown away |
| Hash map of complements | Inserts $2$, looks for $7$, and returns $[1, 2]$ on the second element | $O(N)$ | $O(N)$ | Matches the time bound but violates the explicit constant-space requirement, and ignores that the input is already sorted |
| Binary search for `target - numbers[i]` | Runs a search for $7$ after fixing $2$ and finds it at index $2$ | $O(N \log N)$ | $O(1)$ | Uses no extra memory but still pays a logarithmic factor per index |
| Two pointers moving inward | Rejects $15$, then $11$, then matches $2 + 7$ in three steps | $O(N)$ | $O(1)$ | Reaches both optimal bounds at once; the only cost is that it depends on the array being sorted |
| Two pointers on an unsorted array | Would prune the wrong element, because the extremes are no longer the range's minimum and maximum | Undefined bound | $O(1)$ | The pruning proof collapses: with $[15, 2, 11, 7]$ the first sum $15 + 7 = 22$ wrongly blames index $4$ |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `numbers`. Each step advances either $L$ forward or $R$ backward, running at most $N$ iterations.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant memory, requiring only two pointer indices $L$ and $R$.
