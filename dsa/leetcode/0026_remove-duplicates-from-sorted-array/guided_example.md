# Guided Example: Remove Duplicates from Sorted Array

We trace the step-by-step two-pointer fast-reader / slow-writer compaction on a representative sorted array instance:

- **Input:** $\text{nums} = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]$
- **Required output:** $k = 5$ with prefix $[0, 1, 2, 3, 4]$

This instance demonstrates in-place contiguous run deduplication, slow write-pointer advancement, discarding duplicate elements without shifting remaining elements with expensive $O(N)$ array deletions, and preserving sorted order in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 10$ sorted in non-decreasing order:
$$
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
$$

We must remove duplicates in place such that each unique element appears exactly once in the prefix $\text{nums}[0 \dots k-1]$. The relative order must be preserved, and the function must return the count of unique elements $k = 5$.

A naive approach calls `nums.pop(i)` or `del nums[i]` whenever a duplicate is found. Each deletion shifts all subsequent elements left, leading to $O(N^2)$ time. The optimal approach uses two pointers (a slow write pointer $k$ and a fast read pointer $i$), overwriting duplicates in a single forward pass in $O(N)$ time and $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Dual-Pointer Roles
Because $\text{nums}$ is sorted, all occurrences of any value appear consecutively.
- **Fast Reader $i$:** Scans elements from index $1$ to $N - 1$.
- **Slow Writer $k$:** Points to the next index where a newly discovered unique element should be placed.

### Transition Rule
The first element $\text{nums}[0]$ is always unique, so we start with $k = 1$.
For each reader index $i \in [1, N-1]$:
- If $\text{nums}[i] \ne \text{nums}[k-1]$, element $\text{nums}[i]$ is a new distinct value.
  - Write $\text{nums}[k] \leftarrow \text{nums}[i]$.
  - Increment $k \leftarrow k + 1$.
- If $\text{nums}[i] == \text{nums}[k-1]$, element $\text{nums}[i]$ is a duplicate of the last written element. Skip it.

> **Invariant.** At step $i$, the prefix $\text{nums}[0 \dots k-1]$ contains the deduplicated sequence of all unique values observed in $\text{nums}[0 \dots i-1]$ in strictly increasing order.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]$:

### Initialization ($k = 1$)
- $\text{nums}[0] = 0$ is confirmed unique.
- Active unique prefix: $[0]$. Write cursor $k = 1$.

---

### Reader Steps ($i = 1$ to $9$)

- **Index 1 ($i = 1$):**
  - Read value: $\text{nums}[1] = 0$.
  - Compare with $\text{nums}[k-1] = \text{nums}[0] = 0$.
  - Identical: Duplicate detected. Skip. $k$ remains $1$.

- **Index 2 ($i = 2$):**
  - Read value: $\text{nums}[2] = 1$.
  - Compare with $\text{nums}[k-1] = 0$.
  - Different ($1 \ne 0$): New unique value!
  - Write $\text{nums}[1] \leftarrow 1$. Increment $k \to 2$.
  - Active prefix: $[0, 1]$.

- **Index 3 & 4 ($i = 3, 4$):**
  - Read values: $\text{nums}[3] = 1, \text{nums}[4] = 1$.
  - Compare with $\text{nums}[k-1] = 1$.
  - Identical: Duplicates skipped. $k$ remains $2$.

- **Index 5 ($i = 5$):**
  - Read value: $\text{nums}[5] = 2$.
  - Compare with $\text{nums}[k-1] = 1$.
  - Different ($2 \ne 1$): New unique value!
  - Write $\text{nums}[2] \leftarrow 2$. Increment $k \to 3$.
  - Active prefix: $[0, 1, 2]$.

- **Index 6 ($i = 6$):**
  - Read value: $\text{nums}[6] = 2$.
  - Compare with $\text{nums}[k-1] = 2$.
  - Duplicate skipped. $k$ remains $3$.

