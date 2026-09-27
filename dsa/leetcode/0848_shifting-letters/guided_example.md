# Guided Example: Shifting Letters

We trace the step-by-step prefix shift aggregation, right-to-left suffix sum accumulation ($t = \sum_{k=i}^{n-1} shifts[k]$), modulo 26 cyclic alphabet rotation ($(\text{ord}(c) - \text{ord}('a') + t) \bmod 26$), in-place character transversion, and $O(N)$ transformed string generation on representative shift schedules:

- **Input:**
  $$
  s = \text{"abc"}, \quad shifts = [3, 5, 9]
  $$
- **Required output:**
  $$
  \text{"rpl"}
  $$
  - Prefix shift semantics:
    - We are given a string $s$ of length $n$ and an array $shifts$ of length $n$.
    - For each index $i$, the operation shifts the first $i + 1$ characters of $s$ forward in the alphabet by $shifts[i]$ positions.
    - Shifting wraps cyclically around the 26-letter English alphabet (`'z'` wraps to `'a'`).
    - Objective: Return the final string after all $n$ prefix shifts are executed.
    - For $s = \text{"abc"}$ and $shifts = [3, 5, 9]$:
      - Operation 0 ($i = 0, shift = 3$): shifts $s[0..0]$ by 3 $\implies$ `"dbc"`.
      - Operation 1 ($i = 1, shift = 5$): shifts $s[0..1]$ by 5 $\implies$ `"igc"`.
      - Operation 2 ($i = 2, shift = 9$): shifts $s[0..2]$ by 9 $\implies$ `"rpl"`.
      - Cumulative shifts per index:
        - Index 2 ('c'): receives only operation 2 $\implies$ shift $= 9$.
        - Index 1 ('b'): receives operations 1 and 2 $\implies$ shift $= 5 + 9 = 14$.
        - Index 0 ('a'): receives operations 0, 1, and 2 $\implies$ shift $= 3 + 5 + 9 = 17$.
      - Result: `"rpl"`.
- **Suffix Sum & Modulo Invariant:**
  - **The Suffix Sum Decomposition:**
    - Notice that operation $i$ affects all characters at indices $k \le i$.
    - Inverting this relation: character at index $k$ is affected by **all operations from $k$ up to $n - 1$**:
      $$
      \text{total\_shift}(k) = \sum_{i = k}^{n - 1} shifts[i]
      $$
    - Naively shifting prefix after prefix takes $\mathcal{O}(N^2)$ time.
    - However, $\text{total\_shift}(k)$ is simply the **suffix sum** of the array $shifts$!
  - **Right-to-Left Monotone Pass:**
    - Maintain a running suffix sum accumulator $t$, initialized to 0.
    - Walk backwards from $i = n - 1$ down to 0:
      - Add current shift:
        $$
        t \leftarrow (t + shifts[i]) \bmod 26
        $$
      - The character at index $i$ shifts forward by $t$ positions:
        $$
        new\_char = \text{chr}\big( \text{ord}('a') + (\text{ord}(s[i]) - \text{ord}('a') + t) \bmod 26 \big)
        $$
    - Every character is updated in strictly $\mathcal{O}(1)$ time, yielding an optimal $\mathcal{O}(N)$ overall runtime.
- **Step-by-Step Worked Execution Trace on $s = \text{"abc"}$ ($n = 3$):**
  - Convert string to character list: $s = [\text{'a'}, \text{'b'}, \text{'c'}]$.
  - Initialize running shift accumulator: $t = 0$.
  - **Index 2 ($s[2] = \text{'c'}, shifts[2] = 9$):**
    - Suffix sum update:
      $$
      t \leftarrow 0 + 9 = \mathbf{9}
      $$
    - Initial coordinate of `'c'`: $\text{ord}('c') - \text{ord}('a') = 2$.
    - Shifted coordinate:
      $$
      (2 + 9) \bmod 26 = 11 \bmod 26 = \mathbf{11} \implies \mathbf{\text{'l'}}
      $$
    - Update: $s[2] \leftarrow \text{'l'}$.
  - **Index 1 ($s[1] = \text{'b'}, shifts[1] = 5$):**
    - Suffix sum update:
      $$
      t \leftarrow 9 + 5 = \mathbf{14}
      $$
    - Initial coordinate of `'b'`: $\text{ord}('b') - \text{ord}('a') = 1$.
    - Shifted coordinate:
      $$
      (1 + 14) \bmod 26 = 15 \bmod 26 = \mathbf{15} \implies \mathbf{\text{'p'}}
      $$
    - Update: $s[1] \leftarrow \text{'p'}$.
  - **Index 0 ($s[0] = \text{'a'}, shifts[0] = 3$):**
    - Suffix sum update:
      $$
      t \leftarrow 14 + 3 = \mathbf{17}
      $$
    - Initial coordinate of `'a'`: $\text{ord}('a') - \text{ord}('a') = 0$.
    - Shifted coordinate:
      $$
      (0 + 17) \bmod 26 = 17 \bmod 26 = \mathbf{17} \implies \mathbf{\text{'r'}}
      $$
    - Update: $s[0] \leftarrow \text{'r'}$.
  - **Assembled String Output:**
    $$
    s = [\text{'r'}, \; \text{'p'}, \; \text{'l'}] \implies \mathbf{\text{"rpl"}}
    $$
