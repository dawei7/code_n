## General

The exact implementation tests every candidate index `i` against array positions `j` until it finds one that both contains `key` and lies within distance `k`.

If such a witness exists, `i` is appended. Candidate indices are processed from zero upward, so the answer is automatically sorted.

This is the enumeration approach from the editorial, not the linear interval-emission strategy described by the Optimal manifest.

**Choose each candidate output index**

The outer loop visits `i` from zero through `n - 1`. Each index is considered once as a possible k-distant index.

The decision for one `i` is an existence question: does at least one valid `j` exist? The method does not need to count how many key positions are nearby.

**Search all possible witness positions lazily**

The generator iterates `j` over the complete array. For each position it evaluates

`abs(i - j) <= k and nums[j] == key`.

The absolute difference handles witnesses on either side of `i`. Equality at distance exactly `k` is accepted because the contract uses `<=`.

The expression checks distance first. If it is too large, Python short-circuits `and` and does not read the value comparison for logical purposes, though index generation still continues.

**Use `any` to stop at the first witness**

`any(...)` returns true as soon as one generated predicate is true. It does not examine later `j` values after a witness has been found.

If every position fails, it consumes the entire generator and returns false.

This matches the existential definition exactly. One witness is sufficient, and several witnesses must still cause only one output occurrence.

**Append each qualifying index once**

The append occurs outside the inner generator and at most once per outer `i`. Therefore overlapping neighborhoods of several key positions cannot create duplicate indices.

For example, an index within distance of keys at both positions two and five still receives one true result from `any` and one append.

**Why output order needs no sort**

The outer loop is increasing. Every appended value is the current `i`, so later appends are always larger.

The returned list is strictly increasing and hence meets the sorted-order requirement without additional work.

**Why the result is exact**

If the algorithm appends `i`, `any` found a position `j` satisfying both `nums[j] == key` and `abs(i-j) <= k`. This is precisely a valid witness, so every output index is k-distant.

Conversely, if `i` is k-distant, at least one witness position exists. The generator enumerates every `j`, reaches that witness unless an earlier valid witness already stopped it, and makes `any` true. Thus every required index is appended.

Each candidate is considered once, so the result contains all and only k-distant indices without duplicates.

For `nums = [3,4,9,1,3,9,5]`, key positions two and five witness indices one through six within distance one, while index zero finds no qualifying `j`.

**Contrast with interval union**

Every key at position `j` covers clipped interval

$$
[\max(0,j-k),\min(n-1,j+k)].
$$

A linear method can merge or emit these intervals without rechecking all pairs. The exact source does not do that; it restarts a witness search for every `i`.

## Complexity detail

There are $n$ outer candidates. In the worst case, `any` examines $O(n)$ positions for each one—for example, when the only key lies near the end and no early witness is found for many candidates. Worst-case time is $O(n^2)$.

The generator and `any` use $O(1)$ auxiliary state. The returned list can contain all $n$ indices and uses $O(n)$ output space.

The manifest's $O(n)$ time describes interval emission, not this all-pairs source. Its $O(n)$ space includes the output; exact working space excluding output is constant.

## Alternatives and edge cases

- **Emit uncovered interval suffixes:** Scan key positions left to right and append only indices beyond the last emitted endpoint. This achieves the manifest's $O(n)$ time.
- **Boolean difference array:** Mark the start and end of every key neighborhood, prefix-sum coverage, and emit covered indices in $O(n)$ time and space.
- **Precollect key positions:** Binary search the nearest key for each `i` in $O(n\log q)$ time, where $q$ is the number of key occurrences.
- **Candidate equals key position:** Distance zero is within every positive `k`, so all key positions qualify.
- **Overlapping neighborhoods:** `any` and one outer append prevent duplicates.
- **Key guaranteed present:** At least one neighborhood exists.
- **`k >= n - 1`:** Every index is within range of every key position, so all indices are returned.
- **Key at an endpoint:** Absolute distance and complete `j` enumeration handle one-sided neighborhoods.
- **Exact boundary distance:** `<= k` includes it.
- **First witness:** `any` short-circuits and avoids unnecessary later checks for that candidate.
- **No witness:** The complete inner range is consumed and `i` is skipped.
- **Sorted output:** Increasing outer iteration supplies the order directly.
- **Input preservation:** The array, key, and distance are only read.
- **Manifest discrepancy:** The stored code is quadratic enumeration rather than linear interval merging.
