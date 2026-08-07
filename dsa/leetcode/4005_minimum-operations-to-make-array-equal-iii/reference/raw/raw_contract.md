## Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers.

Each operation changes exactly one array entry. Multiplication must use an integer factor of at least $2$. Division must be exact, and its factor must be at least $2$ but strictly smaller than the entry's current value.

For the Required Complexity bound, let $U$ be the number of distinct entries, let $V=\max(\texttt{nums})$, let $D$ be the total number of divisors generated across those distinct values, and let $P=\sqrt V\log\log V$ denote the prime-sieve work.

**Return value**

Return the minimum number of permitted multiplication and division operations required to make all entries equal.
