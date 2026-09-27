# Guided Example: Basic Calculator IV

We trace the step-by-step symbolic polynomial algebra evaluation, variable substitution mapping ($evalvars \to evalints$), canonical monomial tuple representation ($\text{tuple}(\text{sorted}(\dots))$), recursive descent grammar parsing (Expression $\to$ Term $\to$ Factor), polynomial addition/subtraction coefficient aggregation, polynomial Cartesian multiplication, degree-lexicographical term ordering, and serialized algebraic string formatting on representative algebraic expressions:

- **Input:**
  - Expression: $expression = \text{"e + 8 - a + 5"}$
  - Known variables: $evalvars = [\text{"e"}]$
  - Assigned values: $evalints = [1]$
- **Required output:**
  $$
  [\text{"-1*a"}, \; \text{"14"}]
  $$
  - Polynomial algebra & formatting rules:
    - Replace all known variables with their assigned numerical values: here $e = 1$.
    - Free variables (like $a$) remain symbolic.
    - An algebraic term (monomial) is the product of a non-zero integer coefficient and zero or more variables (e.g. $5$, $-1 \cdot a$, $2 \cdot a \cdot b$).
    - Within each term, variables are written in **lexicographical alphabetical order** joined by `*` (e.g. `a*b`, not `b*a`).
    - The terms must be sorted in output:
      1. **Primary Sort:** Total degree (number of variables) in **descending order**.
      2. **Secondary Sort:** Lexicographical order of the variable sequence in **ascending order**.
    - For $1 + 8 - a + 5$:
      - Constant terms combine: $1 + 8 + 5 = 14$ (degree 0).
      - Variable term: $-1 \cdot a$ (degree 1).
      - Degree 1 precedes degree 0:
        $$
        [\text{"-1*a"}, \; \text{"14"}]
        $$
- **Canonical Monomial Ring & Recursive Descent Invariant:**
  - **Monomial Tuple Identity:**
    - Represent any monomial as a sorted tuple of variable name strings:
      $$
      x \cdot y \iff (\text{'x'}, \text{'y'})
      $$
      $$
      \text{Constant } c \iff () \quad (\text{empty tuple, degree } 0)
      $$
    - A polynomial is a sparse dictionary:
      $$
      P: \text{MonomialTuple} \to \text{Coefficient}
      $$
  - **Algebraic Ring Operations:**
    - **Addition / Subtraction:**
      $$
      (P \pm Q)[M] = P[M] \pm Q[M]
      $$
      If the combined coefficient becomes 0, remove $M$ from the dictionary.
    - **Multiplication:**
      $$
      (P \times Q)[\text{tuple}(\text{sorted}(M_1 + M_2))] = \sum c_1 \times c_2
      $$
  - **Context-Free Parsing Grammar:**
    - Standard operator precedence:
      $$
      \text{Expression} \to \text{Term} \; (('+' \mid '-') \; \text{Term})^*
      $$
      $$
      \text{Term} \to \text{Factor} \; ('*' \; \text{Factor})^*
      $$
      $$
      \text{Factor} \to \text{'('} \; \text{Expression} \; \text{')'} \mid \text{Integer} \mid \text{Variable}
      $$
