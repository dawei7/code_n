## General

**Sorting turns valid partners into one contiguous interval**

For a fixed first value $x$, a partner value $y$ is valid exactly when

$$
\texttt{lower}-x\le y\le\texttt{upper}-x.
$$

In an unsorted array, qualifying partners can appear anywhere. After sorting, every value in this numeric interval appears in one contiguous block, whose boundaries can be found with binary search.

Sorting changes element positions, but the answer asks for the number of unordered pairs of distinct original indices, not for the indices themselves. Sorting preserves every occurrence as a separate element and preserves every pair sum. It only gives the values a useful order.

**Fix the left member of each sorted pair**

The loop visits sorted index $i$ with value `x`. It searches only the suffix beginning at `i + 1`. This restriction serves two purposes:

- an element can never pair with itself;
- every pair is counted once, when its smaller sorted index is the fixed index.

Even when values are equal, their array occurrences have different sorted positions. One occurrence at $i$ can pair with equal occurrences after it, and those are distinct original-index pairs.

**Find the first partner meeting the lower bound**

The expression

`j = bisect_left(nums, lower - x, lo=i + 1)`

returns the first suffix position whose value is at least `lower - x`. Every suffix element before $j$ is too small: adding it to $x$ produces a sum below `lower`. Every element from $j$ onward satisfies the lower inequality until values perhaps become too large for the upper inequality.

Passing `lo=i + 1` is essential. Without it, the binary search could return the fixed element or an earlier element, causing self-pairs or double counting.

**Find the position just after the upper bound**

The code uses

`k = bisect_left(nums, upper - x + 1, lo=i + 1)`.

All values are integers. The first value at least `upper - x + 1` is the first value strictly greater than `upper - x`. Thus $k$ is the exclusive end of the valid partner block.

This is equivalent to asking for a right insertion point of `upper - x`. The added one is a convenient integer-boundary transformation:

$$
y\le\texttt{upper}-x
\quad\Longleftrightarrow\quad
y<\texttt{upper}-x+1.
$$

Valid partner positions are exactly $j,j+1,\ldots,k-1$, so their count is `k - j`.

**Why summing these block lengths is exact**

Take any fair pair in the sorted array and call its positions $(i,t)$ with $i<t$. When the loop fixes $i$, the partner value at $t$ is at least `lower - nums[i]` and less than `upper - nums[i] + 1`. Binary-search boundaries therefore place $t$ inside $[j,k)$, and the pair contributes one to `k-j`.

Conversely, every position counted between $j$ and $k$ is after $i$, meets the transformed lower bound, and remains below the exclusive upper boundary. Its sum with `nums[i]` lies inside the required inclusive interval, so no invalid pair is counted.

The suffix rule ensures that the same two occurrences cannot be counted again when the later one becomes the fixed index. Hence every fair pair contributes exactly once.

**Example with repeated and negative values**

Suppose the sorted values are `[-3,-1,-1,4,7]` and the desired sum interval is $[-2,3]$. Fix $x=-3$ at index $0$. A partner must be between $1$ and $6$, so only $4$ qualifies. The two binary searches surround that single position.

When $x=-1$ at index $1$, a partner must be between $-1$ and $4$. The suffix contains another $-1$ and $4$, so both count. The duplicate $-1$ is a separate occurrence and forms a legitimate pair. Sorting and positional suffixes handle these details without a special duplicate rule.

**Following the sample**

For `nums = [0,1,7,4,4,5]`, sorting gives `[0,1,4,4,5,7]`. With bounds $3$ and $6$, fixing $0$ finds partners `[4,4,5]`. Fixing $1$ also finds `[4,4,5]`. Later fixed values have no suffix partners small enough. The total is $3+3=6$.

The function calls `nums.sort()` directly, so the caller's list is reordered. That mutation is not relevant to the returned count but matters if the input is needed later.

## Complexity detail

Let $n$ be the number of values. Python sorting takes $O(n\log n)$ time. The loop runs $n$ times and performs two $O(\log n)$ binary searches, adding another $O(n\log n)$ time. The combined bound remains $O(n\log n)$.

The manifest lists $O(n)$ space. In Python, `list.sort` is in-place with respect to the list object but Timsort may use $O(n)$ temporary memory in the worst case, so that bound is appropriate. Apart from sorting workspace, the algorithm stores only counters and indices. The answer may be as large as $n(n-1)/2$; Python integers handle it safely.

## Alternatives and edge cases

- **Two threshold sweeps:** Count pairs with sum below `upper + 1` using two pointers, subtract the count below `lower`, and obtain the same answer after sorting in $O(n)$ scan time.
- **Check every pair:** Two nested loops take $O(n^2)$ time, which is too slow for $10^5$ values.
- **Frequency map:** Counting by value can help when the number of distinct values is small, but duplicate multiplicities and range queries make the sorted method simpler and reliably $O(n\log n)$.
- **Exact single sum:** When `lower == upper`, the two boundaries isolate partners producing exactly that sum.
- **Negative values:** Binary search works on sorted numeric order without assuming positivity.
- **Duplicate values:** Occurrences remain separate list entries, so all distinct-index combinations are counted.
- **One-element array:** Every suffix is empty, both bisections return the same position, and the answer is zero.
- **No valid partner:** The lower and upper insertion points coincide, contributing zero.
- **All pairs valid:** Each fixed index contributes the size of its suffix, and the total becomes $n(n-1)/2$.
- **Input mutation:** `nums.sort()` changes the original order; sort a copy if the caller requires preservation.
- **Inclusive bounds:** The lower search uses “at least,” while `upper - x + 1` converts the inclusive upper condition into an exclusive lower-bound search.
