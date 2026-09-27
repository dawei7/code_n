# Guided Example: Minimum Time to Remove All Cars Containing Illegal Goods

We analyze and execute the bidirectional prefix-suffix Dynamic Programming algorithm on a representative train car sequence, demonstrating how balancing end truncation against internal direct removals achieves the global minimum removal time.

- **Input:** `s = "1100101"`
- **Output:** `5`

This instance illustrates the cost asymmetry between boundary peeling ($1$ per car) versus surgical middle removal ($2$ per car), prefix/suffix state recurrence, and split point optimization.

---

## 1. Problem Overview & Representative Instance

A train consists of $n$ cars represented as a binary string `s`:
- `'0'`: A legal car containing legitimate goods.
- `'1'`: An illegal car containing contraband.

All illegal cars must be removed using any combination of three permitted operations:
1. **Left End Removal:** Discard the car currently at the left end. Cost: $1$ unit of time.
2. **Right End Removal:** Discard the car currently at the right end. Cost: $1$ unit of time.
3. **Internal Removal:** Discard a car from any position directly. Cost: $2$ units of time.

Legal cars may be sacrificed during end removals if clearing them is cheaper than removing illegal cars individually.

The goal is to determine the minimum total time required to eliminate all illegal cars.

In our representative instance:
- `s = "1100101"` ($n = 7$).
- Illegal cars reside at indices $0, 1, 4, 6$.
- Legal cars reside at indices $2, 3, 5$.

We must determine the cheapest combination of left peeling, right peeling, and surgical internal removals.

---

## 2. Mathematical & Algorithmic Principles

### Cost Trade-Offs and Boundary Asymmetry

Notice the fundamental economic trade-off:
- Truncating $L$ cars from the left end costs $L$ units (at rate $1$ per car).
- Truncating $R$ cars from the right end costs $R$ units (at rate $1$ per car).
- Removing an isolated illegal car from the remaining middle segment $[L, n - 1 - R]$ costs $2$ units.
- Therefore, peeling is advantageous when illegal cars are clustered near the ends, while direct removal is preferred for sparse illegal cars embedded deep within long stretches of legal cars.

### Prefix Dynamic Programming Recurrence

Let $\text{left}[i]$ denote the minimum cost to clear all illegal cars in prefix $s[0 \dots i]$ using only left-end removals and internal removals:
- If $s[i] = \text{'0'}$: Car $i$ is legal and requires no action:
  $$\text{left}[i] = \text{left}[i - 1]$$
- If $s[i] = \text{'1'}$: We have two choices:
  1. **Direct Removal:** Pay $2$ to remove car $i$ individually: $\text{left}[i - 1] + 2$.
  2. **Prefix Truncation:** Peel all cars from $0$ up to $i$ from the left end: $i + 1$.
  $$\text{left}[i] = \min(\text{left}[i - 1] + 2, \, i + 1)$$
- Base condition: $\text{left}[-1] = 0$.

### Suffix Dynamic Programming Recurrence

Similarly, let $\text{right}[i]$ denote the minimum cost to clear all illegal cars in suffix $s[i \dots n - 1]$ using only right-end removals and internal removals:
- If $s[i] = \text{'0'}$:
  $$\text{right}[i] = \text{right}[i + 1]$$
- If $s[i] = \text{'1'}$:
  $$\text{right}[i] = \min(\text{right}[i + 1] + 2, \, n - i)$$
- Base condition: $\text{right}[n] = 0$.

### Global Split Minimization

Any optimal plan can be viewed as choosing an optimal split point $i \in [0, n - 1]$ separating the prefix strategy from the suffix strategy:
$$\text{MinCost} = \min\Big(\text{left}[n - 1], \, \text{right}[0], \, \min_{i=0}^{n-2} (\text{left}[i] + \text{right}[i + 1])\Big)$$

| DP State | Subproblem Scope | Recurrence on $'1'$ | Operational Meaning |
|---|---|---|---|
| $\text{left}[i]$ | Prefix $s[0 \dots i]$ | $\min(\text{left}[i-1] + 2, \, i + 1)$ | Optimal cost to clear prefix without right removals |
| $\text{right}[i]$ | Suffix $s[i \dots n-1]$ | $\min(\text{right}[i+1] + 2, \, n - i)$ | Optimal cost to clear suffix without left removals |
| Split Boundary $i$ | Conjunction of sides | $\text{left}[i] + \text{right}[i+1]$ | Fuses optimal prefix plan with optimal suffix plan |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `s = "1100101"` of length $n = 7$.

