# Guided Example: Maximum Size Subarray Sum Equals k

We trace the step-by-step prefix sum calculation, hash map earliest-occurrence caching (`d[s]`), zero-index sentinel initialization (`d = {0: -1}`), algebraic complement lookup ($s - k$), and maximum subarray length maximization on representative integer array instances:

- **Input:** $\text{nums} = [1, -1, 5, -2, 3], \quad k = 3$
- **Required output:** $4$
  - Running prefix sums: $[1, 0, 5, 3, 6]$
  - At index $3$ ($x = -2$), running sum $s = 3$
  - Target complement: $s - k = 3 - 3 = 0$
  - Earliest occurrence of prefix sum $0$: index $-1$ (empty prefix)
  - Subarray length: $3 - (-1) = \mathbf{4}$ (Subarray $\text{nums}[0 \dots 3] = [1, -1, 5, -2]$, sum $= 3$)
  - At index $4$ ($x = 3$), running sum $s = 6$, $s - k = 3$, length $4 - 3 = 1 \le 4$
  - Global maximum length: $4$
- **Negative Numbers Present:** Sliding window fails because sums are non-monotonic; prefix hash map correctly handles negatives
- **No Matching Subarray:** $\text{nums} = [1, 2, 3], k = 7 \implies 0$
- **Single Element Match:** $\text{nums} = [5], k = 5 \implies 1$

This instance demonstrates prefix sum complement lookups with negative integers, mathematically proves why recording only the *earliest* occurrence of each prefix sum maximizes subarray length, explains the `{0: -1}` sentinel, and operates in $O(N)$ linear time and $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given array $\text{nums} = [1, -1, 5, -2, 3]$ ($N = 5$) and target $k = 3$:
Find the maximum length of a contiguous subarray whose elements sum to $k$:
$$
\sum_{j=a}^b \text{nums}[j] = k
$$

```text
Indices:     0    1    2    3    4
nums:        1   -1    5   -2    3
Prefix sum:  1    0    5    3    6

Subarrays summing to k = 3:
- nums[0..3]: [1, -1, 5, -2] -> sum = 3, length = 4 (MAXIMUM!)
- nums[2..3]: [5, -2]        -> sum = 3, length = 2
- nums[4..4]: [3]            -> sum = 3, length = 1

Optimal Length: 4
```

### Why Sliding Window Fails
A two-pointer sliding window assumes that expanding the right pointer increases the sum and shrinking the left pointer decreases the sum.
Because $\text{nums}$ contains negative numbers (like $-1$ and $-2$), the prefix sum is **not monotonic**:
- Adding an element can decrease the total.
- Removing an element can increase the total.
The only linear-time method that works with arbitrary signed integers is **Prefix Sum + Hash Map**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Prefix Sum Equation
Let $P[i] = \sum_{j=0}^i \text{nums}[j]$ be the prefix sum ending at index $i$.
The sum of subarray $\text{nums}[a \dots i]$ is:
$$
\text{Sum}(a \dots i) = P[i] - P[a - 1] = k \iff P[a - 1] = P[i] - k
$$
At each index $i$, we know $P[i]$ and $k$. We check if the required preceding prefix sum $P[i] - k$ has already occurred!

### 2. Earliest Index Invariant for Maximum Length
The length of subarray $\text{nums}[a \dots i]$ is $i - (a - 1)$.
To **maximize** length for a fixed ending index $i$, we must **minimize** $a - 1$.
Therefore:
- In hash map $d$, store the **earliest** index where each prefix sum was seen:
  $$
  \text{if } s \notin d: \quad d[s] = i
  $$
- Never overwrite an existing key in $d$!

### 3. The Sentinel `{0: -1}`
If a subarray summing to $k$ starts at index $0$, then $P[i] - k = 0$.
The required preceding prefix sum is $0$.
Pre-populating $d[0] = -1$ represents the virtual empty prefix before index $0$:
$$
\text{Length} = i - (-1) = i + 1
$$
This unifies all lookups without special branching.

> **Invariant.** For every key $s$ in $d$, $d[s]$ stores the minimum index with prefix sum $s$. If $s - k \in d$, $i - d[s - k]$ is the maximum valid subarray length ending at $i$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, -1, 5, -2, 3]$ with $k = 3$:
Initialized: `d = {0: -1}, ans = 0, s = 0`.

---

### Step 1: Index $0$, $x = 1$
- Running sum: $s = 0 + 1 = 1$.
- Complement needed: $s - k = 1 - 3 = -2$.
- Is $-2 \in d$? No.
- Record sum: $1 \notin d \implies d[1] = 0$.
- State: $d = \{0: -1, \; 1: 0\}$, $ans = 0$.

---

### Step 2: Index $1$, $x = -1$
- Running sum: $s = 1 + (-1) = 0$.
- Complement needed: $s - k = 0 - 3 = -3$.
- Is $-3 \in d$? No.
- Record sum: $0 \in d$ already ($d[0] = -1$).
  - **Do not overwrite!** Keeping $-1$ preserves earlier starting positions.
