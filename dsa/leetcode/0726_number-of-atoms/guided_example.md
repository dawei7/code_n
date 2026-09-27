# Guided Example: Number of Atoms

We trace the step-by-step chemical formula parsing, right-to-left reverse lexical tokenization, multiplier stack tracking ($multipliers$), closing parenthesis factor propagation ($multipliers.\text{push}(multipliers[-1] \times pending)$), opening parenthesis scope closing ($multipliers.\text{pop}()$), multi-letter atomic symbol recognition ($[A-Z][a-z]*$), atom count accumulation ($counts[atom] \leftarrow counts[atom] + pending \times multipliers[-1]$), and alphabetical canonical serialization on representative molecular formulas:

- **Input:** $formula = \text{"Mg(OH)2"}$
- **Required output:** `"H2MgO2"`
  - Chemical formula syntax:
    - Each chemical element begins with one uppercase letter, followed optionally by one or more lowercase letters (e.g. `"H"`, `"Mg"`, `"He"`).
    - If an element or parenthesized group is followed by a number $k > 1$, its count is multiplied by $k$. If omitted, the count is implicitly $1$.
    - Parentheses `(...)` group atoms, and trailing multipliers apply recursively to all enclosed elements.
    - Required format:
      - Element names sorted **strictly in alphabetical order**.
      - Followed by the count if strictly greater than 1 (count 1 is omitted).
    - For `"Mg(OH)2"`:
      - `"Mg"` count: 1.
      - Enclosed group `(OH)` has multiplier 2:
        - `"O"` count: $1 \times 2 = 2$.
        - `"H"` count: $1 \times 2 = 2$.
      - Alphabetical sorting: `"H"` (2), `"Mg"` (1), `"O"` (2).
      - Serialized string: `"H2MgO2"`.
- **Right-to-Left Scanning & Multiplier Stack Invariant:**
  - **The Forward Parsing Bottleneck:**
    - In standard left-to-right parsing, when encountering an element inside parentheses, its true quantity depends on trailing group multipliers that appear in the future (e.g. the `'2'` in `(OH)2`).
  - **The Reverse Parsing Advantage:**
    - Scanning from **right to left** encounters group multipliers *before* entering the corresponding parentheses!
    - We maintain:
      1. `multipliers = [1]`: Stack of active nested group multipliers.
      2. `pending = 1`: Multiplier of the immediately following token (number or default 1).
  - **State Transition Rules (Right-to-Left):**
    - **1. Digits:**
      - Parse the full multi-digit integer from right to left:
        $$
        pending \leftarrow \text{parsed integer}
        $$
    - **2. Closing Parenthesis `')'`:**
      - The pending multiplier belongs to this entire parenthesized block.
      - Push the compounded multiplier to the stack:
        $$
        multipliers.\text{push}(multipliers[-1] \times pending)
        $$
      - Reset: $pending \leftarrow 1$.
    - **3. Opening Parenthesis `'('`:**
      - We have exited this parenthesized block.
      - Pop the top multiplier:
        $$
        multipliers.\text{pop}()
        $$
    - **4. Chemical Element (Letters):**
      - Gather lowercase letters and the leading uppercase letter to isolate $atom$.
      - The total count contributed by this occurrence is:
        $$
        \Delta = pending \times multipliers[-1]
        $$
        $$
        counts[atom] \leftarrow counts[atom] + \Delta
        $$
      - Reset: $pending \leftarrow 1$.
