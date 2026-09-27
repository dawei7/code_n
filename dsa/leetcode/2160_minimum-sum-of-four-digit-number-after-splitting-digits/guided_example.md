# Guided Example: Minimum Sum of Four Digit Number After Splitting Digits

We analyze and execute the greedy place-value weight assignment algorithm on a representative four-digit problem instance, establishing why the rearrangement inequality mandates pairing the smallest digits with the highest positional decimal weights.

- **Input:** `num = 2932`
- **Output:** `52`

This instance illustrates digit extraction, sorting in non-decreasing order, positional place-value weighting ($10, 10, 1, 1$), and linear combination minimization.

---

## 1. Problem Overview & Representative Instance

We are given a four-digit integer `num` ($1000 \le \text{num} \le 9999$). We must partition its four constituent digits into two non-empty integers, $\text{num}_1$ and $\text{num}_2$, using every digit occurrence exactly once. The digits within $\text{num}_1$ and $\text{num}_2$ may be arranged in any order. Leading zeros are permitted in either integer and contribute zero to its numeric value.

The goal is to determine the minimum possible value of the sum:
$$\text{Sum} = \text{num}_1 + \text{num}_2$$

In our representative instance:
- `num = 2932`.
- Digits present: $\{2, 9, 3, 2\}$.

We must find the digit assignment that produces the minimal possible sum.

---

## 2. Mathematical & Algorithmic Principles

### Structural Partitioning: Equal Digit Distribution

Four digits can be partitioned into two positive integers in two length configurations:
1. **$1$-digit and $3$-digit numbers:**
   $$\text{num}_1 = d_A, \quad \text{num}_2 = 100 \cdot d_B + 10 \cdot d_C + d_D$$
   The positional weights of the four digits are:
   $$\{100, \, 10, \, 1, \, 1\}$$
2. **Two $2$-digit numbers:**
   $$\text{num}_1 = 10 \cdot d_A + d_B, \quad \text{num}_2 = 10 \cdot d_C + d_D$$
   The positional weights of the four digits are:
   $$\{10, \, 10, \, 1, \, 1\}$$

Because $10 \cdot d_A + 10 \cdot d_C$ is strictly smaller than $100 \cdot d_B$ whenever positive digits occupy the hundreds place, allocating two digits to each integer strictly dominates or ties the $1$-digit/$3$-digit split. Therefore, the optimal configuration is always two 2-digit numbers:
$$\text{Sum} = 10 \cdot (d_A + d_C) + (d_B + d_D)$$

### The Rearrangement Inequality

Let the four digits sorted in non-decreasing order be:
$$d_0 \le d_1 \le d_2 \le d_3$$

The objective function is a linear combination of the digits:
$$\text{Sum} = w_0 d_{\pi(0)} + w_1 d_{\pi(1)} + w_2 d_{\pi(2)} + w_3 d_{\pi(3)}$$
where the multiset of positional weights is $\{10, 10, 1, 1\}$.

By the **Rearrangement Inequality**, a sum of products $\sum w_i d_i$ is minimized when the sequences are sorted in opposite directions:
- The largest weights ($10$ and $10$) must be paired with the smallest digits ($d_0$ and $d_1$).
- The smallest weights ($1$ and $1$) must be paired with the largest digits ($d_2$ and $d_3$).

Thus, the minimal sum is:
$$\text{Sum}_{\min} = 10 \cdot (d_0 + d_1) + (d_2 + d_3)$$

Equivalently, forming the two numbers $\text{num}_1 = 10 \cdot d_0 + d_2$ and $\text{num}_2 = 10 \cdot d_1 + d_3$ achieves this global minimum.

| Place-Value Role | Positional Weight | Assigned Digit | Concrete Value (`num = 2932`) |
|---|---|---|---|
| Tens Digit 1 | $10$ | Smallest digit $d_0$ | $2$ (contributes $20$) |
| Tens Digit 2 | $10$ | Second smallest digit $d_1$ | $2$ (contributes $20$) |
| Units Digit 1 | $1$ | Third smallest digit $d_2$ | $3$ (contributes $3$) |
| Units Digit 2 | $1$ | Largest digit $d_3$ | $9$ (contributes $9$) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the algorithm on `num = 2932`.

```
Input: num = 2932
Extracted digits: [2, 9, 3, 2]
Sorted digits:    [2, 2, 3, 9]

Tens digits:   d_0 = 2,  d_1 = 2
Units digits:  d_2 = 3,  d_3 = 9

Formed numbers:
num_1 = 10 * 2 + 3 = 23
num_2 = 10 * 2 + 9 = 29

Sum = 23 + 29 = 52
```

### Step 1: Extract Individual Decimal Digits
Decompose $2932$ via modulo and integer division:
- $2932 \bmod 10 = 2$
- $\lfloor 2932 / 10 \rfloor \bmod 10 = 3$
- $\lfloor 2932 / 100 \rfloor \bmod 10 = 9$
- $\lfloor 2932 / 1000 \rfloor \bmod 10 = 2$

Unordered digit multiset: $[2, 9, 3, 2]$.

### Step 2: Sort Digits in Non-Decreasing Order
Sort the four digits ascending:
$$d = [2, 2, 3, 9]$$
- $d_0 = 2$ (minimum)
- $d_1 = 2$
- $d_2 = 3$
- $d_3 = 9$ (maximum)

### Step 3: Assign Place Values
- Tens place multipliers: $d_0 = 2$ and $d_1 = 2$.
  $$\text{Tens Contribution} = 10 \cdot (d_0 + d_1) = 10 \cdot (2 + 2) = 10 \cdot 4 = 40$$
