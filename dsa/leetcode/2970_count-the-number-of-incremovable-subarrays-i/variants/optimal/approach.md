## General

**Describe what remains after a removal**

Removing a nonempty subarray leaves at most two pieces: a prefix ending before the removed interval and a suffix starting after it. The remaining array is strictly increasing exactly when:

1. the retained prefix is strictly increasing;
2. the retained suffix is strictly increasing; and
3. if both pieces are nonempty, the prefix’s last value is smaller than the suffix’s first value.

The implementation counts compatible prefix/suffix choices directly instead of testing every removed interval.

**Find the longest increasing prefix**

Pointer `i` begins at zero and advances while `nums[i] < nums[i + 1]`. When this scan stops, indices zero through `i` form the longest strictly increasing prefix.

If `i == n - 1`, the entire array is already strictly increasing. Removing any nonempty subarray preserves the relative order of the remaining values, so the remainder is still strictly increasing. There are $N(N+1)/2$ nonempty subarrays, and the method returns that count immediately.

Otherwise, `nums[i] >= nums[i + 1]` is the first broken adjacency. Any retained prefix must end at or before `i`; retaining both sides of that broken adjacency without removing one of them would be invalid.

**Count removals that leave no suffix**

Before scanning suffixes, the code sets `ans = i + 2`. These choices correspond to retaining a prefix ending at positions $-1,0,\ldots,i$, where endpoint $-1$ means retaining no prefix at all, and removing everything after that endpoint through the final array position.

There are `i + 2` such endpoints. Every retained prefix in this range is strictly increasing, and an empty suffix creates no cross-boundary comparison, so all these removals are valid.

**Add increasing suffixes from right to left**

Pointer `j` starts at `n - 1`, where the one-element suffix is trivially strictly increasing. For the current suffix start `j`, the code moves `i` left while `nums[i] >= nums[j]`. After this adjustment, every retained prefix endpoint $p$ from $-1$ through `i` satisfies the bridge condition `nums[p] < nums[j]` when nonempty.

Therefore, there are again `i + 2` valid prefix choices for this fixed suffix: endpoint $-1$ plus endpoints zero through `i`. Each choice uniquely determines the removed subarray between the prefix and suffix. The method adds that count.

It then checks whether the suffix can extend one position left. If `nums[j - 1] >= nums[j]`, including index `j - 1` would destroy strict increase, so no still-longer suffix beginning farther left can be used in this right-to-left extension and the loop stops. Otherwise `j` decreases and the next increasing suffix is processed.

**A concrete trace**

For `nums = [6, 5, 7, 8]`, the longest increasing prefix ends at `i = 0`. Removals that leave no suffix contribute `i + 2 = 2`. With suffix start three (value eight), prefix endpoints $-1$ and zero both bridge correctly, adding two. The suffix extends to index two (values seven, eight), again allowing two prefix endpoints. It extends to index one (values five, seven, eight); now `nums[0] = 6` is not smaller than five, so `i` moves to $-1$ and only the empty prefix choice remains. The total is seven.

**Why both pointers only move left**

As `j` moves left through a strictly increasing suffix, `nums[j]` becomes smaller. A prefix endpoint that was too large to bridge to a previous suffix start cannot become valid for this smaller first suffix value. Therefore, `i` never needs to move right again. This monotonicity makes the scan linear.

**Why every valid removal is counted exactly once**

Any removal determines a unique retained suffix start, or no suffix if the removal reaches the end. The no-suffix cases are counted in the initialization. For a nonempty suffix, validity requires that suffix to be strictly increasing, so its start appears during the `j` scan before the first suffix break. The adjusted `i` includes exactly the increasing prefix endpoints with a valid bridge. Thus the removal is counted once for its unique prefix endpoint and suffix start.

Conversely, every counted pair consists of an increasing prefix, an increasing suffix, and a valid cross-boundary comparison, so concatenating them is strictly increasing. The removed middle is nonempty because the chosen prefix endpoint lies before `j` under the maintained scan structure.

## Complexity detail

Let $N$ be the array length. The initial prefix scan moves `i` right at most $N-1$ times. During suffix processing, `j` moves left at most $N-1$ times, while `i` moves left at most the distance it previously moved right and never reverses. The total time is $O(N)$.

The algorithm stores only pointers, the length, and the answer, so auxiliary space is $O(1)$. It never modifies `nums`. Although this is the smaller-constraint version of the problem, the exact implementation already uses the optimal linear two-pointer method.

## Alternatives and edge cases

- **Enumerate every removed subarray:** There are $O(N^2)$ candidates, and checking each remainder directly can make the method $O(N^3)$. Even optimized prefix checks still lose the linear pointer reuse.
- **Binary search bridges:** With precomputed increasing prefix/suffix ranges, each suffix could binary-search a compatible prefix in $O(\log N)$, but monotone `i` yields $O(N)$ total time.
- **Already strictly increasing:** Every nonempty subarray is incremovable, producing $N(N+1)/2$.
- **Strict versus non-decreasing:** Equality is invalid. Both scans and the bridge use strict `<`, while `>=` triggers rejection.
- **Removing the whole array:** The remainder is empty and is considered strictly increasing; it is included through the empty-prefix, empty-suffix choice.
- **Leaving one element:** A one-element remainder is strictly increasing and is counted naturally.
- **No retained prefix:** Endpoint $-1$ explains the extra one in `i + 2`.
- **No retained suffix:** Those cases are counted once in the initial `ans = i + 2` and not duplicated in the suffix loop.
- **Input preservation:** Pointer movement only reads `nums` and leaves it unchanged.