- **Alphabet Wrap-Around Trace ($s = \text{"z"}, shifts = [1]$):**
  - $t = 1$. Initial coordinate 25.
  - $(25 + 1) \bmod 26 = 26 \bmod 26 = 0 \implies \mathbf{\text{'a'}}.$
- **Large Shift Magnitude Trace ($shifts[i] = 10^9$):**
  - Modulo arithmetic handles large integers seamlessly: $10^9 \bmod 26 = 14$.
  - Suffix sum can be reduced modulo 26 at each step to prevent large integer expansion.

This instance demonstrates linear difference array inversion and cyclic group actions on free alphabets $\mathbb{Z}_{26}$, mathematically proves why reversing the direction of integration converts interval update queries into single-pass cumulative potentials, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$ and array $shifts$:
Operation $i$ shifts the first $i + 1$ characters of $s$ forward by $shifts[i]$ positions.
Find the final string.

```text
s = "abc", shifts = [ 3, 5, 9 ]

Shifts per position:
  Index 2 ('c'): receives shifts[2] = 9                 -> 'c' + 9  = 'l'
  Index 1 ('b'): receives shifts[1] + shifts[2] = 14    -> 'b' + 14 = 'p'
  Index 0 ('a'): receives shifts[0] + shifts[1] + shifts[2] = 17 -> 'a' + 17 = 'r'

Result: "rpl"
```

### The Invariant of Suffix Sum Shifting
- Character at index $i$ shifts by the **suffix sum**:
  $$
  \text{total\_shift}(i) = \sum_{k = i}^{n - 1} shifts[k]
  $$
- Scanning backwards from right to left accumulates this running sum in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Suffix Integration:
$$
T(i) = \sum_{k = i}^{n - 1} shifts[k] \pmod{26}
$$

### 2. Coordinate Transversion:
$$
s'[i] = \text{'a'} + \Big( (s[i] - \text{'a'} + T(i)) \bmod 26 \Big)
$$

> **Difference Equation Invariant.** Prefix addition is the adjoint of difference encoding. Denoting by $D$ the backward difference operator on sequences, the shift operator satisfies $D(T)_i = shifts[i]$. Integrating from the boundary $n - 1$ reconstructs the net transformation potential in a single linear pass.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abc"}, shifts = [3, 5, 9]$:

---

### Step 1: Index 2
- $t = 9$.
- $'c' + 9 = 'l'$.

---

### Step 2: Index 1
- $t = 9 + 5 = 14$.
- $'b' + 14 = 'p'$.

---

### Step 3: Index 0
- $t = 14 + 3 = 17$.
- $'a' + 17 = 'r'$.

---

### Step 4: Output
$$
\mathbf{\text{"rpl"}}
$$

---

## 4. Complete Execution Trace

| Position $i$ | Character $s[i]$ | Base Index $s[i] - \text{'a'}$ | Running Shift $t$ | Modulo Shift $t \bmod 26$ | Transformed Character |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | `'c'` | $2$ | $9$ | $9$ | **`'l'`** |
| $1$ | `'b'` | $1$ | $14$ | $14$ | **`'p'`** |
| **$0$** | **`'a'`** | **$0$** | **$17$** | **$17$** | **`'r'`** |
| **Final** | — | — | — | — | **`"rpl"`** |

---

## 5. Boundary Cases & Failure Modes

- **Full Wrap-Around ($'z' \to 'a'$):** $(25 + 1) \bmod 26 = 0 \implies 'a'$.
- **Single Character ($s = "a", shifts = [52]$):** $52 \bmod 26 = 0 \implies 'a'$ unchanged.
- **Large Shifts ($shifts[i] = 10^9$):** Modulo 26 prevents integer overflow.
- **Uniform Shifts ($s = "aaa", shifts = [1, 2, 3]$):** Outputs `"gfd"`.

---

## 6. Traps & Common Anti-Patterns

- **Simulating Each Shift Step Directly ($O(N^2)$):** Applying each prefix shift iteratively modifies $O(N)$ characters $N$ times, causing severe TLE for $N = 10^5$. Suffix sum completes in $O(N)$.
- **Scanning Forward Instead of Backward:** Scanning forward requires precomputing the entire suffix sum array; scanning backward computes and applies the shift in a single pass with $O(1)$ extra space.
- **Neglecting Modulo During Suffix Sum:** Accumulating without modulo can create arbitrarily large numbers; maintain $t = (t + shifts[i]) \bmod 26$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single backward pass through string of length $N$: $\mathcal{O}(N)$.
  - Constant-time scalar modulo arithmetic per character: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond the mutable character list.