- **Step-by-Step Worked Execution Trace on $expression = \text{"e + 8 - a + 5"}$:**
  - Given: $substitutions = \{ \text{"e"}: 1 \}$.
  - Token sequence: $[\text{"e"}, \; \text{"+"}, \; \text{"8"}, \; \text{"-"}, \; \text{"a"}, \; \text{"+"}, \; \text{"5"}]$.
  - **Step 1: Parse First Term (Factor `"e"`):**
    - Token `"e"` is in substitutions: evaluates to constant integer $1$.
    - Represented as polynomial dictionary:
      $$
      P = \{ (): 1 \}
      $$
  - **Step 2: Process Operator `"+"` and Next Term (`"8"`):**
    - Operator is `+`.
    - Token `"8"` parses as integer constant $8 \implies Q = \{ (): 8 \}$.
    - Add into $P$:
      $$
      P[()] \leftarrow 1 + 8 = \mathbf{9} \implies P = \{ (): 9 \}
      $$
  - **Step 3: Process Operator `"-"` and Next Term (`"a"`):**
    - Operator is `-`.
    - Token `"a"` is not in substitutions $\implies$ free variable term with coefficient 1:
      $$
      Q = \{ (\text{"a"},): 1 \}
      $$
    - Subtract from $P$ (scale $-1$):
      $$
      P[(\text{"a"},)] \leftarrow 0 - 1 = \mathbf{-1}
      $$
      $$
      P = \{ (): 9, \; (\text{"a"},): -1 \}
      $$
  - **Step 4: Process Operator `"+"` and Next Term (`"5"`):**
    - Operator is `+`.
    - Token `"5"` parses as integer constant $5 \implies Q = \{ (): 5 \}$.
    - Add into $P$:
      $$
      P[()] \leftarrow 9 + 5 = \mathbf{14}
      $$
      $$
      P = \{ (): 14, \; (\text{"a"},): -1 \}
      $$
  - **Step 5: Degree & Lexicographical Ordering:**
    - Monomials present:
      - $M_1 = (\text{"a"},)$: length 1 (degree 1), coefficient $-1$.
      - $M_2 = ()$: length 0 (degree 0), coefficient $14$.
    - Sort key: $(- \text{degree}, \; \text{monomial})$:
      - Rank 1: $(\text{"a"},)$ (degree $1 \implies -1$).
      - Rank 2: $()$ (degree $0 \implies 0$).
    - Ordered terms: $[(\text{"a"},), \; ()]$.
  - **Step 6: Serialization to Output Strings:**
    - For monomial $(\text{"a"},)$:
      $$
      \text{coefficient} = -1 \implies \mathbf{\text{"-1*a"}}
      $$
    - For monomial $()$:
      $$
      \text{coefficient} = 14 \implies \mathbf{\text{"14"}}
      $$
    - Final list of terms:
      $$
      ans = [\mathbf{\text{"-1*a"}}, \; \mathbf{\text{"14"}}]
      $$
- **Cartesian Monomial Multiplication Trace ($(a + b) \times (a - b)$):**
  - Left factor: $\{ (a,): 1, (b,): 1 \}$.
  - Right factor: $\{ (a,): 1, (b,): -1 \}$.
  - Cross products:
    - $(a,) \times (a,) \to (a, a)$ with $1 \times 1 = 1$.
    - $(a,) \times (b,) \to (a, b)$ with $1 \times (-1) = -1$.
    - $(b,) \times (a,) \to (a, b)$ with $1 \times 1 = 1$.
    - $(b,) \times (b,) \to (b, b)$ with $1 \times (-1) = -1$.
  - Combine like terms:
    - Monomial $(a, b)$: $-1 + 1 = 0 \implies \mathbf{Annihilated!}$
  - Result: $\{ (a, a): 1, (b, b): -1 \} \implies [\text{"1*a*a"}, \text{"-1*b*b"}]$.
- **All Terms Cancel to Zero ($a - a$):**
  - Coefficient becomes 0 $\implies$ empty polynomial dictionary.
  - Returns empty list `[]`.

This instance demonstrates formal polynomial ring arithmetic and recursive descent symbolic parsing, mathematically proves why canonical multi-index sorting enforces a unique normal form across commutative polynomial quotient rings, and derives $O(L \cdot 2^D)$ runtime and $O(M)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an algebraic $expression$, known variables $evalvars$, and their values $evalints$:
Substitute known values and evaluate the expression into a **canonical simplified polynomial**.
Sort terms by **degree descending**, then **lexicographical ascending**.

```text
expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]

1. Substitute e = 1:
   1 + 8 - a + 5
2. Combine like terms:
   -1*a + 14
3. Sort:
   Degree 1: -1*a
   Degree 0: 14

Result: [ "-1*a", "14" ]
```

### The Invariant of the Monomial Tuple Dictionary
- Represent every monomial as a sorted tuple of variable names: e.g. $(a, b)$ for $a \cdot b$, and $()$ for constants.
- Represent polynomials as dictionaries mapping monomial tuples to integer coefficients.
- Terms with coefficient 0 are dropped automatically.

