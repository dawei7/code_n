# Guided Example: Find All Lonely Numbers in the Array

We analyze and execute the frequency-map neighborhood isolation algorithm on a representative problem instance, demonstrating how hashing transforms adjacency and uniqueness validation into constant-time queries.

- **Input:** `nums = [10, 6, 5, 8]`
- **Output:** `[10, 8]`

This instance illustrates exact multiplicity verification, bilateral adjacency checking, mutual disqualification of neighbor pairs, and filter extraction.

---

## 1. Problem Overview & Representative Instance

Given an integer array `nums`, a number $x \in \text{nums}$ is defined as **lonely** if and only if:
1. **Uniqueness (Multiplicity Criterion):** $x$ appears exactly once in `nums`.
2. **Left Isolation (Adjacency Criterion):** The immediate predecessor $x - 1$ does not appear anywhere in `nums`.
3. **Right Isolation (Adjacency Criterion):** The immediate successor $x + 1$ does not appear anywhere in `nums`.

Any violation of these three conditions disqualifies $x$:
- If $x$ occurs two or more times, it is not lonely (even if $x - 1$ and $x + 1$ are absent).
- If either $x - 1$ or $x + 1$ exists in the array, $x$ is not lonely (even if $x$ is unique).

We are tasked with returning all lonely numbers from `nums` in any order.

In our representative instance:
- `nums = [10, 6, 5, 8]` of length $n = 4$.
- Values present: $\{10, 6, 5, 8\}$.
- Notice that $5$ and $6$ are adjacent integers ($6 - 5 = 1$), mutually disqualifying each other.
- $10$ and $8$ each appear once with no adjacent integers present.

The output must contain $10$ and $8$.

---

## 2. Mathematical & Algorithmic Principles

### Hash Table Multiplicity Representation

Let $\text{freq}: \mathbb{Z} \to \mathbb{N}_0$ denote the frequency count of each integer in `nums`:
$$\text{freq}[v] = \sum_{i=0}^{n-1} \mathbf{1}_{\{\text{nums}[i] = v\}}$$

Under this representation, the three loneliness conditions for value $x$ can be evaluated as:
1. $\text{freq}[x] = 1$
2. $\text{freq}[x - 1] = 0$
3. $\text{freq}[x + 1] = 0$

Conjoining these conditions yields the indicator predicate:
$$\text{IsLonely}(x) \iff \Big(\text{freq}[x] = 1\Big) \land \Big(\text{freq}[x - 1] = 0\Big) \land \Big(\text{freq}[x + 1] = 0\Big)$$

### Two-Pass Linear Algorithm

1. **Pass 1 (Frequency Population):** Iterate through `nums`, incrementing the frequency of each element in a hash map or direct-indexed array.
2. **Pass 2 (Loneliness Filter):** Iterate through each element $x \in \text{nums}$ (or each unique key in the hash table). Test the three constant-time lookup conditions. If all three hold, append $x$ to the lonely list.

### Mutual Disqualification Symmetry

The relation $|a - b| = 1$ is symmetric. If $a = b + 1$, then $b$ invalidates $a$ via the left neighbor check ($a - 1 = b$), and $a$ invalidates $b$ via the right neighbor check ($b + 1 = a$). Both members of any consecutive pair in the multiset are eliminated simultaneously.

| Parameter / Condition | Algebraic Predicate | Concrete Role in Instance |
|---|---|---|
| Frequency Count | $\text{freq}[x]$ | Verifies uniqueness ($\text{freq}[x] = 1$) |
| Left Neighbor Check | $\text{freq}[x - 1] = 0$ | Ensures no predecessor exists in `nums` |
| Right Neighbor Check | $\text{freq}[x + 1] = 0$ | Ensures no successor exists in `nums` |
| Mutual Disqualification | $|a - b| = 1 \implies \text{freq}[a] > 0 \land \text{freq}[b] > 0$ | Eliminates both $5$ and $6$ from contention |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the algorithm on `nums = [10, 6, 5, 8]`.

