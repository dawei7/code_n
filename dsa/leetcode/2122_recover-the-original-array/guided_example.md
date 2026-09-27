# Guided Example: Recover the Original Array

We trace the step-by-step execution of the candidate gap enumeration and greedy two-pointer pairing approach on a representative problem instance:

- **Input Array (`nums`):** `[2, 10, 6, 4, 8, 12]`
- **Expected Output:** `[3, 7, 11]`

This instance demonstrates how sorting forces the global minimum to be an element of `lower`, restricting possible values of the offset parameter $k$ to candidate differences between the first element and subsequent elements, and showing how greedy pairing verifies candidates deterministically.

---

## 1. Problem Overview & Representative Instance

Alice had an original array `arr` of $n$ positive integers and chose a positive integer $k > 0$. She generated two arrays:
- $\text{lower}[i] = \text{arr}[i] - k$
- $\text{higher}[i] = \text{arr}[i] + k$

She then merged $\text{lower}$ and $\text{higher}$ in an arbitrary order to form `nums` of length $2n$. Our task is to recover any valid original array `arr`.

In our representative instance `nums = [2, 10, 6, 4, 8, 12]`:
- Length is $2n = 6$, so the original array has size $n = 3$.
- Sorting `nums` yields `[2, 4, 6, 8, 10, 12]`.
- Each original element $x$ generates a pair $(x - k, x + k)$ with constant separation:

$$(x + k) - (x - k) = 2k$$

Because $k > 0$, the smaller element in every pair belongs to $\text{lower}$ and the larger belongs to $\text{higher}$. The global minimum of `nums` (here $2$) must therefore be an element of $\text{lower}$.

---

## 2. Mathematical & Algorithmic Principles

### Global Extremum Lower-Bound Lemma
Let `nums` be sorted in ascending order: $s_0 \le s_1 \le \dots \le s_{2n-1}$.
Because every element in $\text{higher}$ is accompanied by an element in $\text{lower}$ that is strictly smaller by $2k$, the absolute minimum $s_0$ cannot belong to $\text{higher}$. Hence, $s_0 \in \text{lower}$.

### Finite Candidate Space for $k$
Since $s_0$ is a lower element, its corresponding higher counterpart $s_0 + 2k$ must appear somewhere in the array. Thus, there exists some index $j \in \{1, 2, \dots, 2n - 1\}$ such that:

$$s_j - s_0 = 2k \implies k = \frac{s_j - s_0}{2}$$

For $k$ to be a valid positive integer:
1. $s_j - s_0 > 0$ (strict positivity of $k$).
2. $s_j - s_0 \equiv 0 \pmod 2$ (even parity of the gap).

This bounds the search space of candidate offsets $k$ to at most $2n - 1$ distinct values.

### Deterministic Greedy Pairing Invariant
For a fixed candidate $k$:
1. Identify the smallest unvisited element $u$ in the sorted array. Because $u$ is the minimal available value, it cannot be a higher element for any remaining number; it must be a lower element.
2. Its required partner is uniquely fixed to $u + 2k$.
3. If $u + 2k$ is present among unvisited elements, we pair them, mark both as visited, and record the midpoint $u + k$ into our recovered array.
4. If $u + 2k$ cannot be found, candidate $k$ is invalid. We immediately abort and test the next candidate.

| Component | Role in Search | Verification Rule |
|---|---|---|
| Anchor $s_0$ | Minimum element | Must be paired with some $s_j$ |
| Candidate Gap $2k$ | Difference $s_j - s_0$ | Must be even and $> 0$ |
| Current Smallest $u$ | Minimal unvisited element | Forced lower partner |
| Required Target | $u + 2k$ | Must exist and be unvisited |
| Midpoint | $u + k$ | Recovered element for `arr` |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Sorted array: `nums = [2, 4, 6, 8, 10, 12]` with $n = 3$.
Anchor: $s_0 = 2$.

### Testing Candidate 1: Partner $s_1 = 4$
- Difference: $s_1 - s_0 = 4 - 2 = 2$.
- Candidate $k$: $2 / 2 = 1$.
- Gap: $2k = 2$.

#### Pairing Round 1:
- Smallest unused element: index $0$ ($u = 2$).
- Required higher partner: $u + 2k = 2 + 2 = 4$.
- Element $4$ exists at index $1$.
- Pair formed: $(2, 4)$. Midpoint: $2 + 1 = 3$.
- Recovered array: `[3]`.
- Remaining unused: `[6, 8, 10, 12]`.

