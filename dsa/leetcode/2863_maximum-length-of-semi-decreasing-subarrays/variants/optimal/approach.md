## General

**Only record undominated starts**

A result is determined by indices $i<j$ satisfying `nums[i] > nums[j]`; the interior of the subarray is irrelevant. Suppose two possible starts satisfy $i<k$ and `nums[i] >= nums[k]`. Any endpoint smaller than `nums[k]` is also smaller than `nums[i]`, and starting at $i$ produces the longer subarray. Therefore $k$ can never improve the answer.

Scan from left to right and store an index only when its value is strictly larger than every previously stored candidate. The resulting stack contains increasing indices with strictly increasing values. Keeping the earliest occurrence of a repeated value is essential because the inequality at the endpoint is strict and the earlier equal start always gives a longer span.

**Resolve candidates from the farthest endpoints**

Visit endpoint indices from right to left. Before testing an endpoint `right`, discard stack indices at or to its right because a start must satisfy `left < right`, and no still-earlier endpoint can make those indices valid starts.

If the top candidate value is greater than `nums[right]`, this is the farthest-right compatible endpoint that candidate will ever encounter. Record `right - left + 1` and pop the candidate permanently. Because candidate values increase toward the top, continue popping while the strict inequality holds. If the top value is not greater, every lower stack value also fails for this endpoint, so move left to the next endpoint.

Every index enters and leaves the stack at most once. A popped valid start has already received its longest possible endpoint, while an undominated start that remains available can still match a smaller value farther left. These facts ensure the maximum recorded span is exactly the longest semi-decreasing subarray.

## Complexity detail

Let $n$ be the length of `nums`. The construction scan is $O(n)$. The reverse scan is also $O(n)$ amortized because each candidate is popped at most once, even though it contains nested `while` loops. The stack holds at most $n$ indices, so auxiliary space is $O(n)$.

The benchmark uses the array length $n$ as `size` and supplies strictly decreasing legal arrays. The monotonic-stack method processes each index a constant number of times. A correct implementation that tests every endpoint pair completes all tiers and exhibits $O(n^2)$ scaling.

## Alternatives and edge cases

- **Sort value-index pairs:** Process values from largest to smallest while tracking the earliest eligible index. Equal values must be handled as a batch to preserve strictness. This takes $O(n \log n)$ time and $O(n)$ space.
- **Test every endpoint pair:** Check all $i<j$ and retain the largest qualifying span. It is simple and correct but takes $O(n^2)$ time.
- **Increasing or constant array:** No earlier value is strictly greater than a later one, so return `0`.
- **Duplicate start values:** Retain the earliest occurrence; a later equal value cannot produce a longer valid subarray.
- **One element:** A single element has equal first and last values and therefore is not semi-decreasing.
- **Negative values:** Comparisons use their ordinary signed ordering; no positivity assumption is needed.
- **Endpoint-only condition:** Rising or falling interior values never affect whether a chosen subarray qualifies.
