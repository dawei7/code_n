## General

For each position, the solution counts how many earlier prefix sums would make a subarray ending here sum to `k`.

Let the running prefix sum `s` after reading the current element equal the sum from the array start through that element. If an earlier prefix sum was `p`, then the elements after that earlier prefix through the current position have sum:

$$
s-p.
$$

This equals `k` exactly when:

$$
p=s-k.
$$

Therefore the algorithm needs to know how many earlier prefixes had value `s - k`.

**Store frequencies, not only existence.** Counter `cnt` maps each prefix-sum value to the number of times it has occurred.

Different earlier positions can have the same prefix sum, especially when zero-sum sections or negative values exist. Each position defines a different subarray start and must contribute separately. A set would lose this multiplicity; a Counter preserves it.

**Initialize the empty prefix.** `cnt = Counter({0: 1})` records one prefix before the array begins, with sum zero.

This allows a qualifying subarray starting at index zero. If the running sum itself equals `k`, then `s - k = 0`, and the empty prefix contributes one start.

**Process one endpoint at a time.** For each value `x`:

1. `s += x` extends the current prefix through this element.
2. `ans += cnt[s - k]` counts all earlier prefix positions that produce sum `k` to the current endpoint.
3. `cnt[s] += 1` records the current prefix for future endpoints.

The lookup happens before recording the current prefix. This ensures the selected subarray is nonempty. If `k = 0` and the current prefix were inserted first, it could pair with itself and incorrectly count an empty subarray.

For `nums = [1,1,1]` and `k = 2`:

- after the first one, `s = 1` and no prefix `-1` exists;
- after the second, `s = 2` and the empty prefix zero contributes subarray indices zero through one;
- after the third, `s = 3` and earlier prefix one contributes indices one through two.

The result is two.

For `[1,2,3]` and `k = 3`, running sum three finds the empty prefix, representing `[1,2]`. Running sum six finds earlier prefix three, representing `[3]`. Both are nonempty and distinct.

**Why negative values cause no problem.** Sliding-window methods rely on sums changing monotonically as boundaries move, which fails with negatives. Prefix equality uses exact arithmetic and hash lookup, so the running sum may increase, decrease, or repeat freely.

**Why every counted subarray is valid.** Every unit added to `ans` corresponds to an earlier prefix occurrence with value `s-k`. Subtracting it from current `s` gives exactly `k`, and earlier recording order makes the interval nonempty and contiguous.

**Why every valid subarray is counted.** A valid subarray ending at the current position has some boundary immediately before its start. The prefix at that boundary equals current `s-k`. It was already inserted into `cnt`, so its occurrence contributes during this endpoint's lookup.

If several valid subarrays share one endpoint, their boundary prefixes are counted through the frequency. If the same numeric prefix arose at several indices, each gives a distinct start.

The answer counts subarrays, not unique value sequences. Two equal-looking subarrays at different indices count separately, exactly as the prefix occurrences do.

The input is scanned once and not modified.

At the start of each iteration, `cnt` contains exactly the prefix sums ending strictly before the current element, including the synthetic empty prefix. After the lookup, inserting `s` restores this invariant for the next iteration. This precise timing explains both completeness and the nonempty requirement without needing explicit start indices.

For a trace with repetition, `nums = [0, 0]` and `k = 0` starts with one zero prefix. The first running zero finds one prior zero and contributes one subarray. It then raises the zero frequency to two. The second running zero finds both earlier boundaries and contributes two more subarrays, for the three valid intervals `[0]`, the other `[0]`, and `[0,0]`.

## Complexity detail

Let $n$ be the array length. Each element performs constant arithmetic and expected-$O(1)$ Counter lookup/insertion, so expected time is $O(n)$.

There can be $O(n)$ distinct prefix sums, so `cnt` uses $O(n)$ space, matching the manifest. The answer and running sum use constant extra storage.

Python integers safely represent prefix sums across the stated ranges. Hash-table complexity uses the standard expected-time model.

The answer itself can be quadratic in $n$ even though it is computed in linear time—for example, many zeroes with `k = 0`. Counting does not require enumerating those subarrays individually because one frequency lookup adds all starts sharing the needed prefix.

## Alternatives and edge cases

- **Enumerate every subarray:** Maintaining a running sum per start still takes $O(n^2)$ time.
- **Prefix array plus nested endpoints:** Sum queries become constant time, but there remain quadratic pairs.
- **Sliding window:** It is not correct when values may be negative.
- **Use a set:** It undercounts when the same prefix sum occurs at several indices.
- **Omit the empty prefix:** Subarrays starting at index zero would be missed.
- **Insert before querying:** For `k = 0`, it falsely counts an empty subarray.
- **Single element equal to `k`:** The empty prefix makes it count once.
- **Zero values:** Repeated prefix sums correctly create multiple start positions.
- **Negative `k`:** The same equation `p=s-k` applies.
- **No qualifying subarray:** Every lookup contributes zero and the result remains zero.
- **Repeated value patterns:** Index-distinct subarrays are counted separately.
