# Guided Example: Permutation in String

We trace the step-by-step fixed-size sliding window mechanism (window span $m = |s_1|$), character frequency delta accounting ($cnt$), unmet distinct character quota tracking ($need = |\text{distinct}(s_1)|$), window entry decrement and exit increment, and exact anagram discovery on representative string pairs:

- **Input:** $s_1 = \text{"ab"}, \quad s_2 = \text{"eidbaooo"}$
- **Required output:** `true`
  - Substring permutation contract: Return `true` if and only if there exists some substring of $s_2$ of length $m = |s_1| = 2$ that is an anagram of $s_1$ (i.e. identical multiset of characters).
- **Fixed-Size Sliding Window Trace:**
  - Let $m = |s_1| = 2$.
  - Character target frequency map from $s_1 = \text{"ab"}$:
    $$
    cnt = \{\text{'a'}: 1, \; \text{'b'}: 1\}
    $$
  - Track the number of distinct characters whose frequencies in the active window have not yet reached their exact required quota:
    $$
    need = 2 \quad (\text{both 'a' and 'b' unsatisfied})
    $$
  - When incoming character $c$ brings $cnt[c] = 0$, that character's requirement is perfectly satisfied $\implies need \leftarrow need - 1$.
  - When outgoing character leaves the window and causes $cnt[\text{out}] = 1$, that character becomes unsatisfied $\implies need \leftarrow need + 1$.
  - A valid permutation substring occurs whenever:
    $$
    need == 0
    $$
  - **Slide window through $s_2 = \text{"eidbaooo"}$:**
    - **Step 0 ($i = 0, \; c = \text{'e'}$):**
      - Incoming: `'e'`. $cnt[\text{'e'}] \leftarrow 0 - 1 = -1$.
      - $need = 2$.
    - **Step 1 ($i = 1, \; c = \text{'i'}$):**
      - Incoming: `'i'`. $cnt[\text{'i'}] \leftarrow -1$.
      - Active window $s_2[0 \dots 1] = \text{"ei"}$.
      - $need = 2$.
    - **Step 2 ($i = 2, \; c = \text{'d'}$):**
      - Incoming: `'d'`. $cnt[\text{'d'}] \leftarrow -1$.
      - Outgoing ($i \ge 2$, evict $s_2[0] = \text{'e'}$):
        - $cnt[\text{'e'}] \leftarrow -1 + 1 = 0$.
      - Active window $s_2[1 \dots 2] = \text{"id"}$.
      - $need = 2$.
    - **Step 3 ($i = 3, \; c = \text{'b'}$):**
      - Incoming: `'b'`. $cnt[\text{'b'}] \leftarrow 1 - 1 = \mathbf{0}$.
        - Frequency of `'b'` satisfied! $need \leftarrow 2 - 1 = \mathbf{1}$.
      - Outgoing (evict $s_2[1] = \text{'i'}$):
        - $cnt[\text{'i'}] \leftarrow -1 + 1 = 0$.
      - Active window $s_2[2 \dots 3] = \text{"db"}$.
      - $need = 1$.
    - **Step 4 ($i = 4, \; c = \text{'a'}$):**
      - Incoming: `'a'`. $cnt[\text{'a'}] \leftarrow 1 - 1 = \mathbf{0}$.
        - Frequency of `'a'` satisfied! $need \leftarrow 1 - 1 = \mathbf{0}$.
      - Outgoing (evict $s_2[2] = \text{'d'}$):
        - $cnt[\text{'d'}] \leftarrow -1 + 1 = 0$.
      - Active window $s_2[3 \dots 4] = \mathbf{\text{"ba"}}$.
      - Check satisfaction:
        $$
        need == 0 \implies \mathbf{True!}
        $$
      - Substring `"ba"` at indices $3 \dots 4$ is an exact permutation of `"ab"`!
      - Early return: **`true`**.
- **Dispersed Characters Failing Instance ($s_1 = \text{"ab"}, s_2 = \text{"eidboaoo"}$):**
  - `'b'` appears at index 3, but `'a'` is at index 5.
  - In every window of length 2, at least one character is missing $\implies need > 0$ throughout $\implies \mathbf{false}$.
- **Permutation at the Beginning ($s_1 = \text{"ab"}, s_2 = \text{"ab"}$):**
  - Satisfied at index $i = 1 \implies \mathbf{true}$.
- **$s_1$ Longer Than $s_2$ ($|s_1| > |s_2|$):**
  - Loop cannot form a full window of size $m \implies \mathbf{false}$.