- State: $d = \{0: -1, \; 1: 0\}$, $ans = 0$.

---

### Step 3: Index $2$, $x = 5$
- Running sum: $s = 0 + 5 = 5$.
- Complement needed: $s - k = 5 - 3 = 2$.
- Is $2 \in d$? No.
- Record sum: $5 \notin d \implies d[5] = 2$.
- State: $d = \{0: -1, \; 1: 0, \; 5: 2\}$, $ans = 0$.

---

### Step 4: Index $3$, $x = -2$
- Running sum: $s = 5 + (-2) = 3$.
- Complement needed: $s - k = 3 - 3 = \mathbf{0}$.
- Is $0 \in d$? **Yes!** $d[0] = -1$.
  - Subarray starts after index $-1$ (i.e. at index 0): $\text{nums}[0 \dots 3]$.
  - Length: $i - d[0] = 3 - (-1) = \mathbf{4}$.
  - Update: $ans = \max(0, 4) = \mathbf{4}$.
- Record sum: $3 \notin d \implies d[3] = 3$.
- State: $d = \{0: -1, \; 1: 0, \; 5: 2, \; 3: 3\}$, $ans = 4$.

---

### Step 5: Index $4$, $x = 3$
- Running sum: $s = 3 + 3 = 6$.
- Complement needed: $s - k = 6 - 3 = \mathbf{3}$.
- Is $3 \in d$? **Yes!** $d[3] = 3$.
  - Subarray starts after index $3$ (index 4): $\text{nums}[4 \dots 4] = [3]$.
  - Length: $i - d[3] = 4 - 3 = 1$.
  - Update: $ans = \max(4, 1) = 4$.
- Record sum: $6 \notin d \implies d[6] = 4$.

---

### Final Maximum Length
$$
ans = \mathbf{4}
$$

---

## 4. Complete Execution Trace

```text
nums = [1, -1, 5, -2, 3], k = 3
d = {0: -1}

i=0, x= 1: s=1, s-k=-2 (not in d), d[1]=0
i=1, x=-1: s=0, s-k=-3 (not in d), 0 already in d (kept -1)
i=2, x= 5: s=5, s-k= 2 (not in d), d[5]=2
i=3, x=-2: s=3, s-k= 0 (FOUND at -1) -> len = 3 - (-1) = 4 -> ans = 4, d[3]=3
i=4, x= 3: s=6, s-k= 3 (FOUND at  3) -> len = 4 - 3 = 1    -> ans = 4, d[6]=4

Maximum Length: 4
```

| Index $i$ | Element $x$ | Prefix Sum $s$ | Needed Complement $s - k$ | Found in $d$? | Earliest Index | Subarray Length | Current Max `ans` | Dictionary $d$ After Step |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 1 | 1 | -2 | No | - | - | 0 | `{0: -1, 1: 0}` |
| 1 | -1 | 0 | -3 | No | - | - | 0 | `{0: -1, 1: 0}` |
| 2 | 5 | 5 | 2 | No | - | - | 0 | `{0: -1, 1: 0, 5: 2}` |
| **3** | **-2** | **3** | **0** | **Yes** | **-1** | **$3 - (-1) = 4$** | **4** | `{0: -1, 1: 0, 5: 2, 3: 3}` |
| 4 | 3 | 6 | 3 | Yes | 3 | $4 - 3 = 1$ | 4 | `{..., 6: 4}` |

---

## 5. Algorithmic Correctness

**Soundness.** A subarray from $a$ to $i$ sums to $k$ if and only if $P[i] - P[a-1] = k$, which is algebraically identical to $P[a-1] = P[i] - k$. If $s - k$ exists in $d$ at index $p$, the elements from $p + 1$ to $i$ have sum $s - (s - k) = k$, confirming that the identified contiguous range is a valid candidate.

**Completeness.** Every possible subarray end index $i \in [0, N-1]$ is inspected. Because $d$ preserves the smallest index where each prefix sum first appeared, the longest possible subarray ending at $i$ is evaluated. Taking the maximum across all $i$ guarantees finding the global maximum size.

---

## 6. Traps This Instance Exposes

- **Overwriting Earliest Occurrence:** Updating $d[s] = i$ when $s$ is already in $d$ shortens all future candidate subarrays that could use prefix $s$. The check `if s not in d` is critical.
- **Missing the `{0: -1}` Sentinel:** Without mapping $0$ to $-1$, any valid subarray starting at index $0$ cannot find a matching complement and is omitted unless complex special-case logic is added.
- **Signed Arithmetic:** In arrays with negative numbers, prefix sums can fluctuate arbitrarily. Only a hash map accurately records arbitrary integer keys in $O(1)$ expected time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. We perform a single linear pass over the array, with each hash table lookup and insertion executing in $O(1)$ expected time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store at most $N + 1$ distinct prefix sums in hash map $d$.
