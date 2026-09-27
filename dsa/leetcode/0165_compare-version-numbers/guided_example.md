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

### Character-Level Streaming Trace

The two pointers advance independently, which is what lets the scan stay $O(1)$ in auxiliary space. Every read either folds a digit into the accumulator or ends the current revision:

| Step | Character read from `version1` | $a$ after the step | Character read from `version2` | $b$ after the step | Why this read happens |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `'1'` at $i = 0$ | $0 \times 10 + 1 = 1$ | `'1'` at $j = 0$ | $0 \times 10 + 1 = 1$ | Both strings open with the same digit, so neither revision can decide the order yet |
| 2 | `'.'` at $i = 1$ | $1$ (unchanged) | `'.'` at $j = 1$ | $1$ (unchanged) | A delimiter ends revision $0$; the accumulated values are compared and found equal |
| 3 | — | $i \leftarrow 2$ | — | $j \leftarrow 2$ | Both pointers step past the delimiter, aligning the next revision for both strings at once |
| 4 | `'2'` at $i = 2$ | $0 \times 10 + 2 = 2$ | `'1'` at $j = 2$ | $0 \times 10 + 1 = 1$ | Revision $1$ starts; `version2` still has another digit to consume, so the comparison must wait |
| 5 | — ($i = 3 = M$) | $2$ (final) | `'0'` at $j = 3$ | $1 \times 10 + 0 = 10$ | `version1` is exhausted while `version2` is mid-revision; the already-finished value $a = 2$ is held |
| 6 | — | — | — ($j = 4 = N$) | $10$ (final) | `version2` reaches its end, so revision $1$ is now fully known on both sides |
| 7 | — | — | — | — | Compare $2 < 10$ and return $-1$; later revisions never need to be read |

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

### Alternative Approaches on This Pair

| Approach | What it does with `"1.2"` versus `"1.10"` | Time | Comparison time | Auxiliary space | Why it fails or costs more |
|:---|:---|:---:|:---|:---:|:---|
| Raw lexicographic string compare | Compares character `'2'` against `'1'` at the third position and declares `"1.2"` larger | $O(\min(M, N))$ | $O(1)$ per character | $O(1)$ | Wrong answer: character order disagrees with numeric order whenever revisions differ in digit count |
| Split both strings on `'.'`, convert every token, then compare | Produces $[1, 2]$ and $[1, 10]$, then walks the two lists | $O(M + N)$ | $O(1)$ per revision | $O(M + N)$ for the token lists and substrings | Correct but allocates a token list proportional to the input, breaking the constant-space requirement |
| Pad the shorter token list with zeros, then compare | Pads `"1.0"` into $[1, 0, 0, 0]$ so list lengths match before walking | $O(M + N)$ | $O(1)$ per revision | $O(M + N)$ | Padding is a symptom, not a fix: the streaming scan already reads a missing revision as $0$ with no list at all |
| Stream revisions on demand with two pointers | Reads `"2"` and `"10"` in place and returns at the first unequal pair | $O(M + N)$ | $O(1)$ per revision | $O(1)$ | None for this contract; digits are folded into $a$ and $b$ without ever materialising a substring |
| Manual digit-string compare with leading-zero stripping | Strips zeros from both revisions, then compares digit by digit | $O(M + N)$ | $O(K)$ for a revision of $K$ digits | $O(1)$ | Correct but re-implements arithmetic comparison; the streaming accumulator gets the same result in one pass |

### Boundary Scenarios Behind the Four Control Inputs

| Input pair | Condition exercised | Expected | Why the streaming scan produces it |
|:---|:---|:---:|:---|
| `"1.01"` vs `"1.001"` | Leading zeros inside a revision | 0 | Both accumulators build $0 \times 10 + 1 = 1$ from different character counts, so leading zeros cannot influence the values |
| `"1.0"` vs `"1.0.0.0"` | One string runs out of revisions first | 0 | Once $i = M$, the next revision of `version1` is read with $a$ reset to $0$ without reading any character, matching the explicit `"0"` of the longer string |
| `"1"` vs `"1.10"` | Prefix string versus dotted string | $-1$ | Revision $0$ ties at $1$; revision $1$ then pairs `version1`'s phantom $0$ with `version2`'s $10$ |
| `"111"` vs `"1.10"` | Revision with more digits than the whole rival prefix | 1 | Horner accumulation yields $a = 111$ for the single revision, and $111 > 1$ decides the order at revision $0$ before any padding question arises |
| `"2.0.1"` vs `"1.999.999"` | Later revisions are numerically far larger | 1 | The first revision already satisfies $2 > 1$, so the scan returns immediately and never inspects `"999.999"` |
| `"1.0000000000000000000000002"` vs `"1.0000000000000000000000003"` | Revisions of tens of digits, far longer than a fixed-width conversion would tolerate | $-1$ | Accumulation is exact integer arithmetic over arbitrarily many digits, so the long revision still yields a true value rather than an approximated one |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$, where $M = |\text{version1}|$ and $N = |\text{version2}|$. Each character is processed at most once during digit accumulation and dot skipping.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory when streaming characters with pointers $i$ and $j$, avoiding substring or array allocations.
