## General

**The nearest occurrence must be on one of two sides**

For any index `i`, the closest occurrence of `c` is either the nearest occurrence at or before `i`, or the nearest occurrence at or after `i`. No other occurrence can be better: an earlier occurrence farther left is more distant than the nearest left one, and a later occurrence farther right is more distant than the nearest right one.

The solution computes these two directional distances with two linear scans and stores their minimum.

**Prepare a safe initial upper bound**

Let `n = len(s)`. The answer list begins as `ans = [n] * n`.

The largest possible distance between two valid indices is `n - 1`, so `n` is larger than every real answer. It works as a finite placeholder until a scan discovers an occurrence of `c`. Using a finite placeholder also ensures the final list contains ordinary integers after both passes.

The Reference guarantees that `c` occurs at least once, so every placeholder will eventually be replaced by a genuine distance.

**Left-to-right pass**

Variable `pre` stores the index of the most recent occurrence of `c` at or before the current position. It begins at negative infinity because no left occurrence has been seen.

At index `i`:

- if `s[i] == c`, set `pre = i`;
- update `ans[i]` with `min(ans[i], i - pre)`.

When the current character is `c`, the distance becomes `i - i = 0`. Otherwise, `pre` remains the closest occurrence on the left. It is the closest because the scan replaces it every time a newer, larger occurrence index is found.

Before the first `c`, `i - (-inf)` is positive infinity. Taking the minimum with the placeholder `n` leaves `ans[i] = n`. Those positions do not yet have a left-side candidate and will be corrected by the right-to-left pass.

After this pass, every position at or after the first occurrence holds its exact nearest-left distance.

**Right-to-left pass**

Variable `suf` stores the nearest occurrence of `c` at or after the current index. It begins at positive infinity because no right occurrence has been seen from the scan's perspective.

The loop visits indices from `n - 1` down to 0:

- if `s[i] == c`, set `suf = i`;
- replace `ans[i]` with `min(ans[i], suf - i)`.

As the scan moves left, the most recently encountered `c` has the smallest index at least `i` and is therefore the nearest occurrence on the right. At a target character, `suf - i` is zero.

The minimum combines the nearest-left distance already stored with the nearest-right distance just computed. It handles ties naturally: if both distances are equal, their common value remains.

**Trace on a small string**

For `s = "aaab"` and `c = "b"`, `n = 4`. The forward pass has no left occurrence until index 3, so it leaves `[4,4,4,0]`. The backward pass starts with `suf = 3` and computes right distances 0, 1, 2, and 3, producing `[3,2,1,0]`.

For adjacent occurrences, each occurrence resets both directional distances to zero. Positions between two occurrences receive the smaller distance to either endpoint.

**Why two passes are sufficient**

Fix an index `i`. After the first pass, `ans[i]` is the distance to the greatest occurrence index not exceeding `i`, if one exists. After the second pass, the other candidate is the distance to the smallest occurrence index not less than `i`, if one exists.

Every occurrence lies in one of those two directions. Within a direction, the remembered occurrence is closest by index order. Therefore, the minimum is the distance to the closest occurrence anywhere in the string.

No binary search or per-index outward expansion is needed because the scans propagate exactly the useful nearest occurrence information.

## Complexity detail

Let `n = len(s)`. Initializing `ans` takes `O(n)` time. Each of the two scans visits every character once and performs constant work, so total time is `O(n)`.

The returned answer array contains `n` integers and therefore uses `O(n)` space, matching the manifest. Beyond the required output, the algorithm uses only `n`, `pre`, `suf`, the loop variables, and the current character, so auxiliary working space excluding the output is `O(1)`.

Infinity values are temporary sentinels. Arithmetic with them remains infinite, and `min` keeps the finite placeholder or real distance as intended.

## Alternatives and edge cases

- **Collect occurrence indices and binary-search each position:** This works in `O(n\log m)` time for `m` occurrences. Two directional scans are simpler and linear.

- **Expand outward from every index:** Searching left and right independently for each position can take `O(n^2)` on long gaps.

- **Multi-source BFS on indices:** Starting from every `c` and spreading distances left and right also gives `O(n)` time, but the two-pass method needs no queue.

- **Current index contains `c`:** Both passes can produce zero, and zero is necessarily the minimum distance.

- **Only one occurrence:** Positions on both sides receive their absolute distance to that one index.

- **Occurrence only near the end:** Forward placeholders before it remain `n` until the backward scan supplies finite distances.

- **Occurrence only near the beginning:** The forward scan supplies all later distances; the backward scan cannot make them worse because it takes a minimum.

- **Several consecutive occurrences:** Every such position is zero, and distances grow outward from the block.

- **Tie between left and right:** Either occurrence is equally close, and the numeric answer is their shared distance.

- **Length-one string:** The guaranteed occurrence is at index zero, so the result is `[0]`.

- **Input immutability:** The scans read `s` and write only the new answer list.
