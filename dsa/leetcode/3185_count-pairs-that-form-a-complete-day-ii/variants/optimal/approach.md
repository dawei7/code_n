## General

**Work with remainder classes.** Two durations form a whole number of days exactly when their remainders modulo 24 sum to a multiple of 24. For a current remainder $r$, the required previous remainder is $(24-r)\bmod24$. This expression correctly maps remainder 0 back to 0 and remainder 12 back to 12.

**Count pairs as their right endpoint arrives.** Scan `hours` from left to right and store how many earlier durations have each of the 24 possible remainders. Before inserting the current remainder, add the stored count of its complement to the answer. Those are exactly the valid pairs whose right index is the current position, so no pair is missed or counted again.

After any processed prefix, the frequency array records precisely the remainder multiplicities in that prefix, and the answer contains every qualifying pair entirely inside it. The next complement lookup adds all and only qualifying pairs ending at the next index; recording its remainder restores the invariant. By induction, the completed scan returns exactly all pairs with $i<j$.

The large input limit is why the 24-slot summary matters: it replaces comparisons against all earlier indices with one constant-time lookup.

## Complexity detail

Let $n$ be the length of `hours`. Each duration causes a constant number of arithmetic operations and array accesses, so the time complexity is $O(n)$. The remainder table has exactly 24 entries regardless of $n$, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Brute-force pair enumeration:** Testing all $i<j$ is correct but costs $O(n^2)$ time, which is not viable for $n$ up to $5\cdot10^5$.
- **Sort the remainders:** Sorting can organize complementary classes but raises the time bound to $O(n\log n)$ without improving the fixed-size storage.
- **Remainder zero:** Durations already divisible by 24 pair with one another, so complement computation must not look for remainder 24.
- **Remainder twelve:** Two remainder-12 values qualify, including equal durations at different indices.
- **Duplicate values:** Index pairs remain distinct even when their duration values are identical.
- **Large answer:** When many durations share a compatible remainder, the count can be on the order of $n^2$ and exceed 32-bit integer range.
- **Large hour values:** Reduce each duration modulo 24; multiples of 24 beyond the first day do not require separate classes.
- **Single duration:** No pair exists, so the result is zero.
