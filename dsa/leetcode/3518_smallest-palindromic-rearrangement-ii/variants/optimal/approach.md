## General

**Reduce the palindrome to a multiset permutation**

A palindrome is fixed once its left half and optional center are known. For each letter with total frequency `f`, exactly `f // 2` copies must occur in the left half and the same number must occur in reverse order on the right. If `f` is odd, its one leftover copy is the center.

Because `s` is guaranteed to be palindromic, at most one character has an odd frequency. The source counts all 26 letters, builds:

`half_counts[c] = frequencies[c] // 2`,

and records the first odd-frequency letter as `middle`. Under the guarantee, “first” is also “only.”

Every distinct palindromic permutation corresponds one-to-one with a distinct permutation of this left-half multiset. Lexicographic order is also preserved: the first difference between two full palindromes occurs in their left halves, because the center and mirrored right side are reached only after the entire left prefix. Therefore, finding the `k`-th palindrome is exactly finding the one-indexed `k`-th lexicographic permutation of `half_counts`, then returning:

`half + middle + reverse(half)`.

**Count distinct permutations of a multiset**

If the remaining half contains `R` letters with counts `f_0, f_1, ..., f_25`, the number of distinct permutations is the multinomial coefficient:

`T = R! / (f_0! f_1! ... f_25!)`.

The source computes the same value as a product of binomial coefficients. Imagine adding one character group at a time. If `used` positions have already been filled in all distinguishable ways and the next letter has `count` identical copies, choose which `count` of the new `used + count` positions belong to that new letter:

`C(used + count, count)`.

Multiplying these factors over all nonzero counts telescopes to the multinomial coefficient. This avoids building enormous factorials and divides exactly at every binomial step.

**Cap a binomial when an exact huge value is unnecessary**

`capped_binomial(n, r, limit)` returns `min(C(n,r), limit)`.

It first uses symmetry:

`C(n,r) = C(n,n-r)`,

so `r = min(r, n-r)` minimizes the loop. Starting from one, step `i` applies the exact recurrence:

`value = value * (n - r + i) // i`.

Every intermediate result is an integer binomial coefficient. As soon as `value >= limit`, the helper returns `limit`, because callers need only know that the count has reached the cap. If `limit <= 1`, returning it immediately is valid since every ordinary binomial coefficient in this use is at least one.

**Cap the complete multinomial safely**

`capped_permutations(counts, limit)` similarly returns `min(T, limit)`. It maintains the exact product `ways` while that product is below `limit`.

Before multiplying by the next binomial factor, it computes:

`factor_limit = ceil(limit / ways)`

using

`(limit + ways - 1) // ways`.

If the true factor reaches `factor_limit`, then `ways * factor >= limit`, so the whole result may safely be capped. If it stays below that threshold, `capped_binomial` returns the exact factor and multiplication remains exact. Thus the cap never changes a value that is still relevant to a later comparison.

**Lexicographic permutations form consecutive first-letter blocks**

Suppose `R` letters remain and the current multiset has `T` distinct permutations. For a candidate letter `c` with frequency `f_c > 0`, the number of permutations beginning with `c` is:

`B_c = (R - 1)! / ((f_c - 1)! product of other f_j!)`.

Comparing this with `T` gives the useful identity:

`B_c = T * f_c // R`.

All permutations beginning with `a` come first, followed by those beginning with `b`, and so on. Therefore the source can try available letters in alphabetic order:

- if `k > B_c`, the desired permutation lies after this entire block, so subtract `B_c` from `k`;
- otherwise, choose `c` and continue within that block with the unchanged one-indexed `k`.

After choosing a letter, its count and `R` each decrease by one. Repeating this constructs one left-half position at a time.

**Why the source caps at k times remaining**

The exact total `T` can be astronomically large, while `k <= 10^6`. At a position with `R` letters remaining, the source asks for:

`total = min(T, k * R)`.

This particular cap enables a shortcut. If `total >= k * R`, then the true `T >= kR`. Let `c` be the lexicographically first available letter. Since its frequency is at least one:

`B_c = T * f_c / R >= T / R >= k`.

So the `k`-th permutation must lie in the very first letter block. The source selects the first nonzero count without needing exact `T` or `B_c`.

If `total < k * R`, the capped result must equal the exact `T`. The source can then compute every block exactly with `total * count // remaining` and subtract skipped blocks. This two-case logic is the central optimization: either the count is huge enough that the first choice is forced, or it is small enough to use exactly.

**Detect a rank beyond the available permutations**

