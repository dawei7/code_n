# 0-1 Knapsack (FPTAS Approximation)

| | |
|---|---|
| **ID** | `approx_07` |
| **Category** | approximation |
| **Complexity (required)** | $O(N^3 / ε)$ |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Polynomial-time approximation scheme](https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme) |

## Problem statement

The 0-1 Knapsack problem is NP-Hard, meaning there is no known polynomial-time algorithm to solve it exactly. However, it is **weakly NP-Hard**, meaning it has a Dynamic Programming solution of $O(N \cdot W)$. If the capacity W is a billion, the DP fails (pseudo-polynomial time).
Your task is to implement a **Fully Polynomial-Time Approximation Scheme (FPTAS)**. Given an error parameter \epsilon (e.g., \epsilon = 0.1 for a 10% error margin), return a valid knapsack packing whose total value is mathematically guaranteed to be \ge (1 - \epsilon) x OPT, while running in strictly polynomial time relative to N and 1/\epsilon (completely independent of the massive W!).

**Input:** N items with `values` and `weights`, a capacity `W`, and a float `epsilon`.
**Output:** The approximated maximum value.

## When to use it

- When you have a massive knapsack capacity and astronomical item values that make both standard DP arrays explode, but you still need an incredibly precise mathematical guarantee (like 99.9% optimal).

## Approach

The standard Knapsack DP array can be flipped: Instead of DP[weight] = max\_value, we can use DP[value] = min\_weight!
This DP[value] approach runs in $O(N \cdot V_{max})$, where V_{max} is the sum of all values.
If the item values are in the billions, V_{max} is massive, and $O(N \cdot V_{max})$ still fails.

**The Brilliant FPTAS Insight:**
What if we just divided all the item values by a massive number (a scaling factor K) and rounded them down?
Instead of an item being worth \1,482,912, we scale it to \14.
Now, V_{max} is tiny! The DP[value] algorithm will run instantly!
Because we rounded down, we lose a tiny bit of precision. The FPTAS mathematics calculates the exact scaling factor K required to ensure our precision loss is strictly bounded by the user's \epsilon.

1. Let V_{highest} be the maximum value of any single item.
2. Define the scaling factor: K = \frac{\epsilon \cdot V_{highest}}{N}.
3. Create a new array of scaled values: `scaled_v[i] = floor(value[i] / K)`.
4. Run the flipped Knapsack DP using these tiny `scaled_v` values!
   - `dp[v]` will store the **minimum weight** required to achieve exactly scaled value `v`.
5. Find the maximum scaled value `v` in the DP table where `dp[v] <= W`.
6. To return the true approximation, look at the items that formed that scaled value, and sum up their **original, unscaled** values!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_07: 0/1 Knapsack FPTAS.

Given n items with values and weights and capacity
"""


def solve(values, weights, n, capacity, eps):
    """0/1 Knapsack FPTAS: scale values, run DP, return result."""
    if capacity <= 0 or n == 0:
        return 0
    v_max = max(values) if values else 1
    if v_max == 0:
        return 0
    K = (eps * v_max) / n
    if K <= 0:
        K = 1
    scaled = [max(1, int(v / K)) for v in values]
    # DP: dp[w] = max scaled value for weight w.
    dp = [0] * (capacity + 1)
    for i in range(n):
        wi = min(weights[i], capacity)
        vi = scaled[i]
        for w in range(capacity, wi - 1, -1):
            cand = dp[w - wi] + vi
            if cand > dp[w]:
                dp[w] = cand
    return dp[capacity] * K
```

</details>

## Walk-through

*(Conceptual)*
`values = [1000000, 2000000, 3000000]`, `W = 50`.
`epsilon = 0.3`, `N = 3`.

1. V_{highest} = 3000000.
2. K = (0.3 x 3000000) / 3 = 300000.
3. Scaled Values:
   - 1000000 / 300000 = 3.33 \rightarrow 3.
   - 2000000 / 300000 = 6.66 \rightarrow 6.
   - 3000000 / 300000 = 10.0 \rightarrow 10.
4. Our DP array is now only of size 3+6+10 = 19!
5. We run DP finding the min weight for values 0 to 19. This takes exactly 3 x 19 = 57 operations, instead of millions!
6. If the best scaled value found is `16`, our approximate real value is 16 x 300000 = 4,800,000.
The optimal might have been 5,000,000, but our answer is guaranteed to be \ge (1 - 0.3) x 5,000,000 = 3,500,000. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Average** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Worst** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |

The size of the DP array is bounded by the maximum possible scaled sum.
Max\_Scaled\_Sum \le N x (V_{highest} / K).
Substitute K = \frac{\epsilon \cdot V_{highest}}{N}:
Max\_Scaled\_Sum \le N x \frac{V_{highest}}{\epsilon \cdot V_{highest} / N} = \frac{N^2}{\epsilon}.
The DP iterates N times over an array of size \frac{N^2}{\epsilon}.
Total time is exactly $O(N \cdot \frac{N^2}{\epsilon})$ = $O(\frac{N^3}{\epsilon})$.
Space complexity is $O(\frac{N^2}{\epsilon})$ to store the 1D DP array.

## Variants & optimizations

- **Tracing the Items:** To get the exact value of the chosen items, instead of just multiplying by K at the end, maintain a 2D DP table to trace back the exact items selected, then return the sum of `original_value[i]` for the chosen items.

## Real-world applications

- **Computational Finance:** Portfolio optimization where monetary values are incredibly large, rendering exact DP impossible, but 99% accuracy is completely sufficient.

## Related algorithms in cOde(n)

- **[dp_03 - 0-1 Knapsack](../dynamic/dp_03_knapsack.md)** — The classic $O(N \cdot W)$ pseudo-polynomial time exact solution.
- **[bb_01 - 0-1 Knapsack Branch and Bound](../branch_and_bound/bb_01_0-1-knapsack.md)** — The exact exponential time solution that prunes search spaces.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
