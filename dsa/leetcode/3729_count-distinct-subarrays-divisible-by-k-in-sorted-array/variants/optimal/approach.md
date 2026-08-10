## General

**First count all good occurrences**

Let the running prefix remainder after an index be `s`. A subarray sum is divisible by `k` when the prefix sums at its two boundaries have the same remainder modulo `k`. The dictionary `cnt` stores how many earlier boundaries have each remainder.

It begins with `{0: 1}` for the empty prefix. For each value `x`, the source updates

`s = (s + x) % k`.

Every earlier boundary with the same remainder creates one good subarray ending here, so `ans += cnt[s]`. The new prefix boundary is then recorded with `cnt[s] += 1`.

This standard prefix-remainder scan counts occurrences by indices. The problem, however, asks for distinct value sequences. The second phase removes repeated occurrences that represent the same sequence.

**Why duplicates can only be constant sequences**

The sorted, non-descending property is crucial. Suppose two subarrays at different starts have the same value sequence. If that sequence contained two different values, it would have an increase somewhere. Repeating the same increasing pattern later would require the sorted array to return to the pattern's smaller starting value after already reaching its larger value, which is impossible.

Equivalently, shifting an equal sequence within a non-descending array forces all values across the spanned overlap or gap to be equal. Thus the only value sequences that can occur more than once are constant sequences such as `[2,2,2]` lying within one run of equal values.

Every non-constant good subarray occurrence is already distinct and must remain in `ans`.

**Correct the overcount inside each equal-value run**

The two-pointer loop finds each maximal run `nums[i:j]` of one value `v = nums[i]`. Let its length be `m = j-i`.

For any length `h` from one through `m`, the constant sequence of `h` copies of `v` has sum `h*v`. It is good exactly when

`(h * v) % k == 0`.

Within a run of length `m`, that same sequence occurs at `m-h+1` different starting positions. The prefix phase counted all of them, but distinct-sequence counting should retain only one. The number of excess occurrences is therefore

$$
(m-h+1)-1=m-h.
$$

Whenever the divisibility condition holds, the code subtracts exactly `m-h`.

For six copies of two and `k=6`, lengths three and six are divisible. Length three occurs four times, so the correction subtracts three and leaves one. Length six occurs once, so it subtracts zero. The two distinct good sequences remain.

Runs are maximal and values differ between runs, so constant sequences from different runs cannot be identical. Processing each run independently removes every duplicate exactly once.

**Why the corrected answer is exact**

The first phase includes every good subarray occurrence using the exact prefix-remainder criterion. Partition those occurrences by their value sequence. Every non-constant class has size one because the array is sorted. A constant class of length `h` in a run of length `m` has size `m-h+1`, and the second phase subtracts `m-h` precisely when that class is good. Every class is therefore reduced to one representative, which is exactly the number of distinct good sequences.

## Complexity detail

Let `n` be the length. The prefix scan takes expected $O(n)$ time. The run scan advances `i` and `j` only forward. Its inner `h` loops perform a total of

$$
\sum_{\text{runs}}m=n
$$

iterations, so correction also takes $O(n)$ time. Total expected time is $O(n)$.

The remainder counter can hold up to `n+1` keys, requiring $O(n)$ space. Run processing uses constant extra state, so auxiliary space is $O(n)$. Dictionary access gives the expected-time qualification.

## Alternatives and edge cases

- **Insert every good subarray tuple into a set:** This is direct but constructing $O(n^2)$ sequences and hashing their contents can require cubic character/value work and quadratic storage.
- **Return the prefix-remainder count:** That counts index occurrences, not distinct sequences. Equal runs demonstrate the required correction.
- **Deduplicate all subarrays with rolling hashes:** Hashing can identify repeated sequences, but it is much more complex. Sorted order proves only constant sequences can repeat.
- **Apply the run correction to non-sorted input:** It would be invalid because non-constant patterns can repeat in an arbitrary array. The method relies essentially on non-descending order.
- **Run length one:** For `m=1`, a good length-one sequence subtracts `m-h=0`, correctly keeping its single occurrence.
- **All values equal:** Every distinct subarray is determined solely by its length. The correction reduces each divisible length to one count.
- **`k=1`:** Every occurrence is initially good. The run correction leaves exactly one per distinct sorted subarray sequence.
- **Repeated values in separate runs:** A sorted array cannot have separate maximal runs of the same value; once it increases, it never returns.
- **Large values and `k`:** Updating modulo at every step avoids unbounded prefix sums while preserving divisibility equivalence.
- **Empty prefix seed:** `cnt[0]=1` is required to count a good subarray beginning at index zero.
- **Correction never makes the answer negative:** Every subtraction removes occurrences known to have been included by the first phase.
