# Guided Example: Minimum Size Subarray Sum

We trace the step-by-step two-pointer sliding window expansion, monotonic sum contraction, and minimal length tracking on representative positive integer arrays:

- **Input:** $\text{target} = 7, \quad \text{nums} = [2, 3, 1, 2, 4, 3]$
- **Required output:** $2$ (Subarray $[4, 3]$ has sum $7 \ge 7$ and length $2$)
- **Single-Element Match Instance:** $\text{target} = 4, \quad \text{nums} = [1, 4, 4] \implies 1$ (Individual element meets target)
- **Unreachable Target Instance:** $\text{target} = 11, \quad \text{nums} = [1, 1, 1, 1] \implies 0$ (Total sum $< 11$)

This instance demonstrates the variable-size sliding window paradigm on positive numbers, explains why positivity guarantees monotonic prefix sums ($\text{nums}[i] > 0$), proves why contracting $L$ whenever $\text{sum} \ge \text{target}$ identifies the minimal valid window, and operates in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given a positive target integer $\text{target} = 7$ and an array of strictly positive integers:
$$
\text{nums} = [2, 3, 1, 2, 4, 3]
$$
Find the **minimal length** of a contiguous subarray whose sum is **greater than or equal to** $\text{target}$. If no such subarray exists, return $0$.

Evaluating valid candidate subarrays with sum $\ge 7$:
- Prefix $[2, 3, 1, 2]$: sum $= 8 \ge 7$, length $= 4$.
- Interior $[3, 1, 2, 4]$: sum $= 10 \ge 7$, length $= 4$.
- Subarray $[1, 2, 4]$: sum $= 7 \ge 7$, length $= 3$.
- Subarray $[4, 3]$: sum $= 7 \ge 7$, length $= \mathbf{2}$.
The minimal length is $2$.

A brute-force evaluation tests all $O(N^2)$ pairs $(L, R)$.
However, because all elements are strictly positive ($\text{nums}[i] > 0$):
- Expanding $R$ strictly **increases** the sum.
- Contracting $L$ strictly **decreases** the sum.
This monotonic property guarantees that both pointers only advance forward, achieving linear $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### The Monotonic Sliding Window Protocol
Initialize:
$$
L = 0, \quad \text{current\_sum} = 0, \quad \text{min\_len} = \infty
$$

For right pointer $R$ from $0$ to $N - 1$:
1. **Window Expansion:**
   Add $\text{nums}[R]$ to the accumulator:
   $$
   \text{current\_sum} \leftarrow \text{current\_sum} + \text{nums}[R]
   $$
2. **Window Contraction:**
   While $\text{current\_sum} \ge \text{target}$:
   - Update minimal length:
     $$
     \text{min\_len} \leftarrow \min(\text{min\_len}, \, R - L + 1)
     $$
   - Shrink window from the left to test if a shorter valid subarray ends at $R$:
     $$
     \text{current\_sum} \leftarrow \text{current\_sum} - \text{nums}[L]
     $$
     $$
     L \leftarrow L + 1
     $$

3. **Termination:**
   If $\text{min\_len} == \infty$, return $0$; otherwise return $\text{min\_len}$.

> **Invariant.** For each right boundary $R$, the while loop tests every valid left boundary $L$ such that $\sum_{k=L}^{R} \text{nums}[k] \ge \text{target}$, ensuring the shortest valid window ending at $R$ is recorded.

---

## 3. Step-by-Step Worked Execution

We trace the sliding window across $\text{nums} = [2, 3, 1, 2, 4, 3]$ with $\text{target} = 7$:

### Step 1: $R = 0 \dots 2$ (Expansion Phase)
- $R = 0$ ($x = 2$): $\text{current\_sum} = 2 < 7$. Window: $[2]$.
- $R = 1$ ($x = 3$): $\text{current\_sum} = 2 + 3 = 5 < 7$. Window: $[2, 3]$.
- $R = 2$ ($x = 1$): $\text{current\_sum} = 5 + 1 = 6 < 7$. Window: $[2, 3, 1]$.

---

### Step 2: $R = 3$ ($x = 2$, First Valid Window)
- Add $\text{nums}[3]$: $\text{current\_sum} = 6 + 2 = \mathbf{8} \ge 7$.
- Window $[0, 3]$ is valid!
  $$
  \text{min\_len} = \min(\infty, \, 3 - 0 + 1) = \mathbf{4}
  $$
- Contract from left:
  - Subtract $\text{nums}[0] = 2$: $\text{current\_sum} = 8 - 2 = 6 < 7$.
  - Advance $L \leftarrow 1$.

---

