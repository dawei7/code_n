## General

**Separate the problem into window costs and non-overlapping selection.** For every length-$x$ window, first compute the minimum operations needed to make all its elements equal. Then choose exactly $k$ of these windows without overlap so their total cost is minimum.

This works because selected windows are disjoint. Operations applied inside one selected window do not affect another, so their optimal costs add.

**The best target for one window is a median.** Changing value $a$ to target $v$ costs $\lvert a-v\rvert$. The sum of absolute deviations

$$
\sum\lvert a_i-v\rvert
$$

is minimized by any median of the window values. The source uses the lower median rank `(x + 1) // 2` under one-based order statistics. For even $x$, any value between the two middle values is optimal, so choosing the lower one remains correct.

The challenge is obtaining each sliding window's median and deviation sum efficiently.

**Coordinate-compress all values.** `values = sorted(set(nums))` lists distinct values in increasing order. Each input value is replaced by its index in this list through `bisect_left`.

Compression preserves order, which is all the median data structure needs, while letting Fenwick trees use compact indices even though values range from $-10^6$ to $10^6$.

**Maintain counts and sums in two Fenwick trees.** `count_tree` stores how many current-window values occupy each compressed coordinate. `sum_tree` stores their numeric sum.

As right endpoint advances, the source adds the new value to both trees. Once more than $x$ values would remain, it subtracts the value at `right - x`. Thus, whenever `right >= x - 1`, both trees represent exactly window `[right-x+1,right]`.

Fenwick `add` updates all tree nodes covering one coordinate in $O(\log n)$. `sum(index)` returns the inclusive prefix count or sum through that coordinate.

**Find the median by cumulative frequency.** `count_tree.kth(target)` performs Fenwick binary lifting to find the smallest compressed index whose prefix count reaches `target`. Passing `(x + 1) // 2` returns the lower median coordinate.

The method grows a candidate index bit by bit. It skips a Fenwick block only when that block contains fewer than the remaining target count, subtracting the skipped count. The final index is the required order statistic.

**Compute absolute deviations from prefix aggregates.** Let median be $v$. `left_count` and `left_sum` include all window values at or below $v$. Their cost to increase to $v$ is

$$
v\cdot left\_count-left\_sum.
$$

Values strictly above $v$ have counts and sums derived by subtracting the left aggregates from total window values. Their cost to decrease is

$$
right\_sum-v\cdot right\_count.
$$

Adding these expressions gives `window_cost[start]`. Values equal to the median contribute zero even though they are included in the left group.

**Choose exactly \(k\) non-overlapping windows with prefix DP.** `previous[p]` represents minimum cost to choose the already processed number of windows entirely within first $p$ elements.

Before choosing any windows, every prefix has cost zero, so `previous` is all zeros.

For each of $k$ layers, `current[length]` considers the first `length` elements:

- `current[length - 1]` skips element `length - 1`, allowing chosen windows to end earlier;
- if `length >= x`, taking window `[length-x,length)` adds `window_cost[length-x]` to `previous[length-x]`.

The previous state ends within the prefix before the new window, so overlap is impossible. Using a fresh layer means the transition adds exactly one new window. Infinity marks impossible states.

For the first example, the window-cost phase finds how cheaply every consecutive triple can be equalized. The DP can combine the window at indices one through three with the one at five through seven while preventing overlapping alternatives, totaling eight.

**Why the two phases prove correctness.** Median optimality gives the exact independent cost of every possible selected window. Any legal set of $k$ windows has a last window or skips the final element, matching one DP transition. Conversely, every take transition joins a valid earlier selection with a disjoint length-$x$ window. Induction over layers and prefix length proves `previous[n]` is the minimum total.

## Complexity detail

Let $n$ be array length. Sorting distinct values and compressing all entries costs $O(n\log n)$. Each of $n$ sliding steps performs a constant number of Fenwick updates, prefix sums, and one order-statistic search, all $O(\log n)$. Window preprocessing is $O(n\log n)$.

The selection DP has $k$ layers and scans $n$ prefix lengths per layer, costing $O(nk)$. Total time is

$$
O(n\log n+nk),
$$

matching the manifest.

Compressed arrays, two Fenwick trees, window costs, and two DP rows each use $O(n)$ space. Total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Sort every window independently:** This costs $O(nx\log x)$ and repeats almost all work between adjacent windows.
- **Two heaps with lazy deletion:** They can maintain a sliding median, but sums and delayed removals require more bookkeeping than the two Fenwick trees.
- **Use the mean as target:** Mean minimizes squared error, while median minimizes absolute unit changes.
- **Even window size:** Either middle interval target is optimal; the source consistently chooses the lower median.
- **Overlapping cheap windows:** The DP cannot select both because a take jumps back exactly $x$ positions to the previous layer.
- **Exactly \(k\):** One new layer per selection prevents returning fewer windows merely because they are cheaper.
- **Already equal window:** Its median deviation cost is zero.
- **Negative values:** Coordinate compression and sum arithmetic preserve their order and exact deviation cost.
- **Duplicate medians:** Inclusive left aggregates give zero contribution for every copy equal to the median.
- **Back-to-back windows:** A previous prefix ending at `length-x` allows the next window to start there, which is non-overlapping.
- **Feasibility guarantee:** `k*x <= n` ensures the final exact-count DP state is reachable.
- **Large operation totals:** Infinity and Python integers safely exceed every legal cost.
