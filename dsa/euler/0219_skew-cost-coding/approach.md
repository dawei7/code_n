# Skew-Cost Coding - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $A$ and $B$ be bit strings. $A$ is a **prefix** of $B$ if $B$ begins with $A$.
A **prefix-free code** of size $n$ is a set of $n$ distinct bit strings such that no string is a prefix of any other.

The cost of a bit string is $1$ for each digit `'0'` and $4$ for each digit `'1'`.
The cost of a prefix-free code is the sum of costs of all its codewords.

For example, a minimum-cost prefix-free code of size $6$ is $\{000, 001, 01, 10, 110, 111\}$ with total cost:

$$
C(6) = (1+1+1) + (1+1+4) + (1+4) + (4+1) + (4+4+1) + (4+4+4) = 3 + 6 + 5 + 5 + 9 + 12 = \mathbf{35}
$$

Find **$C(10^9)$**, the minimum total cost of a prefix-free code of size $10^9$:

$$
C(10^9) = \min \left\{ \sum_{w \in S} \operatorname{Cost}(w) \;\middle|\; S \subset \{0, 1\}^*, \; |S| = 10^9, \; S \text{ is prefix-free} \right\}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Priority Queue Individual Leaf Splitting
A naive approach uses a min-heap to pop one leaf at a time:
```python
def naive_skew_huffman():
    # Popping 10^9 nodes one-by-one takes > 100 seconds
    # ...
```

### Greedy Skew Huffman Tree Bulk Group Expansion
1. **Tree Growth & Node Splitting:**
   A prefix-free code corresponds to the leaves of a binary tree.
   Initially, the root is a single leaf at cost $0$ ($n = 1, \text{Total Cost} = 0$).
   Splitting a leaf of cost $c$ creates two child leaves with costs $c + 1$ (bit `'0'`) and $c + 4$ (bit `'1'`).
   - The number of leaves increases by $+1$.
   - The total cost changes by:

$$
\Delta C = (c + 1) + (c + 4) - c = c + 5
$$

2. **Greedy Minimum-Cost Splitting:**
   To minimize the total cost increase, we must always greedily split the leaf with the smallest available cost $c$.
3. **Bulk Frequency Grouping:**
   Instead of splitting leaves one by one, maintain a frequency table `count[c]` of active leaves with cost $c$.
   At each step, split all $\text{cnt}$ leaves of the current minimum cost $c$ at once:
   - `count[c + 1] += cnt`
   - `count[c + 4] += cnt`
   - `total_cost += cnt * (c + 5)`
   - `curr_n += cnt`
4. The maximum cost depth is $< 70$, so bulk expansion completes in $< 100$ loop iterations ($\approx 0.0001$ seconds).

---

## 3. Core Intuition & Mathematical Structure

### Skew Binary Tree Branch Splitting Dynamics

| Operation | Parent Node | Left Child (Bit `'0'`) | Right Child (Bit `'1'`) | Net Cost Change $\Delta C$ | Leaf Count Change $\Delta N$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Leaf Split** | Cost $c$ | Cost $c + 1$ | Cost $c + 4$ | $+ (c + 5)$ | $+1$ |
| **Initial Root** | — | — | — | Base: Cost $= 0$ | $N = 1$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Bulk Expansion Algorithm
```python
def solve(n: int = 10**9) -> int:
    target_n = n
    count = {0: 1}
    curr_n = 1
    total_cost = 0
    curr_min_cost = 0

    while curr_n < target_n:
        while count.get(curr_min_cost, 0) == 0:
            curr_min_cost += 1

        cnt = count[curr_min_cost]
        needed = target_n - curr_n

        if cnt <= needed:
            count[curr_min_cost] = 0
            count[curr_min_cost + 1] = count.get(curr_min_cost + 1, 0) + cnt
            count[curr_min_cost + 4] = count.get(curr_min_cost + 4, 0) + cnt
            total_cost += cnt * (curr_min_cost + 5)
            curr_n += cnt
        else:
            count[curr_min_cost] -= needed
            count[curr_min_cost + 1] = count.get(curr_min_cost + 1, 0) + needed
            count[curr_min_cost + 4] = count.get(curr_min_cost + 4, 0) + needed
            total_cost += needed * (curr_min_cost + 5)
            curr_n += needed
            break

    return total_cost
```
Evaluating for $N = 10^9$:

$$
C(10^9) = \mathbf{64\,564\,225\,042}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Tracing First 5 Splits to Reach $N = 6$
- **Step 0 ($n = 1$):** Leaves $=\{0: 1\}$. Total Cost $= 0$.
- **Step 1 ($n = 2$):** Split $c = 0 \implies$ Leaves $=\{1: 1, 4: 1\}$. Total Cost $= 0 + 5 = 5$.
- **Step 2 ($n = 3$):** Split $c = 1 \implies$ Leaves $=\{2: 1, 4: 1, 5: 1\}$. Total Cost $= 5 + 6 = 11$.
- **Step 3 ($n = 4$):** Split $c = 2 \implies$ Leaves $=\{3: 1, 4: 1, 5: 1, 6: 1\}$. Total Cost $= 11 + 7 = 18$.
- **Step 4 ($n = 5$):** Split $c = 3 \implies$ Leaves $=\{4: 2, 5: 1, 6: 1, 7: 1\}$. Total Cost $= 18 + 8 = 26$.
- **Step 5 ($n = 6$):** Split one $c = 4 \implies$ Leaves $=\{4: 1, 5: 2, 6: 1, 7: 1, 8: 1\}$. Total Cost $= 26 + 9 = \mathbf{35}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $N = 10^9$
- Bulk greedy expansion over 1 billion leaves:

$$
C(10^9) = \mathbf{64\,564\,225\,042}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Initialization** | `count = {0: 1}, curr_n = 1, total_cost = 0` | $\mathcal{O}(1)$ |
| **Stage 2** | **Find Min Cost** | While `count[min_c] == 0`: `min_c += 1` | $\mathcal{O}(1)$ amortized |
| **Stage 3** | **Bulk Split** | Add $\Delta N$ leaves of cost $c+1$ and $c+4$ | $\mathcal{O}(1)$ |
| **Stage 4** | **Cost Update** | `total_cost += cnt * (curr_min_cost + 5)` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Cost** | Return scalar integer $64564225042$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\log_\phi N)$ where $N = 10^9$ | $\approx 0.0001$ seconds ($< 100$ bulk steps) |
| **Space Complexity** | $\mathcal{O}(\log_\phi N)$ | Hash table $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | Greedy skew-cost tree bulk expansion |

### Critical Invariants & Edge Cases Handled:
1. **Exact Leaf Quota**: When `cnt > needed`, only `needed` nodes of the minimum cost are split, ensuring the final code size is exactly $10^9$.
2. **Monotonic Cost Advancement**: Because child costs $c+1$ and $c+4$ are strictly greater than $c$, the minimum cost `curr_min_cost` is strictly non-decreasing.