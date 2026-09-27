# Guided Example: Minimum Unique Word Abbreviation

We trace the step-by-step bitwise difference extraction, exact hitting set formulation, branch-and-bound search with most-constrained-pivot heuristic, and minimal token reconstruction on representative string instances:

- **Input:** $target = \text{"apple"}, \quad dictionary = [\text{"blade"}, \text{"plain"}, \text{"amber"}]$
- **Required output:** `"1p3"`
  - Word length: $m = 5$
  - Step 1 (Filter by length & compute difference bitmasks):
    - `blade`: differs at indices $0, 1, 2, 3$ (matches at $4$, `'e'`) $\implies diff_1 = 01111_2 = 15$
    - `plain`: differs at all indices $0, 1, 2, 3, 4$ $\implies diff_2 = 11111_2 = 31$
    - `amber`: differs at indices $1, 2, 3, 4$ (matches at $0$, `'a'`) $\implies diff_3 = 11110_2 = 30$
  - Step 2 (Hitting set constraint):
    - A valid retention mask must intersect all three difference masks:
      $$
      mask \ \& \ diff_k \ne 0 \quad \forall k \in \{1, 2, 3\}
      $$
  - Step 3 (Branch-and-bound exploration):
    - Mask $mask = 00001_2$ (retain `'a'`): $00001_2 \ \& \ 11110_2 = 0 \implies$ Collides with `amber` (`"a4"` matches both `apple` and `amber`).
    - Mask $mask = 00010_2$ (retain index $1$, `'p'`):
      - $00010_2 \ \& \ 15 \ne 0$, $00010_2 \ \& \ 31 \ne 0$, $00010_2 \ \& \ 30 \ne 0 \implies$ Covers all dictionary words!
      - Abbreviation formed: index $0$ abbreviated ($1$), index $1$ retained (`'p'`), indices $2\dots 4$ abbreviated ($3$) $\implies \text{"1p3"}$.
      - Abbreviation length: $3$ characters.
  - Minimal unique abbreviation: `"1p3"`
- **No Conflicting Words:** $target = \text{"apple"}, dictionary = [\text{"dog"}, \text{"cat"}] \implies$ length mismatch $\implies \text{"5"}$
- **Empty Dictionary:** $target = \text{"word"}, dictionary = [] \implies \text{"4"}$

This instance demonstrates modeling string disambiguation as a bitwise minimum hitting set problem, shows how branch-and-bound with most-constrained pivots prunes exponential search trees, and derives $O(|D| \cdot m + 2^k)$ complexity bounds.

---

## 1. Instance & Teaching Goal

Given a target string $target = \text{"apple"}$ ($m = 5$) and an exclusion dictionary $[\text{"blade"}, \text{"plain"}, \text{"amber"}]$:
Find an abbreviation of $target$ with the **minimum total character length** such that **no word** in the dictionary can produce the exact same abbreviation:

```text
Target: "apple" (m = 5)

Potential Abbreviations & Dictionary Conflicts:
  "5"    -> Abbreviates ANY 5-letter word -> Conflicts with "blade", "plain", "amber" (Ambiguous)
  "a4"   -> Retains index 0 ('a')         -> Matches "amber" ("amber" also starts with 'a'!)
  "4e"   -> Retains index 4 ('e')         -> Matches "blade" ("blade" also ends with 'e'!)
  "1p3"  -> Retains index 1 ('p')         -> blade[1]='l', plain[1]='l', amber[1]='m' (Unique! Length 3)
  "3l1"  -> Retains index 3 ('l')         -> Unique (Length 3)
  "a3e"  -> Retains indices 0 and 4       -> Unique (Length 3)

Minimal Length Unique Abbreviation: "1p3"
```

### The Conflict Elimination Requirement
An abbreviation is unique if and only if for every word $w \in dictionary$ of the same length:
At least **one** retained letter in our abbreviation does **not match** the letter at that same position in $w$.
If all retained letters in our abbreviation match the corresponding characters in $w$, then $w$ could be abbreviated to the exact same string, causing an ambiguous collision.

