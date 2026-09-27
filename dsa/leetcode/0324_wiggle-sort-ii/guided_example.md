# Guided Example: Wiggle Sort II

We trace the step-by-step array partition into lower and upper halves, reverse order interleaving ($L_{\text{descending}}$ at even indices, $U_{\text{descending}}$ at odd indices), duplicate median separation, and in-place strict wiggle sequence construction on representative array instances:

- **Input:** $\text{nums} = [1, 5, 1, 1, 6, 4]$
- **Required output:** $[1, 6, 1, 5, 1, 4]$
  - Sorted array: $[1, 1, 1, 4, 5, 6]$
  - Lower half: $[1, 1, 1]$ (indices $0..2$)
  - Upper half: $[4, 5, 6]$ (indices $3..5$)
  - Reverse interleaving:
    - Even indices: $[1, 1, 1]$ (from right of lower half)
    - Odd indices: $[6, 5, 4]$ (from right of upper half)
    - Combined: $[1, 6, 1, 5, 1, 4]$
  - Satisfies: $1 < 6 > 1 < 5 > 1 < 4$ strictly
- **Odd Length Array:** $\text{nums} = [1, 3, 2, 2, 3, 1] \implies [2, 3, 1, 3, 1, 2]$
- **Identical Numbers at Boundary:** Duplicate median elements are kept strictly separated by reverse indexing
- **Minimal Two Element Array:** $[1, 2] \implies [1, 2]$ ($1 < 2$)

This instance demonstrates median-split interleaving, mathematically proves why reading both halves in descending order prevents duplicate median values from landing in adjacent positions, contrasts forward vs reverse interleaving, and analyzes time ($O(N \log N)$) and space ($O(N)$) bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 5, 1, 1, 6, 4]$ ($N = 6$):
Reorder $\text{nums}$ in-place such that:
$$
\text{nums}[0] < \text{nums}[1] > \text{nums}[2] < \text{nums}[3] > \text{nums}[4] < \text{nums}[5]
$$
Note that **strict** inequalities are required ($<$ and $>$, not $\le$ or $\ge$).

```text
Input: [1, 5, 1, 1, 6, 4]
Sorted: [1, 1, 1, 4, 5, 6]

Lower Half (valleys): [1, 1, 1]
Upper Half (peaks):   [4, 5, 6]

Even positions (0, 2, 4): filled from lower half in reverse -> 1, 1, 1
Odd positions  (1, 3, 5): filled from upper half in reverse -> 6, 5, 4

Wiggled Result:
Index:   0    1    2    3    4    5
Value:   1 <  6  > 1 <  5  > 1 <  4

Strict Wiggle Validated!
```

### The Median Collision Trap
Why can't we interleave the sorted halves forward (left-to-right)?
Consider $\text{nums} = [1, 2, 2, 3]$.
- Lower half: $[1, 2]$, Upper half: $[2, 3]$.
- Forward interleaving:
  - $\text{nums}[0] = 1$
  - $\text{nums}[1] = 2$
  - $\text{nums}[2] = 2$
  - $\text{nums}[3] = 3$
  $\implies [1, 2, 2, 3]$, which fails at $\text{nums}[1] > \text{nums}[2]$ because $2 \ngtr 2$!
- **The Reverse Interleaving Solution:**
  Reading both halves **backward** places the largest lower-half element at index $0$ and the largest upper-half element at index $1$. The duplicate medians are pushed to opposite ends of the resulting array, preventing collisions!

---

## 2. Conceptual Foundation & Invariants

### Array Partition Bounds
Let $arr = \text{sorted}(nums)$ of length $n$:
- Lower half end pointer: $i = (n - 1) \gg 1$.
  - Covers indices $[0, i]$.
  - For $n = 6$: $i = (6 - 1) // 2 = 2$. Lower half: $arr[0..2]$ (length 3).
  - For odd $n = 2q + 1$: $i = q$. Lower half has $q + 1$ elements (matching $q + 1$ even indices).
- Upper half end pointer: $j = n - 1$.
  - Covers indices $[i + 1, n - 1]$.
  - For $n = 6$: $j = 5$. Upper half: $arr[3..5]$ (length 3).

### Placement Loop:
Iterate destination index $k$ from $0$ to $n - 1$:
- If $k$ is even ($k \pmod 2 == 0$):
  $$
  \text{nums}[k] = arr[i], \quad i \leftarrow i - 1
  $$
- If $k$ is odd ($k \pmod 2 == 1$):
  $$
  \text{nums}[k] = arr[j], \quad j \leftarrow j - 1
  $$

> **Invariant.** For every even index $2m$ and adjacent odd index $2m+1$, $\text{nums}[2m] < \text{nums}[2m+1]$ and $\text{nums}[2m+1] > \text{nums}[2m+2]$, because the descending traversal ensures elements drawn from the upper half are strictly greater than elements drawn from the lower half at corresponding offsets.

---

## 3. Step-by-Step Worked Execution

We trace the placement on $\text{nums} = [1, 5, 1, 1, 6, 4]$ ($n = 6$):
Sorted copy: $arr = [1, 1, 1, 4, 5, 6]$.
Pointers:
- $i = (6 - 1) \gg 1 = 2$ (points to $arr[2] = 1$).
- $j = 6 - 1 = 5$ (points to $arr[5] = 6$).

---

### Step 1: $k = 0$ (Even Index — Valley)
- $k \pmod 2 == 0 \implies$ take from lower pointer $i = 2$:
  $$
  \text{nums}[0] = arr[2] = \mathbf{1}
  $$
