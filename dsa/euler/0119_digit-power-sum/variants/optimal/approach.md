# Digit Power Sum - Optimal Approach

## Algorithm Explanation

Find the $30^{\text{th}}$ term $a_{30}$ of the sequence of integers $V \ge 10$ that are equal to the sum of their decimal digits raised to an integer power $e \ge 2$:
$$V = (\text{sum\_digits}(V))^e$$

### Power Generation Strategy:
Instead of searching through billions of integers $V$ and testing digit sums, we directly generate candidate powers $V = b^e$:

1. Iterate base $b \in [2, 100]$.
2. Iterate exponent $e \in [2, 50]$.
3. Calculate candidate value $V = b^e$.
4. Check if $V \ge 10$ and sum of decimal digits of $V$ equals base $b$.
5. Store valid numbers in a set, sort in ascending order, and return $a_{30}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(B \cdot E)$ where $B = 100, E = 50$ ($5000$ operations). Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(B \cdot E)$ - Storage for valid sequence candidates.