---

## 2. Conceptual Foundation & Invariants

### 1. Difference Bitmask:
For any dictionary word $w$ with $|w| = |target| = m$:
Construct a bitmask $diff(w)$ where bit $i$ is set to $1$ if $target[i] \ne w[i]$, and $0$ if $target[i] == w[i]$:
$$
diff(w) = \sum_{i=0}^{m-1} \left( [target[i] \ne w[i]] \ll i \right)
$$

### 2. The Hitting Set / Disambiguation Condition:
Let $mask \in [0, 2^m - 1]$ be a retention bitmask where bit $i = 1$ means character $target[i]$ is explicitly retained, and bit $i = 0$ means index $i$ is compressed into a numerical count.
- The abbreviation specified by $mask$ is valid if and only if:
  $$
  mask \ \& \ diff(w) \ne 0 \quad \forall w \in dictionary \text{ with } |w| = m
  $$
- This is the classic **Hitting Set** problem: choose a subset of bits that has non-empty intersection with every difference mask.

### 3. Abbreviation Token Length Formula:
Given a bitmask $mask$, we compute the length of its string representation:
- Each contiguous sequence of zeros (abbreviated characters) of length $L > 0$ contributes $1$ token (the number string).
- Each one (retained character) contributes $1$ token.

> **Invariant.** A candidate mask is safe if and only if its bitwise AND with every difference mask in the filtered dictionary is strictly greater than zero.

---

## 3. Step-by-Step Worked Execution

We trace $target = \text{"apple"}$, $dictionary = [\text{"blade"}, \text{"plain"}, \text{"amber"}]$:

---

### Step 1: Compute Difference Masks

| Dictionary Word $w$ | $target = \text{"apple"}$ vs $w$ Alignment | Matching Indices | Differing Indices | Binary Mask | Decimal Mask |
|:---|:---|:---:|:---:|:---:|:---:|
| `blade` | `a`$\ne$`b`, `p`$\ne$`l`, `p`$\ne$`a`, `l`$\ne$`d`, `e`$=$`e` | $\{4\}$ | $\{0, 1, 2, 3\}$ | $01111_2$ | $15$ |
| `plain` | `a`$\ne$`p`, `p`$\ne$`l`, `p`$\ne$`a`, `l`$\ne$`i`, `e`$\ne$`n` | $\emptyset$ | $\{0, 1, 2, 3, 4\}$ | $11111_2$ | $31$ |
| `amber` | `a`$=$`a`, `p`$\ne$`m`, `p`$\ne$`b`, `l`$\ne$`e`, `e`$\ne$`r` | $\{0\}$ | $\{1, 2, 3, 4\}$ | $11110_2$ | $30$ |

The set of difference masks to hit is:
$$
\mathcal{D} = \{15, \, 31, \, 30\}
$$

---

### Step 2: Evaluate Single-Bit Retentions (Length 2 Candidates)

Can an abbreviation of length 2 distinguish `apple` from all three words?
Length 2 abbreviations have either the form `c4` ($mask = 00001_2$) or `4c` ($mask = 10000_2$):
- **Candidate $mask = 00001_2$ (`"a4"`):**
  - $00001_2 \ \& \ 15 = 1 \ne 0$ (Distinguishes `blade`)
  - $00001_2 \ \& \ 31 = 1 \ne 0$ (Distinguishes `plain`)
  - $00001_2 \ \& \ 30 = 0$ (**Collides with `amber`!**)
  - Failed: `"a4"` is ambiguous.
- **Candidate $mask = 10000_2$ (`"4e"`):**
  - $10000_2 \ \& \ 30 = 16 \ne 0$ (Distinguishes `amber`)
  - $10000_2 \ \& \ 31 = 16 \ne 0$ (Distinguishes `plain`)
  - $10000_2 \ \& \ 15 = 0$ (**Collides with `blade`!**)
  - Failed: `"4e"` is ambiguous.

No length 2 abbreviation can hit both $15$ and $30$. Therefore, minimal unique length must be **at least 3**.

