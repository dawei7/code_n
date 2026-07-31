## General

**Count prefixes by their inversion total**

The actual values in a prefix are irrelevant to the transition; only their
relative order matters. Let `dp[j]` be the number of valid relative orders of
the already-built prefix that contain exactly $j$ inversions. Initially the
empty prefix contributes `dp[0] = 1`.

When extending a prefix of length $\ell-1$ to length $\ell$, insert the new
largest value into its relative order. Placing it at the right end adds zero
inversions. Moving it left across $a$ existing values adds exactly $a$
inversions, so every $a\in[0,\ell-1]$ is possible exactly once. Therefore,

$$
\operatorname{next}[j]
=\sum_{a=0}^{\ell-1}\operatorname{dp}[j-a],
$$

where indices below zero contribute zero. This construction is bijective:
removing the largest value from any length-$\ell$ permutation uniquely
recovers its previous relative order and the number of inversions added by
that value.

**Evaluate each transition with a sliding window**

For consecutive inversion totals, the summation ranges differ by only one
entering and one leaving term. Maintain their sum in `window`: add `dp[j]`,
and once $j\ge\ell$, subtract `dp[j - length]`. This computes all states for
one prefix in $O(C)$ time instead of summing up to $\ell$ terms per state.

After constructing the states for prefix ending at `length - 1`, inspect its
requirement. If that prefix must have exactly `target` inversions, discard
every other state. Thus every state retained for the next iteration satisfies
all requirements seen so far. By the insertion bijection and this filtering,
the final required state counts exactly all valid full permutations.

## Complexity detail

Let $C$ be the maximum required inversion count. There are $n$ prefix lengths,
and each sliding-window transition scans inversion totals from $0$ through
$C$, so the running time is $O(nC)$. Two arrays of $C+1$ counts and an
$n$-element requirement lookup are used, for $O(n+C)$ auxiliary space.

## Alternatives and edge cases

- **Directly sum every insertion range:** Applying the same recurrence with an
  inner loop over all added inversions is correct, but costs
  $O(nC\min(n,C))$ time in the worst case.
- **Two-dimensional DP table:** Keeping every prefix layer makes the proof
  explicit but consumes $O(nC)$ space even though only the previous layer is
  needed.
- **Enumerate permutations:** Generating all $n!$ permutations and checking
  their prefixes is useful only as a tiny-input oracle.
- A length-one prefix can have only zero inversions; a positive requirement at
  `end = 0` makes the answer zero.
- Prefix inversion counts can never decrease as the prefix grows, so
  conflicting requirements naturally eliminate every DP state.
- Requiring zero inversions for the full permutation leaves only increasing
  order, while requiring $n(n-1)/2$ leaves only decreasing order.
- The required count for the full prefix always exists, so the returned DP
  index is well-defined even when its value is zero.
