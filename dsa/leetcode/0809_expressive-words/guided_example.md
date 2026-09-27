# Guided Example: Expressive Words

We trace the step-by-step run-length encoding (RLE) block decomposition, character identity matching ($s[i] == t[j]$), group length extension constraints ($c_1 \ge c_2$), minimum stretchy group size threshold ($c_1 \ge 3 \lor c_1 == c_2$), group-by-group validation, and stretchy vocabulary word counting on representative string sets:

- **Input:**
  $$
  s = \text{"heeellooo"}
  $$
  $$
  words = [\text{"hello"}, \; \text{"hi"}, \; \text{"helo"}]
  $$
- **Required output:** `1`
  - Stretchy word extension rules:
    - In string $s$, people express excitement by stretching groups of identical adjacent characters.
    - A query word $t$ can be stretched into $s$ if for each group of identical adjacent characters with length $c_2$ in $t$ and corresponding length $c_1$ in $s$:
      1. Both groups share the **same character**.
      2. $c_1 \ge c_2$ (characters can be added to $t$, never removed).
      3. The resulting group length in $s$ must be **at least 3** ($c_1 \ge 3$), **OR** the groups were already equal ($c_1 == c_2$).
      *(You cannot stretch a group of length 1 to length 2, because a stretchy group must have size $\ge 3$)*.
    - For $s = \text{"heeellooo"}$:
      - Run-length decomposition of $s$:
        $$
        (\text{'h'}, 1), \; (\text{'e'}, 3), \; (\text{'l'}, 2), \; (\text{'o'}, 3)
        $$
      - Candidate 1: `"hello"` $\to (\text{'h'}, 1), (\text{'e'}, 1), (\text{'l'}, 2), (\text{'o'}, 1)$:
        - `'h'`: $1 == 1$ (Match).
        - `'e'`: $1 \to 3$ ($c_1 = 3 \ge 3$) (Valid stretch).
        - `'l'`: $2 == 2$ (Match).
        - `'o'`: $1 \to 3$ ($c_1 = 3 \ge 3$) (Valid stretch).
        - **"hello" is Stretchy!**
      - Candidate 2: `"hi"`:
        - Contains `'i'` where $s$ has `'e'` $\implies$ Character mismatch.
      - Candidate 3: `"helo"` $\to (\text{'h'}, 1), (\text{'e'}, 1), (\text{'l'}, 1), (\text{'o'}, 1)$:
        - `'l'` in $t$ has length 1, but in $s$ has length 2.
        - $c_1 = 2 < 3$ and $c_1 \ne c_2 \implies$ **Illegal stretch** (resulting size must be $\ge 3$).
      - Total valid stretchy words: **1**.
- **Run-Length Invariant & Group Sizing Criteria:**
  - **Sequential Group Tracking ($i, j$):**
    - Align two pointers $i$ in $s$ and $j$ in $t$:
      1. **Character Equality:** If $s[i] \ne t[j]$, return `false`.
      2. **Measure Run Length in $s$ ($c_1$):** Advance pointer $k_1$ until $s[k_1] \ne s[i]$:
         $$
         c_1 = k_1 - i
         $$
      3. **Measure Run Length in $t$ ($c_2$):** Advance pointer $k_2$ until $t[k_2] \ne t[j]$:
         $$
         c_2 = k_2 - j
         $$
      4. **Stretch Feasibility Predicate:**
         - If $c_1 < c_2$: Cannot shrink characters $\implies$ return `false`.
         - If $c_1 < 3$ and $c_1 \ne c_2$: Stretched group has size $< 3 \implies$ return `false`.
      5. Advance both pointers to the start of their next groups: $i \leftarrow k_1, j \leftarrow k_2$.
    - Return `true` if and only if both strings are exhausted simultaneously ($i == |s| \land j == |t|$).
