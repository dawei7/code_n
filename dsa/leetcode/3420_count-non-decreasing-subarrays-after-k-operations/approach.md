## General

**For a fixed subarray, the cheapest target is forced.** Only increments are allowed. To make `nums[left:right+1]` non-decreasing with minimum cost, keep the first value unchanged, then raise each later value only as much as necessary:

$$
\textit{target}[i]
=
\max(\textit{target}[i-1],\texttt{nums}[i]).
$$

Equivalently, each target is the maximum original value seen from `left` through that position. The required operations are

$$
\sum_{i=\textit{left}}^{\textit{right}}
(\textit{target}[i]-\texttt{nums}[i]).
$$

The source scans `left` from right to left, maintains this cost for a window `[left, right]`, and shrinks `right` until the cost is at most `k`.

**Compress equal target heights into blocks.** The deque `blocks` stores indices whose values serve as target heights for consecutive portions of the current window. It is arranged from the rightmost block at the front to the leftmost block at the back. Every block leader's original value is the prefix maximum applied across that block.

When a new `left` is inserted, its value becomes the first prefix maximum. If it is greater than the target height of one or more immediately following blocks, those blocks must all be raised to `nums[left]`. The loop

`while blocks and nums[left] > nums[blocks[-1]]`

pops such leftmost blocks from the deque's back.

Suppose a popped block begins at `index`. Its next block begins at `blocks[-1]` after the pop, or at `right + 1` if no block remains. Therefore, its length is `next_index - index`. Raising its target from `nums[index]` to `nums[left]` costs

`(next_index - index) * (nums[left] - nums[index])`

additional operations. Adding this for every absorbed block updates `cost` exactly. Finally, appending `left` makes it the leader of the merged leftmost block.

For a simple fragment `[3,1,2]`, inserting the leading $3$ absorbs the blocks of heights $1$ and $2$. The extra cost is $(3-1)+(3-2)=3$, matching the operations needed to obtain `[3,3,3]`.

**Shrink the right edge when the budget is exceeded.** After adding a left endpoint, the window may cost more than `k`. The target value currently applied at position `right` is `nums[blocks[0]]`, because the deque's front is the leader of the rightmost block. Removing that position from the window removes exactly

`nums[blocks[0]] - nums[right]`

operations from `cost`.

If `blocks[0] == right`, the removed position is itself the leader of a one-position rightmost block, so the leader is popped from the deque's front. The source then decrements `right` and repeats until `cost <= k`.

**Count every valid right endpoint at once.** Once the maintained window `[left,right]` fits the budget, every shorter subarray `[left,end]` with `end <= right` also fits: deleting a suffix removes nonnegative cost contributions. There are `right - left + 1` such endings, which the source adds to `answer`.

No ending beyond `right` can become newly valid. Whenever a position was removed, including it made the cost exceed $k$. Later iterations move `left` farther left, which can only keep or raise prefix-maximum targets for the shared suffix, never lower their cost. Thus `right` moves only left and remains the greatest feasible ending for each new `left`.

**Why the block representation remains correct.** Before insertion, blocks describe the prefix maxima for the old window. A new left value affects exactly the consecutive initial blocks whose heights are smaller; the pop loop merges and raises them. The first remaining block, if any, already has height at least the new value and all later targets stay unchanged. Right removal subtracts the exact final position's target gap and removes a block leader only when its block becomes empty. These operations preserve both the target profile and `cost`.

Together with the maximal-right argument, this proves that every counted subarray can be made non-decreasing within $k$ operations, and every omitted longer ending cannot. Each pair of endpoints is considered under exactly one `left`, so the sum is the requested count.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Every index is appended to `blocks` once. It can be removed once, either from the back when its block is absorbed or from the front when the shrinking window passes it. Although the code contains nested `while` loops, all deque removals total $O(n)$ over the full run.

The `right` pointer also decreases from $n-1$ at most $n$ times. All arithmetic and deque-end operations are $O(1)$. Total time is therefore $O(n)$.

The deque can hold up to $n$ block leaders in a non-decreasing or equal-valued arrangement, so auxiliary space is $O(n)$. The counters and pointers use constant extra space, matching the manifest.

## Alternatives and edge cases

- **Evaluate every subarray independently:** Recomputing prefix maxima for all endpoint pairs takes $O(n^3)$ naively or $O(n^2)$ with incremental costs, still too slow for $n=10^5$.
- **Balanced tree of values:** The required target depends on prefix maxima in order, not merely the multiset, so an order-free frequency structure is insufficient.
- **Monotonic block stack without a right pointer:** It can update costs for added left endpoints but cannot enforce the budget across all endings. The deque supports removals at both ends.
- **Already non-decreasing input:** Every subarray costs zero, blocks remain unmerged as appropriate, and the answer becomes $n(n+1)/2$.
- **Strictly decreasing input:** Adding a large left value may absorb many blocks at once, but amortized analysis still charges each pop to one index.
- **Equal values:** The pop condition is strict `>`, so equal-height blocks may remain separate. This is harmless: raising between equal targets costs zero, and right removal still uses the correct height.
- **Single-element subarrays:** Their cost is always zero, so each left endpoint contributes at least itself even when `k` is small.
- **Large numeric values:** Cost can exceed 32-bit range. Python integers safely hold products of block lengths and value differences.
- **Changes are independent:** The maintained cost is a hypothetical value for each endpoint pair. The source never modifies `nums`, correctly reflecting that operations on one subarray do not persist.
- **Increment-only rule:** Prefix maxima are optimal specifically because values cannot be decreased. If both increment and decrement were allowed, medians or isotonic regression variants would be relevant instead.
