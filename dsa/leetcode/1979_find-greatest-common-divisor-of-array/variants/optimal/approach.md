## General
**Reduce the array to the two required endpoints**

Scan `nums` to find its minimum and maximum. The contract asks only for the
greatest common divisor of these two values, so no other array value needs to
participate in the number-theory calculation.

**Apply the Euclidean remainder identity**

For positive integers $a$ and $b$ with $a\le b$,

$$
\gcd(a,b)=\gcd(b\bmod a,a).
$$

Replacing the larger pair by the remainder pair preserves every common
divisor: a number divides both $a$ and $b$ exactly when it divides $a$ and
`b % a`. Repeating the replacement strictly reduces the nonzero second
operand until the remainder becomes zero. The remaining positive operand is
therefore the greatest common divisor.

## Complexity detail
Finding the endpoints reads all $N$ values in $O(N)$ time. Euclid's algorithm
performs $O(\log M)$ remainder steps in the worst case, giving
$O(N+\log M)$ total time. Endpoint values and Euclidean state require $O(1)$
auxiliary space.

## Alternatives and edge cases
- **Repeated subtraction:** Replace the larger endpoint by its difference
  from the smaller until they match. This is correct but can take $O(M)$
  iterations for endpoints `1` and `M`.
- **Test divisors downward:** Try candidates from the smaller endpoint to `1`.
  This may also take linear time in the value bound.
- **Sort the array:** Sorting exposes the endpoints but costs
  $O(N\log N)$ time when a linear scan is enough.
- When all entries are equal, the minimum, maximum, and returned GCD are that
  shared value.
- A minimum value of `1` forces the answer to `1`.
- Duplicate endpoints do not change the calculation.
- Array values strictly between the minimum and maximum cannot alter the
  requested GCD.
