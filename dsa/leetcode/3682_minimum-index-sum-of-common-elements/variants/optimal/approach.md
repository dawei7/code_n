## General

A good pair depends only on a shared value. For a fixed value `x`, suppose it occurs at several indices in each array. The smallest index sum involving `x` must use the earliest occurrence of `x` in `nums1` and the earliest occurrence of `x` in `nums2`. Choosing a later occurrence in either array can only increase, never decrease, the sum.

This observation removes the need to inspect every pair of positions. The exact Optimal source records the earliest position of each value in `nums2`, then scans `nums1` and evaluates one candidate whenever the value is present in that table.

**Why one index per value is sufficient**

Let

$$
i_x = \min\{i \mid \texttt{nums1}[i]=x\}
$$

and

$$
j_x = \min\{j \mid \texttt{nums2}[j]=x\}.
$$

For any good pair containing value $x$, its indices satisfy $i \ge i_x$ and $j \ge j_x$. Therefore,

$$
i+j \ge i_x+j_x.
$$

So the best pair for value $x$ is completely characterized by those two earliest positions. All later duplicates of $x$ are irrelevant to the minimum.

The source chooses to store earliest positions from `nums2`:

`d[x] = i`

but only when `x not in d`. Since `nums2` is scanned from left to right, the first time a value appears is its smallest index. Refusing to overwrite that entry preserves the useful index. Although the manifest summary describes recording positions from `nums1` and scanning `nums2`, the exact source does the symmetric reverse; the result and complexity are identical, and this explanation follows the actual code.

For example, if `nums2 = [7, 3, 7, 3]`, the dictionary stores `d[7] = 0` and `d[3] = 1`. The occurrences at indices $2$ and $3$ cannot improve a sum for their values, so they are intentionally ignored.

**Scanning the other array**

The variable `ans` begins as positive infinity:

`ans = inf`

This sentinel means that no good pair has been found yet. The source then enumerates `nums1`. At position `i` with value `x`:

- if `x` is absent from `d`, there is no occurrence of `x` anywhere in `nums2`, so index `i` cannot form a good pair;
- if `x` is present, `d[x]` is the earliest matching index in `nums2`, and `i + d[x]` is the smallest sum possible using this particular occurrence of `nums1[i]`.

The candidate updates

`ans = min(ans, i + d[x])`.

The scan does not explicitly skip later duplicates in `nums1`. That is harmless: for the same value `x`, a later index `i` produces a sum at least as large as the one produced by its earliest occurrence. The `min` operation simply leaves the better earlier candidate unchanged. Storing an earliest-index dictionary for both arrays would save a few redundant checks but would use another data structure without improving the asymptotic bound.

Consider `nums1 = [3, 2, 1]` and `nums2 = [1, 3, 1]`. The dictionary is `{1: 0, 3: 1}`. At `nums1[0] = 3`, the candidate sum is $0+1=1$. The value $2$ has no match. At `nums1[2] = 1`, the candidate is $2+0=2$. The minimum remains $1$.

**Why the final minimum covers every good pair**

Take any good pair $(i,j)$ with shared value $x$. When the algorithm scans `nums1[i]`, the dictionary contains the earliest occurrence `d[x] = j_x` of $x$ in `nums2`. Since $j_x \le j$,

$$
i + j_x \le i + j.
$$

Thus, for every possible good pair, the algorithm evaluates another good pair with the same `nums1` index and an index sum no larger. The minimum over the evaluated candidates can therefore be no greater than the true optimum.

In the other direction, every evaluated candidate uses an index `i` where `nums1[i] = x` and a stored index `d[x]` where `nums2[d[x]] = x`. Every candidate is a genuine good pair, so the algorithm cannot produce a value smaller than the true optimum by using an invalid combination.

Together, these two directions show that the smallest evaluated sum is exactly the minimum index sum among all good pairs.

If no common value exists, no candidate ever replaces `inf`. The final expression

`return -1 if ans == inf else ans`

then returns the required sentinel $-1$. If at least one match exists, every index sum is a finite nonnegative integer, so `ans` differs from infinity and the stored minimum is returned.

## Complexity detail

Let $n$ be the common length of the two arrays, and let $u$ be the number of distinct values in `nums2`.

The first loop examines all $n$ elements of `nums2` once. Each dictionary membership check and insertion takes expected $O(1)$ time. The second loop examines all $n$ elements of `nums1` once and performs expected constant-time dictionary work for matching values. The total expected time is therefore $O(n)$.

The expected qualifier comes from Python's hash-table operations. Under the standard expected-cost model used by the manifest, this is the stated linear-time algorithm.

The dictionary stores one index for each distinct value in `nums2`, requiring $O(u)$ space. Since $u \le n$, the worst-case auxiliary space complexity is $O(n)$. The infinity sentinel, loop indices, and current answer require $O(1)$ additional space.

Reading both arrays already requires $\Omega(n)$ work in the worst case: if the only common value is at the final position, an algorithm cannot safely decide the result without inspecting that position. The linear scan is therefore asymptotically optimal.

## Alternatives and edge cases

- **Check every pair of indices:** Comparing every `nums1[i]` with every `nums2[j]` directly takes $O(n^2)$ time and repeats work for equal values.
- **Store all positions per value:** Lists of every occurrence are unnecessary because only the earliest index can minimize a sum. One integer per distinct value is enough.
- **Build two earliest-index maps:** This also leads to an $O(n)$ solution by intersecting their keys, but the second dictionary is optional. The exact source scans `nums1` directly.
- **Sort value-index pairs:** Sorting can group common values while retaining original indices, but it increases the running time to $O(n \log n)$.
- **Overwrite dictionary entries:** Assigning every occurrence from `nums2` would leave the latest index rather than the earliest one and could produce a nonminimum result. The `if x not in d` guard is essential.
- **No common value:** `ans` remains `inf` and the method returns $-1$, rather than leaking the sentinel.
- **A common value at index zero in both arrays:** The minimum possible sum is zero. The dictionary stores zero normally, and membership is tested with `x in d` rather than truthiness of the stored index.
- **Duplicate values in either array:** Only the earliest `nums2` index is stored. Later `nums1` occurrences may be checked, but cannot improve on an earlier occurrence of the same value.
- **Negative and zero element values:** Values are dictionary keys, not indices. Their sign has no effect on matching or on the nonnegative index sum.
- **Equal-length guarantee:** The method does not rely on synchronized positions; a good pair may use any `i` and `j`. Equal lengths affect only the shared symbol $n$ used in the complexity bound.