- Units place multipliers: $d_2 = 3$ and $d_3 = 9$.
  $$\text{Units Contribution} = 1 \cdot (d_2 + d_3) = 1 \cdot (3 + 9) = 12$$

### Step 4: Compute Minimal Sum
Combine tens and units contributions:
$$\text{Total Sum} = 40 + 12 = 52$$

Alternatively, reconstructing the two distinct numbers:
- $\text{num}_1 = 10 \cdot d_0 + d_2 = 10(2) + 3 = 23$.
- $\text{num}_2 = 10 \cdot d_1 + d_3 = 10(2) + 9 = 29$.
- $\text{Sum} = 23 + 29 = 52$.

Final result emitted: $52$.

---

## 4. Comprehensive State Trace

The table below compares the optimal place-value assignment against competing alternative digit configurations:

| Partition Strategy | Assignment Formula | Decimal Values Formed | Sum Expression | Evaluated Sum | Relative Optimality |
|---|---|---|---|---|---|
| **Optimal (2 + 2 Balanced)** | $10(d_0+d_1) + (d_2+d_3)$ | $\text{num}_1 = 23, \, \text{num}_2 = 29$ | $40 + 12$ | **52** | **Global Minimum** |
| Suboptimal 2 + 2 | $10(d_0+d_2) + (d_1+d_3)$ | $\text{num}_1 = 22, \, \text{num}_2 = 39$ | $50 + 11$ | $61$ | $+9$ excess |
| Suboptimal 2 + 2 | $10(d_0+d_3) + (d_1+d_2)$ | $\text{num}_1 = 23, \, \text{num}_2 = 92$ | $110 + 5$ | $115$ | $+63$ excess |
| 1 + 3 Split (Best) | $d_0 + (100d_1 + 10d_2 + d_3)$ | $\text{num}_1 = 2, \, \text{num}_2 = 239$ | $2 + 239$ | $241$ | $+189$ excess |
| 1 + 3 Split (Worst) | $d_3 + (100d_0 + 10d_1 + d_2)$ | $\text{num}_1 = 9, \, \text{num}_2 = 223$ | $9 + 223$ | $232$ | $+180$ excess |

The $2 + 2$ balanced partition with small digits in the tens positions strictly minimizes the total sum.

---

## 5. Algorithmic Correctness & Soundness

### Formal Optimality Proof
Let $D = \{d_0 \le d_1 \le d_2 \le d_3\}$ be the four sorted digits.
1. Any two integers formed from $D$ have total value $S = \sum_{i=0}^3 w_i d_{\pi(i)}$, where $\{w_0, w_1, w_2, w_3\}$ are the positional powers of $10$.
2. Because the total number of digits is $4$, the only possible weight multisets are $W_1 = \{100, 10, 1, 1\}$ and $W_2 = \{10, 10, 1, 1\}$.
3. For any permutation of digits, the inner product with $W_2$ satisfies:
   $$\min_\pi \sum_{i=0}^3 W_2[i] d_{\pi(i)} = 10 d_0 + 10 d_1 + d_2 + d_3$$
   by the Rearrangement Inequality.
4. For $W_1$, the minimum is $100 d_0 + 10 d_1 + d_2 + d_3$.
5. Comparing the two minima:
   $$(100 d_0 + 10 d_1 + d_2 + d_3) - (10 d_0 + 10 d_1 + d_2 + d_3) = 90 d_0 \ge 0$$
   Since $d_0 \ge 0$, $W_2$ is always less than or equal to $W_1$.
   Hence, $10(d_0 + d_1) + (d_2 + d_3)$ is globally optimal across all possible partitions and permutations.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Zeros Present in Input:** `num = 4009`. Sorted digits: $[0, 0, 4, 9]$.
   - Tens digits: $d_0 = 0, d_1 = 0$.
   - Units digits: $d_2 = 4, d_3 = 9$.
   - Formed numbers: $10(0) + 4 = 4$ and $10(0) + 9 = 9$.
   - Sum: $4 + 9 = 13$. Leading zeros naturally collapse to single-digit numbers.
2. **All Digits Equal:** `num = 7777`. Sorted: $[7, 7, 7, 7]$. Sum $= 10(7 + 7) + (7 + 7) = 140 + 14 = 154$.
3. **Distinct Ascending Digits:** `num = 1234`. Digits $[1, 2, 3, 4]$. Numbers $13$ and $24$. Sum $= 13 + 24 = 37$.

### Common Anti-Patterns
- **Forming 3-Digit and 1-Digit Numbers:** Placing a digit in the hundreds column multiplies that digit by $100$, incurring an unnecessary $90 \times d_i$ penalty.
- **Placing Large Digits in Tens Place:** Creating $92 + 32 = 124$ instead of $29 + 23 = 52$ inverts the rearrangement principle.
- **Permutation Exhaustion:** Generating all $4! = 24$ permutations is unnecessary when sorting $4$ digits and applying $10(d_0 + d_1) + d_2 + d_3$ executes in closed form.

---

## 7. Complexity Analysis

### Time Complexity
- Digit extraction requires $4$ division and modulo operations: $O(1)$.
- Sorting an array of $4$ digits takes at most $6$ comparisons: $O(1)$.
- Computing the arithmetic formula $10(d_0 + d_1) + (d_2 + d_3)$ takes $O(1)$ operations.
- Total time complexity is strictly $O(1)$, executing in under $1$ microsecond.

### Auxiliary Space Complexity
- A fixed 4-element array stores the four extracted digits.
- No dynamic memory allocation or recursion stack is used.
- Total auxiliary space complexity is strictly $O(1)$.