### Step 3: $R = 4$ ($x = 4$, Shrinking to Length 3)
- Add $\text{nums}[4]$: $\text{current\_sum} = 6 + 4 = \mathbf{10} \ge 7$.
- Iteration 1 ($L = 1$):
  - $\text{min\_len} = \min(4, \, 4 - 1 + 1) = 4$.
  - Subtract $\text{nums}[1] = 3$: $\text{current\_sum} = 10 - 3 = \mathbf{7} \ge 7$.
  - Advance $L \leftarrow 2$.
- Iteration 2 ($L = 2$):
  - $\text{min\_len} = \min(4, \, 4 - 2 + 1) = \mathbf{3}$ *(Subarray $[1, 2, 4]$)*.
  - Subtract $\text{nums}[2] = 1$: $\text{current\_sum} = 7 - 1 = 6 < 7$.
  - Advance $L \leftarrow 3$.

---

### Step 4: $R = 5$ ($x = 3$, Optimal Length 2 Achieved!)
- Add $\text{nums}[5]$: $\text{current\_sum} = 6 + 3 = \mathbf{9} \ge 7$.
- Iteration 1 ($L = 3$):
  - $\text{min\_len} = \min(3, \, 5 - 3 + 1) = 3$.
  - Subtract $\text{nums}[3] = 2$: $\text{current\_sum} = 9 - 2 = \mathbf{7} \ge 7$.
  - Advance $L \leftarrow 4$.
- Iteration 2 ($L = 4$):
  - $\text{min\_len} = \min(3, \, 5 - 4 + 1) = \mathbf{2}$ *(Subarray $[4, 3]$)*.
  - Subtract $\text{nums}[4] = 4$: $\text{current\_sum} = 7 - 4 = 3 < 7$.
  - Advance $L \leftarrow 5$.

Search completes. The global minimal length is $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
Target: 7, nums: [ 2,  3,  1,  2,  4,  3 ]

R = 0 (2): sum = 2 < 7
R = 1 (3): sum = 5 < 7
R = 2 (1): sum = 6 < 7
R = 3 (2): sum = 8 >= 7 -> min_len = 4, shrink L=0 (sum=6, L=1)
R = 4 (4): sum = 10 >= 7-> shrink L=1 (sum=7), min_len = 3, shrink L=2 (sum=6, L=3)
R = 5 (3): sum = 9 >= 7 -> shrink L=3 (sum=7), min_len = 2, shrink L=4 (sum=3, L=5)

Final Minimal Length: 2
```

| $R$ | Added $x$ | Cumulative Sum | Valid ($\ge 7$)? | Contracted $L$ Indices | Recorded `min_len` | Active Window Range |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 2 | 2 | No | - | $\infty$ | `[2]` |
| 1 | 3 | 5 | No | - | $\infty$ | `[2, 3]` |
| 2 | 1 | 6 | No | - | $\infty$ | `[2, 3, 1]` |
| **3** | **2** | **8** | **Yes** | $L: 0 \to 1$ | **4** | `[3, 1, 2]` |
| **4** | **4** | **10** | **Yes** | $L: 1 \to 3$ | **3** | `[2, 4]` |
| **5** | **3** | **9** | **Yes** | $L: 3 \to 5$ | **2** | **`[4, 3]` (Final: 2)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every recorded window length $R - L + 1$ satisfies $\sum_{i=L}^{R} \text{nums}[i] \ge \text{target}$. Since we minimize over all valid windows encountered, the result cannot overestimate or violate the target constraint.

**Completeness.** Suppose the true optimal subarray is $[L^*, R^*]$. When $R = R^*$, $\text{current\_sum}$ contains all elements from $L \le L^*$ to $R^*$. Because elements are strictly positive, any window starting before $L^*$ has sum $\ge \text{target}$ and will be shrunk. Thus, $L$ will advance until it reaches $L^*$, at which point length $R^* - L^* + 1$ is evaluated and compared.

---

## 6. Traps This Instance Exposes

- **Zero or Negative Numbers:** This two-pointer sliding window relies strictly on the guarantee that $\text{nums}[i] > 0$. If negative numbers were present, expanding $R$ could decrease the sum and contracting $L$ could increase it, breaking monotonicity (requiring a monotonic deque or prefix-sum hash map as in LeetCode 862).
- **Target Never Reached:** If $\sum \text{nums} < \text{target}$, $\text{min\_len}$ remains $\infty$. The algorithm must return $0$, not $\infty$.
- **Off-by-One in Window Length:** Window length spanning indices $[L, R]$ is $R - L + 1$, not $R - L$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. The right pointer $R$ moves from $0$ to $N - 1$. The left pointer $L$ only moves forward and advances at most $N$ times across the entire algorithm. Total pointer operations are bounded by $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only the scalar variables $L, R, \text{current\_sum}$, and $\text{min\_len}$.