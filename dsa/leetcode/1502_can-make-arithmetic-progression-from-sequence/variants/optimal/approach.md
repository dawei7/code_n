## General

**Derive the only possible nonnegative step from the endpoints**

Any valid progression can be reversed without changing whether it exists.
Therefore, consider its non-decreasing orientation. Its first value must be
`min(arr)` and its last value must be `max(arr)`. If the common difference is
$d$, moving across the $n-1$ gaps gives

$$
\max(\texttt{arr})-\min(\texttt{arr})=(n-1)d.
$$

The span must be divisible by $n-1$, and when it is divisible the nonnegative
difference is forced. There is no second candidate step to try. If the span is
zero, every value equals the minimum and the array already forms a
zero-difference progression.

**Check the complete forced progression**

For a positive difference, the only possible non-decreasing progression is

$$
\min(\texttt{arr}),\ \min(\texttt{arr})+d,\ \ldots,\
\min(\texttt{arr})+(n-1)d.
$$

Put all input values in a hash set. A positive-step progression has $n$
distinct positions, so first require the set to contain exactly $n$ values.
This rejects duplicates even when the endpoints and span appear plausible.
Then generate each required term and test expected constant-time membership.

These checks are sufficient. When they all pass, the generated terms use every
input occurrence and their increasing order has constant difference $d$.
Conversely, any valid arrangement has the same endpoints and therefore the same
forced $d$; it must contain every term the membership scan checks.

## Complexity detail

Finding the endpoints, building the set, and checking the $n$ forced terms each
take $O(n)$ expected time because hash-set membership is expected $O(1)$. The
set stores at most $n$ values, so auxiliary space is $O(n)$.

The implementation leaves `arr` unchanged. Integer arithmetic is exact over
the stated bounds. This branch is the default because it has the best expected
asymptotic time, even though it needs more boundary reasoning than sorting.

## Alternatives and edge cases

- **Sort and compare adjacent gaps:** This is the Simplified branch. It exposes the progression directly and is usually easier to explain, but costs $O(n\log n)$ time.
- **Index each value by normalized offset:** Mapping each value to a unique offset from the minimum is also linear, but needs the same careful handling of a zero difference and duplicates.
- **Two elements:** Any pair forms an arithmetic progression because it has only one adjacent difference.
- **All values equal:** The span is zero, so duplicates are required rather than disqualifying.
- **Duplicates with a nonzero span:** A positive-difference progression has distinct terms, so any duplicate makes the answer false.
- **Span not divisible by $n-1$:** No integer common difference can connect the endpoints in exactly $n-1$ steps.
- **Negative values:** Minimum, span, divisibility, and membership need no special sign rule.
