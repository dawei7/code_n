## General
**Reject incompatible sum ranges**

An array of length $k$ can have only sums from $k$ through $6k$. Therefore equality is impossible when the largest possible sum of one array is smaller than the smallest possible sum of the other: `6 * n < m` or `6 * m < n`. This length check detects the only global impossibility before considering individual values.

**Express every replacement as a possible gain**

Orient the arrays so `nums1` has the smaller current sum. The gap must then be closed by increasing an element `value` from `nums1`, which can contribute at most `6 - value`, or decreasing an element `value` from `nums2`, which can contribute at most `value - 1`. Every useful operation consequently has a maximum gain from `1` to `5`. Count how many operations offer each gain; no sorting is needed because there are only five nonzero buckets.

**Use the largest gains first**

Process gains from `5` down to `1`. If a solution used a smaller available gain while leaving a larger one unused, exchanging those operations could only close at least as much of the gap with the same operation count. Thus some minimum solution always takes gains in descending order. For each bucket, use only as many operations as needed to cover the remaining gap. The first point where the gap becomes nonpositive is the minimum operation count.

## Complexity detail
Computing both sums and counting gains visits every input value once, so it takes $O(n+m)$ time. Processing the five gain buckets is constant work. The six-entry frequency array and scalar state use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sort all possible gains:** Build one gain per element and sort in descending order before taking a prefix. This preserves the greedy reasoning but costs $O((n+m)\log(n+m))$ time.
- **Repeated best-operation search:** Scan both arrays before every replacement to find the largest remaining gain. It is correct but can require $O((n+m)^2)$ time.
- If the initial sums are equal, zero operations are required.
- Different array lengths do not by themselves imply impossibility; their attainable sum intervals must be compared.
- A replacement may overshoot the remaining gap in terms of its maximum gain because the chosen element can be changed to any intermediate value from `1` to `6`.
- Swapping the lower- and higher-sum roles changes only the interpretation of gains, not the answer.
