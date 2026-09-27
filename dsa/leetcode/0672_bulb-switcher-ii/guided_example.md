# Guided Example: Bulb Switcher II

We trace the step-by-step involution properties of toggle operations (pressing button twice $\equiv$ identity), abelian commutativity of XOR compositions ($2^4 = 16$ candidate button subsets), press parity reachability ($cnt \le presses \land cnt \equiv presses \pmod 2$), least-common-multiple spatial periodicity ($\text{lcm}(1, 2, 3) = 6$), and reachable state set enumeration on representative bulb and press constraints:

- **Input:** $n = 2, \quad presses = 1$
- **Required output:** `3`
  - System components:
    - $n = 2$ light bulbs, initially all turned **ON**: $[1, 1]$.
    - 4 control buttons:
      - Button 1: Flips **all** bulbs ($1, 2, 3, \dots$).
      - Button 2: Flips bulbs with **even labels** ($2, 4, 6, \dots$).
      - Button 3: Flips bulbs with **odd labels** ($1, 3, 5, \dots$).
      - Button 4: Flips bulbs with labels $3k + 1$ ($1, 4, 7, 10, \dots$).
    - Constraint: Exactly $presses = 1$ button press must be performed.
    - Objective: Return the total number of distinct bulb configurations achievable.
- **Algebraic Reductions & Invariants:**
  - **1. Involution & Order Invariance:**
    - Each button toggle is a binary addition modulo 2 ($\mathbb{F}_2$).
    - Pressing any button twice restores its original state:
      $$
      x \oplus 1 \oplus 1 = x
      $$
    - The sequence order of button presses does not matter because XOR is strictly commutative and associative.
    - Therefore, regardless of how large $presses$ is, each button is effectively pressed either **0 or 1 time**.
    - There are only $2^4 = \mathbf{16}$ conceivable button combination subsets!
  - **2. Parity Reachability Invariant:**
    - A subset of $cnt$ distinct buttons can be realized in $presses$ total operations if and only if:
      $$
      cnt \le presses \quad \land \quad cnt \equiv presses \pmod 2
      $$
    - Any excess presses ($presses - cnt$) can be dissipated in neutral pairs on any arbitrary button without changing the net outcome.
  - **3. Spatial Periodicity (Period 6):**
    - The periodicities of the four operations are:
      - Button 1: period 1
      - Button 2: period 2
      - Button 3: period 2
      - Button 4: period 3
    - The overall pattern repeats every $\text{lcm}(1, 2, 2, 3) = \mathbf{6}$ bulbs.
    - The state of all $n$ bulbs is completely and uniquely determined by the states of the first $\min(n, 6)$ bulbs.
- **Step-by-Step Worked Execution Trace on $n = 2, presses = 1$:**
  - Active bulb count: $n = 2$.
  - Initial configuration (all ON):
    $$
    S_{init} = [\text{ON}, \; \text{ON}] = [1, \; 1]
    $$
  - Target operations: $presses = 1$.
  - Parity constraint:
    $$
    cnt \le 1 \quad \land \quad cnt \equiv 1 \pmod 2 \implies cnt = \mathbf{1}
    $$
    (Exactly one distinct button must be pressed!).
  - **Evaluate All 4 Single-Button Options ($cnt = 1$):**
    - **Option A (Press Button 1 only):**
      - Flips both bulbs (all bulbs).
      - State: $[1 \oplus 1, \; 1 \oplus 1] = [\mathbf{0}, \; \mathbf{0}]$ (`[OFF, OFF]`).
      - State 1: `[OFF, OFF]`.
    - **Option B (Press Button 2 only):**
      - Flips even-indexed bulbs (Bulb 2).
      - Bulb 1 remains $1$; Bulb 2 becomes $1 \oplus 1 = 0$.
      - State: $[\mathbf{1}, \; \mathbf{0}]$ (`[ON, OFF]`).
      - State 2: `[ON, OFF]`.
    - **Option C (Press Button 3 only):**
      - Flips odd-indexed bulbs (Bulb 1).
      - Bulb 1 becomes $1 \oplus 1 = 0$; Bulb 2 remains $1$.
      - State: $[\mathbf{0}, \; \mathbf{1}]$ (`[OFF, ON]`).
      - State 3: `[OFF, ON]`.
    - **Option D (Press Button 4 only):**
      - Flips bulbs with index $3k + 1$ (for $k = 0 \implies$ Bulb 1).
      - Bulb 1 flips to $0$; Bulb 2 remains $1$.
      - State: $[\mathbf{0}, \; \mathbf{1}]$ (`[OFF, ON]`).
      - Notice: This produces the exact same state as Option C!
  - **Step 3: Deduplicate Configuration Set:**
    - Unique configurations collected:
      1. `[OFF, OFF]` (from Button 1)
      2. `[ON, OFF]` (from Button 2)
      3. `[OFF, ON]` (from Button 3 or Button 4)
    - Total unique configurations:
      $$
      |\text{Configurations}| = \mathbf{3}
      $$
    - Output: **`3`**.
- **Single Bulb Case ($n = 1, presses = 1$):**
  - Initial: `[ON]`.
  - Button 1, 3, 4 flip Bulb 1 to `[OFF]`.
  - Button 2 leaves Bulb 1 as `[ON]`.
  - Distinct states: `{[ON], [OFF]}` $\implies \mathbf{2}$.
- **Zero Presses ($presses = 0$):**
  - $cnt = 0$ only $\implies$ only initial state `[ON, ON]` reachable $\implies \mathbf{1}$.
