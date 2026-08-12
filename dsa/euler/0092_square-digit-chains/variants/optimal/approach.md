# Square Digit Chains - Optimal Approach

## Algorithm Explanation

Find how many starting positive integers below $10,000,000$ arrive at $89$ under the square digit chain transformation $n \to \sum d^2$.

### Digit Combinatorics Optimization:
For a 7-digit number ($n < 10,000,000$), the maximum possible sum of squared digits is $7 \times 9^2 = 567$.

Instead of checking all $10,000,000$ numbers sequentially:
1. Precompute chain outcomes ($1$ or $89$) for all digit square sums $S \in [1, 567]$.
2. Iterate all multiset combinations of 7 digits from $\{0, 1, \dots, 9\}$ with replacement ($\binom{10+7-1}{7} = 11440$ combinations).
3. For each combination with sum of squares $S$ ending at $89$, compute the multinomial coefficient (number of distinct permutations):
   $$\text{Permutations} = \frac{7!}{f_0! f_1! \cdots f_9!}$$
4. Accumulate and return the total count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\binom{D+K-1}{K}\right)$ where $D=10, K=7$ ($11440$ operations). Runs in $< 0.015\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
