# Guided Example: Binary Gap

We trace the step-by-step binary bit shifting, least significant bit inspection, previous set-bit index tracking, consecutive set-bit distance calculation, and maximum gap derivation on representative integers:

- **Input:**
  $$
  n = 22
  $$
- **Required output:** `2`
  - Binary gap definition:
    - Given a positive integer $n$, convert $n$ to its binary representation.
    - Find the **longest distance between two consecutive set bits** (bits with value $1$) in its binary representation.
    - Two set bits at indices $i$ and $j$ ($i < j$) are consecutive if there are no other $1$s strictly between indices $i$ and $j$.
    - The distance between them is $j - i$.
    - If there are fewer than two set bits in $n$, there are no consecutive set bits $\implies$ return $0$.
    - For $n = 22$:
      - Binary decomposition:
        $$
        22 = 16 + 4 + 2 = 2^4 + 2^2 + 2^1 = 10110_2
        $$
      - 0-indexed bit positions from the right (LSB at index 0):
        - Bit at index $1$ is $1$.
        - Bit at index $2$ is $1$.
        - Bit at index $4$ is $1$.
      - Consecutive pairs:
        - Pair 1: Between index $1$ and index $2$: distance $2 - 1 = 1$.
        - Pair 2: Between index $2$ and index $4$: distance $4 - 2 = 2$.
      - Maximum distance: $\max(1, 2) = \mathbf{2}$.
- **Right-Shift & Anchor Tracking Invariant:**
  - **Single-Pass Bit Extraction:**
    - Rather than converting $n$ into a formatted string or allocating an array of bit positions, we stream through bits from right to left using bitwise operations:
      $$
      \text{Current Bit} = n \ \& \ 1, \quad n \leftarrow n \gg 1
      $$
  - **Previous Set-Bit Memory ($pre$):**
    - Maintain the 0-indexed position of the most recently seen set bit, initialized to $\infty$ (unseen).
    - Maintain the current bit position index $cur$, initialized to $0$.
    - Whenever $n \ \& \ 1 == 1$:
      - If $pre$ is not $\infty$, a previous consecutive $1$ exists:
        $$
        ans \leftarrow \max(ans, cur - pre)
        $$
      - Update anchor: $pre \leftarrow cur$.
    - Increment bit position: $cur \leftarrow cur + 1$.
    - Repeat until $n = 0$.

---

## 1. Instance & Teaching Goal

Given $n = 22$ ($10110_2$), find the maximum gap between adjacent $1$s.

```text
Binary:   1   0   1   1   0
Index:    4   3   2   1   0

Bit 0: 0 -> no set bit
Bit 1: 1 -> first 1 encountered (anchor pre = 1)
Bit 2: 1 -> gap from pre(1) is 2 - 1 = 1. Update pre = 2.
Bit 3: 0 -> no set bit
Bit 4: 1 -> gap from pre(2) is 4 - 2 = 2. Update pre = 4.

Maximum gap = max(1, 2) = 2
```

The teaching goal is to show how consecutive neighborhood relations can be evaluated during an online bitwise scan without materializing the binary string.

---

## 2. Conceptual Foundation & Invariants

### 1. Mathematical Bit Position Set:
Let $S = \{k \in \mathbb{N}_0 \mid \lfloor n / 2^k \rfloor \equiv 1 \pmod 2\} = \{p_1, p_2, \dots, p_m\}$ with $p_1 < p_2 < \dots < p_m$.
The objective is:
$$
ans = \begin{cases}
0 & \text{if } |S| < 2 \\
\max_{1 \le i < m} (p_{i+1} - p_i) & \text{if } |S| \ge 2
\end{cases}
$$

---

## 3. Step-by-Step Worked Execution

We trace $n = 22$:
Initialize: $ans = 0, cur = 0, pre = \infty$.

---

### Step 1: Bit Position $cur = 0$
- Bit value: $n \ \& \ 1 = 22 \ \& \ 1 = 0$.
- Bit is $0$, no set bit.
- Advance: $n \leftarrow 22 \gg 1 = 11, cur \leftarrow 0 + 1 = 1$.
- State: $ans = 0, pre = \infty$.

---

