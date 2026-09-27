# Guided Example: Find All Anagrams in a String

We trace the step-by-step fixed-size sliding window frequency histogramming, multiset character matching ($cnt_1 == cnt_2$), leading-character contraction, and start-index extraction on representative text strings:

- **Input:** $s = \text{"cbaebabacd"}, \quad p = \text{"abc"}$
- **Required output:** `[0, 6]`
  - Window size: $K = |p| = 3$
  - Target frequency profile ($p = \text{"abc"}$):
    $$
    cnt_p = \{a: 1, \; b: 1, \; c: 1\}
    $$
  - Window step-by-step execution:
    - **Window $[0 \dots 2]$ (`"cba"`):**
      - Frequencies: $\{a: 1, b: 1, c: 1\}$
      - Matches $cnt_p$ identically $\implies$ **Record start index $0$**
    - **Slide to $[1 \dots 3]$ (`"bae"`):**
      - Remove $s[0]$ (`'c'`), add $s[3]$ (`'e'`) $\implies \{a: 1, b: 1, e: 1\}$ (Mismatch)
    - **Slide to $[2 \dots 4]$ (`"aeb"`):**
      - Remove $s[1]$ (`'b'`), add $s[4]$ (`'b'`) $\implies \{a: 1, b: 1, e: 1\}$ (Mismatch)
    - **Slide to $[3 \dots 5]$ (`"eba"`):**
      - Remove $s[2]$ (`'a'`), add $s[5]$ (`'a'`) $\implies \{a: 1, b: 1, e: 1\}$ (Mismatch)
    - **Slide to $[4 \dots 6]$ (`"bab"`):**
      - Remove $s[3]$ (`'e'`), add $s[6]$ (`'b'`) $\implies \{a: 1, b: 2\}$ (Mismatch)
    - **Slide to $[5 \dots 7]$ (`"aba"`):**
      - Remove $s[4]$ (`'b'`), add $s[7]$ (`'a'`) $\implies \{a: 2, b: 1\}$ (Mismatch)
    - **Slide to $[6 \dots 8]$ (`"bac"`):**
      - Remove $s[5]$ (`'a'`), add $s[8]$ (`'c'`) $\implies \{a: 1, b: 1, c: 1\}$
      - Matches $cnt_p$ identically $\implies$ **Record start index $6$**
    - **Slide to $[7 \dots 9]$ (`"acd"`):**
      - Remove $s[6]$ (`'b'`), add $s[9]$ (`'d'`) $\implies \{a: 1, c: 1, d: 1\}$ (Mismatch)
  - Result: `[0, 6]`
- **Overlapping Anagrams Instance:** $s = \text{"abab"}, p = \text{"ab"} \implies$ Windows `"ab"`, `"ba"`, `"ab"` $\implies \mathbf{[0, 1, 2]}$
- **Source Shorter Than Pattern ($|s| < |p|$):** Window cannot be formed $\implies \mathbf{[]}$

This instance demonstrates fixed-length sliding window character multiset comparison, mathematically proves why updating boundary counts in $O(1)$ preserves multiset equivalence without re-hashing, and derives $O(|s| \cdot |\Sigma|)$ runtime and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $s = \text{"cbaebabacd"}$ and $p = \text{"abc"}$:
Find all the start indices of $p$'s **anagrams** in $s$.
An anagram of a string is another string that contains the exact same characters with the exact same frequencies in any order.

```text
Target Pattern: p = "abc" -> Required Counts: {a: 1, b: 1, c: 1} (Length 3)
Source String:  s = "cbaebabacd"

Slide window of length 3 across s:
  Index 0: "cba" -> {a: 1, b: 1, c: 1}  (Match -> Record 0)
  Index 1: "bae" -> {a: 1, b: 1, e: 1}
  Index 2: "aeb" -> {a: 1, b: 1, e: 1}
  Index 3: "eba" -> {a: 1, b: 1, e: 1}
  Index 4: "bab" -> {a: 1, b: 2}
  Index 5: "aba" -> {a: 2, b: 1}
  Index 6: "bac" -> {a: 1, b: 1, c: 1}  (Match -> Record 6)
  Index 7: "acd" -> {a: 1, c: 1, d: 1}

Output Indices: [0, 6]
```

### The Fixed-Width Window Invariant
Because an anagram of $p$ must contain exactly $|p|$ characters:
- Every valid anagram candidate in $s$ corresponds to a contiguous substring $s[l \dots r]$ of fixed width:
  $$
  W = r - l + 1 = |p|
  $$
- Two strings of equal length are anagrams if and only if their character frequency distributions are identical:
  $$
  cnt(s[l \dots r]) == cnt(p)
  $$
