# Guided Example: Ambiguous Coordinates

We trace the step-by-step outer delimiter stripping ($s \to digits$), bipartite coordinate comma partition ($digits \to (X, Y)$), decimal point placement rules (leading zero integer constraint $l == \text{'0'} \lor \neg l.\text{starts}(0)$, trailing zero fraction constraint $\neg r.\text{ends}(0)$), Cartesian product combination ($X \times Y$), and valid coordinate string formatting on representative numeric strings:

- **Input:**
  $$
  s = \text{"(123)"}
  $$
- **Required output:**
  $$
  [\text{"(1, 23)"}, \; \text{"(1, 2.3)"}, \; \text{"(12, 3)"}, \; \text{"(1.2, 3)"}]
  $$
  *(Order of coordinates in output list is arbitrary)*
  - Coordinate formatting & number validity rules:
    - We are given an ambiguous string $s$ formed by stripping parentheses, commas, spaces, and decimal points from 2D coordinates $(x, y)$.
    - We must reconstruct all valid original coordinates `"(x, y)"`.
    - **Valid Number Syntax:**
      1. **Integer Part $l$:** Cannot contain superfluous leading zeros:
         $$
         l = \text{"0"} \quad \lor \quad \text{does not start with '0'}
         $$
         *(e.g. `"0"` and `"12"` are valid; `"00"` and `"03"` are invalid)*.
      2. **Fractional Part $r$:** Cannot contain superfluous trailing zeros:
         $$
         \text{does not end with '0'}
         $$
         *(e.g. `".5"` is valid; `".50"` and `".0"` are invalid)*.
      3. An integer alone (without decimal point) has $r = \emptyset$, which vacuously satisfies the trailing zero rule.
    - For $s = \text{"(123)"}$:
      - Core digits: `"123"`.
      - Comma split 1: $X = \text{"1"}$, $Y = \text{"23"}$
        - Valid $X$: `"1"`
        - Valid $Y$: `"23"`, `"2.3"`
        - Generates: `"(1, 23)"`, `"(1, 2.3)"`.
      - Comma split 2: $X = \text{"12"}$, $Y = \text{"3"}$
        - Valid $X$: `"12"`, `"1.2"`
        - Valid $Y$: `"3"`
        - Generates: `"(12, 3)"`, `"(1.2, 3)"`.
      - Result: 4 valid coordinate strings.
- **Cartesian Product & Decimal Rule Invariant:**
  - **The Two-Tiered Search Space:**
    - **Tier 1 (Coordinate Split):**
      - Strip the outer `(` and `)`.
      - Choose a split point $i$ between $2$ and $n - 1$ to partition digits into $X = s[1 \dots i - 1]$ and $Y = s[i \dots n - 2]$.
      - Both $X$ and $Y$ must be non-empty.
    - **Tier 2 (Decimal Placements within a Segment):**
      - For a digit substring $sub$ of length $L$, try inserting a decimal point after $k$ digits ($1 \le k \le L$):
        - Integer part: $l = sub[0 \dots k - 1]$
        - Fractional part: $r = sub[k \dots L - 1]$
      - **Grammar Acceptance Test:**
        $$
        \text{Valid}(l, r) \iff (l = \text{"0"} \lor \neg l.\text{startswith}('0')) \;\land\; (\neg r.\text{endswith}('0'))
        $$
      - If valid and $r \ne \emptyset$: candidate is $l + \text{"."} + r$.
      - If valid and $r = \emptyset$: candidate is $l$.
    - **Tier 3 (Cartesian Assembly):**
      - Form all coordinate pairs:
        $$
        \{ \text{"("} + x + \text{", "} + y + \text{")"} \mid x \in \text{Valid}(X), \; y \in \text{Valid}(Y) \}
        $$
