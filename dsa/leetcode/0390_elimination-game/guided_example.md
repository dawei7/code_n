# Guided Example: Elimination Game

We trace the step-by-step arithmetic progression interval state reduction ($[a_1, a_n]$ with common difference $step$), alternating directional parity updates (Left-to-Right vs Right-to-Left), logarithmic count halving ($cnt \leftarrow \lfloor cnt / 2 \rfloor$), and final survivor convergence on representative elimination ranges:

- **Input:** $n = 9$
- **Required output:** $6$
  - Initial state ($arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]$):
    - $a_1 = 1, a_n = 9, step = 1, cnt = 9, i = 0$
  - Pass 0 (Left-to-Right, odd count $cnt = 9$):
    - Deletes odd-indexed elements: $[1, 3, 5, 7, 9]$ eliminated
    - Head advances: $a_1 \mathrel{+}= 1 = 2$
    - Tail contracts ($cnt$ odd): $a_n \mathrel{-}= 1 = 8$
    - Survivors: $[2, 4, 6, 8]$, parameters: $cnt = 4, step = 2$
  - Pass 1 (Right-to-Left, even count $cnt = 4$):
    - Deletes from right: $[8, 4]$ eliminated
    - Tail contracts: $a_n \mathrel{-}= 2 = 6$
    - Head stays ($cnt$ even): $a_1 = 2$
    - Survivors: $[2, 6]$, parameters: $cnt = 2, step = 4$
  - Pass 2 (Left-to-Right, even count $cnt = 2$):
    - Deletes from left: $[2]$ eliminated
    - Head advances: $a_1 \mathrel{+}= 4 = 6$
    - Tail stays ($cnt$ even): $a_n = 6$
    - Survivors: $[6]$, parameters: $cnt = 1$
  - Terminal survivor: $a_1 = \mathbf{6}$
- **Single Element Base Case:** $n = 1 \implies 1$
- **Power of Two:** $n = 8 \implies 6$
- **Boundary $10^9$ Scale:** Requires only $\approx 30$ iterations of scalar arithmetic

This instance demonstrates modeling large discrete collections via invariant arithmetic progressions, mathematically proves endpoint shift rules based on directional pass parity and survivor count, avoids allocating $O(N)$ memory, and operates in $O(\log N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 9$, consider the array $arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]$:
1. Start from left to right, remove the first number and every other number until the end.
2. Repeat from right to left, remove the rightmost number and every other number.
3. Keep alternating directions until a single number remains:

```text
Pass 0 (L -> R): [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
Eliminated:        x     x     x     x     x
Remaining:            2     4     6     8      (step = 2, cnt = 4)

Pass 1 (R -> L): [ 2,    4,    6,    8 ]
Eliminated:              x           x
Remaining:         2           6               (step = 4, cnt = 2)

Pass 2 (L -> R): [ 2,          6 ]
Eliminated:        x
Remaining:                     6               (step = 8, cnt = 1)

Final Remaining Number: 6
```

### The $O(1)$ Memory Arithmetic Progression Abstraction
Materializing an array of $10^9$ integers is impossible. However, after every elimination pass, the surviving elements form an **Arithmetic Progression (AP)**:
$$
a_k = a_1 + (k - 1) \cdot step
$$
We only need to maintain 4 scalars:
- $a_1$: Head of the surviving sequence.
- $a_n$: Tail of the surviving sequence.
- $step$: Common difference between consecutive survivors (doubles every pass).
- $cnt$: Total number of survivors (halves every pass).

---

## 2. Conceptual Foundation & Invariants

### 1. The Progression Update Rules:
At pass $i$ with direction ($i \% 2 == 0 \implies \text{L-to-R}$, $i \% 2 == 1 \implies \text{R-to-L}$):

1. **Left-to-Right ($i \% 2 == 0$):**
   - $a_1$ is always eliminated:
     $$
     a_1 \leftarrow a_1 + step
     $$
   - $a_n$ is eliminated if and only if $cnt$ is **odd**:
     $$
     \text{if } cnt \% 2 == 1: \quad a_n \leftarrow a_n - step
     $$

2. **Right-to-Left ($i \% 2 == 1$):**
   - $a_n$ is always eliminated:
     $$
     a_n \leftarrow a_n - step
     $$
   - $a_1$ is eliminated if and only if $cnt$ is **odd**:
     $$
     \text{if } cnt \% 2 == 1: \quad a_1 \leftarrow a_1 + step
     $$

3. **Step Doubling & Halving:**
   $$
   cnt \leftarrow \lfloor cnt / 2 \rfloor, \quad step \leftarrow step \times 2, \quad i \leftarrow i + 1
   $$

> **Invariant.** At every pass, the survivors are uniquely and exactly the arithmetic progression starting at $a_1$, ending at $a_n$, with spacing $step$ and count $cnt$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 9$:
Initial: $a_1 = 1, a_n = 9, step = 1, cnt = 9, i = 0$.

---

### Step 1: Pass 0 (Left-to-Right, $i = 0$)
- Direction: Left-to-Right ($i \% 2 == 0$).
- Count parity: $cnt = 9$ is **odd** ($cnt \% 2 == 1$).
- **Head Update:**
  $$
  a_1 \leftarrow a_1 + step = 1 + 1 = \mathbf{2}
  $$
- **Tail Update (odd count):**
  $$
  a_n \leftarrow a_n - step = 9 - 1 = \mathbf{8}
  $$
