## General

Ranks depend only on relative order among distinct values:

- the smallest distinct value has rank one;
- the next larger distinct value has rank two;
- equal values share a rank; and
- there are no gaps caused by duplicates.

The exact Optimal solution first creates a sorted list of unique values, then uses binary search to determine each original value's one-based position:

`t = sorted(set(arr))`

followed by:

`bisect_right(t, x)`.

**Removing duplicates first**

`set(arr)` retains one copy of every distinct value. This ensures that duplicates do not occupy multiple rank positions.

For `[100,100,100]`, the set contains only `100`. Sorting gives `[100]`, so every original occurrence receives rank one.

If duplicates remained in the sorted list, the next larger value could receive a rank with an unnecessary gap, violating the “as small as possible” rule.

**Sorting establishes rank order**

After sorting, `t` has strictly increasing values:

$$
t[0] < t[1] < \cdots < t[u-1],
$$

where $u$ is the number of distinct values.

The value at index zero must have rank one, the value at index one rank two, and generally `t[k]` rank `k + 1`.

Negative numbers and large magnitudes cause no special problem because only comparisons determine order.

This also explains why numerical gaps do not create rank gaps. If the only distinct values are `-100` and `5000`, their positions in `t` are zero and one, so their ranks are one and two. Rank measures how many distinct input values are no larger, not the arithmetic distance between values.

**Why `bisect_right` returns the rank**

`bisect_right(t, x)` returns the insertion position after all entries less than or equal to `x`.

Every `x` being queried came from `arr` and therefore appears exactly once in `t`. If it is at zero-based index `k`, there are `k + 1` distinct values at most `x`. The right insertion position is consequently `k + 1`, exactly its required one-based rank.

For `t = [10,20,30,40]`:

- `bisect_right(t, 10)` is one;
- `bisect_right(t, 20)` is two;
- `bisect_right(t, 40)` is four.

`bisect_left(t, x) + 1` would be an equivalent expression. The exact source uses the right boundary so no explicit addition is needed.

Using `bisect_right` on a list that still contained duplicates would not work this way: it would return the position after every equal copy and inflate the rank. Deduplicating before binary search is therefore part of the correctness argument, not merely a memory optimization.

**Preserving original order**

The list comprehension iterates through `arr` in its original order. It replaces each occurrence conceptually with its independently computed rank and returns a new list.

The sorted unique list is used only as a lookup structure; it does not reorder the output.

For `[40,10,20,30]`, the lookup structure is `[10,20,30,40]`, but queries occur in original order, producing `[4,1,2,3]`.

**Why every rank is correct and minimal**

For any value `x`, the returned number equals the count of distinct array values less than or equal to `x`. That count begins at one for the minimum, increases exactly once for every strictly larger distinct value, and remains equal for duplicate occurrences.

Therefore, larger values receive larger ranks, equal values share ranks, and no unused rank is inserted. These are precisely the rank rules.

For the mixed example `[37,12,28,9,100,56,80,5,12]`, the sorted unique list is `[5,9,12,28,37,56,80,100]`. The two occurrences of 12 both query the same list and receive three. Value 37 has five distinct values at most it, so it receives five. This illustrates equality handling, minimal consecutive ranks, and preservation of original positions together.

**Empty input**

The constraints allow an empty array. `set(arr)` and `sorted` produce an empty `t`, and the output comprehension has no iterations. The method returns an empty list without calling binary search.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values.

Building the set takes expected $O(n)$ time and $O(u)$ space. Sorting its values takes $O(u\log u)$ time.

The exact source performs one binary search for every original element. Each costs $O(\log u)$, so lookup time is $O(n\log u)$.

Total time is:

$$
O(n + u\log u + n\log u),
$$

which is $O(n\log n)$ in the worst case.

The set, sorted unique list, and returned list require $O(n)$ total space in the worst case, matching the manifest.

A dictionary from value to rank could reduce the post-sort lookup phase to expected $O(n)$, but the exact source uses binary search.

## Alternatives and edge cases

- **Rank dictionary:** Enumerate the sorted unique values and map each to index plus one, then perform expected constant-time lookups.
- **Sort the full array:** It can still derive ranks by skipping duplicates, but stores and processes repeated values unnecessarily.
- **`bisect_left + 1`:** It is equivalent because every queried value exists exactly once in `t`.
- **All values equal:** The unique list has length one, and every rank is one.
- **Strictly increasing input:** Output is `[1,2,\ldots,n]`.
- **Strictly decreasing input:** Ranks appear in decreasing order while preserving input positions.
- **Negative values:** Sorting and binary search handle them normally.
- **Empty array:** Both the lookup and result lists are empty.
- **Duplicate values:** Deduplication ensures equal ranks and no gaps.
- **Original array unchanged:** The method returns a new rank list rather than overwriting `arr`.
- **Binary-search cost:** Although sorting dominates broadly, exact lookup is $O(\log u)$ per element rather than hash-map constant expected time.
