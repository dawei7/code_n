# Guided Example: Sum of Subsequence Widths

We trace the step-by-step contribution technique (counting element participation), array sorting invariance, combinatorial subset powers ($2^i$ and $2^{n-1-i}$), symmetric difference accumulation, and modular arithmetic on representative integer arrays:

- **Input:**
  $$
  nums = [2, 1, 3]
  $$
- **Required output:** `6`
  - Subsequence width definition:
    - The **width** of a non-empty sequence is defined as the difference between its maximum element and its minimum element:
      $$
      \text{width}(S) = \max(S) - \min(S)
      $$
    - We consider all $2^n - 1 = 2^3 - 1 = 7$ non-empty subsequences:
      - $[1] \implies 1 - 1 = 0$
      - $[2] \implies 2 - 2 = 0$
      - $[3] \implies 3 - 3 = 0$
      - $[1, 2] \implies 2 - 1 = 1$
      - $[2, 3] \implies 3 - 2 = 1$
      - $[1, 3] \implies 3 - 1 = 2$
      - $[1, 2, 3] \implies 3 - 1 = 2$
    - Sum of widths across all 7 subsequences:
      $$
      0 + 0 + 0 + 1 + 1 + 2 + 2 = \mathbf{6}
      $$
    - Result modulo $10^9 + 7$: $\mathbf{6}$.
- **The Contribution & Sorting Invariant:**
  - **Order Independence:**
    - The set of elements in a subsequence dictates its minimum and maximum regardless of the initial array order.
    - Sorting the array in non-decreasing order:
      $$
      nums[0] \le nums[1] \le \dots \le nums[n-1]
      $$
      does not change the multiset of all possible subsequence widths!
  - **The Principle of Linear Contribution:**
    - Instead of enumerating $2^n$ subsequences, we ask: **How many times does each element $nums[i]$ act as the maximum, and how many times as the minimum?**
    - **$nums[i]$ as Maximum:**
      - For $nums[i]$ to be the maximum of a subsequence, all other chosen elements must come from the $i$ elements smaller than or equal to it ($nums[0 \dots i-1]$).
      - There are $2^i$ such subsets. In each, $nums[i]$ adds $+nums[i]$ to the width.
    - **$nums[i]$ as Minimum:**
      - For $nums[i]$ to be the minimum of a subsequence, all other chosen elements must come from the $n - 1 - i$ elements larger than or equal to it ($nums[i+1 \dots n-1]$).
      - There are $2^{n - 1 - i}$ such subsets. In each, $nums[i]$ subtracts $-nums[i]$ from the width.
  - **Unified Symmetric Formula:**
    - Total sum of widths:
      $$
      \text{Total} = \sum_{i=0}^{n-1} nums[i] \cdot (2^i - 2^{n - 1 - i}) \pmod{10^9 + 7}
      $$
    - Factoring by powers of two:
      $$
      \text{Total} = \sum_{i=0}^{n-1} \left( nums[i] - nums[n - 1 - i] \right) \cdot 2^i \pmod{10^9 + 7}
      $$

---

## 1. Instance & Teaching Goal

Given $nums = [2, 1, 3]$, sort to $[1, 2, 3]$ and calculate the net coefficient for each index.

```text
Sorted Array: [1, 2, 3]
Index i:       0  1  2

Subsets where nums[i] is MAX (count = 2^i):
  nums[0] = 1: 2^0 = 1 subset  {[1]}                   -> +1 * 1
  nums[1] = 2: 2^1 = 2 subsets {[2], [1, 2]}           -> +2 * 2
  nums[2] = 3: 2^2 = 4 subsets {[3], [1, 3], [2, 3], [1, 2, 3]} -> +3 * 4

Subsets where nums[i] is MIN (count = 2^(n-1-i)):
  nums[0] = 1: 2^2 = 4 subsets {[1], [1, 2], [1, 3], [1, 2, 3]} -> -1 * 4
  nums[1] = 2: 2^1 = 2 subsets {[2], [2, 3]}           -> -2 * 2
  nums[2] = 3: 2^0 = 1 subset  {[3]}                   -> -3 * 1

Net Sum:
  (1 * 1 + 2 * 2 + 3 * 4) - (1 * 4 + 2 * 2 + 3 * 1)
= (1 + 4 + 12) - (4 + 4 + 3)
= 17 - 11 = 6
```