- **Step-by-Step Worked Execution Trace on $s = \text{"(123)"}$:**
  - Outer string length $n = 5$.
  - Internal digits: $s[1:4] = \text{"123"}$.
  - Possible split positions $i \in [2, 3]$:
  - **Split Point $i = 2$ ($X = s[1:2] = \text{"1"}$, $Y = s[2:4] = \text{"23"}$):**
    - **Parse $X = \text{"1"}$ (Length 1):**
      - $k = 1$: $l = \text{"1"}, r = \text{""}$.
        - $l$ starts with nonzero $\implies$ Valid!
        - $r$ is empty $\implies$ Valid!
        - Candidate $X$: `["1"]`.
    - **Parse $Y = \text{"23"}$ (Length 2):**
      - $k = 1$: $l = \text{"2"}, r = \text{"3"}$.
        - $l$ starts with nonzero $\implies$ Valid.
        - $r = \text{"3"}$ does not end with `'0'` $\implies$ Valid.
        - Decimal candidate: $\mathbf{\text{"2.3"}}$.
      - $k = 2$: $l = \text{"23"}, r = \text{""}$.
        - $l = \text{"23"}$ starts with nonzero $\implies$ Valid.
        - $r$ is empty $\implies$ Valid.
        - Integer candidate: $\mathbf{\text{"23"}}$.
      - Candidate $Y$: `["2.3", "23"]`.
    - **Cross Product for Split $i = 2$:**
      - `"1"` $\times$ `"23"` $\implies \mathbf{\text{"(1, 23)"}}$
      - `"1"` $\times$ `"2.3"` $\implies \mathbf{\text{"(1, 2.3)"}}$
  - **Split Point $i = 3$ ($X = s[1:3] = \text{"12"}$, $Y = s[3:4] = \text{"3"}$):**
    - **Parse $X = \text{"12"}$ (Length 2):**
      - $k = 1$: $l = \text{"1"}, r = \text{"2"} \implies \mathbf{\text{"1.2"}}$.
      - $k = 2$: $l = \text{"12"}, r = \text{""} \implies \mathbf{\text{"12"}}$.
      - Candidate $X$: `["1.2", "12"]`.
    - **Parse $Y = \text{"3"}$ (Length 1):**
      - $k = 1$: $l = \text{"3"}, r = \text{""} \implies \mathbf{\text{"3"}}$.
      - Candidate $Y$: `["3"]`.
    - **Cross Product for Split $i = 3$:**
      - `"12"` $\times$ `"3"` $\implies \mathbf{\text{"(12, 3)"}}$
      - `"1.2"` $\times$ `"3"` $\implies \mathbf{\text{"(1.2, 3)"}}$
  - **Assembly of All Generated Coordinates:**
    $$
    ans = [\text{"(1, 23)"}, \; \text{"(1, 2.3)"}, \; \text{"(12, 3)"}, \; \text{"(1.2, 3)"}]
    $$
- **Leading Zero Disqualification Trace ($s = \text{"(00011)"}$):**
  - Consider segment `"0001"`:
    - $k = 1$: $l = \text{"0"}, r = \text{"001"}$. $l = \text{"0"}$ (valid!), $r$ ends with `'1'` (valid!) $\implies \mathbf{\text{"0.001"}}$.
    - $k = 2$: $l = \text{"00"}$ (starts with 0, not `"0"`) $\implies$ Rejected.
    - $k = 3$: $l = \text{"000"}$ $\implies$ Rejected.
    - $k = 4$: $l = \text{"0001"}$ $\implies$ Rejected.
  - Zero-rules eliminate ill-formed decimal expansions deterministically!

This instance demonstrates formal language grammar parsing on ambiguous string encodings and regular expression filtering over 2D product domains, mathematically proves why canonical decimal representations admit at most one valid decimal insertion per prefix boundary, and derives $O(N^3)$ execution time and $O(N^3)$ output space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$ with digits between parentheses:
Find all valid 2D coordinates `"(x, y)"` that could have produced $s$.

```text
s = "(123)" -> digits: "123"

Split 1: X = "1", Y = "23"
  X valid: "1"
  Y valid: "23", "2.3"
  Pairs: "(1, 23)", "(1, 2.3)"

Split 2: X = "12", Y = "3"
  X valid: "12", "1.2"
  Y valid: "3"
  Pairs: "(12, 3)", "(1.2, 3)"

Result: [ "(1, 23)", "(1, 2.3)", "(12, 3)", "(1.2, 3)" ]
```