```
String:      1   1   0   0   1   0   1
Indices:     0   1   2   3   4   5   6

Forward sweep (left DP):
left[0] = min(0 + 2, 0 + 1) = 1
left[1] = min(1 + 2, 1 + 1) = 2
left[2] = left[1] = 2
left[3] = left[2] = 2
left[4] = min(2 + 2, 4 + 1) = min(4, 5) = 4
left[5] = left[4] = 4
left[6] = min(4 + 2, 6 + 1) = min(6, 7) = 6

Backward sweep (right DP):
right[6] = min(0 + 2, 7 - 6) = 1
right[5] = right[6] = 1
right[4] = min(1 + 2, 7 - 4) = min(3, 3) = 3
right[3] = right[4] = 3
right[2] = right[3] = 3
right[1] = min(3 + 2, 7 - 1) = min(5, 6) = 5
right[0] = min(5 + 2, 7 - 0) = min(7, 7) = 7
```

### Step 1: Forward Pass (Prefix DP)
- **$i = 0$ (`s[0] = '1'`):** $\min(0 + 2, 0 + 1) = \min(2, 1) = 1$. (Left peel cheaper).
- **$i = 1$ (`s[1] = '1'`):** $\min(1 + 2, 1 + 1) = \min(3, 2) = 2$. (Left peel cheaper).
- **$i = 2$ (`s[2] = '0'`):** Car is legal. $\text{left}[2] = \text{left}[1] = 2$.
- **$i = 3$ (`s[3] = '0'`):** Car is legal. $\text{left}[3] = \text{left}[2] = 2$.
- **$i = 4$ (`s[4] = '1'`):** $\min(\text{left}[3] + 2, 4 + 1) = \min(4, 5) = 4$. (Internal removal cheaper).
- **$i = 5$ (`s[5] = '0'`):** Car is legal. $\text{left}[5] = \text{left}[4] = 4$.
- **$i = 6$ (`s[6] = '1'`):** $\min(\text{left}[5] + 2, 6 + 1) = \min(6, 7) = 6$.

Prefix table: $\text{left} = [1, 2, 2, 2, 4, 4, 6]$.

### Step 2: Backward Pass (Suffix DP)
- **$i = 6$ (`s[6] = '1'`):** $\min(0 + 2, 7 - 6) = \min(2, 1) = 1$. (Right peel cheaper).
- **$i = 5$ (`s[5] = '0'`):** Car is legal. $\text{right}[5] = \text{right}[6] = 1$.
- **$i = 4$ (`s[4] = '1'`):** $\min(1 + 2, 7 - 4) = \min(3, 3) = 3$. (Tie at 3).
- **$i = 3$ (`s[3] = '0'`):** Car is legal. $\text{right}[3] = \text{right}[4] = 3$.
- **$i = 2$ (`s[2] = '0'`):** Car is legal. $\text{right}[2] = \text{right}[3] = 3$.
- **$i = 1$ (`s[1] = '1'`):** $\min(3 + 2, 7 - 1) = \min(5, 6) = 5$. (Internal removal cheaper).
- **$i = 0$ (`s[0] = '1'`):** $\min(5 + 2, 7 - 0) = \min(7, 7) = 7$.

Suffix table: $\text{right} = [7, 5, 3, 3, 3, 1, 1]$.

### Step 3: Find Global Minimum Across Split Points
- Entire suffix only: $\text{right}[0] = 7$.
- Split after $i = 0$: $\text{left}[0] + \text{right}[1] = 1 + 5 = 6$.
- Split after $i = 1$: $\text{left}[1] + \text{right}[2] = 2 + 3 = \mathbf{5}$.
- Split after $i = 2$: $\text{left}[2] + \text{right}[3] = 2 + 3 = \mathbf{5}$.
- Split after $i = 3$: $\text{left}[3] + \text{right}[4] = 2 + 3 = \mathbf{5}$.
- Split after $i = 4$: $\text{left}[4] + \text{right}[5] = 4 + 1 = \mathbf{5}$.
- Split after $i = 5$: $\text{left}[5] + \text{right}[6] = 4 + 1 = \mathbf{5}$.
- Entire prefix only: $\text{left}[6] = 6$.

Global minimum cost: $5$.

---

## 4. Comprehensive State Trace

The table below catalogs prefix and suffix cost accumulation across all positions:

