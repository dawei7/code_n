# Guided Example: Find the Index of the First Occurrence in a String

We trace the step-by-step fixed-window substring matching on representative string instances:

- **Primary Input:** $\text{haystack} = \text{"sadbutsad"}$, $\text{needle} = \text{"sad"}$
- **Required output:** $0$
- **Negative Variant:** $\text{haystack} = \text{"leetcode"}$, $\text{needle} = \text{"leeto"}$
- **Required output:** $-1$

This instance demonstrates sliding window alignment, upper bound index calculations ($N - M$), early return upon the first verified match, and character-by-character mismatch detection.

---

## 1. Instance & Teaching Goal

Given two strings $\text{haystack}$ of length $N$ and $\text{needle}$ of length $M$, we must return the smallest index $i$ such that the substring of length $M$ beginning at $i$ is identical to $\text{needle}$. If $\text{needle}$ does not appear anywhere in $\text{haystack}$, return $-1$.

For $\text{haystack} = \text{"sadbutsad"}$ ($N = 9$) and $\text{needle} = \text{"sad"}$ ($M = 3$):
- At index $0$, $\text{haystack}[0 \dots 2] = \text{"sad"}$, which matches $\text{needle}$ exactly.
- The earliest occurrence index is $0$.

The goal is to systematically evaluate all candidate starting positions in increasing index order, verifying substrings without indexing beyond the end of $\text{haystack}$.

---

## 2. Conceptual Foundation & Invariants

### Candidate Starting Window Range
For $\text{needle}$ of length $M$ to fit within $\text{haystack}$ of length $N$, the last character of the candidate window at start index $i$ must not exceed the end of $\text{haystack}$:
$$
i + M - 1 \le N - 1 \iff i \le N - M
$$
The valid candidate start indices are exactly:
$$
i \in [0, N - M]
$$
If $M > N$, $N - M < 0$, meaning no candidate window can exist. The search returns $-1$ immediately.

### Linear Scan Invariant
We iterate $i$ from $0$ up to $N - M$:
1. Compare the slice $\text{haystack}[i \dots i + M - 1]$ with $\text{needle}$.
2. If equal, return $i$ immediately (guaranteeing the *first* occurrence).
3. If no match is found after testing all indices up to $N - M$, return $-1$.

> **Invariant.** Before inspecting index $i$, no occurrence of $\text{needle}$ begins at any index $k < i$. Returning the first matching index $i$ guarantees the global minimum occurrence index.

---

## 3. Step-by-Step Worked Execution

### Case A: Successful Early Match ($\text{"sadbutsad"}$, $\text{"sad"}$)
- Parameters: $N = 9$, $M = 3$. Valid search range: $i \in [0, 6]$.

- **Candidate $i = 0$:**
  - Substring window: $\text{haystack}[0 \dots 3] = \text{"sad"}$.
  - Target pattern: $\text{"sad"}$.
  - Character comparison:
    - Index $0 + 0$: `'s' == 's'` (match)
    - Index $0 + 1$: `'a' == 'a'` (match)
    - Index $0 + 2$: `'d' == 'd'` (match)
  - Full match confirmed! Return starting index $0$.

---

### Case B: Unsuccessful Match ($\text{"leetcode"}$, $\text{"leeto"}$)
- Parameters: $N = 8$, $M = 5$. Valid search range: $i \in [0, 3]$.

- **Candidate $i = 0$:**
  - Window: $\text{haystack}[0 \dots 5] = \text{"leetc"}$.
  - Compare with $\text{"leeto"}$: Mismatch at position 4 (`'c'` vs `'o'`).
- **Candidate $i = 1$:**
  - Window: $\text{haystack}[1 \dots 6] = \text{"eetco"}$.
  - Compare with $\text{"leeto"}$: Mismatch at position 0 (`'e'` vs `'l'`).
- **Candidate $i = 2$:**
  - Window: $\text{haystack}[2 \dots 7] = \text{"etcod"}$.
  - Compare with $\text{"leeto"}$: Mismatch at position 0 (`'e'` vs `'l'`).
- **Candidate $i = 3$:**
  - Window: $\text{haystack}[3 \dots 8] = \text{"tcode"}$.
  - Compare with $\text{"leeto"}$: Mismatch at position 0 (`'t'` vs `'l'`).
- **Search Exhausted:** All legal start positions tested. Return $-1$.

---

## 4. Complete Execution Trace

### Window Evaluation Table for $\text{"leetcode"}$ vs $\text{"leeto"}$

| Candidate $i$ | Window Slice $\text{haystack}[i \dots i+M]$ | Target $\text{needle}$ | First Mismatch Offset | Match Status | Action |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `"leetc"` | `"leeto"` | Offset 4 (`'c'` $\ne$ `'o'`) | Mismatch | Advance to $i = 1$ |
| 1 | `"eetco"` | `"leeto"` | Offset 0 (`'e'` $\ne$ `'l'`) | Mismatch | Advance to $i = 2$ |
| 2 | `"etcod"` | `"leeto"` | Offset 0 (`'e'` $\ne$ `'l'`) | Mismatch | Advance to $i = 3$ |
| 3 | `"tcode"` | `"leeto"` | Offset 0 (`'t'` $\ne$ `'l'`) | Mismatch | End of valid range reached |
| Terminal | - | - | - | Exhausted | **Return $-1$** |

---

## 5. Algorithmic Correctness

**Soundness.** A returned index $i$ satisfies $\text{haystack}[i \dots i+M-1] == \text{needle}$ by explicit string comparison. Because the search evaluates candidate indices in strictly increasing order ($0, 1, 2, \dots$), the first match found is mathematically guaranteed to be the earliest occurrence.

**Completeness.** Any occurrence of $\text{needle}$ must start at some index between $0$ and $N - M$. Because the loop tests every integer $i \in [0, N - M]$, no valid starting window is skipped. If no match is found, returning $-1$ is correct.

---

## 6. Traps This Instance Exposes

- **Off-by-One on Search Bound:** In languages with half-open ranges like Python's `range(stop)`, using `range(N - M)` misses the final valid window at index $N - M$. The loop bound must be `range(N - M + 1)`.
- **Needle Longer Than Haystack ($M > N$):** If $M > N$, $\text{needle}$ cannot appear in $\text{haystack}$. The upper bound $N - M + 1 \le 0$, yielding an empty range that safely returns $-1$ without error.
- **Empty Needle:** If $\text{needle} = \text{""}$, standard conventions dictate returning $0$ because the empty string is trivially a prefix of any string at index $0$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((N - M + 1) \cdot M)$. In the worst case (e.g. $\text{haystack} = \text{"aaaaa"}$, $\text{needle} = \text{"aab"}$), checking each of the $N - M + 1$ windows takes $O(M)$ character comparisons, resulting in $O(N \cdot M)$ worst-case time. In typical strings, mismatches occur within the first 1–2 characters, yielding $O(N)$ average runtime.
- **Auxiliary Space Complexity:** $O(1)$. Slicing or index-based comparisons require no additional heap memory.
