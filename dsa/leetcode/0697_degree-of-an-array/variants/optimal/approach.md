## General

The degree of the full array is the largest occurrence count of any value. A subarray has the same degree only if it still contains all occurrences needed for at least one value that reaches that maximum frequency.

The key observation is that, for a fixed maximum-frequency value `v`, the shortest subarray containing all of its occurrences starts at its first occurrence and ends at its last occurrence. The solution therefore records three facts for each distinct value:

- its total count;
- its first index;
- its last index.

It then minimizes the first-to-last span among values whose count equals the array's degree.

**Computing frequencies and the degree**

`cnt = Counter(nums)` maps each value to its number of occurrences.

Because the input array is nonempty, `cnt.most_common()` returns at least one entry. Its first entry has a maximum frequency, and

`degree = cnt.most_common()[0][1]`

extracts that frequency.

Only the number is needed; it does not matter which value appears first among values tied for maximum frequency.

**Recording first and last positions**

The dictionaries `left` and `right` are populated in one left-to-right pass.

When value `v` appears at index `i`:

- if `v` is not in `left`, `left[v] = i` records its first occurrence;
- `right[v] = i` always runs, so after the pass it records the most recent and therefore final occurrence.

Never overwriting `left[v]` is essential. Always overwriting `right[v]` is equally essential. Together, they identify the narrowest interval that contains every occurrence of `v` in the full array.

**Why a degree-preserving subarray must focus on a degree value**

Let the full-array degree be `d`. No value appears more than `d` times anywhere in the array, so no subarray can have degree above `d`.

For a subarray to have degree exactly `d`, some value must occur `d` times inside it. That value also occurs at least `d` times in the full array, and because `d` is the maximum, its full count must equal `d`.

Therefore, every valid answer is associated with at least one value satisfying `cnt[v] == degree`. Values with smaller total counts can never make a subarray reach the full degree and need not be candidates.

**Why first-to-last is the shortest span for one value**

Suppose `v` occurs `degree` times. A subarray containing `degree` copies of `v` must contain all of `v`'s occurrences because there are no additional copies outside it.

It must begin at or before `left[v]` and end at or after `right[v]`. The shortest possible choice is exactly the inclusive interval from first to last, whose length is

$$
\texttt{right}[v]-\texttt{left}[v]+1.
$$

The plus one converts an index difference into an inclusive element count.

That interval certainly has degree `degree` because it contains every occurrence of `v`. It cannot have degree greater than the full array. Thus it is a valid degree-preserving subarray and the shortest one associated with `v`.

**Selecting the best degree value**

`ans` begins at infinity. The final loop scans `nums` and, for every value with maximum count, computes its span `t` and keeps the smaller one.

The loop may examine the same value several times because it iterates over the original list rather than `cnt`'s unique keys. This repetition does not change correctness: the same candidate length is merely recomputed. It remains linear in the number of input positions.

At least one value reaches the degree, so `ans` is always replaced by a finite integer before return.

**A trace**

For `nums = [1, 2, 2, 3, 1]`:

- `cnt[1] = 2` and `cnt[2] = 2`, so the degree is `2`.
- Value `1` has first index `0` and last index `4`, giving span `5`.
- Value `2` has first index `1` and last index `2`, giving span `2`.
- The minimum is `2`, corresponding to subarray `[2, 2]`.

For `[1, 2, 2, 3, 1, 4, 2]`, only value `2` reaches degree `3`. Its first and last positions are `1` and `6`, so the answer is `6`.

**Why the method is correct**

Every returned candidate is the first-to-last interval of a value occurring `degree` times, so it contains that value `degree` times and is valid.

Conversely, every degree-preserving subarray must contain `degree` copies of some full-array degree value `v`. It must cover `left[v]` through `right[v]` and therefore cannot be shorter than the candidate calculated for `v`.

Taking the minimum across all such values consequently produces a length no larger than any valid answer and itself corresponds to a valid answer. It is exactly optimal.

## Complexity detail

Let `N` be the array length and `U` the number of distinct values.

Building `cnt`, building `left` and `right`, and scanning `nums` for candidates each take `O(N)` expected time under normal hash-table assumptions.

The exact expression `cnt.most_common()` without a requested count orders all `U` Counter entries in CPython, which takes `O(U\log U)` time. Therefore, the literal implementation's bound is

$$
O(N + U\log U).
$$

Since `U <= N`, this is at most `O(N\log N)`. Replacing that line with `max(cnt.values())` would make the entire algorithm `O(N)` expected time.

The three dictionaries store information for `U` values, so auxiliary space is

$$
O(U).
$$

The list produced by `most_common()` also contains `U` entries temporarily and fits the same bound.

## Alternatives and edge cases

- **One-pass combined records:** Store `count`, `first`, and `last` together while scanning, update the degree, then inspect unique records. This achieves `O(N)` expected time without sorting Counter entries.

- **Use `max(cnt.values())`:** This is a minimal change that avoids the `O(U\log U)` full `most_common()` ordering.

- **Sliding window:** A window could search for the shortest range with degree `d`, but first/last positions give the answer more directly.

- **Single-element array:** Its degree is one, first and last indices coincide, and the answer is one.

- **All values distinct:** The degree is one. Every one-element subarray preserves it, and every candidate span is one.

- **All values equal:** The degree is `N`, and preserving all `N` occurrences requires the complete array.

- **Several degree values:** Each first-to-last span is considered; the smallest determines the answer.

- **Inclusive length:** Omitting `+1` would return zero for a single-position span and be off by one everywhere.

- **Nonnegative values:** Dictionary keys handle zero and all allowed values without special cases; the reasoning would also work for arbitrary hashable values.

- **Repeated candidate loop work:** Iterating `for v in nums` is correct but redundant. Iterating unique Counter keys would be more direct.

- **Nonempty guarantee:** It makes `most_common()[0]` safe and ensures a finite candidate exists.
