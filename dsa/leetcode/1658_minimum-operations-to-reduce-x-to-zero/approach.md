## General

**Look at what remains instead of what is removed**

Every operation removes an element from one of the two ends. After any sequence of such operations, the elements not removed must form one contiguous subarray of the original array. The removed elements consist of some prefix, some suffix, or both. There is no way to leave two separated middle pieces because reaching an interior element from an end necessarily removes everything before it.

Let

$$
T = \sum \texttt{nums}
$$

be the sum of all elements. Reducing `x` to exactly zero means the removed elements must sum to `x`. Therefore the elements that remain must sum to

$$
s = T - x.
$$

This is the value computed by `s = sum(nums) - x`.

If a remaining subarray has length `L` and the whole array has length `n`, then exactly `n - L` elements were removed. Minimizing operations is consequently equivalent to maximizing the length of a contiguous subarray whose sum is `s`. Once the longest such subarray is known, the answer is `n - L`.

This transformation handles all valid removal shapes uniformly. Removing only from the right leaves a prefix, removing only from the left leaves a suffix, removing from both ends leaves an interior interval, and removing everything leaves the empty interval.

**Use prefix sums to recognize every target-sum interval**

Define the prefix sum at index `i` as the sum from `nums[0]` through `nums[i]`. The running variable `t` stores this value during the scan. Suppose an earlier prefix ending at index `j` had sum `p`. Then the subarray from `j + 1` through `i` has sum

$$
t - p.
$$

For that subarray to sum to `s`, the earlier prefix must have value `t - s`. Thus, at every right endpoint `i`, the algorithm asks whether prefix sum `t - s` has been seen.

The dictionary `vis` maps a prefix-sum value to an index where it occurred. It begins as `{0: -1}`. The imaginary prefix ending at index `-1` contains no elements and has sum zero. This sentinel makes subarrays beginning at index zero use the same formula as every other subarray: if the current prefix itself sums to `s`, then `t - s = 0` and its length is `i - (-1) = i + 1`.

**Why the earliest index is stored**

When a prefix sum `t` is first encountered, the code records `vis[t] = i`. It does so only when `t not in vis`, preserving the earliest occurrence. For a fixed right endpoint `i` and required earlier sum `t - s`, the subarray length is `i - vis[t - s]`. A smaller earlier index produces a longer interval, so retaining the first occurrence is exactly what the maximum-length objective needs.

Under this problem’s positive-element constraint, prefix sums are strictly increasing and therefore never repeat. The “store only once” guard is still a sound and useful expression of the general prefix-sum principle.

After updating the running sum, the source stores its first index and then checks `t - s`. For a positive target `s`, the required earlier prefix is smaller than `t` and, if it exists, was encountered in an earlier iteration. When `s == 0`, the just-stored current prefix allows a zero-length interval, which is the correct remaining interval when all elements must be removed. Because every array value is positive, no nonempty interval can have sum zero, so length zero is the true maximum in that case.

**Track the longest feasible middle**

`mx` starts at `-1`, a sentinel meaning that no subarray with sum `s` has been found. Whenever `t - s` exists in `vis`, the candidate interval length is `i - vis[t - s]`. The assignment

`mx = max(mx, i - vis[t - s])`

keeps the longest candidate across all right endpoints.

For `nums = [1, 1, 4, 2, 3]` and `x = 5`, the total is `11`, so `s = 6`. The scan finds the middle prefix `[1, 1, 4]` with sum six and length three. Keeping those three elements means removing the final two, so the result is `5 - 3 = 2`.

For an interior example, if a target-sum remaining interval starts after index `j`, the dictionary supplies that earlier boundary directly. The algorithm never needs to separately enumerate how many removals came from the left and right; the interval’s endpoints imply both counts.

**Why the answer is correct**

Every legal removal sequence leaves a contiguous interval whose sum is `T - x = s`, and its number of operations is the array length minus that interval’s length. Conversely, every contiguous interval with sum `s` defines a legal sequence: remove all elements before it from the left and all elements after it from the right. Those removed elements sum to `T - s = x`.

The prefix-sum identity finds every interval with sum `s` because, when its right endpoint is scanned, the prefix immediately before its left endpoint has value `t - s`. Keeping the earliest occurrence yields the longest interval for that right endpoint, and taking `max` across endpoints yields the global longest interval. Therefore `len(nums) - mx` is the minimum possible number of removals.

If `mx` remains `-1`, no such remaining interval exists, so no end-removal sequence can sum exactly to `x` and the source returns `-1`.

## Complexity detail

Let `n` be the length of `nums`. Computing `sum(nums)` takes $O(n)$ time. The following loop visits each element once. Each dictionary lookup and insertion takes expected $O(1)$ time, so the scan takes expected $O(n)$ time and the full method takes expected $O(n)$ time.

The dictionary may contain the sentinel plus one distinct prefix sum for every array position. Because all elements are positive, those prefix sums are indeed distinct. The exact implementation therefore uses $O(n)$ auxiliary space.

The package manifest states $O(1)$ space, which describes the positive-array sliding-window solution from the editorial, not this exact hash-map source. A two-pointer window can exploit positivity to avoid the dictionary, but the implementation documented here explicitly stores prefix sums and consequently has linear space usage.

## Alternatives and edge cases

- **Positive-number sliding window:** Search for the longest interval summing to `T - x`, expanding right and shrinking left whenever the sum is too large. Positivity makes the window sum monotonic, giving $O(n)$ time and $O(1)$ space; this matches the manifest but differs from the exact source.
- **Direct two-ended two pointers:** Start with a removal sum from one side and trade left removals for right removals while tracking the minimum operation count. It can also be linear for positive values, but the remaining-subarray formulation is usually easier to prove.
- **Try every prefix and suffix pair:** This directly models the operations but takes $O(n^2)$ combinations without additional structure.
- **`x == T`:** Then `s == 0`. The empty remaining interval has length zero, so all `n` elements must be removed; the source finds this through the current-prefix lookup.
- **`x > T`:** Then `s < 0`. A positive array has no negative-sum subarray, so no prefix difference matches and the result is `-1`.
- **`x < T` but no matching interval:** The existence of a positive target sum alone is insufficient. If no contiguous interval sums to `s`, no legal combination of end removals reaches exactly `x`.
- **Keep the entire array:** This would require `s == T`, equivalent to `x == 0`. The stated constraints have `x >= 1`, but the prefix sentinel would support that generalized case.
- **Remaining prefix or suffix:** The sentinel handles a prefix beginning at zero, and an ordinary stored prefix handles a suffix ending at the last index.
- **Several intervals with the same sum:** Only the longest matters because it leaves the fewest elements to remove. Preserving earliest prefix indices and maximizing `mx` enforce that objective.
- **Positive-elements dependency:** The prefix-map identity itself also works with negative values, but the exact placement of the `s == 0` current-prefix insertion and the space discussion here rely on the stated positive input. The constant-space sliding-window alternative would fail with arbitrary negative values.