- Decrement pointer: $i \leftarrow 2 - 1 = 1$.

---

### Step 2: $k = 1$ (Odd Index — Peak)
- $k \pmod 2 == 1 \implies$ take from upper pointer $j = 5$:
  $$
  \text{nums}[1] = arr[5] = \mathbf{6}
  $$
- Decrement pointer: $j \leftarrow 5 - 1 = 4$.
- Subsequence: $[1, 6]$ ($1 < 6$ holds).

---

### Step 3: $k = 2$ (Even Index — Valley)
- $k \pmod 2 == 0 \implies$ take from lower pointer $i = 1$:
  $$
  \text{nums}[2] = arr[1] = \mathbf{1}
  $$
- Decrement pointer: $i \leftarrow 1 - 1 = 0$.
- Subsequence: $[1, 6, 1]$ ($6 > 1$ holds).

---

### Step 4: $k = 3$ (Odd Index — Peak)
- $k \pmod 2 == 1 \implies$ take from upper pointer $j = 4$:
  $$
  \text{nums}[3] = arr[4] = \mathbf{5}
  $$
- Decrement pointer: $j \leftarrow 4 - 1 = 3$.
- Subsequence: $[1, 6, 1, 5]$ ($1 < 5$ holds).

---

### Step 5: $k = 4$ (Even Index — Valley)
- $k \pmod 2 == 0 \implies$ take from lower pointer $i = 0$:
  $$
  \text{nums}[4] = arr[0] = \mathbf{1}
  $$
- Decrement pointer: $i \leftarrow 0 - 1 = -1$.
- Subsequence: $[1, 6, 1, 5, 1]$ ($5 > 1$ holds).

---

### Step 6: $k = 5$ (Odd Index — Peak)
- $k \pmod 2 == 1 \implies$ take from upper pointer $j = 3$:
  $$
  \text{nums}[5] = arr[3] = \mathbf{4}
  $$
- Decrement pointer: $j \leftarrow 3 - 1 = 2$.
- Final sequence:
  $$
  \mathbf{[1, 6, 1, 5, 1, 4]}
  $$

---

## 4. Complete Execution Trace

```text
nums = [1, 5, 1, 1, 6, 4]
arr  = [1, 1, 1, 4, 5, 6]
i = 2, j = 5

k=0 (even): nums[0] = arr[2] = 1, i becomes 1
k=1 (odd):  nums[1] = arr[5] = 6, j becomes 4
k=2 (even): nums[2] = arr[1] = 1, i becomes 0
k=3 (odd):  nums[3] = arr[4] = 5, j becomes 3
k=4 (even): nums[4] = arr[0] = 1, i becomes -1
k=5 (odd):  nums[5] = arr[3] = 4, j becomes 2

Result: [1, 6, 1, 5, 1, 4]
Validation: 1 < 6 > 1 < 5 > 1 < 4
```

| Step $k$ | Parity | Source Pointer Used | Pointer Index | Value Written $\text{nums}[k]$ | Pointer Updated | Current Sequence | Verification |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | Even | Lower ($i$) | 2 | **1** | $i = 1$ | `[1]` | Baseline |
| 1 | Odd | Upper ($j$) | 5 | **6** | $j = 4$ | `[1, 6]` | $1 < 6$ |
| 2 | Even | Lower ($i$) | 1 | **1** | $i = 0$ | `[1, 6, 1]` | $6 > 1$ |
| 3 | Odd | Upper ($j$) | 4 | **5** | $j = 3$ | `[1, 6, 1, 5]` | $1 < 5$ |
| 4 | Even | Lower ($i$) | 0 | **1** | $i = -1$ | `[1, 6, 1, 5, 1]` | $5 > 1$ |
| 5 | Odd | Upper ($j$) | 3 | **4** | $j = 2$ | `[1, 6, 1, 5, 1, 4]` | $1 < 4$ |

---

## 5. Algorithmic Correctness

**Soundness.** The array is divided into a lower half ($arr[0 \dots i]$) and upper half ($arr[i+1 \dots n-1]$). Even indices are populated from the lower half, and odd indices from the upper half. Because the problem guarantees a valid wiggle sort exists, the maximum frequency of any element cannot exceed $\lceil n / 2 \rceil$. Reversing both halves ensures that median elements in the lower half (placed at $k = 0, 2, \dots$) and median elements in the upper half (placed at the trailing odd indices) are maximally spaced, guaranteeing strict inequality between all adjacent elements.

**Completeness.** Every element from $arr$ is written to exactly one position in $\text{nums}$. The loop runs for all $n$ indices, completely overwriting $\text{nums}$ in-place without losing or creating values.

---

## 6. Traps This Instance Exposes

- **Overwriting In-Place Without a Copy:** Modifying $\text{nums}$ directly while reading from it corrupts future values before they are placed. Sorting into a separate buffer `arr` is necessary.
- **Forward Interleaving Failure:** Forward interleaving ($arr[0]$ to even, $arr[half]$ to odd) fails whenever elements equal to the median occur more than once, because $arr[half-1]$ and $arr[half]$ can be identical and placed adjacently. Reversing both streams prevents this.
- **Odd Length Arrays:** When $n$ is odd, the lower half must have $\frac{n+1}{2}$ elements and the upper half $\frac{n-1}{2}$ elements. Using $(n - 1) \gg 1$ correctly assigns the extra element to the valleys.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of elements in `nums`.
  - Sorting `nums` takes $O(N \log N)$ time.
  - The placement loop makes a single pass of $N$ steps, copying elements in $O(N)$ time.
  - Total runtime is $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the sorted copy `arr`.
