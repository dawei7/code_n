# Guided Example: Find First and Last Position of Element in Sorted Array

We trace the step-by-step execution of dual-pass binary search (left and right boundary bisection) on a representative sorted array instance:

- **Input:** $\text{nums} = [5, 7, 7, 8, 8, 10]$, $\text{target} = 8$
- **Required output:** $[3, 4]$

This instance demonstrates bisecting to find the leftmost (first) index of an element, bisecting to find the rightmost (last) index of an element, directional contraction upon encountering duplicate target values, and handling missing elements in $O(\log N)$ time.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 6$ sorted in non-decreasing order:
$$
[5, 7, 7, 8, 8, 10]
$$

We must find the starting and ending indices of a given $\text{target} = 8$. If the target is not present, return $[-1, -1]$. The algorithm must run in $O(\log N)$ time.

A standard binary search stops as soon as it encounters any occurrence of $\text{target}$. For $[5, 7, 7, 8, 8, 10]$, stopping at index 4 would not tell us whether earlier copies exist at index 3 or later copies exist beyond. To find both endpoints, we execute two specialized binary searches:
1. **Left Boundary Search:** When $\text{nums}[M] == \text{target}$, record $M$ as a candidate and continue searching left ($R = M - 1$).
2. **Right Boundary Search:** When $\text{nums}[M] == \text{target}$, record $M$ as a candidate and continue searching right ($L = M + 1$).

---

## 2. Conceptual Foundation & Invariants

### Bisection Boundary Principles
Let $f_{\text{left}}(\text{target})$ and $f_{\text{right}}(\text{target})$ be two binary searches over interval $[L, R]$:

1. **Finding Leftmost Index (`find_first`):**
   - If $\text{nums}[M] == \text{target}$: Record $\text{first} \leftarrow M$. Shift right pointer $R \leftarrow M - 1$ to check if an earlier copy exists to the left.
   - If $\text{nums}[M] < \text{target}$: Shift left pointer $L \leftarrow M + 1$.
   - If $\text{nums}[M] > \text{target}$: Shift right pointer $R \leftarrow M - 1$.
2. **Finding Rightmost Index (`find_last`):**
   - If $\text{nums}[M] == \text{target}$: Record $\text{last} \leftarrow M$. Shift left pointer $L \leftarrow M + 1$ to check if a later copy exists to the right.
   - If $\text{nums}[M] < \text{target}$: Shift left pointer $L \leftarrow M + 1$.
   - If $\text{nums}[M] > \text{target}$: Shift right pointer $R \leftarrow M - 1$.

> **Invariant.** The left search interval always maintains all potential occurrences at or to the left of the best recorded candidate. The right search interval maintains all potential occurrences at or to the right of the best recorded candidate.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [5, 7, 7, 8, 8, 10]$ with $\text{target} = 8$:

### Pass 1: Find Leftmost Boundary ($\text{first}$)
Initialize $L = 0, R = 5, \text{first} = -1$.

- **Step 1 ($L = 0, R = 5$):**
  - Midpoint: $M = \lfloor (0 + 5) / 2 \rfloor = 2$.
  - Value: $\text{nums}[2] = 7$.
  - Compare: $7 < \text{target} = 8$.
  - Decision: Target must be in right half $\implies L \leftarrow M + 1 = 3$.

- **Step 2 ($L = 3, R = 5$):**
  - Midpoint: $M = \lfloor (3 + 5) / 2 \rfloor = 4$.
  - Value: $\text{nums}[4] = 8$.
  - Compare: $\text{nums}[4] == \text{target} = 8$. Match found!
  - Record candidate: $\text{first} \leftarrow 4$.
  - Decision: Check for earlier occurrences to the left $\implies R \leftarrow M - 1 = 3$.

- **Step 3 ($L = 3, R = 3$):**
  - Midpoint: $M = \lfloor (3 + 3) / 2 \rfloor = 3$.
  - Value: $\text{nums}[3] = 8$.
  - Compare: $\text{nums}[3] == \text{target} = 8$. Match found!
  - Record candidate: $\text{first} \leftarrow 3$.
  - Decision: Check further left $\implies R \leftarrow M - 1 = 2$.

- **Termination:** $L = 3 > R = 2$. Loop ends. First position is confirmed as $3$.

---

