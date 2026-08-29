## General

**Counting pairs when their right endpoint arrives**

A good pair requires equal values and indices `i < j`. Instead of storing every earlier index, the stored solution records how many times each value has appeared.

When the loop reaches a current value `x` at index `j`, suppose `cnt[x] = c`. There are exactly `c` earlier indices whose values equal `x`. Each can be paired with the current index, so this one occurrence creates `c` new good pairs.

The code adds `cnt[x]` to `ans` and then increments `cnt[x]`. This order is important. The current occurrence must not pair with itself, so it contributes to the count only after all pairs ending here have been counted.

`Counter()` begins empty and supplies zero for a missing key. The first occurrence of any value therefore adds no pairs and creates count one without special-case code.

**A trace with repeated values**

Consider three occurrences of value one:

- The first sees zero earlier ones and adds zero.
- The second sees one earlier one and adds one pair.
- The third sees two earlier ones and adds two pairs.

The total is three, matching the index pairs among three positions. A fourth occurrence would add three more, bringing the total to six.

Values are independent. Seeing a three changes only `cnt[3]` and adds the number of earlier threes. It cannot create a pair with a one because equality is required.

For `[1, 2, 3, 1, 1, 3]`, the second one adds one, the third one adds two, and the second three adds one, giving four.

**The invariant after processing a prefix**

After processing the first `j` elements:

1. `cnt[v]` equals the number of occurrences of value `v` in that prefix.
2. `ans` equals the number of good pairs whose two indices are both in that prefix.

Both statements hold for the empty prefix. When the next value `x` arrives, existing good pairs remain unchanged. The only new pairs are those whose right index is the new position and whose left value is also `x`. There are exactly `cnt[x]` of them, so adding that count updates `ans` correctly. Incrementing the counter then restores the frequency fact for the extended prefix.

By induction, the returned `ans` counts all good pairs in the complete array.

**Why no pair is counted twice**

Every pair has one larger index `j`. It is counted exactly when the loop processes that right endpoint. It was impossible to count earlier because `j` had not been seen, and it is never counted later because later iterations create pairs with different right endpoints.

The method does not need to store indices because only their count matters. Processing left to right automatically enforces `i < j`.

**Connection to the combination formula**

If a value occurs `f` times overall, it contributes

$$
\binom{f}{2} = \frac{f(f-1)}{2}
$$

pairs. The online additions for that value are

$$
0+1+\cdots+(f-1),
$$

which equal the same formula. The source computes these contributions incrementally rather than building all frequencies first and applying combinations afterward.

This online form needs just one pass and makes the right-endpoint reasoning explicit.

It also separates multiplicities without ever mixing their contributions. If one value has frequency four and another has frequency three, their pair totals are computed as six and three independently. There is no cross-term because equality forbids pairing different values. This decomposition is exactly what the counter represents: one small combinatorial process per distinct key, all interleaved safely during the single traversal.

## Complexity detail

Let $N$ be the array length and $U$ the number of distinct values. The loop processes each element once. `Counter` lookup and update take expected $O(1)$ time, so total expected time is $O(N)$.

The counter stores one entry per distinct value, using $O(U)$ space, matching the manifest. The answer and loop variable use constant additional space.

Under the stated values from one through one hundred, a fixed array of 101 counters could give worst-case constant-size storage relative to $N$. The manifest uses the more general distinct-value bound.

Python dictionary hashing gives expected rather than absolute worst-case constant access. Answer size is bounded by $N(N-1)/2$, and Python integers grow as necessary.

## Alternatives and edge cases

- **Count all frequencies first:** Sum `f * (f - 1) // 2` for every value. It has the same $O(N)$ time and $O(U)$ space but uses two conceptual phases.
- **Check every index pair:** Nested loops are simple but take $O(N^2)$ time.
- **Fixed frequency array:** Because values lie from one through one hundred, a small list can replace the hash counter.
- **All values distinct:** Every lookup sees zero earlier matches, so the answer remains zero.
- **All values equal:** Contributions are zero through $N-1$, totaling $N(N-1)/2$.
- **Single element:** No pair exists, and the loop returns zero.
- **Update order:** Incrementing before adding would incorrectly count each element paired with itself.
- **Repeated values far apart:** Position distance is irrelevant; every earlier equal value forms a valid pair.
- **Index order:** Left-to-right processing ensures only pairs with the earlier index first are counted.
- **Required import:** `Counter` must be available from `collections`.
