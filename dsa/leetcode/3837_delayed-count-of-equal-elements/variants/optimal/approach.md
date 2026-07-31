## General

**Expose one newly eligible index at a time**

Process `i` from right to left. Maintain a frequency map for values at indices that are currently far enough to be counted. Before answering index `i`, expose position `p = i + k + 1` when it exists: this is the first position strictly beyond the forbidden delay. Add `nums[p]` to the map, then read the frequency of `nums[i]` as `ans[i]`.

When the scan begins at the last index, no later position is eligible and the map is empty. Moving from `i + 1` to `i` shifts the eligible suffix boundary left by exactly one position, so `i + k + 1` is the only new index that must be inserted. No value ever needs to be removed during the reverse scan.

Immediately after that insertion, the map contains exactly the multiset of values at indices from `i + k + 1` through `N - 1`. Its count for `nums[i]` is therefore precisely the number of indices `j` satisfying both required conditions. This statement holds at every step of the reverse scan, so every stored answer is the requested delayed count.

## Complexity detail

Each array position is visited once and inserted into the frequency map at most once. Under expected hash-table behavior, the time complexity is $O(N)$. If $U$ is the number of distinct values in the eligible suffix, the map uses $O(U)$ space; because $U\le N$, the required auxiliary-space bound is $O(N)$. The returned answer array also has length $N$.

The benchmark uses all-equal arrays with `k = 0` and defines size as $N$. Both the accepted reverse-frequency scan and an independent forward frequency-removal scan perform linear work. Recounting each eligible suffix performs quadratic work on these tiers.

## Alternatives and edge cases

- **Forward frequency removal:** Count the initial eligible suffix for index 0, answer indices from left to right, and remove the old boundary value after each answer. This is also $O(N)$ expected time but needs slightly more boundary bookkeeping.
- **Suffix slicing and recounting:** Evaluate `nums[i + k + 1:].count(nums[i])` independently for every index. It is direct and correct, but repeatedly scans overlapping suffixes and takes $O(N^2)$ time in the worst case.
- **Strict boundary:** An equal value at `j = i + k` does not count. The earliest eligible index is `i + k + 1`.
- **Zero delay:** When `k = 0`, every strictly later equal value contributes; the current index itself never does.
- **Maximum delay:** When `k = N - 1`, no index has an eligible later position, so every answer is zero.
- **Absent matches:** Distinct values or duplicates confined to the excluded gap produce zero without requiring a special case.