In the exact-count case, the source tries all available letters. If `k` exceeds every block combined, no candidate is selected and `chosen` remains `-1`. That means the requested rank is larger than the number of distinct permutations of the current multiset, so it returns the empty string.

If the original rank was valid, exactly one block contains it at every position. The source appends that block's character, decrements its half-count, and continues until no left-half letters remain.

There is a separate empty-half case. When `remaining = 0`, there is exactly one palindromic permutation: `middle`, which may be a single character. The source returns it only for `k = 1` and returns an empty string for larger ranks.

**A rank trace for abba**

For `s = "abba"`, the half counts are one `a` and one `b`, so `R = 2` and `T = 2`.

For `k = 2`, the `a` block has:

`B_a = 2 * 1 // 2 = 1`.

Since `2 > 1`, skip that block and set `k = 1`. The `b` block contains the adjusted rank, so the first half character is `b`. Only `a` remains, giving left half `"ba"`. Mirroring yields `"baab"`.

**Why the constructed answer is correct**

At each position, lexicographic order partitions all remaining multiset permutations into consecutive blocks by their next character. The block-size identity counts each distinct suffix exactly once despite repeated letters. The cap shortcut chooses the first block only when its size is provably at least `k`; otherwise exact counts locate the unique containing block. Inductively, the built prefix is the prefix of the requested one-indexed permutation, or the source correctly discovers that no such rank exists.

Mirroring that left half uses every character pair, the forced odd character occupies the center, and the result is palindromic. Because left-half and full-palindrome orders agree, its full rank is also exactly `k`.

## Complexity detail

Let `n = len(s)`, `h = floor(n/2)`, and let the alphabet size `sigma = 26`. Counting frequencies and constructing the final strings take `O(n)` time.

There are `h` unranking positions. Each calls `capped_permutations`, which scans 26 counts. For a nontrivial binomial factor, choosing the smaller side makes each multiplicative step grow the running combinatorial value rapidly; computation stops once the overall product reaches `kR <= kh`. Across one capped count, the number of meaningful multiplication steps is bounded by `O(log(kh))`, with the fixed alphabet scan adding `O(sigma)`. Candidate selection scans at most 26 letters.

With `sigma` treated as a constant, the source's stated time bound is `O(n log(nk))`. A more explicit expression is `O(n + h(sigma + log(kh)))`.

`frequencies` and `half_counts` each have 26 integers. `left` grows to `h` characters, and the joined half, reverse, and returned string occupy linear space. Auxiliary construction space is `O(n)`, while fixed counting metadata is `O(1)` for the lowercase alphabet.

Python's arbitrary-precision integers avoid overflow. Capping counts at `kR` also keeps their practical magnitude small. In a fixed-width implementation, the multiplication inside the binomial recurrence still needs guarded arithmetic even with a cap.

## Alternatives and edge cases

- **Generate and sort every palindromic permutation:** The number of distinct half permutations can be factorial, so enumeration is infeasible for length `10^4`.
- **Use exact factorial multinomials:** Mathematically direct, but factorials become enormous. Capped incremental combinations compute only the information needed for rank comparisons.
- **Use the editorial's trial-character recount:** Trying every candidate and recomputing its suffix count is valid. The protected source instead computes the current total once and derives each first-letter block as `T * frequency / remaining`.
- **Cap total merely at k:** Knowing `T >= k` does not imply the first character block has `k` items. The stronger cap `k * remaining` guarantees even a frequency-one first block is large enough.
- **Zero-index k:** The source uses one-indexed ranks. Block skipping tests `k > block` and subtracts whole blocks; changing to zero-indexing would require consistent inequalities.
- **Repeated letters:** Multinomial division and the block identity count identical rearrangements once, exactly as required.
- **Even-length input:** No count is odd, so `middle` stays empty.
- **Odd-length input:** The sole odd-frequency letter becomes the center and does not participate in left-half ranking.
- **Length one:** The left half is empty. Rank one returns the character; any larger rank returns an empty string.
- **Only one distinct half letter:** There is one half permutation. The loop repeatedly chooses that letter; `k > 1` eventually leaves no chosen block and returns empty.
- **k larger than the total:** Exact block subtraction exhausts every candidate at some position, leaving `chosen = -1` and producing the required empty string.
- **k equals a block boundary:** The test keeps `k` in the current block when `k <= block`. Thus the last permutation of one block is not incorrectly moved to the next.
- **Multiple odd counts:** The source chooses only the first odd letter, but the input guarantee excludes this case. Without that guarantee, feasibility validation would be necessary.
- **Alphabet order:** Iterating indices zero through 25 maps exactly to `a` through `z`, so block order matches lexicographic order.