- **Step-by-Step Worked Execution Trace on Candidate `"hello"` vs `"heeellooo"`:**
  - Master $s = \text{"heeellooo"}$ ($m = 9$).
  - Candidate $t = \text{"hello"}$ ($n = 5$).
  - Initialize pointers: $i = 0, j = 0$.
  - **Group 1 (Character `'h'`):**
    - $s[0] == t[0] == \text{'h'}$.
    - Length in $s$: $c_1 = 1$.
    - Length in $t$: $c_2 = 1$.
    - Sizing check: $c_1 == c_2 = 1 \implies \mathbf{Valid.}$
    - Advance: $i = 1, j = 1$.
  - **Group 2 (Character `'e'`):**
    - $s[1] == t[1] == \text{'e'}$.
    - Count in $s$: indices $1, 2, 3$ are `'e'` $\implies c_1 = 3$.
    - Count in $t$: index $1$ is `'e'` $\implies c_2 = 1$.
    - Sizing check:
      $$
      c_1 \ge c_2 \quad (3 \ge 1) \quad \text{and} \quad c_1 \ge 3 \quad (3 \ge 3) \implies \mathbf{Valid\ Stretch!}
      $$
    - Advance: $i = 4, j = 2$.
  - **Group 3 (Character `'l'`):**
    - $s[4] == t[2] == \text{'l'}$.
    - Count in $s$: indices $4, 5$ are `'l'` $\implies c_1 = 2$.
    - Count in $t$: indices $2, 3$ are `'l'` $\implies c_2 = 2$.
    - Sizing check: $c_1 == c_2 = 2 \implies \mathbf{Valid.}$
    - Advance: $i = 6, j = 4$.
  - **Group 4 (Character `'o'`):**
    - $s[6] == t[4] == \text{'o'}$.
    - Count in $s$: indices $6, 7, 8$ are `'o'` $\implies c_1 = 3$.
    - Count in $t$: index $4$ is `'o'` $\implies c_2 = 1$.
    - Sizing check: $c_1 \ge c_2$ ($3 \ge 1$) and $c_1 \ge 3$ ($3 \ge 3$) $\implies \mathbf{Valid\ Stretch!}$
    - Advance: $i = 9, j = 5$.
  - **Termination:**
    - Both strings simultaneously exhausted: $i == 9 == m$ and $j == 5 == n$.
    - `"hello"` is certified as **stretchy**!
- **Step-by-Step Worked Execution Trace on Candidate `"helo"`:**
  - Group 1 (`'h'`): $1 == 1 \implies$ Valid.
  - Group 2 (`'e'`): $1 \to 3 \implies$ Valid stretch ($c_1 = 3$).
  - Group 3 (`'l'`):
    - $s$ has 2 `'l'`s ($c_1 = 2$).
    - $t$ has 1 `'l'` ($c_2 = 1$).
    - Test sizing rule:
      $$
      c_1 < 3 \quad (2 < 3) \quad \text{and} \quad c_1 \ne c_2 \quad (2 \ne 1) \implies \mathbf{Illegal\ Stretch!}
      $$
    - Cannot stretch a single letter to a pair of 2 letters!
    - Return `false`.
- **All-Stretchy Words Trace ($s = \text{"zzzzzyyyyy"}$):**
  - Group sizes in $s$: `'z': 5, 'y': 5`.
  - Both groups have $c_1 \ge 3$.
  - Any candidate word with sequence `z...y...` having $1 \le c_2 \le 5$ is stretchy.
  - Candidates `"zzyy"`, `"zy"`, `"zyy"` all qualify $\implies ans = \mathbf{3}$.

This instance demonstrates run-length encoding factoring of formal languages and regular relation parsing under length-dilation constraints, mathematically proves why local block inequalities characterize inverse string dilation morphisms, and derives $O(|s| + \sum |w_i|)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given master string $s$ and a list of candidate $words$:
Count how many words can stretch into $s$ by extending character groups to size $\ge 3$.

```text
s = "heeellooo" -> RLE: [ ('h', 1), ('e', 3), ('l', 2), ('o', 3) ]

Candidates:
  "hello" -> [ ('h', 1), ('e', 1), ('l', 2), ('o', 1) ]
             'e': 1 -> 3 (size >= 3 -> OK)
             'o': 1 -> 3 (size >= 3 -> OK)
             Valid!

  "helo"  -> [ ('h', 1), ('e', 1), ('l', 1), ('o', 1) ]
             'l': 1 -> 2 (size < 3 -> INVALID!)

Result: 1
```

