# Guided Example: Complex Number Multiplication

We trace the step-by-step Cartesian complex format parsing ($a + bi$), FOIL binomial expansion ($(a_1 + b_1 i)(a_2 + b_2 i)$), imaginary unit square substitution ($i^2 = -1$), real component subtraction ($a_1 a_2 - b_1 b_2$), imaginary component cross-multiplication ($a_1 b_2 + a_2 b_1$), and string formatting ($R + I\text{i}$) on representative complex numbers:

- **Input:**
  - First complex number: $num_1 = \text{"1+1i"}$
  - Second complex number: $num_2 = \text{"1+1i"}$
- **Required output:** `"0+2i"`
  - Format specification: `"real+imaginaryi"`
  - Complex arithmetic fundamental identity:
    $$
    i^2 = \mathbf{-1}
    $$
- **Step-by-Step Algebraic Trace:**
  - **Step 1: Component Extraction:**
    - Parse $num_1 = \text{"1+1i"}$:
      - Strip terminal `'i'`: `"1+1"`
      - Split on `'+'`: tokens `["1", "1"]`
      - Real coefficient: $a_1 = \mathbf{1}$
      - Imaginary coefficient: $b_1 = \mathbf{1}$
    - Parse $num_2 = \text{"1+1i"}$:
      - Real coefficient: $a_2 = \mathbf{1}$
      - Imaginary coefficient: $b_2 = \mathbf{1}$
  - **Step 2: Binomial FOIL Expansion:**
    $$
    (a_1 + b_1 i) \cdot (a_2 + b_2 i) = a_1 a_2 + a_1 b_2 i + b_1 a_2 i + b_1 b_2 i^2
    $$
  - **Step 3: Apply $i^2 = -1$ Identity:**
    $$
    b_1 b_2 i^2 = b_1 b_2 (-1) = -(b_1 b_2)
    $$
    Group real and imaginary terms:
    $$
    \text{Real Part } R = a_1 a_2 - b_1 b_2
    $$
    $$
    \text{Imaginary Part } I = a_1 b_2 + a_2 b_1
    $$
  - **Step 4: Arithmetic Calculation ($num_1 = 1+1i, \; num_2 = 1+1i$):**
    - Real component:
      $$
      R = (1 \times 1) - (1 \times 1) = 1 - 1 = \mathbf{0}
      $$
    - Imaginary component:
      $$
      I = (1 \times 1) + (1 \times 1) = 1 + 1 = \mathbf{2}
      $$
  - **Step 5: String Construction:**
    $$
    \text{Formatted Output} = \text{str}(R) + \text{"+"} + \text{str}(I) + \text{"i"} = \mathbf{\text{"0+2i"}}
    $$
- **Negative Imaginary Part Instance ($num_1 = \text{"1+-1i"}, num_2 = \text{"1+-1i"}$):**
  - $a_1 = 1, b_1 = -1, a_2 = 1, b_2 = -1$.
  - Real part: $R = (1)(1) - (-1)(-1) = 1 - 1 = \mathbf{0}$.
  - Imaginary part: $I = (1)(-1) + (1)(-1) = -1 + (-1) = \mathbf{-2}$.
  - Formatted: `"0+-2i"`. (Note the exact requirement preserves `+-2i` format).
- **Complex Conjugate Instance ($num_1 = \text{"100+-100i"}, num_2 = \text{"100+100i"}$):**
  - $R = 100 \times 100 - (-100 \times 100) = 10000 - (-10000) = \mathbf{20000}$.
  - $I = 100 \times 100 + 100 \times (-100) = 10000 - 10000 = \mathbf{0}$.
  - Formatted: `"20000+0i"`.

This instance demonstrates ring operations over Gaussian integers $\mathbb{Z}[i]$, mathematically proves why the algebraic reduction $(a_1 a_2 - b_1 b_2) + (a_1 b_2 + a_2 b_1)i$ completely determines complex multiplication, and derives $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two complex numbers $num_1$ and $num_2$ as strings in the form `"real+imaginaryi"`:
Return the string representing their algebraic multiplication, adhering strictly to the form `"real+imaginaryi"`.

```text
Evaluating (1 + 1i) * (1 + 1i):
  = 1*1 + 1*1i + 1i*1 + 1i*1i
  = 1 + 1i + 1i + 1*(i^2)
  Since i^2 = -1:
  = 1 + 2i - 1
  = 0 + 2i

Result: "0+2i"
```

### The Invariant of Gaussian Integer Multiplication
Every complex number is a point $z = a + bi$ in the complex plane.
Multiplying two numbers $z_1 = a_1 + b_1 i$ and $z_2 = a_2 + b_2 i$:
$$
z_1 z_2 = (a_1 a_2 - b_1 b_2) + (a_1 b_2 + a_2 b_1)i
$$
The problem is reduced to:
1. Parsing $a_1, b_1$ and $a_2, b_2$ from their respective input strings.
2. Computing the two integer products.
3. Serializing the resulting integers into the exact target format string.