This instance demonstrates fixed-span sliding window balance over multiset alphabets, mathematically proves why tracking non-zero deficit counts reduces state comparison from $O(|\Sigma|)$ to $O(1)$, and derives $O(N)$ runtime and $O(|\Sigma|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $s_1$ and $s_2$:
Determine if $s_2$ contains a substring that is a **permutation** of $s_1$.
Return `true` if a match exists, otherwise `false`.

```text
s1 = "ab" (length 2)
s2 = "e i d b a o o o"
            ^ ^
    Window [3..4] = "ba" is an anagram of "ab"!

Result: true
```

### From Full Map Comparisons to an $O(1)$ Deficit Counter
- Checking whether two frequency maps of size 26 match takes $O(26) = O(1)$ time, but comparing 26 values on every step adds constant-factor overhead.
- By tracking an integer `need`:
  - `need` equals the number of distinct characters in $s_1$ whose count in the current window is **not yet fully satisfied**.
  - When an incoming character hits count 0, `need` decrements.
  - When an outgoing character rises from 0 to 1, `need` increments.
- An anagram match is found the instant `need == 0`!

---

## 2. Conceptual Foundation & Invariants

### 1. Invariant of Fixed Window Size:
A permutation of $s_1$ must have length exactly equal to $m = |s_1|$.
The window $[i - m + 1 \dots i]$ in $s_2$ always maintains length $m$ once $i \ge m - 1$.

### 2. State Maintenance:
- Initialize `cnt = Counter(s1)`, `need = len(cnt)`.
- For each character $s_2[i]$:
  1. Add incoming $c = s_2[i]$:
     $$
     cnt[c] \leftarrow cnt[c] - 1
     $$
     If $cnt[c] == 0$: $need \leftarrow need - 1$.
  2. Evict outgoing $prev = s_2[i - m]$ (if $i \ge m$):
     $$
     cnt[prev] \leftarrow cnt[prev] + 1
     $$
     If $cnt[prev] == 1$: $need \leftarrow need + 1$.
  3. If $need == 0$: return `True`.

> **Zero Deficit Invariant.** The condition $need == 0$ in a window of size $|s_1|$ guarantees that every character in $s_1$ is present with its exact required multiplicity, and no extraneous characters are present.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"ab"}$ ($m = 2$), $s_2 = \text{"eidbaooo"}$:

---

### Step 1: Initialize
- $cnt = \{\text{'a'}: 1, \text{'b'}: 1\}$
- $need = 2, \; m = 2$

---

### Step 2: Slide Across $s_2$
- $i = 0$ (`'e'`): $cnt[\text{'e'}] = -1 \implies need = 2$.
- $i = 1$ (`'i'`): $cnt[\text{'i'}] = -1 \implies need = 2$.
- $i = 2$ (`'d'`):
  - In: `'d'` ($cnt = -1$).
  - Out: `'e'` ($cnt = 0$).
  - $need = 2$.
- $i = 3$ (`'b'`):
  - In: `'b'` $\implies cnt[\text{'b'}] = 0 \implies need \leftarrow 2 - 1 = \mathbf{1}$.
  - Out: `'i'` $\implies cnt[\text{'i'}] = 0$.
  - $need = 1$.
- $i = 4$ (`'a'`):
  - In: `'a'` $\implies cnt[\text{'a'}] = 0 \implies need \leftarrow 1 - 1 = \mathbf{0}$.
  - Out: `'d'` $\implies cnt[\text{'d'}] = 0$.
  - Check: $need == 0 \implies \mathbf{True}$!

---

### Step 3: Emit Output
Early exit returns **`True`**.

---

## 4. Complete Execution Trace

| Index $i$ | In Char | $cnt[\text{in}]$ After | Out Char ($i \ge 2$) | $cnt[\text{out}]$ After | Active Window | $need$ Value | Match Found? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'e'` | $-1$ | None | — | `"e"` | $2$ | No |
| $1$ | `'i'` | $-1$ | None | — | `"ei"` | $2$ | No |
| $2$ | `'d'` | $-1$ | `'e'` | $0$ | `"id"` | $2$ | No |
| $3$ | `'b'` | **$0$** | `'i'` | $0$ | `"db"` | $1$ | No |
| **$4$** | **`'a'`** | **$0$** | `'d'` | $0$ | **`"ba"`** | **`0`** | **Yes (`True`)** |

---

## 5. Boundary Cases & Failure Modes

- **$|s_1| > |s_2|$:** Window of size $m$ cannot be formed; loop completes without finding a match $\implies \mathbf{false}$.
- **Single Character Strings ($s_1 = \text{"a"}, s_2 = \text{"a"}$):** Matches on step 0 $\implies \mathbf{true}$.
- **All Identical Letters ($s_1 = \text{"aa"}, s_2 = \text{"aaa"}$):** Matches at index 1 $\implies \mathbf{true}$.
- **Anagram at the Very End ($s_1 = \text{"ab"}, s_2 = \text{"xyzab"}$):** Window arrives at end and satisfies $need == 0$.

---

## 6. Traps & Common Anti-Patterns

- **Sorting Each Substring ($O(N \cdot M \log M)$):** Sorting the window on every slide produces sluggish quadratic time. Incrementing/decrementing frequency counts executes in strictly $O(1)$ time per slide.
- **Evicting at Wrong Index:** Outgoing character is at index $i - m$, not $i - m + 1$. An off-by-one error distorts window width.
- **Checking `sum(cnt.values()) == 0`:** Negative frequencies for unexpected letters cancel positive deficits. Using the distinct satisfied counter `need` prevents false positive cancellations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial frequency counting of $s_1$: $\mathcal{O}(M)$ where $M = |s_1|$.
  - Sliding through $s_2$ takes $N = |s_2|$ steps.
  - Each step performs two dictionary updates and integer checks in $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(M + N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|\Sigma|)$ space for the frequency counter where $|\Sigma| \le 26$ lowercase English letters.