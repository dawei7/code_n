## General

**Convert characters into a numeric array**

Dictionary `d` maps every custom character in `chars` to its paired value from `vals`. Distinctness of `chars` guarantees one unambiguous override per character.

For a character absent from the dictionary, the default expression

`ord(c) - ord('a') + 1`

computes its one-indexed alphabet position. Thus the loop sees the string as a sequence of signed numeric costs.

The task becomes maximum-sum contiguous subarray with an additional option to choose the empty substring of cost zero.

**Prefix-sum view of a substring**

Let $P_r$ be the total cost of the prefix through current position $r$, and let $P_{-1}=0$ for the empty prefix.

The cost of substring starting after prefix boundary $l$ and ending at $r$ is

$$
P_r-P_l.
$$

For fixed endpoint $r$, this difference is maximized by subtracting the smallest prefix total seen before the endpoint.

The solution maintains:

- `tot` as the current prefix total;
- `mi` as the minimum prefix total available before the next endpoint;
- `ans` as the best substring cost found.

All begin at zero, incorporating the empty prefix and empty-substring answer.

The prefix boundary represented by `mi` must occur before the current character. A numerical minimum alone would be insufficient if it could come from the future, but the left-to-right scan prevents that: `mi` contains only the empty prefix and prefixes completed during earlier iterations. Consequently, every difference evaluated by `tot - mi` corresponds to a genuine contiguous substring in the original order.

**Exact update order**

For each character cost $v$:

1. `tot += v` forms the prefix through the current character;
2. `ans = max(ans, tot - mi)` uses the smallest earlier prefix to find the best substring ending here;
3. `mi = min(mi, tot)` makes the current prefix available as a starting boundary for future substrings.

Updating `ans` before `mi` preserves nonempty ending substrings in the prefix-difference interpretation. Even if current `tot` becomes the new minimum, using it against itself would produce an empty substring of zero; `ans` already starts at zero, so the final result remains correct either way.

**Connection to Kadane's algorithm**

Traditional Kadane maintains the best nonnegative running substring sum:

$$
current=\max(0,current+v).
$$

The prefix-minimum formulation is algebraically equivalent. Whenever `tot` falls to a new minimum, future substrings effectively restart after that boundary. `tot - mi` is the accumulated cost since the best restart point.

The exact code uses prefix language rather than an explicit reset.

**Why the minimum prefix gives the best start**

For the same ending total `tot`, subtracting a smaller earlier prefix produces a larger difference. Every substring ending at the current character corresponds to exactly one earlier prefix boundary, so comparing only the minimum loses no candidate.

Taking the maximum across all endpoints then covers every nonempty substring exactly through its right endpoint. Initial zero also lets a substring start at index zero.

This argument establishes both directions needed for correctness. Every value considered by the algorithm is the cost of an allowed substring, so `ans` cannot exceed the true optimum through an invalid construction. Conversely, choose an optimal nonempty substring and look at the iteration for its final character. Its preceding prefix boundary has already been seen, and `mi` is no larger than that boundary's total, so the candidate computed in that iteration is at least the optimum. If the empty substring is optimal, the initial zero supplies it directly.

**Trace `s = "adaa"`**

Custom value for `d` is $-1000$, while `a` has default value one. Numeric costs are $[1,-1000,1,1]$.

- After first `a`, `tot=1` and `ans=1`.
- After `d`, `tot=-999` and `mi` becomes $-999$.
- Next `a` gives `tot=-998`, so difference from `mi` is one.
- Final `a` gives `tot=-997`, difference two.

The best substring is the final `"aa"` with cost two.

If every cost is negative, `tot - mi` never raises `ans` above zero. The empty substring is allowed, so zero is correct.

**Custom values override defaults completely**

A character listed in `chars` uses its supplied value even when that value is negative or differs greatly from its alphabet position. `dict.get` returns the default only for absent keys.

Building the dictionary with `zip(chars, vals)` pairs corresponding positions and stops at their equal guaranteed length.

## Complexity detail

Let $n=|s|$ and $k=|\texttt{chars}|$. Building the dictionary takes $O(k)$ time and space. Scanning `s` takes expected $O(n)$ time with dictionary lookups, so total expected time is $O(n+k)$.

The dictionary stores at most 26 entries. Under the fixed lowercase alphabet this is $O(1)$ bounded space, matching the manifest; expressed in input parameter $k$, it is $O(k)$. All other state is constant.

## Alternatives and edge cases

- **Standard Kadane:** Maintain a running maximum ending sum with reset to zero; it gives the same result.
- **Enumerate substrings:** There are $O(n^2)$ candidates and summing them directly is too slow.
- **Prefix-sum array:** Storing all prefixes works but uses $O(n)$ space when only the minimum is needed.
- **All negative costs:** Empty substring wins with cost zero.
- **Custom positive value:** It participates normally and may expand the best substring.
- **Custom negative override:** The alphabet default must not be used for a listed character.
- **Best substring starts at zero:** Initial `mi=0` makes that candidate available.
- **Repeated characters:** Dictionary lookup applies the same value at every occurrence.
- **Bounded alphabet:** At most 26 custom mappings keep storage constant in this problem domain.
