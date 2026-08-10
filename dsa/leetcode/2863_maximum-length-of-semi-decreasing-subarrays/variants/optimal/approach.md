## General

**Only the endpoints determine validity.** A subarray from index $i$ through index $j$ is semi-decreasing when `nums[i] > nums[j]`. Values between those endpoints may rise, fall, or repeat; they do not affect whether the subarray qualifies. Its length is `j - i + 1`. The goal is therefore to find a value at a late index and some strictly larger value at the earliest possible earlier index.

The exact solution reorganizes indices by value. The first loop builds `d` so that `d[x]` is the increasing list of every index containing value `x`. Because indices are appended during a left-to-right scan:

- `d[x][0]` is the earliest occurrence of `x`;
- `d[x][-1]` is the latest occurrence of `x`.

Those two extremes are sufficient. Once the ending value $x$ is fixed, a later occurrence always gives at least as long a subarray, so only its latest occurrence is useful as the right endpoint. Among all values strictly greater than $x$, an earlier occurrence always gives at least as long a subarray, so only their globally earliest occurrence is useful as the left endpoint.

**Process values from large to small.** The loop `for x in sorted(d, reverse=True)` considers distinct values in descending order. Before processing current value `x`, variable `k` equals the smallest first-occurrence index among all values already processed. Since all processed values are strictly larger than `x`, `k` is exactly the earliest position containing a valid larger left-end value.

The candidate

`d[x][-1] - k + 1`

uses the latest occurrence of current value `x` as the right endpoint and the earliest occurrence of any greater value as the left endpoint. This is the longest possible semi-decreasing subarray whose last value is `x`. The maximum over all ending values is the global answer.

After evaluating `x`, the assignment `k = min(k, d[x][0])` adds current value's earliest occurrence to the pool. It must happen after the candidate calculation, not before: the left endpoint must be strictly greater than the right endpoint's value, so an equal `x` occurrence is not eligible for current `x`. On the next iterations, however, current `x` is greater than those smaller values and should be eligible.

**Why the index order is also enforced.** It is possible that the earliest larger value lies to the right of the latest current value. Then `d[x][-1] - k + 1` is non-positive and cannot describe a valid ordered subarray. The code initializes `ans = 0`, so such a candidate cannot increase the answer. A positive candidate of at least two arises only when the chosen larger occurrence is actually earlier.

At the very first, largest distinct value, `k` is `inf` because no strictly larger value exists. Its candidate is negative infinity and is ignored. The loop then records that largest value's earliest index for smaller ending values.
Take endpoints $(i,j)$ of any valid answer and let $x=\texttt{nums[j]}$. When the descending-value loop reaches $x$, it has already processed `nums[i]` because `nums[i] > x`. Thus maintained `k` is no greater than $i$. Also, `d[x][-1]` is at least $j$. The computed candidate is therefore

$$
\texttt{d[x][-1]}-k+1 \ge j-i+1.
$$

So the algorithm finds a candidate at least as long as every valid subarray. Conversely, every positive candidate it records begins at a value strictly larger than $x$ and ends at value $x$, so that candidate itself is a valid semi-decreasing subarray. It cannot exceed the true optimum. Both directions prove equality.

For an increasing array such as `[1,2,3,4]`, larger values always occur later than smaller ending values. Every candidate is non-positive, so `ans` remains `0`, as required.

**A manifest mismatch worth making explicit.** The manifest says the method uses prefix-maximum candidates in $O(n)$ time. The protected source instead groups indices in a hash map and sorts all distinct values. That is a correct approach, but its worst-case running time is not linear when all values are distinct.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values. Building the dictionary of index lists takes expected $O(n)$ time. Sorting its $u$ keys takes $O(u\log u)$ time. The descending scan does $O(1)$ work per key, so exact total time is $O(n+u\log u)$, which becomes $O(n\log n)$ when $u=n$.

Every input index is stored once across the lists in `d`, and the sorted key list holds $u$ values. Auxiliary space is $O(n+u)=O(n)$. The manifest's $O(n)$ space remains accurate, but its $O(n)$ time does not describe the checked-in implementation.

## Alternatives and edge cases

- **Monotonic prefix candidates:** Store indices that set a new prefix maximum, then scan right endpoints from right to left and pop candidates once their values are strictly greater. This obtains the intended $O(n)$ time and $O(n)$ space.
- **Sorting index-value pairs:** Sorting all elements by value can express the same idea but still costs $O(n\log n)$ and needs careful equal-value batching to preserve strictness.
- **All equal values:** No first value can be strictly greater than a last value; equal values are deliberately never added to `k` until after their own candidate, so the answer stays `0`.
- **Strict inequality:** Processing current value only after querying prevents equal endpoint values from being accepted.
- **Negative values:** Dictionary ordering and numerical comparisons work unchanged; the algorithm does not assume values are positive.
- **Single element:** No two ordered endpoints exist, and the sentinel-based candidate leaves the answer at `0`.
- **Sentinel arithmetic:** Python permits finite integers minus `inf`, producing negative infinity. A language without such a numeric sentinel should explicitly skip the first key.
- **Worst-case distinct values:** Sorting dominates at $O(n\log n)$; describing this exact source as $O(n)$ would be inaccurate.