### The Invariant of Valid Decimal Placement
- Integer part $l$: cannot have leading zeros unless it is `"0"`.
- Fractional part $r$: cannot have trailing zeros.
- Cartesian product of all valid $x \in \text{Valid}(X)$ and $y \in \text{Valid}(Y)$ yields all configurations.

---

## 2. Conceptual Foundation & Invariants

### 1. Decimal Validity Predicate:
$$
\text{Valid}(l, r) \iff (l = \text{"0"} \lor \neg l.\text{starts}('0')) \;\land\; (\neg r.\text{ends}('0'))
$$

### 2. Cartesian Coordinate Formulation:
$$
\text{Coord}(s) = \bigcup_{i = 2}^{n - 2} \Big( \text{Parse}(s[1:i]) \times \text{Parse}(s[i:n-1]) \Big)
$$

> **Canonical Representation Invariant.** The canonical positional decimal representation over $\mathbb{R}$ requires uniqueness of the fractional expansion (no trailing zeros) and uniqueness of the integer part (no leading zeros). Each digit slice generates at most $L$ valid interpretations.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"(123)"}$:

---

### Step 1: Split at $i = 2$ ($X = \text{"1"}, Y = \text{"23"}$)
- $X = \text{"1"}$: `["1"]`.
- $Y = \text{"23"}$: `["23", "2.3"]`.
- Pairs: `"(1, 23)"`, `"(1, 2.3)"`.

---

### Step 2: Split at $i = 3$ ($X = \text{"12"}, Y = \text{"3"}$)
- $X = \text{"12"}$: `["12", "1.2"]`.
- $Y = \text{"3"}$: `["3"]`.
- Pairs: `"(12, 3)"`, `"(1.2, 3)"`.

---

### Step 3: Output
- 4 pairs formatted with parentheses and commas.

---

## 4. Complete Execution Trace

| Coordinate Split $(X, Y)$ | Segment Lengths | Valid $X$ Expressions | Valid $Y$ Expressions | Formed Coordinate Pairs |
|:---:|:---:|:---:|:---:|:---:|
| `("1", "23")` | $1, 2$ | `["1"]` | `["23", "2.3"]` | `"(1, 23)"`, `"(1, 2.3)"` |
| **`("12", "3")`** | **$2, 1$** | **`["12", "1.2"]`** | **`["3"]`** | **`"(12, 3)"`, `"(1.2, 3)"`** |

---

## 5. Boundary Cases & Failure Modes

- **Multiple Leading Zeros ($s = \text{"(00011)"}$):** Only forms starting with `"0."` are valid for $l = \text{"0"}$; all $l = \text{"00"}$ rejected.
- **Pure Zeros ($s = \text{"(00)"}$):** Split into `"0"` and `"0"` $\implies$ only `"(0, 0)"`.
- **Length 4 ($s = \text{"(10)"}$):** $X = \text{"1"}, Y = \text{"0"} \implies \text{"(1, 0)"}$.
- **Trailing Zeros on Fraction ($"0.10"$):** Rejected because $r = \text{"10"}$ ends with 0.

---

## 6. Traps & Common Anti-Patterns

- **Accepting Empty Fractional Parts with a Dot (`"1."`):** A decimal point requires at least one fractional digit ($r \ne \emptyset$).
- **Accepting `"00"` as Zero:** Only the single character `"0"` is valid as integer zero; multiple zeros like `"00"` or `"000"` are invalid.
- **Missing Space After Comma:** Format must be strictly `f"({x}, {y})"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Length of string $N \le 12$.
  - Number of comma splits: $\mathcal{O}(N)$.
  - Decimal placements per split: $\mathcal{O}(N)$.
  - Total combinations generated: $\mathcal{O}(N^3) \le 12^3 = 1728$ operations.
  - Total Time: strictly $\mathcal{O}(N^3)$. Completes in $< 0.5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^3)$ space to store the output candidate coordinate strings.
