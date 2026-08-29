## General

**Turn a range query into two prefix counts**

Let `count(X)` be the number of digit strings representing balanced integers between zero and `X` under the DP's equality test. Then the inclusive range answer is

$$
\texttt{count(high)}-\texttt{count(low-1)}.
$$

The source computes these two values with the same cached digit DP, clearing the cache after changing the bound string `num`.

If `high<11`, no number in the range has at least two digits, so it returns zero immediately. Otherwise `low=max(low,11)` removes all one-digit values from the requested interval.

**Represent balance as one signed difference**

String index zero is position one in the problem and is therefore odd-positioned. The DP adds a digit at even zero-based `pos` and subtracts a digit at odd zero-based `pos`:

$$
\texttt{diff}
=
\begin{cases}
d,&\texttt{pos}\text{ even},\\
-d,&\texttt{pos}\text{ odd}.
\end{cases}
$$

After all digits, `diff==0` exactly means the odd-position digit sum equals the even-position digit sum.

Tracking one difference is smaller and clearer than carrying two independent sums.

**Use `pos` and `lim` to enumerate only bounded numbers**

`pos` identifies the next digit of the fixed-length string `num`. `lim` says whether all earlier chosen digits exactly match the bound prefix.

If `lim` is true, the current digit may range only through `int(num[pos])`. If it is false, the constructed prefix is already smaller and any digit zero through nine is legal.

The next tight flag is

`lim and i == up`.

When the current state is tight, `up` is the bound digit, so choosing it preserves tightness. Choosing anything smaller releases the limit. From a non-tight state, the expression remains false.

At `pos == len(num)`, the digit string represents one number no larger than the bound. The function returns one if its difference is zero and zero otherwise.

**Why leading zeros do not corrupt parity equality**

The DP uses exactly `len(num)` positions and therefore represents shorter numbers with leading zeros. Those zeros contribute nothing to either digit sum.

If the number has an odd count of padding zeros, every real digit's odd/even role is swapped. That changes `diff` to its negative, but

$$
\texttt{diff}=0\iff-\texttt{diff}=0.
$$

If the padding count is even, roles do not change. In either case, the equality of the two sums is preserved.

This special invariance is why the source does not need a `started` flag for parity. It would not be safe for a property that distinguished the sign or actual odd-position sum rather than testing equality.

**Handle zero and one-digit representations by cancellation**

The padded all-zero number has difference zero and is counted by both prefix DP calls. One-digit positive numbers do not have zero difference unless the digit is zero.

After clamping `low` to 11, the lower prefix `count(low-1)` includes the same artificial zero contribution as `count(high)`, so it cancels in subtraction. No forbidden one-digit positive value contributes.

Thus the range result enforces the at-least-two-digit condition even though the internal prefix counter includes padded zero.

**Memoize the reusable states**

`@cache` keys results by `(pos,diff,lim)`. Many digit prefixes lead to the same position, alternating-sum difference, and tightness, after which their possible suffixes are identical.

For a $D$-digit bound, `diff` lies between roughly $-9D$ and $9D$, so there are $O(D)$ possible differences at each of $D$ positions. Tightness has two values. This gives $O(D^2)$ states, each trying at most ten digits.

After computing `a` for `low-1`, the source calls `dfs.cache_clear()` before assigning `num=str(high)`. This is essential because `num` is captured from the enclosing scope but is not part of the cache key. Reusing cached states across different bound strings could return incorrect counts.

**Trace the positional difference**

For 121, the DP visits digits at zero-based positions zero, one, and two:

$$
\texttt{diff}=1-2+1=0,
$$

so it is counted.

For 1234,

$$
\texttt{diff}=1-2+3-4=-2,
$$

so the terminal state returns zero.

All values no larger than the current bound are explored through the same transitions, and prefix subtraction keeps exactly those in the requested inclusive interval.

## Complexity detail

Let $D$ be the maximum decimal digit count, at most 16 for `high<=10^15`. There are $O(D)$ positions and $O(D)$ reachable difference values per position, with two tightness states. Each cached state tries at most ten digits, a constant.

Each prefix count takes $O(D^2)$ time and $O(D^2)$ cache space. Two calls preserve the same asymptotic bounds. Recursion adds $O(D)$ stack space, dominated by the cache.

## Alternatives and edge cases

- **Enumerate every integer:** The range can extend to $10^{15}$, making direct checking impossible.
- **Digit DP with separate odd and even sums:** It works but creates a larger state than their single difference.
- **Add a `started` flag:** This is a conventional way to handle leading zeros; equality's sign symmetry makes it unnecessary here.
- **Reuse the cache after changing `num`:** This is invalid because the bound is captured rather than keyed; clearing is required.
- **Treat string index zero as even problem position:** Problem positions are one-based, so zero-based even indices belong to odd positions and receive the positive sign.
- **One-digit range:** It returns zero through the explicit `high<11` guard.
- **Range crossing 11:** Clamping `low` excludes all shorter numbers.
- **Equal endpoints:** Prefix subtraction returns one exactly when that number is balanced.
- **Leading-zero padding with odd length:** It negates the alternating difference but preserves whether it is zero.
- **Number 100:** Its difference is one, so it is not counted despite internal zeros.
- **Inclusive upper bound:** Tight digit choices are allowed through `range(up+1)`.
- **Large bound:** Only DP states, not all numbers, are explored.
- **Cached Boolean flag:** Python's true/false values safely participate in the cache key.
