# Arithmetic Expressions - Optimal Approach

## Algorithm Explanation

Find the set of four distinct non-zero digits $a < b < c < d$ that maximizes the length $n$ of consecutive expressible positive integers $1, 2, \dots, n$ using arithmetic operations $\{+, -, \times, /\}$ and arbitrary parenthesization.

### Expression Evaluation Strategy:
For a given set of 4 digits $\{a, b, c, d\}$:
1. Permute all $4! = 24$ operand orderings $(x_1, x_2, x_3, x_4)$.
2. Combine with all $4^3 = 64$ operator triples $(o_1, o_2, o_3) \in \{+, -, \times, /\}^3$.
3. Evaluate all $5$ distinct parenthesization binary trees using exact rational arithmetic (`fractions.Fraction`):
   - `((x1 o1 x2) o2 x3) o3 x4`
   - `(x1 o1 (x2 o2 x3)) o3 x4`
   - `x1 o1 ((x2 o2 x3) o3 x4)`
   - `x1 o1 (x2 o2 (x3 o3 x4))`
   - `(x1 o1 x2) o3 (x3 o2 x4)`
4. Collect all positive integer results into a set `targets`.
5. Measure consecutive span $1 \dots n$ and return `abcd` string for the set maximizing $n$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\binom{9}{4} \cdot 4! \cdot 4^3 \cdot 5)$ ($126 \times 24 \times 64 \times 5 = 967,680$ evaluations). Runs in $< 0.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