- **Step-by-Step Worked Execution Trace on $formula = \text{"Mg(OH)2"}$:**
  - Length: 7. Indices: $0 \dots 6$.
  - Initial state:
    $$
    counts = \{\}, \quad multipliers = [1], \quad pending = 1, \quad index = 6
    $$
  - **Step 1 ($index = 6$, character `'2'`):**
    - Character is a digit.
    - Parse integer: value is $2$.
    - Set pending factor:
      $$
      pending \leftarrow \mathbf{2}
      $$
      $$
      index \leftarrow 5
      $$
  - **Step 2 ($index = 5$, character `')'`):**
    - Encounter closing parenthesis!
    - Compound active multiplier:
      $$
      multipliers.\text{push}(multipliers[-1] \times pending) = 1 \times 2 = \mathbf{2}
      $$
      $$
      multipliers = [1, \; \mathbf{2}]
      $$
    - Reset pending: $pending \leftarrow 1$.
    - Advance: $index \leftarrow 4$.
  - **Step 3 ($index = 4$, character `'H'`):**
    - Uppercase letter with no lowercase suffix $\implies atom = \text{"H"}$.
    - Compute total atom count:
      $$
      \Delta = pending \times multipliers[-1] = 1 \times 2 = \mathbf{2}
      $$
      $$
      counts[\text{"H"}] \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Reset pending: $pending \leftarrow 1$.
    - Advance: $index \leftarrow 3$.
  - **Step 4 ($index = 3$, character `'O'`):**
    - Uppercase letter $\implies atom = \text{"O"}$.
    - Compute total atom count:
      $$
      \Delta = pending \times multipliers[-1] = 1 \times 2 = \mathbf{2}
      $$
      $$
      counts[\text{"O"}] \leftarrow 0 + 2 = \mathbf{2}
      $$
    - Reset pending: $pending \leftarrow 1$.
    - Advance: $index \leftarrow 2$.
  - **Step 5 ($index = 2$, character `'('`):**
    - Encounter opening parenthesis!
    - Exit parenthesized scope:
      $$
      multipliers.\text{pop}() \implies multipliers = [1]
      $$
    - Advance: $index \leftarrow 1$.
  - **Step 6 ($index = 1$, character `'g'`):**
    - Lowercase letter `'g'` preceded by uppercase `'M'` at index 0.
    - Full element symbol: $atom = \text{"Mg"}$.
    - Compute total atom count:
      $$
      \Delta = pending \times multipliers[-1] = 1 \times 1 = \mathbf{1}
      $$
      $$
      counts[\text{"Mg"}] \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Reset pending: $pending \leftarrow 1$.
    - Advance: $index \leftarrow -1$.
  - **Step 7: Format Output:**
    - Active counts: $\{\text{"H"}: 2, \; \text{"O"}: 2, \; \text{"Mg"}: 1\}$.
    - Sort element names alphabetically:
      1. `"H"`: count $2 > 1 \implies \text{"H2"}$.
      2. `"Mg"`: count $1 \implies \text{"Mg"}$ (1 omitted).
      3. `"O"`: count $2 > 1 \implies \text{"O2"}$.
    - Concatenate:
      $$
      ans = \mathbf{\text{"H2MgO2"}}
      $$
- **Nested Groups Trace ($formula = \text{"K4(ON(SO3)2)2"}$):**
  - Outer `)2` pushes multiplier $1 \times 2 = 2$.
  - Inner `(SO3)2` pushes multiplier $2 \times 2 = 4$.
  - Enclosed O3 gets $3 \times 4 = 12$. S gets $1 \times 4 = 4$.
  - Enclosed N gets $1 \times 2 = 2$. Outer O gets $1 \times 2 = 2$. Total O: $12 + 2 = 14$.
  - K4 gets $4 \times 1 = 4$.
  - Formatted: `"K4N2O14S4"`.
- **Flat Formula Trace ($formula = \text{"H2O"}$):**
  - O: 1, H: 2.
  - Formatted: `"H2O"`.

This instance demonstrates context-free grammar parsing and reverse pushdown automaton tree reduction, mathematically proves why right-to-left evaluation linearizes nested multiplicative distributive laws, and derives $O(L + A \log A)$ runtime and $O(L)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a chemical formula with elements, counts, and parentheses:
Count each atom across all groups and multipliers.
Return element counts in **alphabetical order**, omitting count 1.

```text
formula = "Mg(OH)2"

Scan right-to-left:
  '2' -> pending multiplier = 2
  ')' -> push active multiplier 1 * 2 = 2 to stack
  'H' -> count = 1 * 2 = 2
  'O' -> count = 1 * 2 = 2
  '(' -> pop multiplier 2
  "Mg" -> count = 1 * 1 = 1

Counts: H: 2, Mg: 1, O: 2
Sorted alphabetically: "H2MgO2"
```

### The Invariant of Right-to-Left Scope Multipliers
- Scanning right-to-left reads the multiplier of a parenthesized group before visiting its contents.
- Pushing `stack.top * pending` on `)` and popping on `(` applies nested multipliers distributively to every atom inside.

---

## 2. Conceptual Foundation & Invariants