```
Input: [10, 6, 5, 8]
Frequency map after Pass 1:
{ 10: 1,  6: 1,  5: 1,  8: 1 }

Pass 2 evaluations:
10: count=1, 9 not in map, 11 not in map => Lonely!
 6: count=1, 5 in map (FAIL)             => Disqualified
 5: count=1, 6 in map (FAIL)             => Disqualified
 8: count=1, 7 not in map, 9 not in map  => Lonely!

Lonely set: [10, 8]
```

### Step 1: Pass 1 — Build Frequency Map
Iterate through `nums` and populate counts:
- Process `10`: $\text{freq}[10] = 1$.
- Process `6`: $\text{freq}[6] = 1$.
- Process `5`: $\text{freq}[5] = 1$.
- Process `8`: $\text{freq}[8] = 1$.

Resulting frequency table:
$$\text{freq} = \{5: 1, \, 6: 1, \, 8: 1, \, 10: 1\}$$

### Step 2: Pass 2 — Evaluate Elements

- **Evaluate $x = 10$:**
  - Multiplicity check: $\text{freq}[10] = 1$ (Pass).
  - Left neighbor check: Is $10 - 1 = 9$ in $\text{freq}$? $\text{freq}[9] = 0$ (Pass).
  - Right neighbor check: Is $10 + 1 = 11$ in $\text{freq}$? $\text{freq}[11] = 0$ (Pass).
  - Conclusion: $10$ meets all criteria. Add $10$ to lonely list.
  - Active result: $[10]$.

- **Evaluate $x = 6$:**
  - Multiplicity check: $\text{freq}[6] = 1$ (Pass).
  - Left neighbor check: Is $6 - 1 = 5$ in $\text{freq}$? $\text{freq}[5] = 1 \ne 0$ (Failed!).
  - Reason: Value $5$ exists in `nums`.
  - Conclusion: $6$ is disqualified.
  - Active result: $[10]$.

- **Evaluate $x = 5$:**
  - Multiplicity check: $\text{freq}[5] = 1$ (Pass).
  - Left neighbor check: Is $5 - 1 = 4$ in $\text{freq}$? $\text{freq}[4] = 0$ (Pass).
  - Right neighbor check: Is $5 + 1 = 6$ in $\text{freq}$? $\text{freq}[6] = 1 \ne 0$ (Failed!).
  - Reason: Value $6$ exists in `nums`.
  - Conclusion: $5$ is disqualified.
  - Active result: $[10]$.

- **Evaluate $x = 8$:**
  - Multiplicity check: $\text{freq}[8] = 1$ (Pass).
  - Left neighbor check: Is $8 - 1 = 7$ in $\text{freq}$? $\text{freq}[7] = 0$ (Pass).
  - Right neighbor check: Is $8 + 1 = 9$ in $\text{freq}$? $\text{freq}[9] = 0$ (Pass).
  - Conclusion: $8$ meets all criteria. Add $8$ to lonely list.
  - Active result: $[10, 8]$.

### Step 3: Emit Result
All entries checked. The lonely numbers are $[10, 8]$.

---

## 4. Comprehensive State Trace

The table below catalogs every unique candidate in `nums`, verifying all three conditions:

| Candidate $x$ | Frequency $\text{freq}[x]$ | Multiplicity Valid ($\text{freq}=1$)? | Predecessor $x - 1$ in Array? | Successor $x + 1$ in Array? | All Conditions Met? | Lonely Status |
|---|---|---|---|---|---|---|
| $10$ | $1$ | Yes ($1 = 1$) | No ($9 \notin \text{nums}$) | No ($11 \notin \text{nums}$) | Yes | **Lonely** |
| $6$ | $1$ | Yes ($1 = 1$) | **Yes** ($5 \in \text{nums}$) | No ($7 \notin \text{nums}$) | No | Disqualified |
| $5$ | $1$ | Yes ($1 = 1$) | No ($4 \notin \text{nums}$) | **Yes** ($6 \in \text{nums}$) | No | Disqualified |
| $8$ | $1$ | Yes ($1 = 1$) | No ($7 \notin \text{nums}$) | No ($9 \notin \text{nums}$) | Yes | **Lonely** |

