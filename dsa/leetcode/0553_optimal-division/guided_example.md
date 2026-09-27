# Guided Example: Optimal Division

We trace the step-by-step algebraic fractional decomposition ($N / D$), numerator/denominator allocation bounds ($nums[0] \in N, \; nums[1] \in D$), reciprocal inversion multiplication theorem ($a / (b / c / d) = (a \cdot c \cdot d) / b$), and canonical parenthetical formatting on representative integer arrays:

- **Input:** $nums = [1000, 100, 10, 2]$
- **Required output:** `"1000/(100/10/2)"`
  - Problem goal: Add parentheses to the sequence of float divisions $nums[0] / nums[1] / \dots / nums[n-1]$ to produce the **maximum possible numerical quotient**.
  - Number constraints: Array length $n \ge 1$; elements are integers $nums[i] \in [2, 1000]$.
- **Algebraic Maximization Proof & Trace:**
  - Any valid parenthesization can be simplified to a single fraction:
    $$
    \frac{\text{Numerator}}{\text{Denominator}}
    $$
  - **Inflexible Anchors:**
    1. The first element $nums[0]$ is the very first dividend and **must always appear in the numerator**.
    2. The second element $nums[1]$ is divided by $nums[0]$ and **must always appear in the denominator**.
  - **Movable Tail Elements ($nums[2 \dots n-1]$):**
    - Every subsequent element $nums[i]$ ($i \ge 2$) can end up either in the numerator or in the denominator depending on parenthesis nesting.
    - Since every integer in $nums$ is $\ge 2$, to maximize the quotient $\frac{\text{Numerator}}{\text{Denominator}}$, we must:
      - Maximize the numerator (multiply by as many elements as possible).
      - Minimize the denominator (divide by as few elements as possible).
    - Can we place **every element** from $nums[2]$ to $nums[n-1]$ into the numerator?
  - **The Universal Reciprocal Inversion Formula:**
    - Group all elements from index 1 to the end inside a single parenthesized block:
      $$
      nums[0] / (nums[1] / nums[2] / \dots / nums[n-1])
      $$
    - Evaluate the parenthesized denominator:
      $$
      (nums[1] / nums[2] / \dots / nums[n-1]) = \frac{nums[1]}{nums[2] \times nums[3] \times \dots \times nums[n-1]}
      $$
    - Dividing $nums[0]$ by this fraction:
      $$
      nums[0] \div \left( \frac{nums[1]}{\prod_{i=2}^{n-1} nums[i]} \right) = \frac{nums[0] \times \prod_{i=2}^{n-1} nums[i]}{nums[1]}
      $$
    - All tail elements $\{nums[2], \dots, nums[n-1]\}$ invert into the numerator as multipliers!
    - For $[1000, 100, 10, 2]$:
      $$
      \frac{1000 \times 10 \times 2}{100} = \frac{20000}{100} = \mathbf{200}
      $$
    - *Compare with default left-to-right division:*
      $$
      ((1000 / 100) / 10) / 2 = (10 / 10) / 2 = 1 / 2 = \mathbf{0.5}
      $$
      Nesting produces $200$, which is $400\times$ larger!
- **Formatting Rule Derivation:**
  - If $n = 1$: No division possible $\implies \text{str}(nums[0]) \implies \mathbf{\text{"2"}}$.
  - If $n = 2$: Only one division $\implies \text{"nums[0]/nums[1]"} \implies \mathbf{\text{"1000/100"}}$.
  - If $n \ge 3$: Wrap indices $1 \dots n-1$ in parentheses:
    $$
    nums[0] + \text{"/("} + \text{"/".join}(nums[1 \dots n-1]) + \text{")"} \implies \mathbf{\text{"1000/(100/10/2)"}}
    $$

This instance demonstrates reciprocal algebraic optimization over operator associativity trees, mathematically proves why a single outer parenthesis pair achieves the absolute supremum for positive quotients $\ge 2$, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Add parentheses to the expression $nums[0] / nums[1] / \dots / nums[n-1]$ to **maximize the numerical result**.
Return the corresponding expression string.

```text
Evaluating [1000, 100, 10, 2]:

Default (Left-to-Right):
  1000 / 100 / 10 / 2 = 10 / 10 / 2 = 0.5

Optimal Parenthesization:
  1000 / (100 / 10 / 2)
  = 1000 / (10 / 2)
  = 1000 / 5
  = 200

Result String: "1000/(100/10/2)"
```

