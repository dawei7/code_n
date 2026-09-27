# Guided Example: Construct the Rectangle

We trace the step-by-step mathematical geometric bounding ($W \le \sqrt{area} \le L$), square-root ceiling initialization ($w = \lfloor\sqrt{area}\rfloor$), descending factor search ($area \pmod w == 0$), minimal difference gap guarantee ($L - W$), and quotient pair emission on representative area targets:

- **Input:** $area = 4$
- **Required output:** `[2, 2]`
  - Constraints:
    1. $L \times W = area$
    2. $L \ge W$
    3. The difference $L - W$ must be minimized.
  - **Mathematical Analysis:**
    - Since $L \ge W$ and $L \times W = area$:
      $$
      W^2 \le L \times W = area \implies W \le \sqrt{area}
      $$
    - The difference $L - W = \frac{area}{W} - W$ is a strictly decreasing function of $W$ for $W \in (0, \sqrt{area}]$.
    - Therefore, to minimize $L - W$, **$W$ must be as large as possible** ($\le \sqrt{area}$).
  - **Execution Trace:**
    - Calculate starting width:
      $$
      w = \lfloor\sqrt{4}\rfloor = \mathbf{2}
      $$
    - Check divisibility:
      $$
      4 \pmod 2 == 0 \quad (\mathbf{True})
      $$
    - Length:
      $$
      L = 4 / 2 = \mathbf{2}
      $$
    - Pair: $[L, W] = \mathbf{[2, 2]}$ with difference $L - W = 0$.
- **Prime Number Instance ($area = 37$):**
  - Start at $w = \lfloor\sqrt{37}\rfloor = 6$:
    - $37 \pmod 6 = 1 \ne 0 \implies w \leftarrow 5$
    - $37 \pmod 5 = 2 \ne 0 \implies w \leftarrow 4$
    - $37 \pmod 4 = 1 \ne 0 \implies w \leftarrow 3$
    - $37 \pmod 3 = 1 \ne 0 \implies w \leftarrow 2$
    - $37 \pmod 2 = 1 \ne 0 \implies w \leftarrow 1$
    - $37 \pmod 1 = 0 \implies L = 37 / 1 = 37$
  - Minimal difference pair: $\mathbf{[37, 1]}$
- **Large Composite Instance ($area = 122122$):**
  - $\sqrt{122122} \approx 349.46 \implies$ scans downwards from $349$ to find the first divisor.

This instance demonstrates mathematical divisor optimization via monotonic gap functions, mathematically proves why descending from $\sqrt{area}$ guarantees the minimal aspect ratio difference, and derives $O(\sqrt{area})$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $area$:
Design a rectangular page with length $L$ and width $W$ satisfying:
1. The area of the rectangle must equal $area$: $L \times W = area$.
2. The length $L$ must be at least the width $W$: $L \ge W$.
3. The difference $L - W$ should be as small as possible.
Return $[L, W]$.

```text
Given area = 4:
  Possible factor pairs (L >= W):
    [4, 1] -> Difference L - W = 3
    [2, 2] -> Difference L - W = 0  <- Minimal!

Best rectangle: [2, 2]
```

### The Monotonicity of the Aspect Ratio Gap
Consider the difference function as a function of the width $W$:
$$
f(W) = L - W = \frac{area}{W} - W
$$
Taking the derivative with respect to $W$:
$$
f'(W) = -\frac{area}{W^2} - 1 < 0
$$
- Because $f'(W)$ is strictly negative for all $W > 0$, the difference $L - W$ is **strictly monotonically decreasing** as $W$ increases!
- Since $L \ge W \implies W \le \sqrt{area}$, the maximum possible value $W$ can take is $\lfloor\sqrt{area}\rfloor$.
- Thus, the first integer divisor $W$ we encounter when scanning downwards from $\lfloor\sqrt{area}\rfloor$ to $1$ is **guaranteed to yield the minimum possible difference $L - W$**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Square-Root Search Algorithm:
1. Initialize width candidate:
   $$
   w = \lfloor\sqrt{area}\rfloor
   $$
2. While $area \pmod w \ne 0$:
   $$
   w \leftarrow w - 1
   $$
3. Compute length:
   $$
   L = area / w
   $$
4. Return $[L, w]$.

> **Optimality Invariant.** Any other factor pair $(L', W')$ with $W' < W$ must satisfy $L' > L$, yielding a strictly larger gap $L' - W' > L - W$.

---

## 3. Step-by-Step Worked Execution

We trace $area = 4$:

---

### Step 1: Initialize $w$ at Square Root
$$
w = \lfloor\sqrt{4}\rfloor = 2
$$

---

### Step 2: Test Divisibility
$$
area \pmod w = 4 \pmod 2 = 0
$$
Since the remainder is 0, $w = 2$ is an exact divisor of $4$.

---

### Step 3: Compute Complementary Dimension $L$
$$
L = \frac{area}{w} = \frac{4}{2} = 2
$$
Check constraints:
- $L \times W = 2 \times 2 = 4 == area$ (Pass).
- $L \ge W \iff 2 \ge 2$ (Pass).
- $L - W = 0$ (Absolute global minimum).

---

### Final Pair:
$$
\mathbf{[2, 2]}
$$

---

## 4. Complete Execution Trace

| Target Area | Initial $\lfloor\sqrt{area}\rfloor$ | Divisor Candidates Tested | First Divisor $W$ Found | Complement $L = area / W$ | Difference $L - W$ | Result $[L, W]$ |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **$4$** | $2$ | $2$ | **$2$** | $2$ | $0$ | **`[2, 2]`** |
| **$6$** | $2$ | $2$ | **$2$** | $3$ | $1$ | **`[3, 2]`** |
| **$37$** | $6$ | $6, 5, 4, 3, 2, 1$ | **$1$** | $37$ | $36$ | **`[37, 1]`** |
| **$100$** | $10$ | $10$ | **$10$** | $10$ | $0$ | **`[10, 10]`** |
| **$12$** | $3$ | $3$ | **$3$** | $4$ | $1$ | **`[4, 3]`** |

---

## 5. Boundary Cases & Failure Modes

- **Unit Area ($area = 1$):** $w = \lfloor\sqrt{1}\rfloor = 1 \implies L = 1 \implies \mathbf{[1, 1]}$.
- **Prime Areas ($area = 37$):** No factors exist except $1$ and $37$. Loop decrements all the way to $w = 1 \implies \mathbf{[37, 1]}$.
- **Perfect Squares ($area = K^2$):** $\sqrt{area} = K$ divides $area$ on the very first attempt $\implies \mathbf{[K, K]}$ with optimal difference $0$.

---

## 6. Traps & Common Anti-Patterns

- **Searching from $1$ Upwards to $\sqrt{area}$:** Scanning $1, 2, 3, \dots$ requires keeping track of the best factor seen so far and doesn't terminate early. Scanning downwards from $\sqrt{area}$ terminates on the very first hit.
- **Floating-Point Imprecision in Sqrt:** For huge areas ($10^7$), rounding errors in `float(sqrt(area))` could theoretically overshoot by $1$. Using integer truncation `int(sqrt(area))` is safe and exact.
- **Returning $[W, L]$ Instead of $[L, W]$:** The problem requires $L \ge W$, meaning the larger number must be the first element of the array.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case (prime number), the while loop decrements $w$ from $\lfloor\sqrt{area}\rfloor$ down to $1$.
  - Number of iterations is bounded by $\sqrt{area}$.
  - Total Time: $\mathcal{O}(\sqrt{area})$. For $area \le 10^7$, $\sqrt{10^7} \approx 3,162$ operations, completing in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using scalar integers.
