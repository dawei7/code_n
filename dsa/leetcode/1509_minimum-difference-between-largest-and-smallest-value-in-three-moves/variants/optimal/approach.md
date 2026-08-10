## General

**Why changing an extreme is equivalent to removing it**

After at most three changes, only the final minimum and maximum matter. If an original extreme is changed to any value inside the eventual surviving range, it no longer influences that range. For purposes of minimizing maximum minus minimum, changing that element is equivalent to removing it from consideration.

Changing a value strictly inside the current minimum and maximum does not shrink the range. Therefore, an optimal set of useful moves targets elements at the low or high ends after sorting.

The stored solution first handles short arrays, then sorts and evaluates the four possible ways to distribute three changes between the two ends.

**Why arrays shorter than five return zero**

If `n < 5`, there are at most four elements. With up to three moves, all but at most one element can be changed to equal the remaining value. The final maximum and minimum are then equal, so their difference is zero.

Zero is the smallest possible difference, so returning immediately is optimal. This also avoids indexing assumptions used by the later four-case loop.

**The four distributions of moves**

After sorting, let `l` be the number of smallest values changed and `r` the number of largest values changed. Spending three useful moves gives

$$
l+r=3.
$$

There are exactly four nonnegative possibilities:

- Change zero smallest and three largest.
- Change one smallest and two largest.
- Change two smallest and one largest.
- Change three smallest and zero largest.

The source loops `l` through zero, one, two, and three and sets `r = 3 - l`.

After removing those extremes from range consideration, the smallest unchanged value is `nums[l]` and the largest unchanged value is `nums[n - 1 - r]`. Their difference is the best range for that distribution because changed values can be placed anywhere inside it.

`ans` starts at positive infinity and keeps the minimum of the four differences.

**Why only these cases can be optimal**

Suppose a move changes an interior sorted element while an unchanged smaller and larger value still define the range. Moving that interior value cannot alter either endpoint, so it does not improve the answer. The move can instead be applied to one of the current extremes without making the range worse.

After each useful extreme change, the next sorted value on that side becomes the possible endpoint. With three moves, every optimal endpoint pair is obtained by discarding some total of three values split between the low and high ends. The loop enumerates every such split.

Although the problem says at most three moves, considering three is safe for `n >= 5`. Any unused move can change another outside endpoint into a value inside the surviving interval, never increasing the range. The four exact-three distributions therefore include a result at least as good as every fewer-move choice, and every computed result is achievable with at most three changes.

**Example of the index calculation**

For sorted five values, choosing `l = 1` and `r = 2` leaves indices one through two as the unchanged range. The code uses largest index `n - 1 - r = 2` and subtracts `nums[1]`.

For `[0, 1, 5, 10, 14]`, the four ranges correspond to keeping:

- `[0, 1]` after changing the three largest, difference one.
- `[1, 5]` after one low and two high changes, difference four.
- `[5, 10]` after two low and one high change, difference five.
- `[10, 14]` after changing the three smallest, difference four.

The minimum is one.

**Input mutation and exact strategy**

`nums.sort()` mutates the caller's list. The method needs only a few extreme values after sorting, but the exact source fully orders all values.

The manifest states linear time and constant space, which can be achieved by selecting the four smallest and four largest values in one scan. Full Python sorting does not have those bounds.

## Complexity detail

Let $N$ be the number of values. The short-array branch is $O(1)$. Otherwise, Python sorting costs $O(N\log N)$ time. The four-case loop is constant time, so total time is $O(N\log N)$.

The source uses a constant number of explicit scalar variables, but Python's Timsort can use $O(N)$ temporary storage in the worst case. Thus practical auxiliary space is $O(N)$, while the list itself is sorted in place.

The manifest's $O(N)$ time and $O(1)$ space describe a selection-based extreme-tracking method, not the exact stored sort. If a language's in-place sort has logarithmic stack use, its auxiliary bound differs, but time remains $O(N\log N)$.

## Alternatives and edge cases

- **Track four smallest and four largest:** Maintain only the extreme candidates during one scan, then evaluate the same four differences. This achieves the manifest's $O(N)$ time and $O(1)$ space.
- **Partial selection:** Selection algorithms can find the necessary order statistics without fully sorting, but are more complex than the four-extreme scan.
- **Fewer than five values:** Three moves can make all values equal, so the answer is zero.
- **Exactly five values:** Each three-move scenario leaves two unchanged endpoint candidates.
- **Already equal values:** Every evaluated difference may already be zero.
- **Negative numbers:** Sorting and subtraction handle them normally.
- **Duplicate extremes:** Changing copies one at a time is correctly represented by moving the retained endpoint index inward.
- **At most versus exactly three:** Extra useful endpoint changes cannot enlarge the best achievable range.
- **Input mutation:** The sorted order remains visible to the caller.
- **Positive infinity:** `inf` must be available in the module environment.
