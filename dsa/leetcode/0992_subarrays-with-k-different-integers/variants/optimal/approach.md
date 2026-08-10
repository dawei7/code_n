## General

**Convert “exactly” into the difference between two “at most” conditions**

Maintaining a sliding window with at most some number of distinct values is straightforward: extend the right end, and move the left end only when too many distinct values appear. Maintaining exactly `k` distinct values is less monotonic because removing one occurrence may or may not reduce the distinct count.

The key identity is:

`count(exactly k) = count(at most k) - count(at most k - 1)`.

Every subarray with at most `k` distinct values belongs to one of two disjoint groups: it has at most `k - 1` distinct values, or it has exactly `k`. Subtracting removes the first group and leaves precisely the desired one.

The exact implementation uses this identity in a boundary form. Helper `f(limit)` does not directly return the total number of “at most” subarrays. It returns, for every right endpoint, the smallest valid left endpoint.

**Meaning of `pos[i]`**

After processing right endpoint `i`, `pos[i]` is the smallest index `j` such that the subarray `nums[j..i]` contains at most `limit` distinct integers.

Because removing values from the left cannot introduce a new distinct value, every later start `j + 1` through `i` is also valid. Thus, all valid starts for subarrays ending at `i` form the continuous range

`pos[i], pos[i] + 1, ..., i`.

The number of such starts is `i - pos[i] + 1`. Saving only the boundary is enough to derive both “at most” and “exactly” counts.

**Maintain frequencies inside the current window**

The `Counter` named `cnt` stores the occurrence count of every value in the current window `nums[j..i]`. Its number of keys, `len(cnt)`, is therefore the number of distinct values in that window.

When right pointer `i` reaches value `x`, `cnt[x] += 1` adds it. If `x` was absent, the number of distinct values increases by one; otherwise, only its frequency increases.

While `len(cnt) > limit`, the window is invalid. The algorithm decreases the frequency of `nums[j]` and increments `j`. If the frequency becomes zero, it removes that key with `cnt.pop(nums[j])`, which reduces the distinct count.

Shrinking stops at the first position where the distinct count is no greater than the limit. That first valid position is recorded in `pos[i]`.

**Why the saved boundary is minimal**

The left pointer only advances when the current window has too many distinct values. If it stops at `j`, the window beginning at `j` is valid. When `j > 0` because of shrinking for this or an earlier right endpoint, any start before the maintained boundary would retain a value whose removal was necessary to restore the distinct limit at the relevant point. The monotonic right extension never makes an invalid earlier start become valid again, because adding elements cannot reduce distinctness.

Therefore, `j` is not merely some valid start; it is the earliest valid start for this right endpoint. The pointer never moves backward, which is what makes the entire helper linear.

**Derive exactly-`k` starts from two boundaries**

Let:

- `b = f(k)[i]`, the earliest start giving at most `k` distinct values;
- `a = f(k - 1)[i]`, the earliest start giving at most `k - 1` distinct values.

The at-most-`k` starts are `b` through `i`. The at-most-`k - 1` starts are `a` through `i`. Since the stricter condition cannot allow an earlier start, `a >= b`.

Starts `b` through `a - 1` are valid for at most `k` but invalid for at most `k - 1`. Each of them therefore produces exactly `k` distinct values. Their count is `a - b`.

This explains the final expression:

`sum(a - b for a, b in zip(f(k - 1), f(k)))`.

The two lists align by right endpoint, and each difference counts exactly-`k` subarrays ending there.

**Trace `[1, 2, 1, 2, 3]` with `k = 2`**

For at most two distinct values, the earliest starts are:

`f(2) = [0, 0, 0, 0, 3]`.

The first four prefixes contain only values one and two. When three arrives at index four, the left pointer removes positions zero, one, and two before the window `[2, 3]` at indices three through four has only two distinct values.

For at most one distinct value:

`f(1) = [0, 1, 2, 3, 4]`.

At every change between one and two, the older distinct value must be removed, leaving only the current repeated run.

Subtracting aligned boundaries gives

`[0, 1, 2, 3, 1]`.

These are the numbers of exactly-two-distinct subarrays ending at indices zero through four. Their sum is seven.

**Why `f(0)` works for `k = 1`**

The input guarantees `k >= 1`, so the stricter helper may receive zero. A nonempty subarray cannot have at most zero distinct values.

After each new right value is added, the while loop removes every value through that right endpoint, leaving an empty window and `j = i + 1`. Thus `f(0)[i] = i + 1`. The formula still works: subtracting the at-most-one boundary from this empty-window boundary counts all subarrays ending at `i` that have exactly one distinct value.

No special-case branch is necessary.

**Why every desired subarray is counted once**

Every subarray has one unique right endpoint. For a fixed right endpoint, the boundary difference identifies exactly those starts whose distinct count is at most `k` but not at most `k - 1`, which is logically equivalent to exactly `k`.

The start ranges contain no duplicates, and summing across different right endpoints cannot duplicate a subarray because their endpoints differ. Conversely, any good subarray's start lies in that difference range for its endpoint, so it contributes one. The final sum is therefore exact.

## Complexity detail

Let `N` be the length of `nums`.

Within one call to `f`, right pointer `i` visits every element once. Left pointer `j` also advances at most `N` times over the entire call, not `N` times per right endpoint. Assuming average `O(1)` hash-table operations, one call takes `O(N)` time. Two calls plus the final zip-and-sum pass remain `O(N)`.

Each returned `pos` list uses `O(N)` space. Both lists exist while the final generator consumes them, and a counter can hold up to `O(N)` distinct values. Total auxiliary space is `O(N)`.

## Alternatives and edge cases

- **Return at-most totals directly:** Add `i - j + 1` in each helper and subtract the two totals. This is the more common presentation; storing boundaries exposes exactly how many valid starts each endpoint contributes.
- **One-pass exact window:** Maintain duplicate-prefix flexibility and count valid starts for exactly `k` in one traversal. It avoids two boundary arrays but has a more delicate invariant.
- **Enumerate every subarray:** Expand from every start while tracking a set. This can require `O(N^2)` time.
- **All values identical:** For `k = 1`, every subarray is good; the boundary difference correctly sums to `N(N + 1)/2`.
- **`k` exceeds total distinct values:** Both relevant boundaries yield no exactly-`k` start range, so the result is zero.
- **Repeated values at the left edge:** The pointer may remove several occurrences before a key disappears; distinct count changes only when frequency reaches zero.
- **Contiguity:** Sliding windows represent contiguous index ranges automatically; no subsequences are counted.
- **Counter cleanup:** Zero-frequency keys must be removed. Leaving them in `cnt` would make `len(cnt)` overstate distinctness.
- **Hash-map assumptions:** The linear bound uses expected constant-time counter updates. The value constraint would also permit an array of frequencies.
- **Input preservation:** The algorithm reads `nums` without modifying it.
