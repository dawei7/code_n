# Guided Example: Scramble String

We trace the step-by-step recursive string scrambling decomposition with memoization and anagram pruning:

- **Input:** $s_1 = \text{"great"}$, $s_2 = \text{"rgeat"}$
- **Required output:** $\text{True}$
- **Unscrambled Negative Instance:** $s_1 = \text{"abcde"}$, $s_2 = \text{"caebd"} \implies \text{False}$

This instance demonstrates recursive binary tree partitioning of strings, evaluating both non-swapped ($x \leftrightarrow x', y \leftrightarrow y'$) and swapped ($x \leftrightarrow y', y \leftrightarrow x'$) split choices, anagram frequency pruning, and memoizing subproblem intervals in $O(N^4)$ time.

---

## 1. Instance & Teaching Goal

We can scramble a string $s$ by recursively splitting it into two non-empty substrings $x$ and $y$ ($s = x + y$), and either:
1. **Keeping the order:** $s' = x + y$
2. **Swapping the order:** $s' = y + x$
and then applying this scrambling procedure recursively to both $x$ and $y$.

Given $s_1 = \text{"great"}$ and $s_2 = \text{"rgeat"}$:
- Split $s_1$ into $x = \text{"gr"}$ and $y = \text{"eat"}$.
- Split $s_2$ into $x' = \text{"rg"}$ and $y' = \text{"eat"}$.
- $y = \text{"eat"}$ matches $y'$ directly without scrambling.
- $x = \text{"gr"}$ splits into `'g'` and `'r'`. Swapping them produces $\text{'r'} + \text{'g'} = \text{"rg"}$, matching $x'$.
- Combining them produces $\text{"rgeat"}$. The answer is $\text{True}$.

A naive recursive exploration explores Catalan-numbered binary tree shapes with exponential $O(4^N)$ complexity.
By introducing memoization over substring tuples $(s_1, s_2)$ and early-terminating non-anagram branches via character frequency hashing, the search runs in polynomial $O(N^4)$ time.

---

## 2. Conceptual Foundation & Invariants

### 2-Way Split Decision Recurrence
Let $L = |s_1| = |s_2|$. For strings $s_1$ and $s_2$:

1. **Base Identity:**
   If $s_1 == s_2$: return $\text{True}$.
2. **Anagram Pruning:**
   If $\text{Counter}(s_1) \ne \text{Counter}(s_2)$: return $\text{False}$.
   *(If character frequencies do not match, no series of swaps can make them identical)*.
3. **Split Point Search ($k \in [1, L - 1]$):**
   Divide $s_1$ into left prefix $s_1[:k]$ and right suffix $s_1[k:]$.
   Test two mutually exclusive cases:
   - **Case 1: No Swap** (prefix aligns with prefix):
     $$
     \text{isScramble}(s_1[:k], s_2[:k]) \land \text{isScramble}(s_1[k:], s_2[k:])
     $$
   - **Case 2: Swap** (prefix aligns with suffix):
     $$
     \text{isScramble}(s_1[:k], s_2[L-k:]) \land \text{isScramble}(s_1[k:], s_2[:L-k])
     $$
4. If either case evaluates to $\text{True}$ for any split index $k$, record $\text{True}$ in cache and return $\text{True}$. If all $k$ fail, return $\text{False}$.

> **Invariant.** For any pair $(s_1, s_2)$ evaluated, the subproblem returns true if and only if there exists a valid binary parse tree whose leaf nodes permute $s_1$ into $s_2$.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"great"}$ and $s_2 = \text{"rgeat"}$ ($L = 5$):

### Top-Level Call: $\text{isScramble}(\text{"great"}, \text{"rgeat"})$
- Check identity: `"great" != "rgeat"`.
- Anagram test: both contain `{'a': 1, 'e': 1, 'g': 1, 'r': 1, 't': 1}`. Valid!

---

### Evaluating Split $k = 2$:
- Partition $s_1$:
  - Left: $s_1[:2] = \text{"gr"}$
  - Right: $s_1[2:] = \text{"eat"}$