---

### Step 3: Evaluate Interior Bit Retentions (Length 3 Candidates)

Retaining an interior character splits the zeros into two numbers: `L` + `c` + `R`.
- **Test $mask = 00010_2$ (Retain index 1, `'p'`):**
  - Bitwise intersections:
    $$
    00010_2 \ \& \ 15 = 2 \ne 0 \quad (\text{differs from blade})
    $$
    $$
    00010_2 \ \& \ 31 = 2 \ne 0 \quad (\text{differs from plain})
    $$
    $$
    00010_2 \ \& \ 30 = 2 \ne 0 \quad (\text{differs from amber})
    $$
  - All three words are covered!
  - String reconstruction:
    - Index $0$: 1 zero $\implies$ `"1"`
    - Index $1$: 1 one $\implies$ `'p'`
    - Indices $2\dots 4$: 3 zeros $\implies$ `"3"`
    - Assembled result: `"1p3"`
  - Total character length: $1 + 1 + 1 = \mathbf{3}$.

Since length 2 was mathematically proven impossible, length 3 is globally optimal.

---

## 4. Complete Execution Trace

| Candidate Mask | Binary Representation | Retained Positions | Reconstructed Abbreviation | Word Collisions | Valid & Unique? | Total Token Length |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $0$ | $00000_2$ | None | `"5"` | `blade`, `plain`, `amber` | No | $1$ |
| $1$ | $00001_2$ | $\{0\}$ | `"a4"` | `amber` | No | $2$ |
| $16$ | $10000_2$ | $\{4\}$ | `"4e"` | `blade` | No | $2$ |
| **$2$** | **$00010_2$** | **$\{1\}$** | **`"1p3"`** | **None** | **Yes (Optimal)** | **$3$** |
| $8$ | $01000_2$ | $\{3\}$ | `"3l1"` | None | Yes | $3$ |
| $17$ | $10001_2$ | $\{0, 4\}$ | `"a3e"` | None | Yes | $3$ |

---

## 5. Boundary Cases & Failure Modes

- **Empty Dictionary ($dictionary = []$):** No exclusion constraints exist. The maximal compression is the entire string replaced by its length (e.g. `"5"` for `"apple"`).
- **No Same-Length Words:** If all dictionary words have lengths different from $target$, none can produce an abbreviation of length $m$. Return $str(m)$.
- **Dictionary Contains Target:** If $target \in dictionary$, the difference mask is $0$. No bitmask can satisfy $mask \ \& \ 0 \ne 0$, meaning no unique abbreviation is possible.
- **Single Character Target ($m = 1$):** Difference mask is either $0$ (identical) or $1$ (different). Optimal abbreviation is either impossible or $target[0]$.

---

## 6. Traps & Common Anti-Patterns

- **Ignoring Word Length Filtering:** Words with length different from $target$ cannot collide with $target$'s abbreviations because abbreviations strictly preserve total original character length. Comparing against words of different lengths wastes time and produces invalid masks.
- **Unpruned Exponential Search ($2^m$):** For $m \le 21$, brute forcing all $2^{21} \approx 2 \times 10^6$ masks against thousands of words causes Time Limit Exceeded. Using branch-and-bound with the most-constrained uncovered difference mask prunes the tree to a few hundred nodes.
- **Miscalculating Abbreviation Length:** Forgetting that multiple consecutive zeros merge into a single numerical token (e.g., $000$ contributes length $1$, not $3$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Filtering dictionary and computing difference masks takes $O(|D| \cdot m)$.
  - The hitting set search operates on at most $m$ bits ($m \le 21$).
  - With branch-and-bound selecting the minimum-cardinality difference mask at each step, search terminates in $\mathcal{O}(|D| \cdot m + 2^k)$ where $k \ll m$ is the minimal hitting set size.
- **Auxiliary Space Complexity:**
  - Storing the filtered difference masks requires $O(|D|)$ space.
  - Recursion call stack depth is bounded by $m \le 21$, requiring $\mathcal{O}(m)$ auxiliary memory.
