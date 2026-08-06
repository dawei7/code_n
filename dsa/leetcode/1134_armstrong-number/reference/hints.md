## Hints

1. Check whether a $k$-digit number equals the sum of the $k$th powers of its digits.
2. Use division and modulus operations to separate the number into decimal digits and accumulate their $k$th powers.
3. `n % 10` extracts the least significant digit, and integer division by `10` removes it. Raise each extracted digit to the $k$th power and add it to the running sum.