### The Closed-Form Maximization Theorem
- No dynamic programming or search is needed!
- For any parenthesized expression of $a_0 / a_1 / \dots / a_{n-1}$:
  $$
  \text{Result} = \frac{a_0 \cdot \prod_{i \in \text{Num}} a_i}{a_1 \cdot \prod_{j \in \text{Den}} a_j}
  $$
- $a_0$ is always in the numerator.
- $a_1$ is always in the denominator.
- By placing parentheses around $a_1 / a_2 / \dots / a_{n-1}$:
  - The inner expression evaluates to $\frac{a_1}{a_2 \times \dots \times a_{n-1}}$.
  - Inverting it places **every single subsequent number** into the numerator.
- Since all numbers are $\ge 2$, this configuration maximizes the numerator and minimizes the denominator simultaneously, achieving the theoretical global maximum!

---

## 2. Conceptual Foundation & Invariants

### 1. The Three Structural Regimes:
- **Case 1 ($n = 1$):**
  $$
  \text{str}(nums[0])
  $$
- **Case 2 ($n = 2$):**
  $$
  nums[0] + \text{"/"} + nums[1]
  $$
  *(No parentheses needed)*
- **Case 3 ($n \ge 3$):**
  $$
  nums[0] + \text{"/("} + \text{"/".join}(nums[1:]) + \text{")"}
  $$

> **Supremum Invariant.** The expression $nums[0] / (nums[1] / \dots / nums[n-1])$ minimizes the denominator to $\frac{nums[1]}{\prod_{i=2}^{n-1} nums[i]}$, which mathematically maximizes the overall quotient across all possible binary operator trees.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1000, 100, 10, 2]$ ($n = 4$):

---

### Step 1: Check Length
- $n = 4 \ge 3$.
- Select Case 3 format:
  $$
  \text{prefix} = nums[0] = 1000
  $$
  $$
  \text{tail} = nums[1:] = [100, 10, 2]
  $$

---

### Step 2: Join Tail Elements
Join elements of $nums[1:]$ with `/`:
$$
\text{"/".join}([\text{"100"}, \text{"10"}, \text{"2"}]) = \mathbf{\text{"100/10/2"}}
$$

---

### Step 3: Format String with Parentheses
Wrap tail inside parentheses preceded by `nums[0]/`:
$$
\text{"1000/("} + \text{"100/10/2"} + \text{")"} = \mathbf{\text{"1000/(100/10/2)"}}
$$

---

## 4. Complete Execution Trace

| Input $nums$ | Length $n$ | Branch | Numerator Multipliers | Denominator Divisors | Output String |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[2]` | $1$ | Case 1 | $2$ | $1$ | **`"2"`** |
| `[3, 4]` | $2$ | Case 2 | $3$ | $4$ | **`"3/4"`** |
| `[1000, 100, 10, 2]` | $4$ | Case 3 | $1000 \times 10 \times 2$ | $100$ | **`"1000/(100/10/2)"`** |
| `[6, 2, 3]` | $3$ | Case 3 | $6 \times 3$ | $2$ | **`"6/(2/3)"`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Must return `"2"`, without slashes or parentheses.
- **$n = 2$:** Must return `"3/4"`, without unnecessary parentheses (not `"3/(4)"`).
- **All Identical Elements ($[2, 2, 2, 2]$):** Same rule holds: `"2/(2/2/2)"` yields $\frac{2 \times 2 \times 2}{2} = 4$.

---

## 6. Traps & Common Anti-Patterns

- **Writing a Full Memoized DP Parser:** Although interval DP can compute optimal parenthesization, it is completely redundant here because the mathematical proof guarantees that a single outer parenthesis pair is always optimal.
- **Adding Redundant Parentheses for $n = 2$:** Formatting $[3, 4]$ as `3/(4)` is redundant and fails output format checks.
- **Simulating Floating-Point Calculations:** Using float arithmetic to compare combinations introduces precision rounding errors. Generating the closed-form string directly eliminates numerical instability.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Converting $N$ integers to strings: $O(N)$.
  - Joining strings with delimiter `/`: $O(N)$.
  - Total Time: strictly $\mathcal{O}(N)$. For $N \le 10$, completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the formatted output string.
