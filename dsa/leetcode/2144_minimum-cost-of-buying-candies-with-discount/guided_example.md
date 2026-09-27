# Guided Example: Minimum Cost of Buying Candies With Discount

We analyze and execute the greedy descending-sort triplet bundling algorithm on a representative problem instance, demonstrating why pairing the most expensive available candies always maximizes the allowed discount.

- **Input:** `cost = [6, 5, 7, 9, 2, 2]`
- **Output:** `23`

This instance illustrates sorting into descending order, decomposing items into triplets, claiming the third item in each triplet for free, and paying full price for items that do not trigger discounts.

---

## 1. Problem Overview & Representative Instance

A store has a promotion: for every two candies a customer purchases, they may choose a third candy for free, provided that:
$$\text{cost}(\text{free candy}) \le \min(\text{cost}(\text{purchased candy 1}), \text{cost}(\text{purchased candy 2}))$$

We are given an array `cost` representing the individual prices of all candies. Our goal is to acquire all candies at the minimum possible total expenditure.

In our representative instance:
- `cost = [6, 5, 7, 9, 2, 2]`
- Total candies $n = 6$.
- Total nominal value: $6 + 5 + 7 + 9 + 2 + 2 = 31$.

Because $n = 6$, we can form exactly $\lfloor 6 / 3 \rfloor = 2$ triplets, allowing us to obtain $2$ candies for free. Minimizing total expenditure is mathematically equivalent to maximizing the sum of the two free candies.

---

## 2. Mathematical & Algorithmic Principles

### Duality of Cost Minimization and Discount Maximization

Let $S_{\text{total}} = \sum_{i=0}^{n-1} \text{cost}[i]$ be the fixed sum of all candy prices. If we obtain a subset $\mathcal{F}$ of free candies through valid promotion groups, the total paid is:
$$\text{Cost}_{\text{paid}} = S_{\text{total}} - \sum_{f \in \mathcal{F}} \text{cost}[f]$$

Minimizing $\text{Cost}_{\text{paid}}$ is strictly identical to maximizing $\sum_{f \in \mathcal{F}} \text{cost}[f]$.

### Descending Greedy Triplet Partitioning

Sort the array of candy prices in non-increasing order:
$$c_0 \ge c_1 \ge c_2 \ge c_3 \ge c_4 \ge \dots \ge c_{n-1}$$

Consider partitioning the sorted elements into consecutive groups of three:
$$(c_0, c_1, c_2), (c_3, c_4, c_5), \dots$$

Within each group $(c_{3k}, c_{3k+1}, c_{3k+2})$:
1. Purchase the two most expensive elements: $c_{3k}$ and $c_{3k+1}$.
2. The third element $c_{3k+2}$ satisfies $c_{3k+2} \le c_{3k+1} \le c_{3k}$, so $\text{cost} \le \min(c_{3k}, c_{3k+1})$ holds unconditionally.
3. Therefore, $c_{3k+2}$ is claimed for free.

### Optimality Proof by Exchange Argument

Suppose an adversary claims that a higher discount could be achieved by using a different grouping:
- To make a candy of value $V$ free, we must pay for at least two candies with values $\ge V$.
- In the sorted list, $c_2$ is the 3rd largest element. At most one element can be larger than $c_2$ among the free items if two elements $\ge c_2$ are paid for. Specifically, among the entire multiset, at most $k$ elements can be free that are $\ge c_{3k-1}$.
- The consecutive greedy grouping $(c_{3k}, c_{3k+1}, c_{3k+2})$ achieves the upper bound on the $k$-th largest possible free candy for every $k \ge 1$ simultaneously.
- Any alternative grouping that pays for a cheaper candy to free an expensive one either violates the $\min$ constraint or sacrifices a larger possible discount.

| Triplet Position | Rule | Action | Cost Implication |
|---|---|---|---|
| Index $3k$ | First purchased item | Pay full price $c_{3k}$ | Anchors promotion condition |
| Index $3k + 1$ | Second purchased item | Pay full price $c_{3k+1}$ | Establishes discount threshold $\min(c_{3k}, c_{3k+1}) = c_{3k+1}$ |
| Index $3k + 2$ | Promotional item | Claim for free ($c_{3k+2}$) | Maximizes discount subject to threshold |
| Tail Remainder | Remaining $1$ or $2$ items | Pay full price | Cannot trigger promotion without third item |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the representative instance `cost = [6, 5, 7, 9, 2, 2]`.

```
Raw costs:       [6, 5, 7, 9, 2, 2]
Sorted desc:     [9, 7, 6, 5, 2, 2]
Triplet groups:  (9, 7, [6]),  (5, 2, [2])
Paid:            9 + 7 + 5 + 2 = 23
Free:            6 + 2 = 8
```

### Step 1: Descending Sort
- Input array: $[6, 5, 7, 9, 2, 2]$.
- Sorted in non-increasing order:
  $$c = [9, 7, 6, 5, 2, 2]$$
- Indices:
  - $c[0] = 9$
  - $c[1] = 7$
  - $c[2] = 6$
  - $c[3] = 5$
  - $c[4] = 2$
  - $c[5] = 2$

### Step 2: Process Triplet $1$ (Indices $0, 1, 2$)
- Candidate items: $c[0] = 9$, $c[1] = 7$, $c[2] = 6$.
- Action:
  - Buy $c[0] = 9$. Paid running sum: $0 + 9 = 9$.
  - Buy $c[1] = 7$. Paid running sum: $9 + 7 = 16$.
  - Discount check: $\min(9, 7) = 7$. Since $c[2] = 6 \le 7$, $c[2]$ is eligible for free.
  - Claim $c[2] = 6$ for free ($0$ added to paid).
