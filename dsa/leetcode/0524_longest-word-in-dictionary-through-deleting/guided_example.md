# Guided Example: Longest Word in Dictionary through Deleting

We trace the step-by-step two-pointer greedy subsequence matching ($check(t, s)$), dual optimization criteria (maximize length $|t|$, tie-break by smallest lexicographical string order $t < ans$), candidate replacement logic, and default empty string fallback on representative dictionary instances:

- **Input:**
  - Source string: $s = \text{"abpcplea"}$
  - Dictionary words: $dictionary = [\text{"ale"}, \text{"apple"}, \text{"monkey"}, \text{"plea"}]$
- **Required output:** `"apple"`
  - Constraint rules:
    1. Word must be formed by deleting characters from $s$ (i.e. word is a **subsequence** of $s$).
    2. Longest word length wins ($\max |t|$).
    3. If lengths tie, the **lexicographically smallest** word wins (e.g. `"apple" < \text{"apply"}`).
    4. If no word can be formed, return empty string `""`.
- **Candidate-by-candidate execution trace:**
  - Initialize best answer: $ans = \text{""}$ ($|ans| = 0$).
  - **Candidate 1: $t = \text{"ale"}$ (Length 3):**
    - Subsequence check $check(\text{"ale"}, \text{"abpcplea"})$:
      - Pointer in $t$: looking for `'a'` $\to$ found at $s[0]$ (`'a'`).
      - Pointer in $t$: looking for `'l'` $\to$ found at $s[5]$ (`'l'`).
      - Pointer in $t$: looking for `'e'` $\to$ found at $s[6]$ (`'e'`).
      - All characters of $t$ matched! $t$ is a valid subsequence.
    - Compare with $ans = \text{""}$:
      - $|t| = 3 > |ans| = 0 \implies$ Update answer!
      - $ans \leftarrow \mathbf{\text{"ale"}}$
  - **Candidate 2: $t = \text{"apple"}$ (Length 5):**
    - Subsequence check $check(\text{"apple"}, \text{"abpcplea"})$:
      - Match `'a'` at $s[0]$ (`'a'`)
      - Match `'p'` at $s[2]$ (`'p'`)
      - Match `'p'` at $s[4]$ (`'p'`)
      - Match `'l'` at $s[5]$ (`'l'`)
      - Match `'e'` at $s[6]$ (`'e'`)
      - All 5 characters matched in order! Valid subsequence.
    - Compare with $ans = \text{"ale"}$ ($|ans| = 3$):
      - $|t| = 5 > |ans| = 3 \implies$ Strictly longer!
      - Update answer: $ans \leftarrow \mathbf{\text{"apple"}}$
  - **Candidate 3: $t = \text{"monkey"}$ (Length 6):**
    - Subsequence check $check(\text{"monkey"}, \text{"abpcplea"})$:
      - Looking for initial letter `'m'`.
      - Scan $s$: character `'m'` does not appear in $s$.
      - Subsequence check fails (`False`).
      - Discarded.
  - **Candidate 4: $t = \text{"plea"}$ (Length 4):**
    - Subsequence check: Matches `'p'`, `'l'`, `'e'`, `'a'` at indices $2, 5, 6, 7$ (`True`).
    - Compare with $ans = \text{"apple"}$ ($|ans| = 5$):
      - $|t| = 4 < |ans| = 5 \implies$ Shorter than current best.
      - Discarded.
  - Dictionary exhausted.
  - Optimal winning word: **`"apple"`**.
- **Lexicographical Tie-Breaking Instance ($dictionary = [\text{"a"}, \text{"b"}, \text{"c"}]$):**
  - All three words have length 1.
  - Alphabetical comparison: $\text{"a"} < \text{"b"} < \text{"c"}$.
  - Word `"a"` wins the tie $\implies \mathbf{\text{"a"}}$.
- **No Qualifying Word Instance ($s = \text{"xyz"}, dictionary = [\text{"abc"}, \text{"def"}]$):**
  - Returns empty string $\mathbf{\text{""}}$.

This instance demonstrates multi-criteria optimization under greedy character containment, mathematically proves why single-pass two-pointer checks verify subsequence invariants in $O(|s|)$ time, and derives $O(\sum |t| + |dictionary| \cdot |s|)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"abpcplea"}$ and an array of strings $dictionary$:
Return the **longest string** in $dictionary$ that can be formed by deleting characters from $s$.
If there are multiple results with the same maximum length, return the one that is **lexicographically smallest**.
If no word qualifies, return `""`.

```text
Source String: "abpcplea"

Testing Words:
  "ale":     a . . . . l e .  -> Valid (Length 3)
  "apple":   a . p . p l e .  -> Valid (Length 5)  <- Longest!
  "monkey":  'm' not in source -> Invalid
  "plea":    . . p . . l e a  -> Valid (Length 4)

Best Word: "apple"
```