The teaching goal is to justify how swapping the summation order from $\sum_{\text{subsequences}} (\max - \min)$ to $\sum_{\text{elements}} (\text{occurrences as max} - \text{occurrences as min})$ reduces an exponential problem to $\mathcal{O}(N \log N)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Element Multiplicities:
For element at index $i$ in sorted array of length $n$:
$$
C_{\max}(i) = 2^i
$$
$$
C_{\min}(i) = 2^{n - 1 - i}
$$

### 2. Stream Accumulation Recurrence:
Starting with power accumulator $p = 1$:
For $i = 0 \dots n - 1$:
$$
ans \leftarrow \left( ans + (nums[i] - nums[n - 1 - i]) \times p \right) \pmod{10^9 + 7}
$$
$$
p \leftarrow (p \times 2) \pmod{10^9 + 7}
$$

---

## 3. Step-by-Step Worked Execution

Sorted array: $nums = [1, 2, 3]$, length $n = 3$.
Initialize: $ans = 0, p = 1, mod = 10^9 + 7$.

---

### Step 1: Index $i = 0$ ($nums[0] = 1$, counterpart $nums[2] = 3$)
- Power of two: $p = 2^0 = 1$.
- Term calculation:
  $$
  (nums[0] - nums[2]) \times p = (1 - 3) \times 1 = \mathbf{-2}
  $$
- Update accumulator:
  $$
  ans \leftarrow (0 - 2) \pmod{mod} = -2
  $$
- Advance power: $p \leftarrow (1 \times 2) = 2$.

---

### Step 2: Index $i = 1$ ($nums[1] = 2$, counterpart $nums[1] = 2$)
- Power of two: $p = 2^1 = 2$.
- Term calculation:
  $$
  (nums[1] - nums[1]) \times p = (2 - 2) \times 2 = \mathbf{0}
  $$
- Update accumulator:
  $$
  ans \leftarrow (-2 + 0) \pmod{mod} = -2
  $$
- Advance power: $p \leftarrow (2 \times 2) = 4$.

---

### Step 3: Index $i = 2$ ($nums[2] = 3$, counterpart $nums[0] = 1$)
- Power of two: $p = 2^2 = 4$.
- Term calculation:
  $$
  (nums[2] - nums[0]) \times p = (3 - 1) \times 4 = 2 \times 4 = \mathbf{8}
  $$
- Update accumulator:
  $$
  ans \leftarrow (-2 + 8) \pmod{mod} = \mathbf{6}
  $$
- Advance power: $p \leftarrow (4 \times 2) = 8$.

---

### Termination:
All indices processed.
- **Final Result:** **`6`**.

---

## 4. Complete Execution Trace

| Index $i$ | Sorted Element $nums[i]$ | Symmetric Counterpart $nums[n-1-i]$ | Difference $\Delta = nums[i] - nums[n-1-i]$ | Power $2^i$ | Term Contribution ($\Delta \times 2^i$) | Running Sum $ans \pmod{10^9 + 7}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1$ | $3$ | $1 - 3 = -2$ | $1$ | $-2$ | $-2 \equiv 10^9 + 5$ |
| $1$ | $2$ | $2$ | $2 - 2 = 0$ | $2$ | $0$ | $-2 \equiv 10^9 + 5$ |
| **$2$** | **$3$** | **$1$** | **$3 - 1 = 2$** | **$4$** | **$+8$** | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($nums = [2]$):** Length $n = 1$. $nums[0] - nums[0] = 2 - 2 = 0 \implies$ returns $0$.
- **All Elements Identical ($nums = [5, 5, 5]$):** Every non-empty subsequence has max == min $\implies$ width is always $0 \implies$ returns $0$.
- **Large Arrays ($N = 10^5$):** The exponential count $2^{10^5}$ must be maintained under modulo $10^9 + 7$ at each step via bit-shifting or incremental multiplication.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Subsequences:** Generating $2^N$ subsequences takes exponential time $\mathcal{O}(2^N)$ and exceeds memory immediately when $N > 25$.
- **Modulo Operations on Negative Numbers:** In languages where `%` preserves negative signs (e.g. C++), $(ans \% mod + mod) \% mod$ ensures non-negative answers. In Python, `%` handles negative numbers naturally.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ elements: $\mathcal{O}(N \log N)$.
  - Single pass through the array: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$, completing in $< 25$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - Sorting takes $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ depending on implementation.
  - Power variable $p$ and accumulator $ans$ require $\mathcal{O}(1)$ scalar registers.