- Intermediate paid sum: $16$.

### Step 3: Process Triplet $2$ (Indices $3, 4, 5$)
- Candidate items: $c[3] = 5$, $c[4] = 2$, $c[5] = 2$.
- Action:
  - Buy $c[3] = 5$. Paid running sum: $16 + 5 = 21$.
  - Buy $c[4] = 2$. Paid running sum: $21 + 2 = 23$.
  - Discount check: $\min(5, 2) = 2$. Since $c[5] = 2 \le 2$, $c[5]$ is eligible for free.
  - Claim $c[5] = 2$ for free ($0$ added to paid).
- Intermediate paid sum: $23$.

### Step 4: Finalization
- All $6$ candies have been processed.
- No remaining items.
- Final expenditure: $23$.

---

## 4. Comprehensive State Trace

The table below catalogs every candy in sorted order, its assignment role, price, and contribution to the total expenditure:

| Index $i$ | Candy Cost $c[i]$ | Triplet ID | Triplet Role | Paid / Free | Incremental Paid | Running Total Paid |
|---|---|---|---|---|---|---|
| $0$ | $9$ | Triplet 1 | Purchased 1 | Paid | $+9$ | $9$ |
| $1$ | $7$ | Triplet 1 | Purchased 2 | Paid | $+7$ | $16$ |
| $2$ | $6$ | Triplet 1 | Discount 1 | Free | $+0$ | $16$ |
| $3$ | $5$ | Triplet 2 | Purchased 1 | Paid | $+5$ | $21$ |
| $4$ | $2$ | Triplet 2 | Purchased 2 | Paid | $+2$ | $23$ |
| $5$ | $2$ | Triplet 2 | Discount 2 | Free | $+0$ | $23$ |

### Mathematical Invariant Verification

- Total nominal value: $9 + 7 + 6 + 5 + 2 + 2 = 31$.
- Total discount obtained: $6 + 2 = 8$.
- Total paid: $31 - 8 = 23$.
- Condition check for Triplet 1: $6 \le \min(9, 7) = 7$ (Valid).
- Condition check for Triplet 2: $2 \le \min(5, 2) = 2$ (Valid).

---

## 5. Algorithmic Correctness & Soundness

### Global Optimality
Let $n = 3k + r$, where $r \in \{0, 1, 2\}$. At most $k$ candies can ever be obtained for free, because each free candy requires at least two distinct paid companions:
$$|\mathcal{F}| \le \left\lfloor \frac{n}{3} \right\rfloor = k$$

Let the free candies in any valid configuration be $f_1 \ge f_2 \ge \dots \ge f_k$.
- To obtain $f_1$ for free, there must exist at least $2$ paid candies $\ge f_1$. Thus $f_1 \le c_2$.
- To obtain $f_1$ and $f_2$ for free, there must exist at least $4$ paid candies (at least $2 \ge f_1$ and another $2 \ge f_2$). Thus $f_2 \le c_5$.
- By induction, for every $j \in \{1, \dots, k\}$, $f_j \le c_{3j-1}$.

The greedy strategy achieves $f_j = c_{3j-1}$ for every $j \in \{1, \dots, k\}$. Because each element in the greedy discount set matches the theoretical maximum possible value at that rank, the greedy discount sum $\sum_{j=1}^k c_{3j-1}$ is strictly maximal across all valid selection strategies.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Fewer Than Three Candies ($n < 3$):** If $n = 1$ or $n = 2$, no promotion can be triggered because at least two items must be paid to unlock a third. The algorithm correctly adds all items to the total, with zero free items.
2. **All Candies Have Identical Cost:** For example, $[5, 5, 5, 5]$. Sorted: $[5, 5, 5, 5]$. Triplet 1 takes two $5$s and frees one $5$. The remaining single $5$ is paid at full price. Total paid $= 5 + 5 + 5 = 15$.
3. **Array Length Not a Multiple of 3 ($n \pmod 3 \ne 0$):**
   - If $n \pmod 3 = 1$: The last item (the cheapest overall) cannot form a triplet and is purchased at full price.
   - If $n \pmod 3 = 2$: The last two items cannot form a complete triplet and are both purchased at full price.

### Common Anti-Patterns
- **Ascending Sort (Freeing the Cheapest):** If we sort ascending and take the third item for free, we pay for $2$ and $2$ to get $5$ free (which is invalid since $5 > 2$), or pay for $5$ and $6$ to get $2$ free. Freeing cheap candies wastes the promotion.
- **Dynamic Programming Overkill:** Trying to formulate knapsack DP over subset sums is completely unnecessary because the greedy choice property holds unconditionally.
- **Arbitrary Pairing:** Pairing $9$ and $2$ allows freeing $2$, but wastes the high capacity of $9$. Pairing $9$ with $7$ allows freeing $6$.

---

## 7. Complexity Analysis

### Time Complexity
- **Sorting:** Sorting $n$ elements in non-increasing order takes $O(n \log n)$ time with comparison sort, or $O(n)$ time using bucket/counting sort since candy prices are bounded by $100$.
- **Linear Scan:** Iterating through the sorted array by stepping across indices $i = 0, 1, \dots, n - 1$ takes $O(n)$ operations.
- Total time complexity is $O(n \log n)$ (or $O(n)$ with counting sort), executing in less than $1$ millisecond for $n \le 100$.

### Auxiliary Space Complexity
- Sorting in-place uses $O(1)$ auxiliary space (or $O(\log n)$ for recursive sorting stack).
- Accumulator variables require $O(1)$ space.
- Total auxiliary space complexity is $O(1)$.