- **Index 7 ($i = 7$):**
  - Read value: $\text{nums}[7] = 3$.
  - Compare with $\text{nums}[k-1] = 2$.
  - Different ($3 \ne 2$): New unique value!
  - Write $\text{nums}[3] \leftarrow 3$. Increment $k \to 4$.
  - Active prefix: $[0, 1, 2, 3]$.

- **Index 8 ($i = 8$):**
  - Read value: $\text{nums}[8] = 3$.
  - Duplicate skipped. $k$ remains $4$.

- **Index 9 ($i = 9$):**
  - Read value: $\text{nums}[9] = 4$.
  - Compare with $\text{nums}[k-1] = 3$.
  - Different ($4 \ne 3$): New unique value!
  - Write $\text{nums}[4] \leftarrow 4$. Increment $k \to 5$.
  - Active prefix: $[0, 1, 2, 3, 4]$.

### Termination
Reader reaches end of array. The final unique count is $k = 5$. Prefix is $[0, 1, 2, 3, 4]$.

---

## 4. Complete Execution Trace

| Fast Reader $i$ | Scanned Value $\text{nums}[i]$ | Last Written $\text{nums}[k-1]$ | Condition ($\ne$) | Action Taken | Write Pointer $k$ | Modified Prefix $\text{nums}[0 \dots k-1]$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| Initial | - | - | - | Initialized with first element | 1 | $[0]$ |
| 1 | 0 | 0 | False | Duplicate; skip | 1 | $[0]$ |
| 2 | 1 | 0 | **True** | Write $\text{nums}[1] \leftarrow 1$ | 2 | $[0, 1]$ |
| 3 | 1 | 1 | False | Duplicate; skip | 2 | $[0, 1]$ |
| 4 | 1 | 1 | False | Duplicate; skip | 2 | $[0, 1]$ |
| 5 | 2 | 1 | **True** | Write $\text{nums}[2] \leftarrow 2$ | 3 | $[0, 1, 2]$ |
| 6 | 2 | 2 | False | Duplicate; skip | 3 | $[0, 1, 2]$ |
| 7 | 3 | 2 | **True** | Write $\text{nums}[3] \leftarrow 3$ | 4 | $[0, 1, 2, 3]$ |
| 8 | 3 | 3 | False | Duplicate; skip | 4 | $[0, 1, 2, 3]$ |
| 9 | 4 | 3 | **True** | Write $\text{nums}[4] \leftarrow 4$ | **5** | $[0, 1, 2, 3, 4]$ |

---

## 5. Algorithmic Correctness

**Soundness.** Because the input array is sorted, any value occurring more than once must be adjacent. A value $\text{nums}[i]$ is unique relative to the prefix if and only if it differs from the most recently accepted element $\text{nums}[k-1]$. Overwriting $\text{nums}[k]$ preserves strict order without modifying already confirmed elements.

**Completeness.** The fast pointer $i$ iterates through every single element in $\text{nums}$. Whenever a new unique value is encountered, it is copied to index $k$ and $k$ is incremented. No unique values can be skipped.

---

## 6. Traps This Instance Exposes

- **Array Modification While Iterating:** Mutating array size (via `del` or `pop`) during iteration shifts indices, causing elements to be skipped or resulting in $O(N^2)$ quadratic slowdown. The two-pointer read-write technique modifies contents in place without resizing.
- **Empty Array Boundary:** If the array is empty ($N = 0$), $k = 0$ must be returned immediately to prevent indexing $\text{nums}[0]$.
- **Elements Beyond $k$:** The judge only inspects elements from index $0$ to $k - 1$. Leaving stale values in indices $\ge k$ is completely valid and expected.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in $\text{nums}$. The fast pointer traverses the array from index $1$ to $N - 1$ in a single pass, performing $O(1)$ comparisons and assignments per element.
- **Auxiliary Space Complexity:** $O(1)$. All modifications occur in place within the existing array buffer, requiring only two integer indices ($i$ and $k$).