### The Invariant of the 3-Threshold Stretch
- Characters cannot be removed ($c_1 \ge c_2$).
- If group sizes differ ($c_1 \ne c_2$), the master string group MUST have size $\ge 3$.
- Stretches to size 2 are strictly forbidden.

---

## 2. Conceptual Foundation & Invariants

### 1. Run-Length Encoding Blocks:
$$
\text{RLE}(w) = [(char_1, c_1), \; (char_2, c_2), \; \dots]
$$

### 2. Group Compatibility Predicate:
For corresponding blocks $(char_s, c_1)$ and $(char_t, c_2)$:
$$
char_s == char_t \;\land\; c_1 \ge c_2 \;\land\; (c_1 == c_2 \;\lor\; c_1 \ge 3)
$$

> **Dilation Monoid Invariant.** Let $\mathcal{R}: \Sigma^* \to (\Sigma \times \mathbb{N})^*$ be the run-length projection. The dilation relation $u \sqsubseteq v$ is a partial order on words having identical character skeletons $\pi_1(\mathcal{R}(u)) = \pi_1(\mathcal{R}(v))$, characterized by component-wise integer dilation satisfying $c_1 \ge c_2$ and $c_1 \notin \{1, 2\} \setminus \{c_2\}$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"heeellooo"}, t = \text{"hello"}$:

---

### Step 1: `'h'`
- $c_1 = 1, c_2 = 1 \implies 1 == 1 \implies$ Valid.

---

### Step 2: `'e'`
- $c_1 = 3, c_2 = 1 \implies 3 \ge 1$ and $3 \ge 3 \implies$ Valid.

---

### Step 3: `'l'`
- $c_1 = 2, c_2 = 2 \implies 2 == 2 \implies$ Valid.

---

### Step 4: `'o'`
- $c_1 = 3, c_2 = 1 \implies 3 \ge 1$ and $3 \ge 3 \implies$ Valid.

---

### Step 5: Output
- Valid! Total count: **`1`**.

---

## 4. Complete Execution Trace

| Block | Character | Master Length $c_1$ | Word Length $c_2$ | Length Check ($c_1 \ge c_2$) | Size $\ge 3$ or Equal? | Compatible? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'h'` | $1$ | $1$ | $1 \ge 1$ | $1 == 1$ | Yes |
| $2$ | `'e'` | $3$ | $1$ | $3 \ge 1$ | $3 \ge 3$ | Yes |
| $3$ | `'l'` | $2$ | $2$ | $2 \ge 2$ | $2 == 2$ | Yes |
| **$4$** | **`'o'`** | **$3$** | **$1$** | **$3 \ge 1$** | **$3 \ge 3$** | **Yes** |
| **Status** | — | — | — | — | — | **Word is Stretchy** |

---

## 5. Boundary Cases & Failure Modes

- **Candidate Word Longer Than $s$ ($|t| > |s|$):** Cannot stretch to a shorter string $\implies$ reject immediately.
- **Single Character Match ($s = \text{"aaa"}, t = \text{"a"}$):** $1 \to 3 \implies$ valid.
- **Invalid Stretch to 2 ($s = \text{"aa"}, t = \text{"a"}$):** $c_1 = 2 < 3$ and $2 \ne 1 \implies$ invalid.
- **Different Characters ($s = \text{"abc"}, t = \text{"abd"}$):** Letter mismatch $\implies$ invalid.

---

## 6. Traps & Common Anti-Patterns

- **Allowing Stretches of Length 2:** The rule requires the stretched group to have length at least 3. If $s$ has 2 `'l'`s and $t$ has 1 `'l'`, $t$ CANNOT be stretched to $s$.
- **Not Checking String Exhaustion:** If $t$ matches a prefix of $s$ but leaves trailing groups in $s$, ensure $i == m \land j == n$ before declaring valid.
- **Generating All Expanded Strings:** Generating all $3^k$ stretched strings creates exponential explosion. Two-pointer group comparison runs in deterministic linear time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Checking each candidate word $t$ takes $\mathcal{O}(|s| + |t|)$ using two pointers.
  - Across $W$ words: $\mathcal{O}(W \cdot |s| + \sum |w_i|)$.
  - Total Time: strictly linear $\mathcal{O}(W \cdot |s| + \sum |w_i|)$ where $|s| \le 100, W \le 100$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (index pointers and integer counters).
