## General

**Compress each ordering check into a run length.** For every position $j$, record the length of the non-increasing run ending at $j$. Scan left to right: extend the previous length when `nums[j - 1] >= nums[j]`, otherwise reset it to 1. Then scan right to left to record the length of the non-decreasing run starting at each $j$, extending when `nums[j] <= nums[j + 1]`.

**Read both requirements at the boundaries.** For a candidate $i$, the block immediately before it ends at `i - 1`, so it is valid exactly when that ending run has length at least `k`. The following block starts at `i + 1`, so it is valid exactly when that starting run has length at least `k`.

Inspect candidates from `k` through `n - k - 1` in order and append those satisfying both comparisons. The run lengths summarize every adjacent relation inside each required block, making each candidate decision constant-time and producing naturally increasing output.

## Complexity detail

The two run-length passes and candidate scan each take $O(n)$ time. Two arrays of length $n$ store the summaries, so the auxiliary space is $O(n)$; the returned indices may also occupy $O(n)$ space.

## Alternatives and edge cases

- **Check both windows per index:** Directly scanning `2k` neighbors for every candidate is correct but costs $O(nk)$ time.
- **Monotonic violation prefix sums:** Prefix counts of increasing and decreasing violations can answer each window in $O(1)$ with the same $O(n)$ total complexity.
- **`k = 1`:** Every one-element block is both non-increasing and non-decreasing, so every interior index is good.
- **Equal values:** Equality satisfies both ordering definitions.
- **No candidate range:** When `n = 2k`, the allowed interval is empty.
- **Excluded center:** Comparisons must not connect the preceding block through `nums[i]` or `nums[i]` into the following block.