### Duplicate Value Verification Example

Consider an instance with duplicates: `nums = [1, 3, 5, 3]`.
- $\text{freq} = \{1: 1, \, 3: 2, \, 5: 1\}$.
- For $x = 3$: $\text{freq}[3] = 2 \ne 1$. Disqualified immediately due to multiplicity.
- For $x = 1$: $\text{freq}[1] = 1$, $0 \notin \text{nums}$, $2 \notin \text{nums}$. Lonely!
- For $x = 5$: $\text{freq}[5] = 1$, $4 \notin \text{nums}$, $6 \notin \text{nums}$. Lonely!
- Result: $[1, 5]$.

---

## 5. Algorithmic Correctness & Soundness

### Soundness
Every number added to the result satisfies $\text{freq}[x] = 1$, meaning it appears exactly once in `nums`. Furthermore, $\text{freq}[x - 1] = 0$ guarantees that no element equal to $x - 1$ exists, and $\text{freq}[x + 1] = 0$ guarantees that no element equal to $x + 1$ exists. Thus, every emitted number strictly meets the problem definition of loneliness.

### Completeness
Every element in `nums` is tested. If an element satisfies the three conditions, it will evaluate to True and be included in the output list. Because hash table queries reflect the complete multiset of `nums`, no valid lonely number can be missed.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Array with a Single Element:** `nums = [42]`. $\text{freq}[42] = 1$, $41 \notin \text{nums}$, $43 \notin \text{nums}$. The single element is lonely; returns `[42]`.
2. **All Elements Identical:** `nums = [5, 5, 5]`. $\text{freq}[5] = 3 \ne 1$. No element qualifies; returns `[]`.
3. **Consecutive Chain:** `nums = [1, 2, 3, 4]`. Every element has at least one adjacent neighbor present. All elements are disqualified; returns `[]`.
4. **Zero-Valued Elements:** Values can be $0$ ($0 \le \text{nums}[i] \le 10^6$). For $x = 0$, the left neighbor is $-1$, which is checked correctly against the frequency table.

### Common Anti-Patterns
- **Linear Scan for Neighbors ($O(n^2)$):** For every element $x$, scanning the array linearly to check for duplicates and neighbors $x \pm 1$ takes $O(n^2)$ time, which times out for $n = 10^5$. Using a hash map achieves $O(1)$ expected lookup per test.
- **Set In place of Frequency Map:** A standard `Set` dedupes values. If `nums = [3, 3]`, the set contains `{3}`. A set-based check would see that $2 \notin \text{Set}$ and $4 \notin \text{Set}$ and incorrectly conclude that $3$ is lonely. Frequency counting is mandatory to detect duplicates.
- **Sorting Approach Overhead:** Sorting `nums` in $O(n \log n)$ allows neighbor checks by inspecting adjacent array slots, but requires extra handling for duplicate runs and boundary edges. Hash counting is simpler and runs in linear $O(n)$ time.

---

## 7. Complexity Analysis

### Time Complexity
- **Pass 1:** Inserting $n$ elements into a hash table takes $O(n)$ expected time.
- **Pass 2:** For each of the $n$ elements, performing $3$ hash table lookups ($\text{freq}[x]$, $\text{freq}[x-1]$, $\text{freq}[x+1]$) takes $O(1)$ expected time.
- Total time complexity is $O(n)$ expected time, taking under $15$ milliseconds for $n = 10^5$.

### Auxiliary Space Complexity
- The hash table stores at most $n$ distinct integer keys and their frequencies.
- The output list stores at most $n$ lonely numbers.
- Total auxiliary space complexity is $O(n)$ auxiliary memory.
