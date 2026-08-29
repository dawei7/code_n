## General

**Translate a square-free product into prime bits**

Every input value is at most 30, so only ten primes can appear:

`[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`.

A good subset's product uses each prime at most once and uses at least one prime. Represent the primes present in a product by a 10-bit mask. Combining values is legal exactly when their masks do not overlap.

**Discard values that already repeat a prime**

If one chosen number is divisible by a square, its own factorization already repeats a prime and can never belong to a good subset.

Within 2 through 30, every relevant prime square is 4, 9, or 25; the next, 49, exceeds the domain. The source skips values divisible by any of those three numbers.

For every remaining value `x`, it sets bit `i` when `x % primes[i] == 0`. Because squareful values were excluded, this mask describes distinct prime factors exactly.

**Compress duplicate input values**

`Counter(nums)` records `cnt[x]`, the number of occurrences of each value. The DP processes numeric values 2 through 30 rather than all $N$ indices individually.

For a valid $x>1$, a good subset can choose at most one occurrence: choosing two copies repeats every prime factor of $x$. If it chooses $x$, there are `cnt[x]` distinct index choices. This multiplicity appears as a factor in the transition.

**Handle ones separately**

Value one contributes no prime factor. Any collection of ones may accompany a good non-one selection without changing its product.

With `cnt[1]` ones, there are $2^{\texttt{cnt[1]}}$ ways to choose their indices, including choosing none. The source initializes

`f[0] = pow(2, cnt[1])`.

Thus every later nonzero-prime state automatically carries all possible one selections. A subset containing only ones remains in mask zero and is excluded from the final sum because its product is one, not a product of one or more primes.

**Define and update the mask DP**

`f[state]` counts processed-index subsets whose square-free prime product has exactly `state`.

For current value mask `mask`, a target `state` can receive new subsets only if it contains all bits of `mask`. The test

`state & mask == mask`

checks this. Clearing those bits with `state ^ mask` gives the previous disjoint prime state.

The contribution is

`cnt[x] * f[state ^ mask]`,

because choose one of the `cnt[x]` occurrences and combine it with any previous subset using none of $x$'s primes.

Existing `f[state]` remains, representing subsets that do not choose $x$.

**Why states are traversed downward**

The loop visits target masks from all ones down to one. Since `mask` is nonzero, `state ^ mask` is numerically smaller than `state` when `state` contains the mask.

Descending order ensures the source state has not yet been updated for the current $x$. Therefore one transition cannot choose the same numeric value twice. This is the mask-DP version of a 0/1 knapsack update.

**Why the DP is correct**

Every accepted transition combines disjoint prime masks, so its product remains square-free. The multiplicity factor chooses exactly one actual occurrence of $x$, and the one initialization accounts for all optional one indices.

Conversely, take any good subset. For each non-one numeric value it contains at most one occurrence, and the selected values' masks are pairwise disjoint. Processing values in increasing order reconstructs this subset through exactly one chain of transitions, with the correct occurrence choices. Hence every good index subset is counted once.

Summing masks one through $2^{10}-1$ includes every product containing at least one prime and excludes the mask-zero, ones-only selections.

## Complexity detail

Let $N$ be input length, $U=29$ candidate values from 2 through 30, and $P=10$ primes. Building the counter costs $O(N)$. Mask construction costs $O(UP)$, and DP scans $2^P$ states per candidate, for $O(U2^P)$ dominant fixed-domain work.

Total time is $O(N+U2^P)$ and space is $O(U+2^P)$, conventionally reported as $O(2^P)$ beyond the fixed-size counter. All counts are reduced modulo $10^9+7$.

## Alternatives and edge cases

- **Enumerate all index subsets:** Exponential in $N$ and impossible at $10^5$ elements.
- **Factor every occurrence independently:** Correct but wastes work because values lie in the tiny domain 1 through 30.
- **Forward mask iteration:** Can reuse the current value within the same pass and overcount invalid repeated primes.
- **Value one:** Any subset of one occurrences can accompany a nonzero mask; ones alone are not good.
- **Squareful values such as 4, 12, 18, or 25:** Skipped because their own product repeats a prime.
- **Prime value:** Its mask has one bit and is a valid singleton.
- **Product of distinct primes such as 30:** Its mask has three bits and can be chosen once.
- **Duplicate valid value:** Choose at most one occurrence, but there are `cnt[x]` choices of index.
- **Overlapping different values:** For example, 6 and 15 share prime three and cannot coexist.
- **No valid non-one value:** All nonzero states stay zero and the answer is zero.
- **Modulo:** Applied to every updated state and to the final sum.
- **Input preservation:** Counting values does not modify `nums`.
