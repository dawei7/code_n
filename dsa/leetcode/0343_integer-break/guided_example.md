# Guided Example: Integer Break

We trace the step-by-step dynamic programming state transitions, optimal substructure decomposition ($f[i] = \max(j(i-j), j \cdot f[i-j])$), mathematical factor-of-3 optimality derivation (Euler's number $e \approx 2.718$), and maximum product extraction on representative integer instances:

- **Input:** $n = 10$
- **Required output:** $36$
  - Partition of 10 into $k \ge 2$ positive integers: $10 = 3 + 3 + 4$
  - Product: $3 \times 3 \times 4 = \mathbf{36}$
  - Comparison with alternative partitions:
    - $5 + 5 = 10 \implies 5 \times 5 = 25 < 36$
    - $2 + 2 + 2 + 2 + 2 = 10 \implies 2^5 = 32 < 36$
    - $3 + 3 + 2 + 2 = 10 \implies 36$
- **Base Case $n = 2$:** $1 + 1 = 2 \implies 1 \times 1 = 1$
- **Base Case $n = 3$:** $1 + 2 = 3 \implies 1 \times 2 = 2$
- **Base Case $n = 4$:** $2 + 2 = 4 \implies 2 \times 2 = 4$

This instance demonstrates dynamic programming with choices over multiple partition points, mathematically proves why breaking integers into factors of 3 maximizes the product, explains the decision boundary between $(i - j)$ and $f[i - j]$, and analyzes $O(N^2)$ time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n = 10$:
Break $n$ into the sum of $k \ge 2$ positive integers:
$$
n = a_1 + a_2 + \dots + a_k \quad (k \ge 2, \; a_i \ge 1)
$$
Maximize the product of those integers:
$$
P = \prod_{i=1}^k a_i
$$

```text
Target Integer: n = 10

Candidate Partitions:
2 + 2 + 2 + 2 + 2 = 10 -> Product = 2 * 2 * 2 * 2 * 2 = 32
5 + 5             = 10 -> Product = 5 * 5             = 25
3 + 3 + 4         = 10 -> Product = 3 * 3 * 4         = 36 (MAXIMUM!)

Optimal Product: 36
```

### Why Factors of 3 Maximize Product
Consider splitting a number $n$ into equal pieces of size $x$.
The product is $f(x) = x^{n/x} = (x^{1/x})^n$.
To maximize $x^{1/x}$, take the derivative of $g(x) = \frac{\ln x}{x}$:
$$
g'(x) = \frac{1 - \ln x}{x^2} = 0 \implies \ln x = 1 \implies x = e \approx 2.718
$$
The closest integers to $e$ are $2$ and $3$:
- $2^{1/2} = \sqrt{2} \approx 1.414$
- $3^{1/3} = \sqrt[3]{3} \approx 1.442$
Since $1.442 > 1.414$, breaking into pieces of size **3** is mathematically superior to size 2. When the remaining piece is 4, $2 \times 2 = 4 > 3 \times 1 = 3$, so we keep 4 as $2 \times 2$.

---

## 2. Conceptual Foundation & Invariants

### DP State Definition:
Let $f[i]$ denote the maximum product obtained by breaking integer $i$ into **at least 2 positive integers**:
- Array size: $n + 1$.
- Initial values: $f[i] = 1$ for all $i$.

### Recurrence Relation:
For each integer $i \in [2, n]$, consider splitting off an initial piece $j \in [1, i - 1]$.
The remaining part is $i - j$.
We have two options for the remaining part $(i - j)$:
1. **Do not break $(i - j)$ further:**
   Product is $j \times (i - j)$.
2. **Break $(i - j)$ further into optimal pieces:**
   Product is $j \times f[i - j]$.
Combining all possibilities:
$$
f[i] = \max_{1 \le j < i} \Big( f[i], \; j \cdot (i - j), \; j \cdot f[i - j] \Big)
$$

> **Invariant.** For every integer $i$, $f[i]$ stores the global maximum product obtainable by breaking $i$ into at least two positive integers.

---

## 3. Step-by-Step Worked Execution

We trace the DP array $f$ up to $n = 10$:

---

### Step 1: Base Integers $i = 2, 3, 4$
1. **$i = 2$:**
   - Only choice is $j = 1 \implies (2 - 1) = 1$.
   - $f[2] = 1 \times 1 = \mathbf{1}$.
2. **$i = 3$:**
   - $j = 1 \implies \max(1 \times 2, 1 \times f[2]=1) = 2$.
   - $j = 2 \implies \max(2 \times 1, 2 \times f[1]=2) = 2$.
   - $f[3] = \mathbf{2}$.
3. **$i = 4$:**
   - $j = 1 \implies 1 \times 3 = 3$.
   - $j = 2 \implies \max(2 \times 2, 2 \times f[2]=2) = 4$.
   - $f[4] = \mathbf{4}$ (Partition $2 + 2$).

---

### Step 2: Intermediate Values $i = 5, 6, 7$
1. **$i = 5$:**
   - Best choice: $j = 2 \implies 2 \times 3 = 6$ (or $j = 3 \implies 3 \times 2 = 6$).
   - $f[5] = \mathbf{6}$ (Partition $2 + 3$).
2. **$i = 6$:**
   - Best choice: $j = 3 \implies \max(3 \times 3, 3 \times f[3]=6) = 9$.
   - $f[6] = \mathbf{9}$ (Partition $3 + 3$).
3. **$i = 7$:**
   - Best choice: $j = 3 \implies \max(3 \times 4, 3 \times f[4]=12) = 12$.
   - $f[7] = \mathbf{12}$ (Partition $3 + 4$ or $3 + 2 + 2$).

---

### Step 3: Advancing to Target $i = 8, 9, 10$
1. **$i = 8$:**
   - Best choice: $j = 3 \implies \max(3 \times 5, 3 \times f[5]=18) = 18$.
   - $f[8] = \mathbf{18}$ (Partition $3 + 3 + 2$).
2. **$i = 9$:**
   - Best choice: $j = 3 \implies \max(3 \times 6, 3 \times f[6]=27) = 27$.
   - $f[9] = \mathbf{27}$ (Partition $3 + 3 + 3$).
3. **$i = 10$ (Target!):**
   - For $j = 3$:
     $$
     \max\big(3 \times 7 = 21, \; 3 \times f[7] = 3 \times 12 = 36\big) = \mathbf{36}
     $$
   - For $j = 4$:
     $$
     \max\big(4 \times 6 = 24, \; 4 \times f[6] = 4 \times 9 = 36\big) = \mathbf{36}
     $$
   - Maximum product recorded:
     $$
     f[10] = \mathbf{36}
     $$

---

## 4. Complete Execution Trace

```text
DP Table Progression:
f[2]  = 1 * 1                                    = 1
f[3]  = 1 * 2                                    = 2
f[4]  = 2 * 2                                    = 4
f[5]  = 2 * 3                                    = 6
f[6]  = 3 * 3                                    = 9
f[7]  = 3 * f[4] = 3 * 4                         = 12
f[8]  = 3 * f[5] = 3 * 6                         = 18
f[9]  = 3 * f[6] = 3 * 9                         = 27
f[10] = 3 * f[7] = 3 * 12                        = 36

Result: f[10] = 36
```

| Integer $i$ | Best Split $j$ | Remaining $i - j$ | Unbroken Product $j \times (i - j)$ | Broken Product $j \times f[i - j]$ | Optimal $f[i]$ | Partition Pieces |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 2 | 1 | 1 | $1 \times 1 = 1$ | $1 \times 1 = 1$ | 1 | $1 + 1$ |
| 3 | 1 | 2 | $1 \times 2 = 2$ | $1 \times 1 = 1$ | 2 | $1 + 2$ |
| 4 | 2 | 2 | $2 \times 2 = 4$ | $2 \times 1 = 2$ | 4 | $2 + 2$ |
| 5 | 2 | 3 | $2 \times 3 = 6$ | $2 \times 2 = 4$ | 6 | $2 + 3$ |
| 6 | 3 | 3 | $3 \times 3 = 9$ | $3 \times 2 = 6$ | 9 | $3 + 3$ |
| 7 | 3 | 4 | $3 \times 4 = 12$ | $3 \times 4 = 12$ | 12 | $3 + 2 + 2$ |
| 8 | 3 | 5 | $3 \times 5 = 15$ | $3 \times 6 = 18$ | 18 | $3 + 3 + 2$ |
| 9 | 3 | 6 | $3 \times 6 = 18$ | $3 \times 9 = 27$ | 27 | $3 + 3 + 3$ |
| **10** | **3** | **7** | **$3 \times 7 = 21$** | **$3 \times 12 = \mathbf{36}$** | **$\mathbf{36}$** | **$3 + 3 + 4$** |

---

## 5. Algorithmic Correctness

**Soundness.** For any partition of $i$ into two or more parts, let $j$ be the first part. The remaining sum $(i - j)$ is either kept as a single integer (yielding product $j(i-j)$) or partitioned further (yielding at most $j \cdot f[i-j]$ by inductive hypothesis). Evaluating the maximum over all $j \in [1, i-1]$ covers all valid two-or-more-part partitions.

**Completeness.** The outer loop iterates from $2$ to $n$, ensuring all subproblem values $f[i - j]$ are strictly precomputed before being referenced. Since every possible partition point $j$ is evaluated, no higher product can exist.

---

## 6. Traps This Instance Exposes

- **Missing the Unbroken Option $j(i - j)$:** For $i = 4$, $f[4 - 2] = f[2] = 1$. If we only evaluated $j \cdot f[i - j]$, $2 \times f[2] = 2$, missing the optimal choice $2 \times 2 = 4$. Comparing with $j(i - j)$ is essential when remaining pieces are small ($2$ and $3$).
- **The $k \ge 2$ Constraint:** The problem requires breaking $n$ into at least two parts. For $n = 3$, returning 3 is invalid; the maximum valid product is $1 \times 2 = 2$.
- **Partitioning into Ones:** Adding $1$ to a product ($1 \times x$) never increases it, and $1 + x < x \times \dots$ for $x > 1$. Ones are only used when forced by $n = 2$ and $n = 3$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N = n$. The outer loop runs $N$ times, and the inner loop runs $i$ times, resulting in $\sum_{i=2}^N i = O(N^2)$ transitions. (Alternatively solvable in $O(\log N)$ or $O(1)$ via the factor-of-3 greedy rule).
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the DP table $f$.