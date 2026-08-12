# Non-bouncy Numbers - Optimal Approach

## Algorithm Explanation

Find the total number of positive integers below $10^{100}$ (a googol) that are **not bouncy** (either non-decreasing or non-increasing).

### Combinatorial Stars and Bars Formulation:
For numbers with up to $D = 100$ digits:

1. **Increasing Numbers (Non-Decreasing Digits)**:
   - Selecting $D$ non-decreasing digits from $10$ options $\{0 \dots 9\}$, excluding all-zero string:
   $$\text{Increasing}(D) = \binom{D + 9}{9} - 1$$

2. **Decreasing Numbers (Non-Increasing Digits)**:
   - Selecting $D$ non-increasing digits from $10$ options $\{0 \dots 9\}$ with zero padding, excluding zero and single-zero sequences:
   $$\text{Decreasing}(D) = \binom{D + 10}{10} - 1 - D$$

3. **Constant Overlap (Single-Digit Repetitions)**:
   - Numbers consisting of a single repeated non-zero digit (e.g. $7, 77, 777 \dots$) are both increasing and decreasing.
   $$\text{Overlap}(D) = 9 \times D$$

### Closed-Form Combined Formula:
$$\text{Non-Bouncy}(D) = \binom{D + 9}{9} + \binom{D + 10}{10} - 10 D - 2$$

Evaluating at $D = 100$ gives the exact count in $\mathcal{O}(1)$ time.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D)$ where $D = 100$. Evaluates in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
