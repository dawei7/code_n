## General

**Turn the interval into two prefix counts**

Let $F(x)$ be the number of positive stepping numbers at most the decimal value represented by `x`. The requested inclusive count is

$$
F(\texttt{high}) - F(\texttt{low} - 1).
$$

Subtract one directly from the string `low`, including ordinary decimal borrowing, because an endpoint may have up to $100$ digits and need not fit a machine integer. Reducing the final difference modulo $10^9 + 7$ also handles the case where the two already-reduced prefix counts wrap in different places.

**Count one prefix with digit DP**

Process the digits of a bound from left to right. Memoize a state containing four facts:

- the current digit position;
- the previous chosen digit, once the number has started;
- whether a nonzero digit has started the represented number; and
- whether the chosen prefix is still equal to the bound's prefix.

The tight flag limits the next digit to the bound's current digit; otherwise any digit from `0` through `9` is available. Before the number starts, a zero is only padding and does not participate in the adjacency rule. A nonzero digit starts the number. Afterward, a candidate digit is legal exactly when its difference from the previous digit has absolute value $1$.

At the end of the string, count the state only if a number has started. Thus the all-zero padding path does not count zero, while every positive integer no greater than the bound has exactly one fixed-width representation in the DP. The transition accepts precisely the representations whose adjacent real digits differ by $1$, so $F(x)$ counts every qualifying positive integer at most `x` exactly once. Subtracting the two prefix counts therefore leaves exactly the stepping numbers in the inclusive requested interval.

## Complexity detail

Let $d = \max(\lvert\texttt{low}\rvert, \lvert\texttt{high}\rvert)$. Each digit DP has $O(d)$ states because the previous digit and both flags have constant-size domains, and each state considers at most ten digits. The two prefix counts and string decrement therefore take $O(d)$ time. Memoization and recursion use $O(d)$ space.

Since $d \le 100$, legal inputs provide too little width for an honest timing-based scaling verdict. The package uses a bounded-domain certificate with direct enumeration over small ranges and an independent recurrence through the full 100-digit boundary.

## Alternatives and edge cases

- **Enumerate integers in the interval:** Checking adjacent digits is simple, but the interval can contain nearly $10^{100}$ values and cannot be traversed.
- **Generate stepping numbers with breadth-first search:** Extending a valid number by a neighboring digit avoids invalid candidates, but the number of generated values still grows exponentially with the digit limit.
- **Length-only dynamic programming:** Counts for complete digit lengths are useful, but an additional tight-prefix state is needed to respect an arbitrary endpoint such as `high`.
- Every one-digit positive integer is a stepping number because it has no adjacent pair that can violate the rule.
- The all-leading-zero DP path represents zero and must not contribute to the count.
- Subtracting one from a power of ten removes leading zeros, so `"1000"` becomes `"999"`; subtracting from `"1"` produces `"0"`.
- The interval is inclusive, so a stepping value equal to either endpoint must be counted.
- Apply modulo reduction during the DP and after prefix-count subtraction.
