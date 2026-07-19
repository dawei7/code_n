## General
**Reject impossible last digits:** Every positive integer containing only `1` is odd and does not end in `0` or `5`. Therefore, if `k` is divisible by `2` or `5`, no requested integer exists.

**Carry only the remainder:** Appending a digit `1` to a decimal integer transforms its remainder to `(remainder * 10 + 1) % k`. Start from zero and apply this update once per candidate length. When the remainder becomes zero, return the current length without ever constructing the potentially enormous integer.

**Why k iterations are sufficient:** There are only `k` possible remainders. When `k` has no factor `2` or `5`, the sequence of repunit remainders must reach zero within the first `k` lengths; otherwise a nonzero remainder would repeat and create a cycle that can never reach zero. The number-theoretic coprimality condition guarantees the zero remainder exists.

Testing lengths in increasing order makes the first zero remainder the smallest valid all-ones integer. The recurrence is exactly decimal append followed by modular reduction, so it preserves divisibility information at every step.

## Complexity detail
At most $k$ remainder updates are performed, each using bounded modular arithmetic, for $O(k)$ time. Only the current remainder and length are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Materialize the repunit:** Repeatedly computing `value = value * 10 + 1` is correct in arbitrary-precision languages but makes arithmetic increasingly expensive and stores thousands of digits.
- **Track seen remainders:** A set can detect cycles explicitly, but uses $O(k)$ space even though the iteration bound already suffices.
- **Factor two or five:** Return `-1` immediately.
- **k equals one:** The first one-digit candidate succeeds.
- **Large answer:** Return its length; never serialize or store the full all-ones number.
