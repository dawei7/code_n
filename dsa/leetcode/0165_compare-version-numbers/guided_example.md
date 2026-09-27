# Guided Example: Compare Version Numbers

We trace the step-by-step revision-by-revision integer parsing and missing-chunk zero padding on representative version string comparisons:

- **Input:** $\text{version1} = \text{"1.2"}, \quad \text{version2} = \text{"1.10"}$
- **Required output:** $-1$ (Revision 1 evaluates $2 < 10$)
- **Leading Zeros Instance:** $\text{version1} = \text{"1.01"}, \quad \text{version2} = \text{"1.001"} \implies 0$ (Integer conversion evaluates $1 == 1$)
- **Trailing Zero Padding Instance:** $\text{version1} = \text{"1.0"}, \quad \text{version2} = \text{"1.0.0.0"} \implies 0$ (Implicit $0$ revisions match)
- **Version 1 Superior Instance:** $\text{version1} = \text{"1.0.1"}, \quad \text{version2} = \text{"1"} \implies 1$ ($1 > 0$ at revision index 2)

This instance demonstrates comparing numerical integer values rather than lexicographical string characters, absorbing arbitrary leading zeroes on the fly ($a \times 10 + \text{digit}$), treating exhausted suffix revisions as virtual $0$, and achieving $O(N + M)$ time with strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given two version strings $\text{version1} = \text{"1.2"}$ and $\text{version2} = \text{"1.10"}$:
Compare them and return:
- $-1$ if $\text{version1} < \text{version2}$
- $1$ if $\text{version1} > \text{version2}$
- $0$ if $\text{version1} == \text{version2}$

Comparing versions as raw strings fails:
- Lexicographically, character `'2'` is greater than `'1'`, which would falsely claim $\text{"1.2"} > \text{"1.10"}$.
- Numerically, revision 2 is strictly less than revision 10 ($2 < 10$), so $\text{version1} < \text{version2}$ (output: $-1$).

Furthermore, versions of unequal length with trailing zeroes must evaluate as equal (e.g. `"1.0"` equals `"1.0.0"`).
By streaming both strings through two pointers without allocating token arrays, each dot-separated revision is converted to an integer in $O(1)$ space, padding missing suffix chunks with $0$.

---

## 2. Conceptual Foundation & Invariants

### In-Place Chunk Streaming Protocol
Maintain pointers $i = 0$ (for `version1`) and $j = 0$ (for `version2`).
Let $M = |\text{version1}|, \, N = |\text{version2}|$.

While $i < M$ or $j < N$:
1. **Accumulate Numerical Value for `version1`:**
   Initialize $a = 0$.
   While $i < M$ and $\text{version1}[i] \ne \text{'.'}:$:
   $$
   a \leftarrow a \times 10 + \text{int}(\text{version1}[i])
   $$
   $$
   i \leftarrow i + 1
   $$
2. **Accumulate Numerical Value for `version2`:**
   Initialize $b = 0$.
   While $j < N$ and $\text{version2}[j] \ne \text{'.'}:$:
   $$
   b \leftarrow b \times 10 + \text{int}(\text{version2}[j])
   $$
   $$
   j \leftarrow j + 1
   $$
3. **Compare Revision Numbers:**
   - If $a < b$: return $-1$.
   - If $a > b$: return $1$.
4. **Skip Delimiters:**
   $$
   i \leftarrow i + 1, \quad j \leftarrow j + 1
   $$

If the loop finishes without returning, all revisions match: return $0$.

> **Invariant.** If one version string is exhausted before the other, its remaining revision values evaluate to $0$. The first differing pair of revision values $(a, b)$ completely determines the relative order of the versions.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{version1} = \text{"1.2"}$ and $\text{version2} = \text{"1.10"}$:

### Revision 0:
- **`version1` Parse:**
  - $i = 0: \text{version1}[0] = \text{'1'} \implies a = 0 \times 10 + 1 = \mathbf{1}$.
  - $i = 1: \text{version1}[1] = \text{'.'}$. Stop parsing.
- **`version2` Parse:**
  - $j = 0: \text{version2}[0] = \text{'1'} \implies b = 0 \times 10 + 1 = \mathbf{1}$.
  - $j = 1: \text{version2}[1] = \text{'.'}$. Stop parsing.
- **Compare:**
  $$
  a == b \quad (1 == 1)
  $$
  Equal. Advance over dots: $i \leftarrow 2, \, j \leftarrow 2$.

---

### Revision 1:
- **`version1` Parse:**
  - $i = 2: \text{version1}[2] = \text{'2'} \implies a = 0 \times 10 + 2 = \mathbf{2}$.
  - $i = 3 == M$. End of string. Stop parsing.
- **`version2` Parse:**
  - $j = 2: \text{version2}[2] = \text{'1'} \implies b = 0 \times 10 + 1 = 1$.
  - $j = 3: \text{version2}[3] = \text{'0'} \implies b = 1 \times 10 + 0 = \mathbf{10}$.
  - $j = 4 == N$. End of string. Stop parsing.
- **Compare:**
  $$
  a < b \quad (2 < 10)
  $$
  Strictly less!

Return $\mathbf{-1}$.

---

## 4. Complete Execution Trace

```text
version1: "1.2"
version2: "1.10"

Revision 0:
  version1: "1"  -> val = 1
  version2: "1"  -> val = 1
  Compare: 1 == 1 -> Continue

Revision 1:
  version1: "2"  -> val = 2
  version2: "10" -> val = 10
  Compare: 2 < 10 -> Return -1
```

| Revision Index | `version1` Substring | Integer Value $a$ | `version2` Substring | Integer Value $b$ | Comparison Condition | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `"1"` | 1 | `"1"` | 1 | $1 == 1$ | Skip dot, continue |
| **1** | **`"2"`** | **2** | **`"10"`** | **10** | **$2 < 10$** | **Return -1** |

### Contrast: Unequal Length with Trailing Zeroes (`"1.0"` vs `"1.0.0"`)
- Rev 0: $a = 1, b = 1 \implies 1 == 1$.
- Rev 1: $a = 0, b = 0 \implies 0 == 0$.
- Rev 2: $v_1$ exhausted $\implies a = 0$. $v_2$ parses `"0"` $\implies b = 0$. $0 == 0$.
- Both exhausted $\implies$ Return **0**.

---

## 5. Algorithmic Correctness

**Soundness.** Revisions are compared strictly in left-to-right hierarchical order (major, minor, patch, etc.). If the $k$-th revision satisfies $a_k \ne b_k$, the version with the larger revision number is globally greater regardless of subsequent revisions.

**Completeness.** Trailing revisions on a shorter version string evaluate to 0 because the accumulator initializes to 0 and the inner parse loop does not execute for exhausted strings. All possible length differences and suffix zeros are handled correctly.

---

## 6. Traps This Instance Exposes

- **Lexicographical Comparison Hazard:** Directly comparing strings `"1.2"` vs `"1.10"` yields `"1.2" > "1.10"` because `'2' > '1'`. Parsing integers $2 < 10$ is mandatory.
- **Leading Zeros in Revisions:** Revisions like `"01"` and `"001"` both evaluate to integer $1$. The Horner accumulators $a \times 10 + d$ absorb arbitrary runs of leading zeros naturally.
- **Asymmetric Revision Counts:** `"1.0"` and `"1.0.0.0"` represent the same version. Simply comparing token array lengths would falsely claim they differ.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$, where $M = |\text{version1}|$ and $N = |\text{version2}|$. Each character is processed at most once during digit accumulation and dot skipping.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory when streaming characters with pointers $i$ and $j$, avoiding substring or array allocations.