- **Large Inputs ($n = 1000, presses = 1000$):**
  - Truncating $n$ to $\min(1000, 6) = 6$ bounds the problem to at most 8 possible binary states regardless of how large $n$ grows!

This instance demonstrates boolean ring involution, group-theoretic action reduction on periodic lattices, and finite configuration space enumeration, mathematically proving why four-button transformations collapse to at most 8 distinct quotient classes, and derives $O(1)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ bulbs initially ON and 4 buttons:
1. Flip all bulbs
2. Flip even bulbs
3. Flip odd bulbs
4. Flip $3k+1$ bulbs
After exactly $presses$ presses, find the **number of different bulb statuses**.

```text
n = 2 bulbs, presses = 1 press

Initial: [ ON, ON ]

Options for 1 press:
  Button 1 -> [ OFF, OFF ]
  Button 2 -> [ ON,  OFF ]
  Button 3 -> [ OFF, ON  ]
  Button 4 -> [ OFF, ON  ]  (same as Button 3 on 2 bulbs)

Unique states: [ OFF, OFF ], [ ON, OFF ], [ OFF, ON ]
Total = 3
```

### The Invariant of Periodicity and Involution
- Pressing a button twice is an identity operation ($x \oplus 1 \oplus 1 = x$).
- Only the parity ($presses \pmod 2$) and whether a button is toggled an odd/even number of times matters.
- The 4 operations have a combined spatial period of $\text{lcm}(1, 2, 2, 3) = 6$. Looking at more than 6 bulbs never reveals new states!

---

## 2. Conceptual Foundation & Invariants

### 1. Parity and Press Reachability:
A 4-bit mask $m \in [0, 15]$ represents which buttons are pressed:
$$
\text{valid}(m) \iff \text{popcount}(m) \le presses \quad \land \quad \text{popcount}(m) \equiv presses \pmod 2
$$

### 2. State Transformation on Period 6:
Let operations be 6-bit vectors:
- $op_1 = 111111_2$
- $op_2 = 010101_2$
- $op_3 = 101010_2$
- $op_4 = 100100_2$
Combined state:
$$
state = \bigoplus_{i=0}^3 \left( \text{if } m_i \text{ then } op_i \text{ else } 0 \right)
$$
Project to first $\min(n, 6)$ bits and collect unique values.

> **Periodic Factor Group Invariant.** The transformation semigroup generated by the four button operators is isomorphic to an abelian quotient group $\mathbb{Z}_2^4 / \mathcal{K}$ acting periodically on $(\mathbb{Z}_2)^6$, restricting the state space cardinality to at most 8 for all $n \ge 3$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2, presses = 1$:

---

### Step 1: Filter 16 Masks
- Masks with $cnt \le 1$ and $cnt \pmod 2 == 1$:
  - $0001_2$ (Button 1): $cnt = 1$.
  - $0010_2$ (Button 2): $cnt = 1$.
  - $0100_2$ (Button 3): $cnt = 1$.
  - $1000_2$ (Button 4): $cnt = 1$.

---

### Step 2: Compute 2-Bulb Projections
- Button 1: flips 1, 2 $\implies [0, 0]$.
- Button 2: flips 2 $\implies [1, 0]$.
- Button 3: flips 1 $\implies [0, 1]$.
- Button 4: flips 1 $\implies [0, 1]$.

---

### Step 3: Deduplicate
- $\{ [0, 0], [1, 0], [0, 1] \}$.
- Size is **`3`**.

---

## 4. Complete Execution Trace

| Tested Button Mask | Button Selected | 6-Bit Periodic Mask | Truncated to $n = 2$ Bits | Distinct Configuration |
|:---:|:---:|:---:|:---:|:---:|
| `0001` | Button 1 (All) | `111111` | `[0, 0]` | **State 1: `[OFF, OFF]`** |
| `0010` | Button 2 (Even) | `010101` | `[1, 0]` | **State 2: `[ON, OFF]`** |
| `0100` | Button 3 (Odd) | `101010` | `[0, 1]` | **State 3: `[OFF, ON]`** |
| `1000` | Button 4 ($3k+1$) | `100100` | `[0, 1]` | Duplicate of State 3 |
| **Total** | — | — | — | **`3` unique states** |

---

## 5. Boundary Cases & Failure Modes

- **$presses = 0$:** Only initial state reachable $\implies 1$.
- **$n = 1$:** Max 2 states (`[ON]` or `[OFF]`).
- **$n = 2, presses \ge 2$:** Reaches all 4 possible 2-bulb states $\implies 4$.
- **$n \ge 3, presses \ge 3$:** Reaches maximum possible ceiling of 8 states.

---

## 6. Traps & Common Anti-Patterns

- **Simulating All $N$ Bulbs ($N = 10^9$):** $N$ can be up to $1000$ (or larger); simulating an array of bulbs wastes memory. Cap $n$ at $\min(n, 6)$!
- **Ignoring Press Parity:** If $presses = 1$, you cannot reach the state produced by 2 button presses. Parity matching ($\equiv \pmod 2$) is required.
- **Overlooking That Button 1 + Button 2 = Button 3:** Flipping all bulbs and then flipping even bulbs is identical to flipping odd bulbs! The operations are linearly dependent over $\mathbb{F}_2$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Exactly 16 masks are evaluated.
  - Each mask executes $\mathcal{O}(1)$ bitwise operations.
  - Total Time: strictly constant $\mathcal{O}(1)$ time. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (hash set of at most 8 integers).