- Scale progression:
  $$
  cnt \leftarrow \lfloor 9 / 2 \rfloor = \mathbf{4}, \quad step \leftarrow 1 \times 2 = \mathbf{2}, \quad i \leftarrow 1
  $$
- Surviving AP: $[2, 4, 6, 8]$.

---

### Step 2: Pass 1 (Right-to-Left, $i = 1$)
- Direction: Right-to-Left ($i \% 2 == 1$).
- Count parity: $cnt = 4$ is **even** ($cnt \% 2 == 0$).
- **Tail Update:**
  $$
  a_n \leftarrow a_n - step = 8 - 2 = \mathbf{6}
  $$
- **Head Update (even count):**
  Since $cnt$ is even, deletions starting from the right eliminate positions $4, 2$ (values $8, 4$). Position 1 (value $2$) survives!
  $$
  a_1 \text{ remains } \mathbf{2}
  $$
- Scale progression:
  $$
  cnt \leftarrow \lfloor 4 / 2 \rfloor = \mathbf{2}, \quad step \leftarrow 2 \times 2 = \mathbf{4}, \quad i \leftarrow 2
  $$
- Surviving AP: $[2, 6]$.

---

### Step 3: Pass 2 (Left-to-Right, $i = 2$)
- Direction: Left-to-Right ($i \% 2 == 0$).
- Count parity: $cnt = 2$ is **even** ($cnt \% 2 == 0$).
- **Head Update:**
  $$
  a_1 \leftarrow a_1 + step = 2 + 4 = \mathbf{6}
  $$
- **Tail Update (even count):**
  Position 2 survives, so $a_n$ remains unchanged:
  $$
  a_n \text{ remains } \mathbf{6}
  $$
- Scale progression:
  $$
  cnt \leftarrow \lfloor 2 / 2 \rfloor = \mathbf{1}, \quad step \leftarrow 4 \times 2 = \mathbf{8}, \quad i \leftarrow 3
  $$
- Surviving AP: $[6]$.

---

### Step 4: Loop Termination
$cnt = 1 \le 1$. The loop terminates.
Return head:
$$
\mathbf{6}
$$

---

## 4. Complete Execution Trace

```text
n = 9
Pass 0 (L->R): a1=1+1=2, an=9-1=8, cnt=4, step=2
Pass 1 (R->L): an=8-2=6, a1=2,     cnt=2, step=4
Pass 2 (L->R): a1=2+4=6, an=6,     cnt=1, step=8
cnt == 1 -> Terminate -> Return a1 = 6
```

| Pass $i$ | Direction | Input Count $cnt$ | Parity | $step$ | Old $[a_1, a_n]$ | New $a_1$ | New $a_n$ | Surviving AP Elements |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | L $\to$ R | 9 | Odd | 1 | $[1, 9]$ | $1 + 1 = \mathbf{2}$ | $9 - 1 = \mathbf{8}$ | $[2, 4, 6, 8]$ |
| 1 | R $\to$ L | 4 | Even | 2 | $[2, 8]$ | $\mathbf{2}$ | $8 - 2 = \mathbf{6}$ | $[2, 6]$ |
| **2** | **L $\to$ R** | **2** | **Even** | **4** | **$[2, 6]$** | **$2 + 4 = \mathbf{6}$** | **$\mathbf{6}$** | **$[6]$** |
| **Exit**| - | 1 | - | 8 | $[6, 6]$ | **`6`** | **`6`** | **`6` (Final Answer)** |

---

## 5. Algorithmic Correctness

**Soundness.** Eliminating alternating elements from an arithmetic progression preserves constant difference between neighbors ($step' = 2 \cdot step$). Moving left-to-right always eliminates the first element $a_1$, replacing it with $a_1 + step$. Moving right-to-left eliminates the first element if and only if the number of elements is odd, because the odd number of steps from the right hits the first element. These mathematical transformations mirror the physical elimination game perfectly.

**Completeness.** Since $cnt$ is divided by 2 at each step ($cnt \leftarrow \lfloor cnt / 2 \rfloor$), the loop is guaranteed to terminate in exactly $\lfloor \log_2 n \rfloor$ iterations. At $cnt = 1$, only one element remains, which is stored in $a_1$.

---

## 6. Traps This Instance Exposes

- **Array Simulation TLE / MLE:** Creating a Python list `[1..n]` or `range(1, n+1)` takes $O(N)$ time and space, causing Memory Limit Exceeded for $n = 10^9$. The mathematical arithmetic progression approach solves it using 4 integer registers.
- **Parity on Right-to-Left:** On right-to-left passes, the head $a_1$ only changes if $cnt$ is odd. If $cnt$ is even, $a_1$ stays identical. Forgetting the `if cnt % 2:` check causes incorrect answers.
- **Bitwise Operators:** Using `cnt >>= 1` and `step <<= 1` ensures fast integer operations without floating-point division issues.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N = n$.
  - In each iteration, $cnt$ is halved.
  - The while loop executes at most $\lfloor \log_2 N \rfloor$ times.
  - Each iteration consists of $O(1)$ scalar additions and bit shifts.
  - For $N = 10^9$, $\log_2(10^9) \approx 30$ iterations, running in under $0.001$ ms.
- **Auxiliary Space Complexity:** $O(1)$ strict constant memory, storing only five scalar integer variables (`a1`, `an`, `i`, `step`, `cnt`).
