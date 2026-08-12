# Factorial Digit Sum - Optimal Approach

## Algorithm Explanation

We calculate the sum of the decimal digits of $100!$.

1. Compute $100!$ using Python's high-precision `math.factorial(100)`.
2. Convert the resulting $158$-digit integer to a string.
3. Sum each digit's integer value `sum(int(d) for d in str_val)`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M)$ where $M = 158$ digits.
- **Space Complexity:** $\mathcal{O}(M)$ - String buffer storage.
