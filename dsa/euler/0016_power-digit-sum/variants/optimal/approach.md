# Power Digit Sum - Optimal Approach

## Algorithm Explanation

We evaluate the sum of the decimal digits of $2^{1000}$.

1. Compute $2^{1000}$ using exponentiation by squaring (native in Python big integers).
2. Convert the resulting $302$-digit integer to string `str(2**1000)`.
3. Iterate over the string digits and sum their integer values `sum(int(d) for d in str_val)`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M)$ where $M = \log_{10}(2^{1000}) \approx 302$ digits.
- **Space Complexity:** $\mathcal{O}(M)$ - String buffer storage.
