## General

**Use associativity to split a triple into a pair and one value**

The direct interpretation tries every ordered index triple and tests

`nums[i] & nums[j] & nums[k] == 0`.

That uses three nested loops. With as many as one thousand values, `N^3` checks are too expensive.

Bitwise AND is associative:

`(x & y) & z = x & (y & z)`.

Therefore, the first two selected values can be summarized by the single mask `x & y`. Once two ordered pairs produce the same mask, they behave identically with every possible third value. The algorithm exploits that equivalence: calculate how many ordered pairs produce each mask once, then test each distinct mask against each possible third value.

**Count ordered pairs, including multiplicity**

The expression

`Counter(x & y for x in nums for y in nums)`

iterates over every ordered pair of array values. The outer and inner loops both range over the full array. Consequently, it includes pairs corresponding to `(i, j)` and `(j, i)` separately, and it permits `i = j`. Both behaviors are required because the definition independently allows every index from zero through `N - 1`.

Although `x & y` has the same numeric result as `y & x`, the two index choices are still different ordered pairs and both increase the counter. Repeated values also contribute separately. If a value appears several times, each occurrence represents a distinct index, and the generator naturally preserves that multiplicity.

The resulting counter maps a bit mask `xy` to a frequency `v`. The meaning of one entry is:

> Exactly `v` ordered choices of the first two indices produce the intermediate result `xy`.

The generator feeds values directly into `Counter`; it does not first allocate a list containing all `N^2` pair results.

**Attach every possible third index**

The return expression is equivalent to the following reasoning:

- visit each distinct pair mask `xy` and its frequency `v`;
- visit every array element `z` as the value at the third index;
- if `xy & z == 0`, add `v` to the answer.

Why add `v` rather than one? For this particular occurrence of `z`, all `v` ordered pairs represented by the counter entry create a valid triple. They share the same intermediate mask, so the final AND result is identical for all of them.

The loop over `nums` is intentionally not a loop over distinct values. If the same `z` occurs at three indices, those are three different choices for `k` and must each contribute. Iterating over the original array counts them separately.

**What bitwise compatibility means**

A bit remains one after AND only when it is one in every operand. Thus `xy & z == 0` means the first pair's common-one bits and the third value's one bits are disjoint. Bits already removed by `x & y` can never reappear, which is why the pair mask contains all information needed about the first two choices.

A pair mask of zero is compatible with every `z`, since `0 & z` is always zero. A nonzero mask may still be compatible if `z` has zeros at all positions where the mask has ones.

**Trace the sample `[2, 1, 3]`**

In binary, the values are `10`, `01`, and `11`. The nine ordered pairs produce:

- mask `2` three times: `2 & 2`, `2 & 3`, and `3 & 2`;
- mask `0` two times: `2 & 1` and `1 & 2`;
- mask `1` three times: `1 & 1`, `1 & 3`, and `3 & 1`;
- mask `3` one time: `3 & 3`.

So the counter is conceptually `{2: 3, 0: 2, 1: 3, 3: 1}`.

For the third value `2`, masks zero and one are compatible, contributing `2 + 3 = 5` triples. For third value `1`, masks zero and two are compatible, contributing another `2 + 3 = 5`. For third value `3`, only mask zero is compatible, contributing `2`. The total is `5 + 5 + 2 = 12`.

This trace also shows why frequencies cannot be discarded. There are only four distinct pair masks, but they represent all nine ordered index pairs.

**Why every valid triple is counted exactly once**

Take any ordered triple of indices `(i, j, k)`. During counter construction, the ordered pair `(i, j)` contributes one unit to the frequency stored under `xy = nums[i] & nums[j]`. During the second phase, the loop reaches the occurrence `nums[k]`.

If the triple's AND is zero, then `xy & nums[k] == 0`, so the counter's frequency is included for that third-index occurrence. The particular pair `(i, j)` is one of those frequency units. If the triple's AND is nonzero, its mask fails the test and is not included.

Conversely, every unit added by the algorithm corresponds to one concrete ordered pair represented by `v` and the concrete third occurrence currently visited. The compatibility test proves their three-way AND is zero. Grouping pairs by mask merges computation, not identities: their multiplicities remain in `v`. Hence all and only valid ordered triples are counted.

**Why zero-valued inputs need no special branch**

If `z = 0`, every pair mask passes because `xy & 0 = 0`. If either member of the first pair is zero, their mask is zero and every third value passes. The normal counter and compatibility test already capture these large contributions. For `[0, 0, 0]`, all nine ordered pairs have mask zero, and each of three third-index occurrences adds nine, producing `27`.

## Complexity detail

Let `N` be the array length, `D` the number of distinct masks produced by pairwise AND, and `U = 2^{16}` the size of the possible mask universe under the input bound.

Building the counter evaluates exactly `N^2` ordered pairs, taking `O(N^2)` time. The summation then tests every one of the `D` stored masks against each of the `N` array occurrences, taking `O(DN)` time. The exact implementation bound is therefore `O(N^2 + DN)`.

Because `D <= U` and `N <= U`, this also lies within the coarser mask-universe bound `O(N^2 + DU)` recorded for the variant. In practice, iterating only through the original `N` third values is substantially smaller than scanning all `U` masks.

The counter stores `D` entries, so auxiliary space is `O(D)`, which is at most `O(U)`. The generator is lazy and does not add an `O(N^2)` pair-result list.

## Alternatives and edge cases

- **Three explicit loops:** It mirrors the definition directly but performs `O(N^3)` AND tests and repeats the same pair result for every third index.
- **Two loops plus a raw pair-result list:** Precomputing all `N^2` masks avoids recomputing AND, but retaining every occurrence individually uses `O(N^2)` space. The counter compresses equal masks while preserving their frequencies.
- **Frequency-compress the input values too:** Count each distinct third value and multiply by its occurrence count. This can reduce work when `nums` has many duplicates, but requires another mapping and slightly more bookkeeping.
- **Subset-transform methods:** A sum-over-subsets dynamic program can precompute how many values are compatible with each mask in roughly `O(U \log U)` after pair counting. It is useful for a large number of distinct third values but is more complex and always pays for the full `2^{16}` universe.
- **Ordered indices:** `(i, j, k)` and `(j, i, k)` are distinct choices even though AND is commutative. The nested generator counts both.
- **Repeated use of an index:** The three indices are not required to differ. Each loop independently ranges over the full array, so choices such as `i = j = k` are included.
- **Duplicate values:** Equal numeric values at different positions remain separate index choices. Pair frequencies and the repeated `z` loop retain their full multiplicity.
- **All zeros:** Every one of the `N^3` ordered triples is valid, and the compressed calculation still returns exactly `N^3`.
- **Single element:** The method evaluates one pair and one third value. It returns one if that value ANDed with itself three times is zero, which happens exactly when the value is zero.
- **Sixteen-bit bound:** Every pairwise AND remains within the same `0` through `2^{16}-1` universe; AND can clear bits but cannot introduce a bit absent from its operands.