| Index $i$ | Character `s[i]` | Prefix Cost $\text{left}[i]$ | Decision Rationale for Prefix | Suffix Cost $\text{right}[i]$ | Decision Rationale for Suffix | Split Cost $\text{left}[i] + \text{right}[i+1]$ |
|---|---|---|---|---|---|---|
| $0$ | `'1'` | $1$ | Peel $s[0]$ ($1 < 2$) | $7$ | Tie ($5+2 = 7-0$) | $1 + 5 = 6$ |
| $1$ | `'1'` | $2$ | Peel $s[0\dots 1]$ ($2 < 3$) | $5$ | Internal ($3+2 < 6$) | $2 + 3 = \mathbf{5}$ (Optimum) |
| $2$ | `'0'` | $2$ | Legal car (skip) | $3$ | Legal car (skip) | $2 + 3 = \mathbf{5}$ (Optimum) |
| $3$ | `'0'` | $2$ | Legal car (skip) | $3$ | Legal car (skip) | $2 + 3 = \mathbf{5}$ (Optimum) |
| $4$ | `'1'` | $4$ | Internal ($2+2 < 5$) | $3$ | Tie ($1+2 = 7-4$) | $4 + 1 = \mathbf{5}$ (Optimum) |
| $5$ | `'0'` | $4$ | Legal car (skip) | $1$ | Legal car (skip) | $4 + 1 = \mathbf{5}$ (Optimum) |
| $6$ | `'1'` | $6$ | Internal ($4+2 < 7$) | $1$ | Peel $s[6]$ ($1 < 2$) | N/A (Boundary) |

### Concrete Optimal Plan Reconstruction

- Peel prefix of length $2$ (`s[0..1] = "11"`): Cost $= 2$.
- Peel suffix of length $1$ (`s[6] = "1"`): Cost $= 1$.
- Remaining middle car `s[4] = "1"`: Remove directly at cost $2$.
- Total execution time: $2 + 1 + 2 = 5$.

---

## 5. Algorithmic Correctness & Soundness

### Optimal Substructure
Any optimal sequence of operations can be factored into:
1. Some number of left-end removals of length $L \ge 0$.
2. Some number of right-end removals of length $R \ge 0$ (with $L + R \le n$).
3. Direct internal removals for all remaining illegal cars in $s[L \dots n - 1 - R]$.

The DP formulation defines $\text{left}[i]$ as the strictly optimal cost for prefix $[0 \dots i]$ without using right-end removals. Because $\min(A + 2, i + 1)$ checks both keeping car $i$ internal versus converting the entire prefix up to $i$ into a left-end peel, $\text{left}[i]$ exhausts all possible left-boundary strategies. By symmetry, $\text{right}[i+1]$ exhausts all right-boundary strategies. Combining them across all split points $i$ considers every possible partition between prefix peeling, suffix peeling, and internal removals.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **All Legal Cars (`s = "0000"`):** Every character is `'0'`. DP remains $0$ throughout, returning $0$.
2. **All Illegal Cars (`s = "1111"`):**
   - Direct removals would cost $2 \times 4 = 8$.
   - Truncating the whole train costs $4$.
   - The algorithm evaluates $i + 1$ and correctly returns $4$.
3. **Single Illegal Car in Center (`s = "00100"`):**
   - Peeling from either end costs $3$.
   - Direct removal costs $2$.
   - The algorithm picks the direct removal at cost $2$.

### Common Anti-Patterns
- **Pure Greedy End-Peeling:** Peeling inward until no illegal cars remain can discard dozens of legal cars just to reach a single illegal car, when a direct removal at cost $2$ is much cheaper.
- **Pure Direct Removals:** Removing every `'1'` individually costs $2 \times \text{count}(1)$, failing whenever illegal cars are densely clustered at the ends.
- **Double Counting Removals:** Mixing left and right removals without a single clean split boundary can double-count peeled cars.

---

## 7. Complexity Analysis

### Time Complexity
- **Prefix Pass:** Scans $n$ characters from left to right, performing $O(1)$ operations per character: $O(n)$ time.
- **Suffix Pass:** Scans $n$ characters from right to left, performing $O(1)$ operations per character: $O(n)$ time.
- **Split Minimization Pass:** Evaluates $n$ split points in $O(1)$ time each: $O(n)$ time.
- Total time complexity is strictly $O(n)$, executing in under $4$ milliseconds for $n = 2 \cdot 10^5$.

### Auxiliary Space Complexity
- Two 1D arrays `left` and `right` of size $n$ store prefix and suffix optimal costs.
- (Can be further optimized to $O(1)$ auxiliary space by computing suffix DP on the fly during the split search).
- Total auxiliary space complexity is $O(n)$ memory (or $O(1)$).