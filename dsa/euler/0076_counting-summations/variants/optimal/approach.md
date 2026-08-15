# Counting Summations - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

It is possible to write five as a sum in exactly six different ways:
- $4 + 1$
- $3 + 2$
- $3 + 1 + 1$
- $2 + 2 + 1$
- $2 + 1 + 1 + 1$
- $1 + 1 + 1 + 1 + 1$

Let $p(n)$ denote the unrestricted integer partition function counting the number of ways to write $n \in \mathbb{N}$ as a sum of positive integers.

The objective is to find how many different ways one hundred ($100$) can be written as a sum of **at least two positive integers**:
$$N_{\text{ways}} = p(100) - 1$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Recursive Tree Enumeration
A naive recursive algorithm enumerates all partitions of 100:
```python
def naive_partitions(n, max_val):
    # explores over 190 million branches!
    # ...
```

### 1D Dynamic Programming Generating Function
1. The generating function for partitions using integers from $1$ to $99$ is:
   $$P_{\le 99}(x) = \prod_{k=1}^{99} \frac{1}{1 - x^k} = \sum_{n=0}^{\infty} p_{\le 99}(n) x^n$$
2. Using an unbounded 1D knapsack DP:
   $$DP[i] \leftarrow DP[i] + DP[i - k] \quad \text{for } k \in [1, 99], \, i \in [k, 100]$$
3. This computes $p(100) - 1$ in exactly $\sum_{k=1}^{99} (101 - k) = 4950$ additions in $\approx 0.0001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Integer Partitions for Early Integers

| Integer $n$ | Total Unrestricted Partitions $p(n)$ | Partitions into $\ge 2$ Summands | $p(n) - 1$ Count |
| :---: | :---: | :--- | :---: |
| **$1$** | $1$ | None | $0$ |
| **$2$** | $2$ | $1+1$ | $1$ |
| **$3$** | $3$ | $2+1, \, 1+1+1$ | $2$ |
| **$4$** | $5$ | $3+1, \, 2+2, \, 2+1+1, \, 1+1+1+1$ | $4$ |
| **$5$** | $7$ | $4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1$ | **$6$ (Sample)** |
| **$6$** | $11$ | $10$ ways | $10$ |
| **$100$** | **$190\,569\,292$** | All except $100$ itself | **$190\,569\,291$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### 1D In-Place DP Algorithm
1. Initialize array $DP = [1, 0, 0, \dots, 0]$ of length $101$.
2. For coin $c = 1 \dots 99$:
   - For $i = c \dots 100$:
     $$DP[i] \leftarrow DP[i] + DP[i - c]$$
3. By stopping at $c = 99$, the single-summand partition $100 = 100$ is never introduced.
4. $DP[100]$ yields $190\,569\,291$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $N = 5$
- Coins: $1, 2, 3, 4$.
- $c = 1 \implies DP = [1, 1, 1, 1, 1, 1]$
- $c = 2 \implies DP = [1, 1, 2, 2, 3, 3]$
- $c = 3 \implies DP = [1, 1, 2, 3, 4, 5]$
- $c = 4 \implies DP = [1, 1, 2, 3, 5, \mathbf{6}]$
- Result: $DP[5] = \mathbf{6}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $N = 100$
- Running DP for coins $1 \dots 99$:
  $$N_{\text{ways}} = \mathbf{190\,569\,291}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **DP Init** | `dp = [0] * 101; dp[0] = 1` | $\mathcal{O}(N)$ |
| **Stage 2** | **Outer Coin Loop** | For $c \in [1, 99]$ | $99$ coins |
| **Stage 3** | **Inner Transition** | For $i \in [c, 100]$: `dp[i] += dp[i - c]` | $4950$ additions |
| **Stage 4** | **Return Value** | Return scalar integer $190569291$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ where $N = 100$ ($4950$ operations) | $\approx 0.0001$ seconds |
| **Space Complexity** | $\mathcal{O}(N)$ | DP array of $101$ integers $\approx 800$ bytes |
| **Dynamic Execution** | $100\%$ Inline | 1D unbounded knapsack DP |

### Critical Invariants & Edge Cases Handled:
1. **$k \ge 2$ Summands Enforced**: By stopping coin iteration at $N - 1$, the partition of $N$ into a single number is strictly excluded.
2. **Order Invariance**: The outer loop over distinct integers enforces non-decreasing partition order, guaranteeing no duplicate permutation counting.
