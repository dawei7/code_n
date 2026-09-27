# Guided Example: Is Subsequence

We trace the step-by-step two-pointer greedy alignment ($i$ on $s$, $j$ on $t$), earliest-match greedy optimality proof, suffix search space preservation, and incoming stream inverted index precomputation on representative string instances:

- **Input:** $s = \text{"abc"}, \quad t = \text{"ahbgdc"}$
- **Required output:** `true`
  - Two-pointer alignment trace:
    - Step 1: $s[0] = \text{'a'}, t[0] = \text{'a'} \implies$ Match! $i = 1, j = 1$
    - Step 2: $s[1] = \text{'b'}, t[1] = \text{'h'} \implies$ Mismatch, advance $j = 2$
    - Step 3: $s[1] = \text{'b'}, t[2] = \text{'b'} \implies$ Match! $i = 2, j = 3$
    - Step 4: $s[2] = \text{'c'}, t[3] = \text{'g'} \implies$ Mismatch, advance $j = 4$
    - Step 5: $s[2] = \text{'c'}, t[4] = \text{'d'} \implies$ Mismatch, advance $j = 5$
    - Step 6: $s[2] = \text{'c'}, t[5] = \text{'c'} \implies$ Match! $i = 3, j = 6$
  - String $s$ fully matched ($i = \text{len}(s) = 3$) $\implies$ Return `true`
- **Missing Character Failure:** $s = \text{"axc"}, t = \text{"ahbgdc"}$
  - Matches `'a'` at $j = 0$; searches for `'x'` in remaining suffix `"hbgdc"`
  - Character `'x'` is never found; pointer $j$ hits end of $t$ with $i = 1 < 3 \implies \text{false}$
- **Empty Subsequence Base Case:** $s = \text{""}, t = \text{"abc"} \implies i = 0 == \text{len}(s) \implies \text{true}$

This instance demonstrates greedy choice optimality in sequential sequence embedding, mathematically proves why matching the earliest available instance leaves the maximal suffix for remaining characters, and analyzes $O(|t|)$ linear scan vs $O(|s| \log |t|)$ binary search indexing for mass queries.

---

## 1. Instance & Teaching Goal

Given two strings $s = \text{"abc"}$ and $t = \text{"ahbgdc"}$:
Check whether $s$ is a **subsequence** of $t$ (can be formed by deleting 0 or more characters from $t$ without disturbing the relative order of remaining characters):

```text
String s:   a       b       c
            |       |       |
String t: [ a,  h,  b,  g,  d,  c ]
Indices:    0   1   2   3   4   5

Selected Indices in t: 0 < 2 < 5 (Strictly Increasing!)
Output: true
```

### The Greedy Earliest-Match Theorem
When looking for $s[i]$ in $t$, should we take the first matching occurrence of $s[i]$ or wait for a later one?
**Theorem:** Greedily picking the **earliest** matching occurrence is always optimal.
*Proof:* Suppose there is a valid subsequence embedding that matches $s[i]$ at a later index $t[j_2]$ ($j_2 > j_1$). If we instead match $s[i]$ at $t[j_1]$, all subsequent characters $s[i+1 \dots]$ must be found in $t[j_1 + 1 \dots |t|-1]$. Since $j_1 < j_2$, the remaining suffix $t[j_1 + 1 \dots]$ is a strict superset of $t[j_2 + 1 \dots]$. Therefore, any valid embedding using $j_2$ can also use $j_1$ without losing any feasible solutions.

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Configuration:
- `i = 0`: Points to the current character in $s$ that needs to be matched.
- `j = 0`: Points to the current character in $t$ being inspected.

### 2. State Transition Rules:
While $i < |s|$ and $j < |t|$:
- If $s[i] == t[j]$:
  Greedily consume $s[i]$:
  $$
  i \leftarrow i + 1
  $$
- Always advance through $t$:
  $$
  j \leftarrow j + 1
  $$

### 3. Termination Condition:
Return `True` if and only if all characters in $s$ were matched:
$$
i == \text{len}(s)
$$

> **Invariant.** At any step, the prefix $s[0 \dots i - 1]$ has been successfully embedded into the prefix $t[0 \dots j - 1]$ in strictly increasing index order.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abc"}, t = \text{"ahbgdc"}$:
Initial: $i = 0, j = 0$.

---

### Step 1: Inspect $s[0] = \text{'a'}, t[0] = \text{'a'}$
- Compare: $s[0] == t[0]$ is **True**.
- Advance both pointers:
  $$
  i \leftarrow 0 + 1 = \mathbf{1}, \quad j \leftarrow 0 + 1 = \mathbf{1}
  $$
- State: $s[0]$ matched at $t[0]$.

---

### Step 2: Inspect $s[1] = \text{'b'}, t[1] = \text{'h'}$
- Compare: $s[1] \ne t[1]$ (`'b' != 'h'`).
- Skip non-matching character in $t$:
  $$
  i \text{ remains } 1, \quad j \leftarrow 1 + 1 = \mathbf{2}
  $$