---

## 2. Conceptual Foundation & Invariants

### 1. Token Extraction:
Given string $s$:
- Strip the trailing character `'i'`: $s[:-1]$.
- Split on `'+'`: produces two tokens $[token_1, token_2]$.
- Parse integers:
  $$
  a = \text{int}(token_1), \quad b = \text{int}(token_2)
  $$

### 2. Multiplicative Reduction:
$$
R = a_1 \cdot a_2 - b_1 \cdot b_2
$$
$$
I = a_1 \cdot b_2 + a_2 \cdot b_1
$$

### 3. Formatting Rule:
The output must format both numbers with a literal `+` between them and an `i` at the end:
$$
\text{Output} = R + \text{"+"} + I + \text{"i"}
$$
If $I$ is negative (e.g. $-2$), the output must be formatted as `0+-2i`, retaining both the addition symbol and the negative sign.

> **Gaussian Closure Invariant.** The set of Gaussian integers $\mathbb{Z}[i]$ is closed under multiplication, ensuring that $R$ and $I$ are strictly integers.

---

## 3. Step-by-Step Worked Execution

We trace $num_1 = \text{"1+1i"}$ and $num_2 = \text{"1+1i"}$:

---

### Step 1: Parse Inputs
- $num_1 \to a_1 = 1, \; b_1 = 1$.
- $num_2 \to a_2 = 1, \; b_2 = 1$.

---

### Step 2: Compute Real Part $R$
$$
R = a_1 \cdot a_2 - b_1 \cdot b_2
$$
$$
R = (1 \times 1) - (1 \times 1) = 1 - 1 = \mathbf{0}
$$

---

### Step 3: Compute Imaginary Part $I$
$$
I = a_1 \cdot b_2 + a_2 \cdot b_1
$$
$$
I = (1 \times 1) + (1 \times 1) = 1 + 1 = \mathbf{2}
$$

---

### Step 4: String Interpolation
$$
\text{str}(0) + \text{"+"} + \text{str}(2) + \text{"i"} = \mathbf{\text{"0+2i"}}
$$

---

## 4. Complete Execution Trace

| $num_1$ | $num_2$ | $(a_1, b_1)$ | $(a_2, b_2)$ | Real $R = a_1 a_2 - b_1 b_2$ | Imag $I = a_1 b_2 + a_2 b_1$ | Result String |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"1+1i"` | `"1+1i"` | $(1, 1)$ | $(1, 1)$ | $1 - 1 = 0$ | $1 + 1 = 2$ | **`"0+2i"`** |
| `"1+-1i"` | `"1+-1i"` | $(1, -1)$ | $(1, -1)$ | $1 - 1 = 0$ | $-1 + (-1) = -2$ | **`"0+-2i"`** |
| `"1+0i"` | `"1+0i"` | $(1, 0)$ | $(1, 0)$ | $1 - 0 = 1$ | $0 + 0 = 0$ | **`"1+0i"`** |
| `"0+1i"` | `"0+1i"` | $(0, 1)$ | $(0, 1)$ | $0 - 1 = -1$ | $0 + 0 = 0$ | **`"-1+0i"`** |

---

## 5. Boundary Cases & Failure Modes

- **Zero Real or Imaginary Coefficients:** Both parts are always present in the input and output (e.g. `"1+0i"`, `"0+1i"`, `"0+0i"`), never omitted.
- **Negative Imaginary Numbers:** Strings like `"1+-1i"` have the plus sign explicitly present. Splitting on `'+'` isolates the negative number `"-1"` cleanly.
- **Large Coefficients ($a, b = \pm 100$):** $R$ and $I$ can reach $\pm 20,000$, well within 32-bit integer limits.

---

## 6. Traps & Common Anti-Patterns

- **Normalizing `+-` into `-`:** Formatting `0+-2i` as `0-2i` fails the test cases! The format strictly specifies `real+imaginaryi`, requiring the literal `+` even before a negative sign.
- **Dropping `0` or `0i`:** Omitting `0+` or `+0i` to make `"2i"` or `"0"` violates the standardized schema.
- **Using Floating Point Numbers:** Parsing as floats can introduce precision errors (e.g. `0.999999999`). All arithmetic must be performed in exact integer arithmetic.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - String parsing and splitting takes $O(1)$ time for strings of length $\le 10$.
  - Integer multiplication and addition takes $O(1)$ time.
  - Total Time: strictly $\mathcal{O}(1)$. Completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space.
