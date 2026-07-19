## General
**Select only the global minimum:** Scan the list once and keep its least value. Sorting would reveal the same value but performs unnecessary ordering work on all other elements.

**Extract decimal digits arithmetically:** Repeatedly add `value % 10` and replace `value` with `value // 10` until it becomes zero. Because every input number is positive, the loop processes exactly the minimum's decimal digits.

**Map parity to the required integer:** Evaluate whether `digit_sum % 2 == 0` and convert that Boolean to `1` or `0`.

The first scan produces the true minimum by comparison with every element. The quotient-and-remainder loop partitions its base-ten representation into each digit exactly once, so `digit_sum` is correct. The final parity test therefore returns precisely the required result.

## Complexity detail
Finding the minimum takes $O(n)$ time, and extracting its $D$ digits takes $O(D)$ time, for $O(n+D)$ total. Only the running minimum, digit sum, and current quotient are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort the array:** Reading the first sorted value is correct but costs $O(n\log n)$ time and may require extra storage or mutate the input.
- **Convert the minimum to text:** Summing converted digit characters is valid but allocates a $D$-character representation.
- **Sum every number's digits:** It answers a different question; only the minimum number is used.
- **Duplicate minimum:** Process the value once; multiplicity does not affect its digit sum.
- **Minimum containing zero digits:** Arithmetic extraction naturally includes each zero with no contribution to the sum.
- **Single element:** That element is the minimum and is processed normally.
