# Double-base Palindromes - Optimal Approach

## Algorithm Explanation

Find the sum of all numbers $N < 1000000$ that are palindromic in base $10$ and base $2$.

### Parity Optimization
A binary representation of a positive integer starts with `'1'`. For it to be palindromic, it must also end with `'1'`. Thus, any binary palindrome must be an **odd integer**.

1. Iterate odd numbers $i \in [1, 3, 5, \dots, 999999]$.
2. Test decimal palindrome string: `s10 == s10[::-1]`.
3. If valid, test binary palindrome string: `bin(i)[2:] == bin(i)[2:][::-1]`.
4. Accumulate and return the sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 500000$ odd candidates. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary string memory.