### Pass 2: Find Rightmost Boundary ($\text{last}$)
Initialize $L = 0, R = 5, \text{last} = -1$.

- **Step 1 ($L = 0, R = 5$):**
  - Midpoint: $M = \lfloor (0 + 5) / 2 \rfloor = 2$.
  - Value: $\text{nums}[2] = 7 < 8 \implies L \leftarrow M + 1 = 3$.

- **Step 2 ($L = 3, R = 5$):**
  - Midpoint: $M = \lfloor (3 + 5) / 2 \rfloor = 4$.
  - Value: $\text{nums}[4] = 8 == \text{target}$. Match found!
  - Record candidate: $\text{last} \leftarrow 4$.
  - Decision: Check for later occurrences to the right $\implies L \leftarrow M + 1 = 5$.

- **Step 3 ($L = 5, R = 5$):**
  - Midpoint: $M = \lfloor (5 + 5) / 2 \rfloor = 5$.
  - Value: $\text{nums}[5] = 10 > 8 \implies R \leftarrow M - 1 = 4$.

- **Termination:** $L = 5 > R = 4$. Loop ends. Last position is confirmed as $4$.

Combined final output: $[3, 4]$.

---

## 4. Complete Execution Trace

### Pass 1: Left Boundary Search Trace Table

| Step | Left $L$ | Right $R$ | Midpoint $M$ | Value $\text{nums}[M]$ | Comparison to Target (8) | Candidate $\text{first}$ | Pointer Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 5 | 2 | 7 | $7 < 8$ | -1 | Shift right: $L \leftarrow 3$ |
| 2 | 3 | 5 | 4 | 8 | $8 == 8$ (Match) | 4 | Search left: $R \leftarrow 3$ |
| 3 | 3 | 3 | 3 | 8 | $8 == 8$ (Match) | **3** | Search left: $R \leftarrow 2$ |
| Done | 3 | 2 | - | - | $L > R$ | **3** | First occurrence locked at index $3$ |

### Pass 2: Right Boundary Search Trace Table

| Step | Left $L$ | Right $R$ | Midpoint $M$ | Value $\text{nums}[M]$ | Comparison to Target (8) | Candidate $\text{last}$ | Pointer Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 5 | 2 | 7 | $7 < 8$ | -1 | Shift right: $L \leftarrow 3$ |
| 2 | 3 | 5 | 4 | 8 | $8 == 8$ (Match) | 4 | Search right: $L \leftarrow 5$ |
| 3 | 5 | 5 | 5 | 10 | $10 > 8$ | 4 | Shift left: $R \leftarrow 4$ |
| Done | 5 | 4 | - | - | $L > R$ | **4** | Last occurrence locked at index $4$ |

---

## 5. Algorithmic Correctness

**Soundness.** Every recorded boundary index satisfies $\text{nums}[\text{idx}] == \text{target}$. In Pass 1, continuing to search $R = M - 1$ when a match is found ensures no earlier index can be missed. Symmetrically, in Pass 2, continuing $L = M + 1$ ensures no later index can be missed.

**Completeness.** Since the array is sorted, all target occurrences form a single contiguous block $[\text{first}, \text{last}]$. If the target does not exist, Pass 1 never encounters $\text{nums}[M] == \text{target}$, keeping $\text{first} = -1$ and immediately returning $[-1, -1]$.

---

## 6. Traps This Instance Exposes

- **Linear Expansion Fallacy:** Finding any occurrence with binary search and then expanding linearly with `while` loops takes $O(N)$ time in the worst case (e.g. $[8, 8, 8, \dots, 8]$). Two pure logarithmic binary searches guarantee $O(\log N)$ worst-case performance.
- **Empty Array:** When $\text{nums} = []$, $L = 0, R = -1$. The loops do not execute, correctly returning $[-1, -1]$.
- **Target Missing But Within Value Range:** If $\text{target} = 6$, Pass 1 narrows interval to $L = 1, R = 0$ without matching, correctly yielding $-1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$. Pass 1 bisects the array in $\lceil \log_2 N \rceil + 1$ iterations. Pass 2 bisects the array in $\lceil \log_2 N \rceil + 1$ iterations. Total time is $2 \cdot O(\log N) = O(\log N)$.
- **Auxiliary Space Complexity:** $O(1)$. Both bisections execute iteratively using a few scalar pointers without extra allocations.