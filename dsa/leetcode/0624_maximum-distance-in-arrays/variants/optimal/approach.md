## General

**Use the sorted property to discard interior values.** For one sorted array, its first element is its minimum and its last element is its maximum. When pairing that array with another array, no interior value can create a wider distance than one of those endpoints. The global answer must therefore combine a minimum endpoint from one array with a maximum endpoint from a different array.

A tempting shortcut is to find the absolute global minimum and maximum across all arrays. That fails when both belong to the same array because the two chosen integers must come from different arrays. The exact solution avoids this by processing arrays in order and comparing the current array only with extrema collected from earlier arrays.

**Define the running state.** Before the loop:

- `mi` is the smallest first element among arrays already processed;
- `mx` is the largest last element among arrays already processed;
- `ans` is the greatest legal distance found between two processed arrays.

The first array initializes `mi` and `mx`. It cannot initialize a legal distance because two values from that one array are not allowed, so `ans` begins at 0.

**Compare a new array with the entire processed prefix using two numbers.** For current sorted `arr`:

- `arr[0]` is its minimum;
- `arr[-1]` is its maximum.

The widest cross-boundary distance using the current minimum is against the largest previous value, so the first candidate is

`a = abs(arr[0] - mx)`.

The widest distance using the current maximum is against the smallest previous value, so the second candidate is

`b = abs(arr[-1] - mi)`.

These candidates cover both possible orientations. The current array may lie entirely above the previous range, entirely below it, or overlap it. `abs` makes the numerical distance correct in every case.

**Why no other current-to-previous pair can do better.** Take any value `y` in the current array and any value `z` from an earlier array. All earlier values lie between `mi` and `mx`, while `y` lies between `arr[0]` and `arr[-1]`. The maximum absolute separation between these two intervals occurs at opposite endpoints. It is therefore no larger than the maximum of `abs(arr[0] - mx)` and `abs(arr[-1] - mi)`. Examining exactly those two candidates is sufficient.

The method updates `ans = max(ans, a, b)` before changing `mi` or `mx`. This ordering is the key to respecting the different-array rule. During candidate calculation, both running extrema come exclusively from earlier arrays, while both current endpoints come from the current array. If the running extrema were updated first, a current endpoint could compare with another endpoint from the same array and create an illegal candidate.

**Extend the prefix state after using it.** Once the current array has been legally compared against the prefix, it becomes part of the processed set:

- `mi = min(mi, arr[0])`;
- `mx = max(mx, arr[-1])`.

These assignments preserve the meaning of `mi` and `mx` for the next iteration.

**Trace the sample.** The first array `[1,2,3]` initializes `mi = 1` and `mx = 3`. For `[4,5]`, the candidates are `abs(4 - 3) = 1` and `abs(5 - 1) = 4`, so `ans` becomes 4. State expands to `mi = 1` and `mx = 5`. For the final `[1,2,3]`, its candidates do not exceed 4. The method returns 4, produced by 1 from the first array and 5 from the second.

**Why the complete scan is correct.** After processing any prefix, assume `ans` is the best legal distance among that prefix and `mi` and `mx` are its true extrema. When the next array arrives, every new legal pair consists of one current value and one previous value. The two endpoint candidates find the best such new pair. Taking their maximum with the old `ans` therefore finds the best pair in the enlarged prefix. Updating the extrema restores the invariant. By induction, after the final array `ans` is the global maximum legal distance.

## Complexity detail

Let $M$ be the number of arrays. Initialization is constant time, and each remaining array contributes a constant number of endpoint reads, subtractions, comparisons, and assignments. The algorithm never scans interior elements because sorted order makes endpoints sufficient. Time complexity is therefore $O(M)$, matching the manifest.

The mathematical algorithm needs only `ans`, `mi`, `mx`, and two candidate variables, so it can use $O(1)$ auxiliary space. However, the exact Python loop is `for arr in arrays[1:]`. A list slice creates a new shallow list containing $M-1$ references, which uses $O(M)$ temporary space and $O(M)$ slice-construction time. The time bound remains $O(M)$, but the literal source does not achieve the manifest's $O(1)$ extra space.

Replacing the slice with `for i in range(1, len(arrays))` or an iterator such as `islice(arrays, 1, None)` restores true $O(1)$ auxiliary space without changing the algorithm.

## Alternatives and edge cases

- **Index-based single scan:** Iterate indices 1 through $M-1$ to preserve the exact logic while avoiding the Python slice allocation.
- **Compare every array pair:** Endpoints reduce each pair to constant work, but considering all pairs still costs $O(M^2)$ and is unnecessary.
- **Compare every element:** This ignores the sorted structure and can be dramatically slower while producing no better candidate.
- **Global minimum and maximum only:** It is unsafe unless their array identities are tracked, because both extrema may come from one array.
- **Exactly two arrays:** The one loop iteration compares their opposite endpoints and returns the correct maximum.
- **Single-element arrays:** Their first and last endpoints are the same; the formulas still work.
- **All values equal:** Both candidates remain zero, so the answer is zero.
- **Negative values:** Absolute difference handles signs naturally; a negative minimum and positive maximum often create the largest result.
- **Extrema in the current array:** Candidate calculation must occur before state update so they are never illegally paired with each other.
- **Long inner arrays:** Their length does not affect scan time beyond constant endpoint access, provided indexing is constant time.
- **Nonempty-array guarantee:** It makes `arr[0]` and `arr[-1]` safe for every array.
- **At least two arrays:** It guarantees that a legal cross-array pair exists; otherwise initial `ans = 0` would not represent a chosen pair.