- Moving the window from $[l, r]$ to $[l+1, r+1]$ requires updating only two character frequencies:
  - Increment the incoming character: $cnt[s[r+1]] \leftarrow cnt[s[r+1]] + 1$
  - Decrement the outgoing character: $cnt[s[l]] \leftarrow cnt[s[l]] - 1$

---

## 2. Conceptual Foundation & Invariants

### 1. Rolling Histogram State:
Let $cnt_1$ be the immutable frequency map of pattern $p$.
Let $cnt_2$ be the rolling frequency map of the current window in $s$.
- Initial window: populate $cnt_2$ with the first $|p| - 1$ characters of $s$.
- For each step $i \in [|p| - 1, |s| - 1]$:
  1. Add incoming character: $cnt_2[s[i]] \leftarrow cnt_2[s[i]] + 1$.
  2. Test equality: if $cnt_1 == cnt_2$, append the window start index $i - |p| + 1$ to $ans$.
  3. Remove outgoing character: $cnt_2[s[i - |p| + 1]] \leftarrow cnt_2[s[i - |p| + 1]] - 1$.

### 2. Frequency Equivalence Invariant:
Comparing two frequency maps over an alphabet of size $|\Sigma| = 26$ requires checking at most 26 counts.
$$
cnt_1 == cnt_2 \iff cnt_1[c] == cnt_2[c] \quad \forall c \in \{\text{'a'} \dots \text{'z'}\}
$$
Because $|\Sigma|$ is constant, each comparison executes in strictly $O(1)$ time.

> **Sliding Invariant.** At the moment of equality comparison at index $i$, the histogram $cnt_2$ accurately represents the exact character multiplicity of the substring $s[i - |p| + 1 \dots i]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"cbaebabacd"}$ with $p = \text{"abc"}$ ($|p| = 3, |s| = 10$):
Target: $cnt_1 = \{a: 1, b: 1, c: 1\}$.
Pre-seed $cnt_2$ with $s[0 \dots 1] = \text{"cb"}: \{c: 1, b: 1\}$.

---

### Step 1: $i = 2, s[2] = \text{'a'}$
- Add $s[2]$: $cnt_2[a] \leftarrow 1 \implies cnt_2 = \{c: 1, b: 1, a: 1\}$.
- Compare: $cnt_1 == cnt_2$ (**True!**).
- Record start index: $i - |p| + 1 = 2 - 3 + 1 = \mathbf{0}$.
- Remove outgoing $s[0]$ (`'c'`): $cnt_2[c] \leftarrow 0$. Window shifts to $[1, 2]$.

---

### Step 2: $i = 3, s[3] = \text{'e'}$
- Add $s[3]$: $cnt_2[e] \leftarrow 1 \implies cnt_2 = \{b: 1, a: 1, e: 1\}$.
- Compare: $cnt_1 \ne cnt_2$ (contains $'e'$, missing $'c'$).
- Remove outgoing $s[1]$ (`'b'`): $cnt_2[b] \leftarrow 0$. Window shifts to $[2, 3]$.

---

### Step 3: $i = 4, s[4] = \text{'b'}$
- Add $s[4]$: $cnt_2[b] \leftarrow 1 \implies cnt_2 = \{a: 1, e: 1, b: 1\}$.
- Compare: $cnt_1 \ne cnt_2$ (Mismatch).
- Remove outgoing $s[2]$ (`'a'`): $cnt_2[a] \leftarrow 0$. Window shifts to $[3, 4]$.

---

### Step 4: $i = 5, s[5] = \text{'a'}$
- Add $s[5]$: $cnt_2[a] \leftarrow 1 \implies cnt_2 = \{e: 1, b: 1, a: 1\}$.
- Compare: $cnt_1 \ne cnt_2$ (Mismatch).
- Remove outgoing $s[3]$ (`'e'`): $cnt_2[e] \leftarrow 0$. Window shifts to $[4, 5]$.

---

### Step 5: $i = 6, s[6] = \text{'b'}$
- Add $s[6]$: $cnt_2[b] \leftarrow 2 \implies cnt_2 = \{b: 2, a: 1\}$.
- Compare: $cnt_1 \ne cnt_2$ (Mismatch).
- Remove outgoing $s[4]$ (`'b'`): $cnt_2[b] \leftarrow 1$. Window shifts to $[5, 6]$.

---

### Step 6: $i = 7, s[7] = \text{'a'}$
- Add $s[7]$: $cnt_2[a] \leftarrow 2 \implies cnt_2 = \{b: 1, a: 2\}$.
- Compare: $cnt_1 \ne cnt_2$ (Mismatch).
- Remove outgoing $s[5]$ (`'a'`): $cnt_2[a] \leftarrow 1$. Window shifts to $[6, 7]$.