### Step 2: Bit Position $cur = 1$
- Bit value: $n \ \& \ 1 = 11 \ \& \ 1 = 1$.
- **Set Bit Detected!**
- Check previous anchor: $pre = \infty$ (first set bit seen).
- Update anchor: $pre \leftarrow 1$.
- Advance: $n \leftarrow 11 \gg 1 = 5, cur \leftarrow 1 + 1 = 2$.
- State: $ans = 0, pre = 1$.

---

### Step 3: Bit Position $cur = 2$
- Bit value: $n \ \& \ 1 = 5 \ \& \ 1 = 1$.
- **Set Bit Detected!**
- Check previous anchor: $pre = 1 \ne \infty$.
- Distance: $cur - pre = 2 - 1 = 1$.
- Update answer: $ans = \max(0, 1) = \mathbf{1}$.
- Update anchor: $pre \leftarrow 2$.
- Advance: $n \leftarrow 5 \gg 1 = 2, cur \leftarrow 2 + 1 = 3$.
- State: $ans = 1, pre = 2$.

---

### Step 4: Bit Position $cur = 3$
- Bit value: $n \ \& \ 1 = 2 \ \& \ 1 = 0$.
- Bit is $0$, no set bit.
- Advance: $n \leftarrow 2 \gg 1 = 1, cur \leftarrow 3 + 1 = 4$.
- State: $ans = 1, pre = 2$.

---

### Step 5: Bit Position $cur = 4$
- Bit value: $n \ \& \ 1 = 1 \ \& \ 1 = 1$.
- **Set Bit Detected!**
- Check previous anchor: $pre = 2 \ne \infty$.
- Distance: $cur - pre = 4 - 2 = 2$.
- Update answer: $ans = \max(1, 2) = \mathbf{2}$.
- Update anchor: $pre \leftarrow 4$.
- Advance: $n \leftarrow 1 \gg 1 = 0, cur \leftarrow 4 + 1 = 5$.
- State: $ans = 2, pre = 4$.

---

### Termination:
$n = 0$, loop ends.
- **Return: `2`**.

---

## 4. Complete Execution Trace

| Current $n$ | Current Index $cur$ | Current Bit ($n \ \& \ 1$) | Action Taken | Previous Anchor $pre$ | Calculated Gap ($cur - pre$) | Running Max $ans$ |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| $22$ | $0$ | $0$ | Skip zero | $\infty$ | — | $0$ |
| $11$ | $1$ | **$1$** | Record first $1$ | $1$ | — | $0$ |
| $5$ | $2$ | **$1$** | Gap check & update $pre$ | $2$ | $2 - 1 = 1$ | $1$ |
| $2$ | $3$ | $0$ | Skip zero | $2$ | — | $1$ |
| **$1$** | **$4$** | **$1$** | **Gap check & update $pre$** | **$4$** | **$4 - 2 = 2$** | **`2`** |
| $0$ | $5$ | Terminated | Output result | $4$ | — | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Powers of Two (e.g. $n = 8 = 1000_2$):** Only one set bit exists. $pre$ is updated once, but $cur - pre$ is never evaluated $\implies$ returns $0$.
- **Alternating Bits (e.g. $n = 5 = 101_2$):** Set bits at index 0 and 2. Gap is $2 - 0 = 2$.
- **Adjacent Bits (e.g. $n = 3 = 11_2$):** Gap is $1 - 0 = 1$.
- **Max Input $n = 10^9 < 2^{30}$:** Loops at most 30 times.

---

## 6. Traps & Common Anti-Patterns

- **Measuring from Non-Adjacent $1$s:** Measuring distance across intervening $1$s violates the "consecutive set bits" requirement. Resetting $pre \leftarrow cur$ on every set bit guarantees strictly adjacent comparisons.
- **Converting to Python String `bin(n)`:** While valid, string manipulation allocates heap memory and runs string scans; bit-shifting operates in $\mathcal{O}(1)$ space on hardware CPU registers.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of bits in $n$ is $\lfloor \log_2 n \rfloor + 1$.
  - For $n \le 10^9$, at most $30$ iterations.
  - Each iteration performs $\mathcal{O}(1)$ bitwise operations.
  - Total Time: $\mathcal{O}(\log n)$, executing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space using three scalar integer registers ($ans, pre, cur$).