---

### Step 3: Inspect $s[1] = \text{'b'}, t[2] = \text{'b'}$
- Compare: $s[1] == t[2]$ is **True**.
- Advance both pointers:
  $$
  i \leftarrow 1 + 1 = \mathbf{2}, \quad j \leftarrow 2 + 1 = \mathbf{3}
  $$
- State: $s[1]$ matched at $t[2]$.

---

### Step 4: Inspect $s[2] = \text{'c'}, t[3] = \text{'g'}$
- Compare: `'c' != 'g'`.
- Skip $t[3]$:
  $$
  i = 2, \quad j \leftarrow 3 + 1 = \mathbf{4}
  $$

---

### Step 5: Inspect $s[2] = \text{'c'}, t[4] = \text{'d'}$
- Compare: `'c' != 'd'`.
- Skip $t[4]$:
  $$
  i = 2, \quad j \leftarrow 4 + 1 = \mathbf{5}
  $$

---

### Step 6: Inspect $s[2] = \text{'c'}, t[5] = \text{'c'}$
- Compare: $s[2] == t[5]$ is **True**.
- Advance both pointers:
  $$
  i \leftarrow 2 + 1 = \mathbf{3}, \quad j \leftarrow 5 + 1 = \mathbf{6}
  $$
- State: all 3 characters of $s$ matched!

---

### Step 7: Termination & Evaluation
$i = 3 == \text{len}(s)$. Loop terminates.
Return:
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
s = "abc", t = "ahbgdc"

j=0, t[0]='a', s[0]='a' -> MATCH -> i=1, j=1
j=1, t[1]='h', s[1]='b' -> skip  -> i=1, j=2
j=2, t[2]='b', s[1]='b' -> MATCH -> i=2, j=3
j=3, t[3]='g', s[2]='c' -> skip  -> i=2, j=4
j=4, t[4]='d', s[2]='c' -> skip  -> i=2, j=5
j=5, t[5]='c', s[2]='c' -> MATCH -> i=3, j=6

Loop ends (i == len(s) == 3) -> Return True
```

| Step | Target Char $s[i]$ | Host Char $t[j]$ | Pointer Indices $(i, j)$ | Match Result | Action Taken | Next State $(i, j)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `'a'` | `'a'` | $(0, 0)$ | **Match** | $i \mathrel{+}= 1, j \mathrel{+}= 1$ | $(1, 1)$ |
| 2 | `'b'` | `'h'` | $(1, 1)$ | Mismatch | $j \mathrel{+}= 1$ | $(1, 2)$ |
| 3 | `'b'` | `'b'` | $(1, 2)$ | **Match** | $i \mathrel{+}= 1, j \mathrel{+}= 1$ | $(2, 3)$ |
| 4 | `'c'` | `'g'` | $(2, 3)$ | Mismatch | $j \mathrel{+}= 1$ | $(2, 4)$ |
| 5 | `'c'` | `'d'` | $(2, 4)$ | Mismatch | $j \mathrel{+}= 1$ | $(2, 5)$ |
| **6** | **'c'** | **'c'** | **$(2, 5)$** | **Match** | **$i \mathrel{+}= 1, j \mathrel{+}= 1$** | **$(3, 6)$** |
| **Exit**| - | - | $(3, 6)$ | Complete | $i == \text{len}(s)$ | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because $j$ only moves forward ($j \leftarrow j + 1$), the indices in $t$ corresponding to matches with $s[0], s[1], \dots, s[k]$ are strictly increasing: $j_0 < j_1 < \dots < j_{|s|-1}$. This satisfies the definition of a subsequence.

**Completeness.** By the Greedy Earliest-Match Theorem, if any subsequence embedding exists, the greedy choice will find one. If the algorithm fails to advance $i$ to $|s|$ before $j$ reaches $|t|$, then no valid embedding exists in the entire string $t$.

---

## 6. Traps This Instance Exposes

- **Character Count Fallacy:** Testing whether $t$ contains all characters of $s$ using sets or count maps ignores order (e.g. $s = \text{"ba"}, t = \text{"ab"}$ has identical counts but is NOT a subsequence).
- **Early Exit Optimization:** As soon as $i == \text{len}(s)$, all characters have been matched. Adding an early break `if i == len(s): return True` avoids scanning the rest of $t$ when $s$ matches early.
- **Mass Queries Follow-Up ($10^9$ Queries):**
  If checking millions of strings against the same $t$:
  Preprocess $t$ into an inverted index `pos[c] = [indices of c in t]`.
  For each character in query $s_k$, find the next index $> prev$ using binary search (`bisect_right`).
  This answers each query in $O(|s| \log |t|)$ time without re-scanning $t$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$, where $T = \text{len}(t)$ (with $S = \text{len}(s) \le T$).
  - Pointer $j$ increments exactly once per iteration, visiting at most $T$ characters.
  - Each step does $O(1)$ constant-time character comparison.
  - Overall time is strictly linear $O(T)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only two integer indices `i` and `j`.