---

### Step 7: $i = 8, s[8] = \text{'c'}$
- Add $s[8]$: $cnt_2[c] \leftarrow 1 \implies cnt_2 = \{b: 1, a: 1, c: 1\}$.
- Compare: $cnt_1 == cnt_2$ (**True!**).
- Record start index: $i - |p| + 1 = 8 - 3 + 1 = \mathbf{6}$.
- Remove outgoing $s[6]$ (`'b'`): $cnt_2[b] \leftarrow 0$. Window shifts to $[7, 8]$.

---

### Step 8: $i = 9, s[9] = \text{'d'}$
- Add $s[9]$: $cnt_2[d] \leftarrow 1 \implies cnt_2 = \{a: 1, c: 1, d: 1\}$.
- Compare: $cnt_1 \ne cnt_2$ (Mismatch).
- Remove outgoing $s[7]$ (`'a'`): $cnt_2[a] \leftarrow 0$.
- Scan finishes.

---

### Final Result:
Recorded indices: **`[0, 6]`**.

---

## 4. Complete Execution Trace

| Right $i$ | Added Char | Active Window Substring | Window Multiset $cnt_2$ | Target Match? | Window Start $i - |p| + 1$ | Removed Char |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| **$2$** | `'a'` | `"cba"` | $\{a: 1, b: 1, c: 1\}$ | **Yes** | **$0$ Recorded** | `'c'` |
| **$3$** | `'e'` | `"bae"` | $\{a: 1, b: 1, e: 1\}$ | No | — | `'b'` |
| **$4$** | `'b'` | `"aeb"` | $\{a: 1, b: 1, e: 1\}$ | No | — | `'a'` |
| **$5$** | `'a'` | `"eba"` | $\{a: 1, b: 1, e: 1\}$ | No | — | `'e'` |
| **$6$** | `'b'` | `"bab"` | $\{a: 1, b: 2\}$ | No | — | `'b'` |
| **$7$** | `'a'` | `"aba"` | $\{a: 2, b: 1\}$ | No | — | `'a'` |
| **$8$** | `'c'` | `"bac"` | $\{a: 1, b: 1, c: 1\}$ | **Yes** | **$6$ Recorded** | `'b'` |
| **$9$** | `'d'` | `"acd"` | $\{a: 1, c: 1, d: 1\}$ | No | — | `'a'` |

---

## 5. Boundary Cases & Failure Modes

- **Pattern Longer than String ($|s| < |p|$):** Window cannot be formed. Returns `[]` immediately without initiating loop.
- **Identical Strings ($s = \text{"abc"}, p = \text{"abc"}):$** Single evaluation at $i = 2$ matches $\implies [0]$.
- **Repeated Character Pattern ($s = \text{"aaaa"}, p = \text{"aa"}):$** Windows $[0\dots 1]$, $[1\dots 2]$, and $[2\dots 3]$ all contain two `'a'`s $\implies [0, 1, 2]$.
- **Disjoint Character Sets ($s = \text{"abcdef"}, p = \text{"xyz"}):$** No window matches $\implies []$.

---

## 6. Traps & Common Anti-Patterns

- **Sorting Every Substring ($O(|s| \cdot |p| \log |p|)$):** Extracting each substring and sorting characters takes excessive time for $|s| = 3 \times 10^4$. A rolling histogram avoids sorting completely.
- **Not Cleaning Zero Counts in Dictionaries:** In Python, leaving keys with count `0` in a `Counter` can cause `cnt1 == cnt2` to return `False` if one dictionary contains `{'c': 0}` and the other omits `'c'`. Using fixed-size 26-element integer arrays or deleting zero keys avoids dictionary inequality bugs.
- **Off-By-One in Start Index:** The start index of a window ending at $i$ is $i - |p| + 1$. Miscalculating this by $\pm 1$ shifts all emitted indices.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initializing $cnt_p$ and the first window takes $O(|p|)$ time.
  - The window slides across $s$ in $|s| - |p| + 1$ steps.
  - At each step, updating two counts takes $O(1)$ time, and comparing the 26 alphabet frequencies takes $O(|\Sigma|) = 26 = O(1)$ time.
  - Total Time: $\mathcal{O}(|s| \cdot |\Sigma|) = \mathcal{O}(|s|)$. For $|s| = 3 \times 10^4$, completes in under 10 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|) = \mathcal{O}(1)$ space to store the frequency arrays for the 26 lowercase English letters.