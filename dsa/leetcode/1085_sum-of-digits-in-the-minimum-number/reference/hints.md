## Hints

1. First consider how to identify the minimum number in an array.
2. A single pass can compare each array value with the smallest value seen so far.
3. After finding the minimum, consider how to obtain the sum of its decimal digits.
4. Repeatedly take the remainder modulo `10` and then divide the number by `10`; add the remainders and map the resulting parity to the required return value.
