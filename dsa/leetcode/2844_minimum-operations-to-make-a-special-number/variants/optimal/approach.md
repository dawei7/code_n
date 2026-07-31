## General

**Reduce divisibility to a suffix.** A non-negative decimal integer is divisible by $25$ exactly when its last two digits are `00`, `25`, `50`, or `75`, except that the one-digit value `0` is also divisible by $25$. Therefore, any nonzero useful result can be identified by choosing two surviving digits that form one of those four endings.

**Match each ending from the right.** For a target such as `25`, scan backward to find the rightmost `5`, then continue backward to find the rightmost `2` before it. Digits skipped after the `5` and between the chosen `2` and `5` must be deleted. Digits before the `2` may remain because they do not change the last two digits.

Choosing the rightmost possible second digit cannot hurt: any valid first digit for an earlier occurrence is also before this later occurrence. After fixing that second digit, choosing the rightmost matching first digit minimizes the deletions between them. Thus this scan gives the minimum deletion cost for its target suffix. Repeating it for the constant set `00`, `25`, `50`, and `75` covers every positive multiple of $25$ that can be formed.

As a fallback, if `num` contains a zero, delete every other digit at cost $n-1$ and retain that zero. If no zero exists, deleting all $n$ digits produces the defined value `0`. The smallest suffix or fallback cost is therefore globally optimal.

## Complexity detail

Let $n=\lvert\texttt{num}\rvert$. Each of four fixed target suffixes performs at most one backward pass over the string, so total time is $O(4n)=O(n)$.

Only indices, counters, the answer, and four constant two-character targets are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every digit pair:** Testing all ordered index pairs is direct and correct but takes $O(n^2)$ time.
- **Dynamic programming over remainders:** Tracking the cheapest subsequence for all $25$ remainders works, but it is more machinery than the four possible final pairs require.
- **Already special:** If the original string ends in `00`, `25`, `50`, or `75`, the matching scan returns `0`.
- **Single retained zero:** A zero anywhere in the input supplies a result with cost at most $n-1$, even when no valid two-digit ending can be formed.
- **Delete every digit:** When no usable suffix and no zero exist, deleting all digits is valid because the problem defines the empty result as `0`.
- **Repeated suffix digits:** Forming `00` requires two distinct zero positions in increasing order; one zero only supports the single-zero fallback.
- **Preserved prefix:** Digits before the chosen suffix remain in their original order and do not affect divisibility by $25$.
