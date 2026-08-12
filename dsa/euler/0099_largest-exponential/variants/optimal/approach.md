# Largest Exponential - Optimal Approach

## Algorithm Explanation

Find the 1-indexed line number in `base_exp.txt` containing the base/exponent pair $(b, e)$ with the greatest numerical value $b^e$.

### Logarithmic Comparison Transformation:
Directly exponentiating $b^e$ yields numbers with over $3,000,000$ digits. Applying natural logarithm maps large exponential comparisons into simple float multiplications:
$$\log(b^e) = e \cdot \ln(b)$$

Since logarithm is a strictly increasing monotonic function:
$$b_1^{e_1} > b_2^{e_2} \iff e_1 \ln(b_1) > e_2 \ln(b_2)$$

Iterate all $1000$ base/exponent lines, compute $e \ln(b)$ in $\mathcal{O}(1)$ time per line, and track the line number maximizing this value.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000$ lines. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Text line buffer.