- **Case 1 (Unswapped):** Compare with $s_2[:2] = \text{"rg"}$ and $s_2[2:] = \text{"eat"}$.
  - Subproblem 1A: $\text{isScramble}(\text{"eat"}, \text{"eat"})$:
    - Identical strings! Immediately returns $\text{True}$.
  - Subproblem 1B: $\text{isScramble}(\text{"gr"}, \text{"rg"})$:
    - `"gr" != "rg"`.
    - Both are anagrams of each other (`{'g': 1, 'r': 1}`).
    - Length $L = 2$, only split is $k = 1$:
      - $x_1 = \text{'g'}, y_1 = \text{'r'}$.
      - Test swap against $s_2 = \text{"rg"}$:
        - Compare $x_1$ (`'g'`) with $s_2[1:]$ (`'g'`): Identical ($\text{True}$).
        - Compare $y_1$ (`'r'`) with $s_2[:1]$ (`'r'`): Identical ($\text{True}$).
      - Swapped match succeeded! $\text{isScramble}(\text{"gr"}, \text{"rg"})$ returns $\text{True}$.
  - Both Subproblem 1A and 1B return $\text{True}$!
  - Therefore, the unswapped split at $k = 2$ succeeds!

Top-level call immediately returns $\text{True}$.

---

## 4. Complete Execution Trace

### Hierarchical Tree Decomposition

```text
               "great" ~ "rgeat"  (k=2, No-Swap)
              /                                \
      "gr" ~ "rg" (k=1, Swap)             "eat" ~ "eat"
      /                     \               (Identical -> True)
 'g' ~ 'g' (True)       'r' ~ 'r' (True)
```

| Recursion Frame | Input $s_1$ | Input $s_2$ | Tested Split $k$ | Branch Type | Sub-calls Evaluated | Result |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `"great"` | `"rgeat"` | $k = 2$ | No-Swap | Call (`"gr"`, `"rg"`) & (`"eat"`, `"eat"`) | **True** |
| 1.1 | `"eat"` | `"eat"` | - | Base Identity | $s_1 == s_2$ | **True** |
| 1.2 | `"gr"` | `"rg"` | $k = 1$ | Swapped | Call (`'g'`, `'g'`) & (`'r'`, `'r'`) | **True** |
| 1.2.1 | `'g'` | `'g'` | - | Base Identity | $s_1 == s_2$ | **True** |
| 1.2.2 | `'r'` | `'r'` | - | Base Identity | $s_1 == s_2$ | **True** |

---

## 5. Algorithmic Correctness

**Soundness.** A string $s_1$ can be scrambled into $s_2$ if and only if there is a split $k$ such that either the two corresponding halves are recursively scrambles of each other, or the swapped halves are scrambles of each other. The algorithm tests exactly these two disjunctions across all possible split indices $k \in [1, L - 1]$.

**Completeness.** Since $k$ ranges over all possible partition boundaries $1 \dots L-1$, and both orientation branches (same vs swapped) are explored, no valid scramble tree configuration is skipped.

---

## 6. Traps This Instance Exposes

- **Missing Anagram Pruning:** Without the `Counter(s1) == Counter(s2)` test, the recursion explores failing permutations of lengths $2 \dots N$, leading to exponential $O(4^N)$ time limit exceeded (TLE) errors.
- **Substring Slice Offsets:** In the swapped branch, matching $s_1[:k]$ against the suffix of $s_2$ requires slicing $s_2[L-k:]$, not $s_2[k:]$. Precise offset arithmetic is critical.
- **Memoization Key Formulation:** Caching the tuple `(s1, s2)` (or interval coordinates $(i_1, j_1, \text{length})$ in 3D DP) prevents recomputing identical string pair evaluations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^4)$, where $N$ is the string length. There are $O(N^3)$ distinct substring pairs $(i, j, \text{length})$, and for each pair, iterating over $k$ split points takes $O(N)$ work ($N^3 \times N = O(N^4)$).
- **Auxiliary Space Complexity:** $O(N^3)$ to store the memoization cache and $O(N)$ recursion depth.