### 1. The Multiplier Stack Protocol:
$$
\text{On } ')': \quad multipliers.\text{push}(multipliers.\text{top}() \times pending), \quad pending \leftarrow 1
$$
$$
\text{On } '(': \quad multipliers.\text{pop}()
$$
$$
\text{On } atom: \quad counts[atom] \leftarrow counts[atom] + pending \times multipliers.\text{top}(), \quad pending \leftarrow 1
$$

### 2. Output Formatting:
$$
ans = \sum_{atom \in \text{sorted}(counts)} atom + (str(counts[atom]) \text{ if } counts[atom] > 1 \text{ else } "")
$$

> **Distributive Tree Reduction Invariant.** The algebraic representation of a chemical formula as an annotated syntax tree $(V, E, \times, +)$ is strictly distributive, allowing the product of path weights from the root to any leaf to be evaluated by a single backward traversal with an accumulator stack.

---

## 3. Step-by-Step Worked Execution

We trace $formula = \text{"Mg(OH)2"}$:

---

### Step 1: Scan Right
- $index = 6$ ('2'): $pending = 2$.
- $index = 5$ (')'): push $1 \times 2 = 2 \implies stack = [1, 2], pending = 1$.

---

### Step 2: Inside Group
- $index = 4$ ('H'): $counts[\text{"H"}] = 1 \times 2 = 2$.
- $index = 3$ ('O'): $counts[\text{"O"}] = 1 \times 2 = 2$.
- $index = 2$ ('('): pop 2 $\implies stack = [1]$.

---

### Step 3: Outside Group
- $index = 1, 0$ ("Mg"): $counts[\text{"Mg"}] = 1 \times 1 = 1$.

---

### Step 4: Serialize
- Sorted: "H" (2), "Mg" (1), "O" (2) $\implies \mathbf{\text{"H2MgO2"}}$.

---

## 4. Complete Execution Trace

| Index | Substring Read | Token Type | Multiplier Stack | Pending Factor | Atom Accumulated | Output Contribution |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $6$ | `'2'` | Number | `[1]` | $2$ | None | — |
| $5$ | `')'` | Open Scope (Right) | `[1, 2]` | $1$ | None | Group factor $2$ |
| $4$ | `'H'` | Element | `[1, 2]` | $1$ | $\text{"H"} \to +2$ | $H_2$ |
| $3$ | `'O'` | Element | `[1, 2]` | $1$ | $\text{"O"} \to +2$ | $O_2$ |
| $2$ | `'('` | Close Scope (Right) | `[1]` | $1$ | None | Exit group |
| $0 \dots 1$| `"Mg"`| Element | `[1]` | $1$ | $\text{"Mg"} \to +1$ | $Mg_1$ |
| **Final**| — | **Alphabetical Sort** | — | — | **H: 2, Mg: 1, O: 2** | **`"H2MgO2"`** |

---

## 5. Boundary Cases & Failure Modes

- **Multi-Digit Numbers (`H12O`):** Accumulates place values $1 \times 10^0 + 1 \times 10^1 = 12$.
- **Deeply Nested Groups (`K4(ON(SO3)2)2`):** Stack multiplies factors: $1 \times 2 \times 2 = 4$.
- **No Parentheses (`H2O`):** Multiplier stack remains $[1]$ throughout.
- **Single Letter vs Double Letter Elements (`N` vs `Na`):** Loop reads lowercase letters until an uppercase letter is reached.

---

## 6. Traps & Common Anti-Patterns

- **Forward Recursive Parsing Complexity:** Forward recursive descent requires looking ahead for trailing numbers after `)`. Reverse parsing naturally consumes the trailing number before entering the group.
- **Appended '1' in Output:** Output format explicitly requires omitting '1' (e.g. `H2O`, not `H2O1`).
- **Unsorted Elements:** Elements must be printed in **strict alphabetical order** (`"H2MgO2"`, not `"MgH2O2"`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One backward pass over the formula string of length $L$: $\mathcal{O}(L)$.
  - Sorting unique chemical elements ($A \le 26$): $\mathcal{O}(A \log A)$.
  - Total Time: strictly linear $\mathcal{O}(L + A \log A)$. Completes in $< 1$ ms for $L = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ memory for the multiplier stack and atom counts hash map.
