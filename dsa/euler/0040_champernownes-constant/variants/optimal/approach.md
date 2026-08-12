# Champernowne's Constant - Optimal Approach

## Algorithm Explanation

Compute product $d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$ of fractional digits of Champernowne's constant $0.123456789101112 \dots$.

1. Concatenate positive integers $1, 2, 3 \dots$ into string `fraction` until string length exceeds $1000000$.
2. Extract $1$-indexed digit positions $idx \in \{1, 10, 100, 1000, 10000, 100000, 1000000\}$ (`fraction[idx - 1]`).
3. Multiply the extracted digits.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000000$ digits. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Concatenated fraction string buffer.