### The Subsequence Equivalence
- "Formed by deleting characters from $s$ without reordering" is the formal definition of a **subsequence**.
- Hence, word $t$ is valid if and only if $t$ is a subsequence of $s$.
- Rather than modifying $s$ or generating substrings, we test whether each dictionary word $t$ is a subsequence of $s$ using a standard greedy **two-pointer sweep**.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Subsequence Checker:
Function $check(t, s) \to \text{bool}$:
- Let $i = 0$ track position in $t$, and $j = 0$ track position in $s$.
- While $i < |t|$ and $j < |s|$:
  - If $t[i] == s[j]$: advance $i \leftarrow i + 1$.
  - Advance $j \leftarrow j + 1$.
- Return $i == |t|$.

### 2. The Dual-Criteria Pareto Update Rule:
Initialize $ans = \text{""}$.
For each word $t \in dictionary$:
If $check(t, s)$ is `True`:
Update $ans \leftarrow t$ if:
$$
|t| > |ans| \quad \lor \quad (|t| == |ans| \land t < ans)
$$

> **Lexicographical Tie Invariant.** Evaluating $|t| > |ans| \lor (|t| == |ans| \land t < ans)$ guarantees that $ans$ always stores the unique optimal candidate under the lexicographical order-statistic hierarchy.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abpcplea"}$ with $dictionary = [\text{"ale"}, \text{"apple"}, \text{"monkey"}, \text{"plea"}]$:

---

### Step 1: Initialize
- $ans = \text{""}$.

---

### Step 2: Word `"ale"`
- Run $check(\text{"ale"}, \text{"abpcplea"})$:
  - Matches `'a'` at index 0
  - Matches `'l'` at index 5
  - Matches `'e'` at index 6
  - Returns `True`.
- Compare criteria:
  $$
  |\text{"ale"}| = 3 > |ans| = 0 \implies ans \leftarrow \mathbf{\text{"ale"}}
  $$

---

### Step 3: Word `"apple"`
- Run $check(\text{"apple"}, \text{"abpcplea"})$:
  - Matches `'a'` (idx 0), `'p'` (idx 2), `'p'` (idx 4), `'l'` (idx 5), `'e'` (idx 6).
  - Returns `True`.
- Compare criteria:
  $$
  |\text{"apple"}| = 5 > |\text{"ale"}| = 3 \implies ans \leftarrow \mathbf{\text{"apple"}}
  $$

---

### Step 4: Word `"monkey"`
- Run $check$: Letter `'m'` not found in $s \implies$ Returns `False`.
- Discarded.

---

### Step 5: Word `"plea"`
- Run $check$: Matches `'p'` (idx 2), `'l'` (idx 5), `'e'` (idx 6), `'a'` (idx 7) $\implies$ Returns `True`.
- Compare criteria:
  $$
  |\text{"plea"}| = 4 < |\text{"apple"}| = 5 \implies \text{Retain } ans = \mathbf{\text{"apple"}}
  $$

---

### Final Output:
$$
ans = \mathbf{\text{"apple"}}
$$

---

## 4. Complete Execution Trace

| Word $t$ | Is Subsequence of $s$? | Word Length $\lvert t \rvert$ | Current Best $ans$ | Update Condition Satisfied? | New Best $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **`"ale"`** | **True** | $3$ | `""` (Length 0) | Yes ($3 > 0$) | `"ale"` |
| **`"apple"`** | **True** | $5$ | `"ale"` (Length 3) | Yes ($5 > 3$) | **`"apple"`** |
| `"monkey"` | **False** | $6$ | `"apple"` (Length 5) | No (not a subsequence) | `"apple"` |
| `"plea"` | **True** | $4$ | `"apple"` (Length 5) | No ($4 < 5$) | `"apple"` |
| **Result** | — | — | — | — | **`"apple"`** |

---

## 5. Boundary Cases & Failure Modes

- **No Match Found ($s = \text{"a"}, dictionary = [\text{"b"}, \text{"c"}]$):** No word is a subsequence $\implies$ returns empty string $\mathbf{\text{""}}$.
- **Length Tie with Alphabetical Sorting ($[\text{"apply"}, \text{"apple"}]$):** Both length 5; `"apple" < \text{"apply"}` $\implies \mathbf{\text{"apple"}}$.
- **Dictionary Contains $s$ Itself:** Entire string matches $\implies$ returns $s$.
- **Source $s$ Contains Duplicate Characters:** Greedy two-pointer correctly matches the earliest available occurrences.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Subsequences of $s$ ($O(2^{|s|})$):** With $|s| = 1000$, generating power sets is impossible. Checking each dictionary word against $s$ takes only $O(|dictionary| \cdot |s|)$ time.
- **Sorting the Entire Dictionary First:** Sorting the dictionary by length descending and lexicographical ascending takes $O(K \log K \cdot L)$ extra time. Scanning once in-flight finds the minimum with zero sorting overhead.
- **Inverted String Comparison on Ties:** In Python, string comparison `t < ans` checks alphabetical precedence. Writing `ans < t` picks the lexicographically *largest* string, failing tie-breakers.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $K = |dictionary|$, $L$ be the average length of a dictionary word, and $M = |s|$.
  - For each of the $K$ words, the two-pointer check takes $O(L + M)$ time.
  - Updating $ans$ takes $O(L)$ time for string comparisons.
  - Total Time: $\mathcal{O}(K \cdot (M + L))$. For $K = 1000, M = 1000, L = 10$, $\approx 10^6$ operations, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space beyond storing the answer string.
