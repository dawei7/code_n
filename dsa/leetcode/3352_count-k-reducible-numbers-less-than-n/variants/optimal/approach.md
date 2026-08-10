## General

**Separate a number's first operation from all later operations.** For any positive integer $x$, the first operation replaces it with the number $c$ of set bits in its binary representation. Once $c$ is known, the actual positions of those set bits no longer matter. The remaining number of operations depends only on $c$.

The array `reduction_steps[c]` stores how many popcount operations are needed to reduce $c$ itself to one. Values zero and one retain the initialized value zero; zero will later be excluded, while one already needs no further operation. For every `c >= 2`,

`reduction_steps[c] = reduction_steps[c.bit_count()] + 1`.

This forward computation is valid because `c.bit_count() < c` for every integer at least two, so the referenced smaller state has already been filled.

An original number with $c$ set bits normally needs one first operation plus `reduction_steps[c]` more. It is reducible within at most `k` operations exactly when

$$
\texttt{reduction\_steps}[c] < k.
$$

The strict inequality is the same as `1 + reduction_steps[c] <= k`. It also includes $x=1$ when `k >= 1`, as required, even though one is already reduced before performing an operation.

**Count smaller numbers by their number of set bits.** The binary string `s` can have length 800, so converting it to an ordinary integer and enumerating every smaller positive number is impossible. Instead, the source performs a digit DP over its bits.

After processing some prefix positions, `less_counts[c]` counts binary prefixes that are already strictly smaller than the corresponding prefix of `s` and contain exactly $c$ ones. Leading zeros are allowed. They are not extra representations; every fixed-length bit pattern uniquely represents one integer below $2^{\lvert s\rvert}$.

The exact prefix equal to `s` is not stored in the array. There is only one such prefix, so `exact_ones` is enough to remember how many ones it contains.

**Extend prefixes that are already smaller.** Once a prefix is smaller, either zero or one may be placed at the next position without losing that status. For each count `ones` with `ways = less_counts[ones]`:

- appending zero adds `ways` to `next_counts[ones]`;
- appending one adds `ways` to `next_counts[ones + 1]`.

All additions are reduced modulo $10^9+7$ immediately.

**Create a newly smaller prefix when the current limit bit is one.** If the current character of `s` is `"1"`, the unique equal prefix may choose zero here. That choice is smaller for the first time and keeps its current `exact_ones` count, so one way is added to `next_counts[exact_ones]`.

The equal path itself chooses one and remains equal, so `exact_ones` is incremented. If the limit bit is zero, the equal path must also choose zero; it remains equal and creates no new smaller state. This compactly implements the usual DP states “tight” and “already smaller” without a two-dimensional Boolean flag.

**Understand the invariant after the final bit.** Once all positions are processed, `less_counts[c]` counts exactly the integers $x$ satisfying $0\le x<n$ whose binary representation contains $c$ ones. The number equal to $n$ followed the separate exact path and was never inserted, so the upper bound is strict.

The return expression sums buckets from one through `length` whose reduction count is below `k`. Starting at one set bit excludes integer zero, which is not positive and never reaches one through the stated operation. Modulo is applied once more after the bucket sum.

**Trace the strict-bound transition with `s = "1000"`.** At the first bit, choosing zero from the equal path creates the all-zero smaller prefix; choosing one preserves the unique exact path. At each remaining zero bit, every already-smaller prefix branches with zero or one, while the exact path must keep zero. The final table consequently represents precisely 0 through 7, grouped by popcount, and never includes 8 itself.

For `k=2`, a bucket with $c=1$ has `reduction_steps[1]=0<2`, and a bucket with $c=2$ has one remaining step because two has one set bit. Buckets are accepted according to this precomputed chain rather than by examining every represented integer.

**Why every answer is counted once and classified correctly.** Every smaller fixed-length bit string has a unique first position where it chooses zero under a one in `s`; that exact transition inserts it into the smaller DP exactly once. Subsequent branching produces its remaining suffix. Its final ones count determines the first popcount result, and `reduction_steps` exactly follows all later results. The final filter therefore includes precisely the positive $k$-reducible integers less than $n$.

## Complexity detail

Let $m=\lvert s\rvert$. At position `position`, the inner loop considers up to `position + 1` possible ones counts. Summing these lengths gives

$$
\sum_{i=0}^{m-1}(i+1)=O(m^2).
$$

Initializing each `next_counts` array also costs $O(m)$ per position and remains within the same $O(m^2)$ time bound. Computing `reduction_steps` and the final sum each cost $O(m)$.

The algorithm retains `reduction_steps`, `less_counts`, and one `next_counts` array, each of length $m+1$. Old arrays become reclaimable after reassignment, so auxiliary space is $O(m)$ rather than $O(m^2)$.

## Alternatives and edge cases

- **Combinatorial prefix counting:** For each eligible popcount, scan `s` and add binomial coefficients when a one can be lowered to zero. It also needs precomputed combinations and typically costs $O(m^2)$.
- **Memoized digit DP:** A state `(position, ones, tight)` is conceptually direct but can store $O(m^2)$ states; the iterative source compresses the position dimension.
- **Enumerate integers below `n`:** This is exponential in the bit-string length and impossible for 800 bits.
- **`s = "1"`:** The only smaller integer is zero, and excluding the zero-ones bucket correctly returns zero.
- **Integer one:** It is positive and already equal to the reduction target, so it is included for every allowed `k >= 1`.
- **Powers of two:** They have one set bit and reach one after a single operation, except one itself needs none.
- **Zero bucket:** Leading-zero patterns collectively represent integer zero only once; beginning the final sum at one excludes it.
- **No leading zeros in `s`:** This ensures its length is the canonical binary length of `n`, though DP candidates intentionally use leading zeros.
- **Strictly less than `n`:** The equal path is never merged into `less_counts` at the end.
- **Current limit bit zero:** Choosing one would exceed `s` at that position and is correctly unavailable to the exact path.
- **Current limit bit one:** Choosing zero is the unique transition that first makes the prefix smaller.
- **Modulo:** Every DP transition is reduced, keeping counts bounded while preserving the final residue.
- **Small `k`:** The strict test `reduction_steps[ones] < k` accounts for the original number's first popcount operation.
- **`reduction_steps[0]`:** Its initialized value is irrelevant because zero is excluded from the final sum.
- **Array bounds:** A processed prefix of length `position` cannot have more than `position` ones, which is why the inner range is safe.
