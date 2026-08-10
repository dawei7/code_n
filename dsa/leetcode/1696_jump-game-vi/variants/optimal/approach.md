## General

**Turn every destination into a best-score state**

Let `f[i]` mean the greatest score obtainable by starting at index zero and ending at index `i`. This state is useful because the final answer is exactly `f[n - 1]`, and every legal way to reach a later index must come from an already solved earlier index.

To land on `i`, the previous position must be one of the indices from `i - k` through `i - 1`, clipped to the beginning of the array. If the path comes from index `j`, its new score is `f[j] + nums[i]`. Therefore the recurrence is

$$
f[i] = \texttt{nums}[i] + \max_{\,\max(0,i-k)\le j<i} f[j].
$$

Checking all of those predecessors separately would take up to `k` work per index. With both the array length and `k` as large as $10^5$, that $O(nk)$ method is too slow. The exact solution instead maintains the maximum of this moving predecessor window with a monotonic deque.

**What the deque stores**

The deque `q` stores indices, not scores. Their indices increase from front to back because each current index is appended after all earlier ones. More importantly, their corresponding DP scores decrease strictly from front to back after maintenance. Thus `q[0]` always identifies the largest surviving score and is the best predecessor for the current destination.

An index can be omitted when a later index has an equal or greater score. Suppose `a < b` and `f[a] <= f[b]`. For every future destination at which `a` is still within jump range, `b` is also within range because it is newer. Choosing `b` gives at least as much accumulated score. The older `a` can never become the uniquely best choice, so retaining it provides no benefit.

**The first iteration establishes the base case**

The implementation initializes `f` with zeros and `q` with index zero, then starts its loop at `i = 0` rather than handling the base case separately. On that iteration, `q[0]` is zero and the still-unwritten `f[0]` is zero, so

`f[0] = nums[0] + f[0]`

sets `f[0]` to `nums[0]`. This works because the zero came from array initialization, not from a real jump from index zero to itself. The following monotonic-maintenance loop removes the existing zero index since its score is equal to the newly computed score, and the final append restores index zero to the deque. After this special first pass, all later iterations use ordinary earlier predecessors.

**Discard a predecessor as soon as its jump is too long**

Before computing `f[i]`, the source checks `i - q[0] > k`. If true, the front index cannot reach `i` and is removed. A single `if` is sufficient here even though many monotonic-deque implementations use `while`. At the end of the preceding iteration, the front was valid for index `i - 1`. Since `i` advances by exactly one, at most that one front index can newly cross the distance boundary. Any indices behind it are newer and therefore cannot already be too old.

After expiration, the deque cannot be empty for a normal iteration: index `i - 1` was appended on the previous pass and `k >= 1`, so that index can always jump to `i`.

**Compute the best score, then remove dominated candidates**

With stale indices gone, `q[0]` has the maximum `f` value among all legal predecessors. The assignment

`f[i] = nums[i] + f[q[0]]`

therefore realizes the DP recurrence exactly. Negative values in `nums` cause no problem: `f` stores the best total, which may itself be negative, and the deque compares totals rather than assuming scores are nonnegative.

Next, the source removes indices from the back while `f[q[-1]] <= f[i]`. Each removed state is dominated by the current index: it has no larger score and will expire earlier. Using `<=` rather than only `<` deliberately discards an older equal-score state in favor of the newer one. Finally, appending `i` restores increasing index order and strictly decreasing score order.

**Why the returned value is optimal**

The base pass gives the only possible score at index zero. Assume all states before `i` are correct. The deque has removed only expired indices or indices dominated by a newer, no-worse state, so its front still represents the greatest DP score among every legal predecessor of `i`. Adding `nums[i]` computes the best score of every path ending at `i`. By induction, every `f[i]` is correct, including the returned `f[-1]`.

For a short trace, consider `nums = [1, -1, -2, 4]` and `k = 2`. The scores become `1`, `0`, `-1`, and `4`. At the last index, the legal predecessors have scores zero and negative one, so the deque exposes the zero and the new total is `0 + 4 = 4`. The method optimizes accumulated score, not merely the value at the preceding array position.

## Complexity detail

Let $n$ be the length of `nums`. Each index is appended to the deque once. It can be removed once from the back when dominated or once from the front when expired, but never repeatedly. Although the source contains a nested `while`, all its iterations across the complete run total $O(n)$. Computing the DP states therefore takes $O(n)$ time.

The array `f` contains $n$ scores, so it uses $O(n)$ space. The deque holds only indices from a window of at most `k + 1` relevant positions and uses $O(k)$ space. Because $k \le n$, total auxiliary space is $O(n)$, matching the Optimal manifest. The returned output is one integer.

Python's deque operations at either end are constant-time. Integer totals can reach approximately $n\cdot 10^4$ in magnitude, but Python integers handle that range without overflow.

## Alternatives and edge cases

- **Direct dynamic programming:** Scan all up to `k` predecessors for each destination. It follows the same recurrence but costs $O(nk)$ time and is impractical at the maximum constraints.
- **Maximum heap:** Keep score-index pairs in a heap and lazily remove expired maximums. It is easier for some readers but costs $O(n\log n)$ time and can retain stale entries.
- **Segment tree:** Range-maximum queries and point updates also implement the recurrence, but take $O(n\log n)$ time and substantially more machinery.
- **Compressed deque state:** Store pairs of index and score directly in the deque and keep only the latest scalar score. That can reduce space from $O(n)$ to $O(k)$; the exact source intentionally retains the full `f` array.
- **One element:** The first self-initializing iteration sets `f[0] = nums[0]` and that value is immediately returned.
- **`k = 1`:** Every move must go to the next index, so the answer is the sum of every element; the deque still applies without special handling.
- **`k >= n - 1`:** Any earlier position can reach far enough until it becomes dominated; the same window logic remains valid.
- **All negative values:** The algorithm chooses the least harmful legal accumulated score at each step. Initial zeros outside established states never enter later comparisons.
- **Equal DP scores:** Removing the older equal state is safe because the newer index remains usable for at least as long.
- **Single expiration check:** It is correct only because indices are processed consecutively and the deque was valid on the prior iteration; changing the traversal pattern would require re-evaluating that assumption.
