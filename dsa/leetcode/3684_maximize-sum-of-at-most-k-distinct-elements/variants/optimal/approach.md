## General

The chosen values must be distinct, and no more than $k$ of them may be returned. Two facts determine the optimum:

1. every value in `nums` is positive, so adding another available distinct value always increases the sum; and
2. among choices with the same number of elements, larger values always produce a sum at least as large as smaller values.

If the array contains $U$ distinct values, the optimal result therefore contains exactly

$$
r=\min(k,U)
$$

values: the $r$ largest distinct values in the array. “At most $k$” becomes exactly $k$ only when at least $k$ distinct values exist. If fewer exist, all of them should be selected.

The exact Optimal source finds those values by sorting the **entire input array** in ascending order and scanning it backward. This differs from the manifest summary, which describes building a set before sorting; the behavior is equivalent, but the exact operations and concrete complexity are not the same.

**Why positivity determines how many values to choose**

Suppose fewer than $r$ distinct values have been selected. Because $r \le U$, another unused distinct value exists. It is positive, so adding it increases the total sum. The smaller selection cannot be optimal.

This argument would fail if zero or negative values were allowed: under an “at most” limit, adding such a value might not help. The problem's positive-integer guarantee is therefore essential, not incidental.

**Sorting places useful values at the end**

The source calls

`nums.sort()`

which mutates `nums` into nondecreasing order. Equal values become adjacent, and the largest values occupy the highest indices.

It then scans indices from `n - 1` down through zero. This direction immediately encounters values in descending order, which serves both goals:

- the first distinct values encountered are the largest ones, so they maximize the sum; and
- appending them in encounter order automatically produces the required strictly descending result.

No separate reversal of `ans` is needed.

**Skipping duplicate occurrences**

At index `i`, the code checks:

`if i + 1 < n and nums[i] == nums[i + 1]:`

`    continue`

Because the scan moves right to left, index `i+1` has already been examined. If the two values are equal, a copy of this value was already encountered farther to the right, so the current occurrence must not be appended again.

The rightmost copy in each equal-value run is selected, and every remaining copy in that run is skipped. The identity of the occurrence does not matter because the output contains values, not original indices.

For example, after sorting `[84, 93, 100, 77, 93]`, the array is `[77, 84, 93, 93, 100]`. The reverse scan proceeds as follows:

- append $100$;
- append the rightmost $93$;
- skip the other $93$ because its right neighbor is equal;
- append $84$ and stop if $k=3$.

The result is `[100, 93, 84]`, already strictly descending.

**Stopping after enough distinct values**

Whenever a new distinct value is appended, the source decrements `k`. Once `k == 0`, exactly the allowed number of distinct values has been selected and the loop stops.

If the array contains fewer than the original $k$ distinct values, `k` never reaches zero. The loop simply reaches the beginning of the array and returns all distinct values. This is correct because the contract says “at most” $k$, not “exactly” $k$.

Reusing the parameter `k` as a countdown changes only the local integer binding inside the method. It does not alter the caller's integer object.

**Why the chosen values maximize the sum**

Write the distinct values in strictly descending order:

$$
d_1>d_2>\cdots>d_U.
$$

The algorithm returns $d_1,\ldots,d_r$. Consider any other valid selection of $r$ distinct values. If it differs from the algorithm's choice, then some selected value lies below one of the top $r$ values that was omitted. Replacing the smaller selected value with that larger omitted value strictly increases the sum. Repeating this exchange eventually transforms the alternative into the algorithm's set without ever decreasing the sum.

No selection with fewer than $r$ values can be better because all values are positive and another distinct value can be added. Therefore, the first $r$ distinct values encountered by the reverse scan form a maximum-sum valid choice.

The output-order requirement follows from the same scan. Each appended value is strictly smaller than the preceding appended value: equal values are skipped, and the sorted array cannot increase while moving left.

## Complexity detail

Let $n$ be the length of `nums` and $U$ its number of distinct values.

The exact source sorts all $n$ elements with `nums.sort()`. Python's in-place Timsort takes $O(n \log n)$ time in the worst case, followed by an $O(n)$ reverse scan. The actual total worst-case time is therefore $O(n \log n)$.

This is a source/manifest distinction. The manifest's `O(n + U log U)` bound describes a different implementation that first creates a set in $O(n)$ expected time and then sorts only its $U$ values. The exact source does not create that set, so when $U$ is much smaller than $n$, its sorting work is still based on $n$, not $U$.

The result list stores $r=\min(k,U)$ values. Python's sorting implementation may also use $O(n)$ temporary references in the worst case, even though `list.sort` rearranges the original list rather than returning a second full list. Thus, the exact Python implementation has $O(n)$ worst-case auxiliary space including sorting workspace, plus an output of $O(r)$, which is already bounded by $O(n)$.

If one abstracts the language's in-place sort as using only its explicit list and counts only source-created containers, `ans` is the only new growing collection and uses $O(r)$. The manifest's `O(U)` space bound matches the size of a set-based alternative and also upper-bounds the returned distinct values, but it does not precisely describe Timsort workspace when many duplicate positions make $n$ much larger than $U$.

The method also mutates the order of `nums`. That does not change the returned mathematical result, but it is a concrete side effect of the exact source.

## Alternatives and edge cases

- **Deduplicate with a set, then sort:** `sorted(set(nums), reverse=True)[:k]` implements the manifest summary in expected $O(n + U \log U)$ time and $O(U)$ explicit space. It avoids sorting duplicate positions but creates a hash set.
- **Keep a size-$k$ min-heap:** After deduplication, retain only the largest $k$ values in $O(n + U \log k)$ expected time. This can help when $k \ll U$, but the final heap still must be sorted descending for the required output.
- **Repeatedly search for the next maximum:** Performing a fresh scan for every chosen value can cost $O(nk)$ time and needs additional logic to exclude duplicates.
- **All values distinct:** No duplicate check succeeds. The algorithm returns the last $k$ sorted values in reverse order.
- **All values equal:** The rightmost copy is appended and every earlier copy is skipped, so the result contains one value even when $k$ is larger.
- **`k > U`:** The scan exhausts the array before the countdown reaches zero and correctly returns all $U$ distinct positive values.
- **`k = 1`:** The first reverse-scan value is the array maximum, and the method stops immediately after appending it.
- **Duplicate boundary:** Comparing with `nums[i+1]` is safe only because of the `i + 1 < n` guard. At the rightmost index there is no already-scanned neighbor.
- **Input mutation:** Callers that need the original array order would have to pass a copy or use a nonmutating sorted expression. The exact method sorts `nums` in place.
- **Hypothetical nonpositive values:** Choosing all available slots would no longer be automatically optimal. The current reasoning is valid because the contract guarantees every element is positive.