#### Pairing Round 2:
- Smallest unused element: index $2$ ($u = 6$).
- Required higher partner: $u + 2k = 6 + 2 = 8$.
- Element $8$ exists at index $3$.
- Pair formed: $(6, 8)$. Midpoint: $6 + 1 = 7$.
- Recovered array: `[3, 7]`.
- Remaining unused: `[10, 12]`.

#### Pairing Round 3:
- Smallest unused element: index $4$ ($u = 10$).
- Required higher partner: $u + 2k = 10 + 2 = 12$.
- Element $12$ exists at index $5$.
- Pair formed: $(10, 12)$. Midpoint: $10 + 1 = 11$.
- Recovered array: `[3, 7, 11]`.
- Remaining unused: `[]`.

All $2n = 6$ elements have been successfully partitioned into $n = 3$ valid pairs for $k = 1$.
The candidate succeeds, and the recovered array is `[3, 7, 11]`.

---

## 4. Comprehensive State Trace

The table below traces the candidate evaluation and greedy pair matching.

| Candidate Partner $s_j$ | Gap ($s_j - s_0$) | Parity Check | Candidate $k$ | Smallest Unused $u$ | Required $u + 2k$ | Partner Found? | Recovered Midpoint ($u + k$) |
|---|---|---|---|---|---|---|---|
| $4$ (Index 1) | $2$ | Even ($> 0$) | $1$ | $2$ | $4$ | Yes | $3$ |
| — | — | — | $1$ | $6$ | $8$ | Yes | $7$ |
| — | — | — | $1$ | $10$ | $12$ | Yes | $11$ |

Resulting array: `[3, 7, 11]`.

For completeness, consider what would have occurred if candidate $k = 2$ had been tested (matching $s_0 = 2$ with $s_2 = 6$, $2k = 4$):
- Pair $(2, 6)$ leaves smallest unused $u = 4$.
- Required partner: $4 + 4 = 8$. Pair $(4, 8)$ leaves $u = 10$.
- Required partner: $10 + 4 = 14$, but $14$ is not in the array!
- Candidate $k = 2$ fails immediately.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** When a candidate $k$ partitions all $2n$ elements into disjoint pairs $(x_i, y_i)$ such that $y_i - x_i = 2k$, setting $a_i = x_i + k$ produces:
- $x_i = a_i - k$
- $y_i = a_i + k$
Hence, the union of $\{a_i - k\}$ and $\{a_i + k\}$ matches `nums` with exact multiplicities. Because $k > 0$, the recovered array satisfies all problem conditions.

**Completeness.** Suppose a valid configuration exists with offset $k^*$. In sorted `nums`, $s_0$ is the minimum element and must be the lower element of some pair $(s_0, s_0 + 2k^*)$. Thus, $s_0 + 2k^*$ must appear at some index $j \in \{1, \dots, 2n - 1\}$. Because our algorithm enumerates all valid candidate indices $j$ with even positive differences, $k^*$ is guaranteed to be tested. Under candidate $k^*$, sorted greedy selection is strictly forced: at each step, the smallest unvisited element cannot be a higher counterpart of any remaining element, so it must be paired with $u + 2k^*$. Therefore, the greedy check will succeed and recover a valid solution.

---

## 6. Edge Cases & Anti-Patterns

- **Duplicate Elements:** If multiple identical values exist (e.g. `[1, 1, 3, 3]`), two-pointer tracking or frequency counts ensure each instance is consumed exactly once.
- **Odd Differences:** If $s_j - s_0$ is odd, $k$ would be fractional, violating the integer constraint. These candidates are skipped in $\mathcal{O}(1)$ time.
- **Zero Differences ($s_j = s_0$):** $k = 0$ is forbidden because $k$ must be strictly positive ($k > 0$).
- **Anti-Pattern — Arbitrary Backtracking:** Attempting recursive search over all possible pairings yields factorial time $\mathcal{O}((2n)!)$. Sorting reduces candidate values of $k$ to at most $2n$ choices, each verifiable in $\mathcal{O}(n)$ time.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n^2)$, where $2n$ is the length of `nums`. Sorting takes $\mathcal{O}(n \log n)$. There are at most $2n - 1$ candidate values of $k$. For each candidate, the two-pointer or frequency verification scans the sorted array in $\mathcal{O}(n)$ time. Total runtime is $\mathcal{O}(n \log n + n \cdot n) = \mathcal{O}(n^2)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(n)$ auxiliary space to store the boolean visited marker array and the output array of length $n$.