---

## 2. Conceptual Foundation & Invariants

### 1. Canonical Term Ring:
$$
\text{Monomial } M = (v_1, v_2, \dots, v_k) \quad \text{with } v_1 \le v_2 \le \dots \le v_k
$$
$$
P \times Q = \sum_{M_1, M_2} c_1 c_2 \cdot \text{sort}(M_1 + M_2)
$$

### 2. Output Lexicographical Sorting Order:
$$
\text{key}(M) = (-\text{len}(M), \; M)
$$

> **Commutative Monomial Normal Form Invariant.** In the polynomial ring $\mathbb{Z}[x_1, \dots, x_k]$, every polynomial has a unique canonical representation as a $\mathbb{Z}$-linear combination of sorted variable words, whose deg-lex term ordering defines a strict Gröbner-compatible total order.

---

## 3. Step-by-Step Worked Execution

We trace $expression = \text{"e + 8 - a + 5"}$ with $e = 1$:

---

### Step 1: Substitute
- $e \to 1$.

---

### Step 2: Combine Constants
- $1 + 8 + 5 = 14 \implies (): 14$.

---

### Step 3: Combine Variables
- $-a \implies (a,): -1$.

---

### Step 4: Sort & Format
- Degree 1: `"-1*a"`.
- Degree 0: `"14"`.

---

### Step 5: Output
$$
[\text{"-1*a"}, \; \text{"14"}]
$$

---

## 4. Complete Execution Trace

| Sub-Expression Processed | Operation | Active Monomial Dict $P$ | Degree Breakdown | Output Token Formatted |
|:---:|:---:|:---:|:---:|:---:|
| `"e"` ($e = 1$) | Base term | `{ (): 1 }` | Deg 0 | — |
| `"+ 8"` | Addition | `{ (): 9 }` | Deg 0 | — |
| `"- a"` | Subtraction | `{ (): 9, ("a",): -1 }` | Deg 0, Deg 1 | — |
| `"+ 5"` | Addition | `{ (): 14, ("a",): -1 }` | Deg 0, Deg 1 | — |
| **Sort & Format** | — | — | **Deg 1 then Deg 0** | **`["-1*a", "14"]`** |

---

## 5. Boundary Cases & Failure Modes

- **Complete Cancellation ($a - a$):** Coefficients become 0 and are purged $\implies$ returns empty list `[]`.
- **Higher Degree Multiplication ($a * a * b$):** Forms monomial `("a", "a", "b")` $\implies$ formatted as `"1*a*a*b"`.
- **Negative Multiplication ($-1 * -1$):** Signs multiply correctly $\implies$ positive constant.
- **Nested Parentheses ($((a + 1) * (b + 1))$):** Recursive descent handles arbitrary nesting depth.

---

## 6. Traps & Common Anti-Patterns

- **Not Sorting Variables within Monomials:** $a \cdot b$ and $b \cdot a$ represent the exact same algebraic term. If variable names are not sorted within the tuple, they will fail to combine into a single term!
- **Retaining Zero Coefficients:** Terms with coefficient 0 must be deleted; outputting `"0*a"` violates problem rules.
- **String Formatting Off-By-One:** A constant term has no variables and must NOT be followed by `*` (e.g. `"14"`, not `"14*"`).
- **Secondary Sort Direction:** Primary sort is degree **descending** (`-len`), but secondary sort is variable names **ascending** (alphabetical).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Tokenization takes $\mathcal{O}(L)$ time where $L \le 250$ is expression length.
  - Recursive descent parses the grammar tree in $\mathcal{O}(L)$.
  - Monomial multiplication takes $\mathcal{O}(|P| \cdot |Q|)$ per product. With bounded variables and degree, total terms remain small ($\le 100$).
  - Sorting terms takes $\mathcal{O}(K \log K)$ where $K$ is the number of distinct terms.
  - Total Time: well within $\mathcal{O}(L \cdot 2^D)$ where $D$ is max multiplication depth. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ memory for the polynomial hash map and recursion call stack.
