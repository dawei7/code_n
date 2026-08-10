## General

**Fix the later index and choose the best earlier value**

For a current value at index `j`, the best possible earlier partner is the minimum value among indices zero through `j-1`. Subtracting the smallest earlier value maximizes `nums[j] - nums[i]` while automatically respecting `i<j`.

The source keeps that prefix minimum in `mi` and scans left to right.

**Start before any real prefix exists**

`mi` is initialized to positive infinity and `ans` to -1. At the first value, `x > mi` is false, so the else branch sets `mi=x`. No pair is evaluated because no earlier index exists.

From the second element onward, `mi` is a real value from a strictly earlier position.

This initialization lets one loop handle the first item without separate indexing.

**Evaluate only positive differences**

If `x > mi`, the current value is strictly larger than some earlier value, so the pair satisfies the increasing-value condition. `x - mi` is positive and is the greatest valid difference ending at the current index.

The source updates `ans = max(ans, x - mi)` to retain the best across all later endpoints.

If `x <= mi`, no positive difference ending here can exist. The value becomes the new prefix minimum through `mi=x`. Equality may replace the minimum with an equal value at a later index, but that does not change any future numerical difference.

**Trace the first example**

For `[7,1,5,4]`, the first value sets `mi=7`. Value one is not larger, so it becomes the new minimum.

Value five is larger than one and gives candidate four, so `ans=4`. Value four gives candidate three, which does not improve the answer.

The invalid numerical gap from one at index one back to seven at index zero is never considered because the scan only pairs current values with earlier minima, never future minima with past maxima.

**Why the prefix minimum is sufficient**

For a fixed current index $j$, every legal earlier index belongs to the prefix. If its value is $v$ and prefix minimum is $m$, then $m\le v$, so

$$
\texttt{nums}[j]-m
\ge
\texttt{nums}[j]-v.
$$

Whenever any earlier value is strictly smaller than the current value, the prefix minimum is also strictly smaller and gives the best candidate. Storing other earlier values cannot improve the result.

This argument also establishes optimality of the information retained: future endpoints need the smallest earlier number, not the index identities or the ordering among all larger prefix values. One scalar preserves exactly the part of the entire prefix that can influence any later maximum difference.

**Why the algorithm is correct**

Before each iteration after the first, `mi` is the minimum of all values at earlier indices. The source tests the maximum possible valid difference ending at the current position and adds it to the global competition if positive.

Every valid pair has some later endpoint $j$, and the candidate considered there is at least as large as that pair's difference. Every candidate considered comes from a real earlier minimum and a strictly larger current value, so it is valid. Therefore the maximum retained candidate is exactly the answer.

If no current value is ever greater than its prefix minimum, no valid pair exists and `ans` remains -1.

Because every valid difference is positive, the -1 sentinel can never be confused with a real answer.

**Why updating only in the else branch works**

When `x > mi`, current `x` cannot lower the prefix minimum, so leaving `mi` unchanged is correct. When `x <= mi`, assigning `x` preserves the minimum. The two branches together are equivalent to always writing `mi=min(mi,x)`, but avoid an unnecessary update on increasing values.

## Complexity detail

Let $N$ be array length. The loop visits every value once and performs constant-time comparisons and arithmetic, so time is $O(N)$.

Only `mi`, `ans`, and the loop value are stored, giving $O(1)$ auxiliary space. The input array is not modified.

## Alternatives and edge cases

- **Check every index pair:** Direct but takes $O(N^2)$ time.
- **Suffix maximum for each earlier index:** Also linear with an array, but uses $O(N)$ space when one rolling prefix minimum suffices.
- **Sort the values:** Incorrect because sorting destroys the required index order.
- **Strictly decreasing array:** No current value exceeds its prefix minimum, so return -1.
- **All equal values:** Equality is not increasing; return -1.
- **Best pair uses nonadjacent indices:** Prefix minimum retains it regardless of distance.
- **First value:** Establishes the prefix minimum and cannot be a later endpoint with an earlier partner.
- **Large values:** Difference fits comfortably in Python integers.
- **Strict comparison:** `x > mi` enforces `nums[i] < nums[j]`; equality must not qualify.
- **Several equal minima:** Any occurrence gives the same numerical candidate, and the earliest/later identity is irrelevant.
- **Answer sentinel:** -1 remains only when no positive valid difference exists.
- **Input preservation:** The scan performs no sorting or writes.
