## General

**Fix the largest value and search the sorted prefix**

After sorting, this variant scans pivot `i` from right to left. `nums[i]` is the largest selected value, and `left = 0`, `right = i - 1` search for the other two values in the prefix.

The current sum is

$$
\texttt{total}=\texttt{nums[left]}+\texttt{nums[right]}+\texttt{nums[i]}.
$$

Increasing `left` raises or preserves the sum; decreasing `right` lowers or preserves it. That supplies the same monotonic closest-sum search as a forward pivot, viewed from the opposite end.

**Track both the best distance and its actual sum**

`min_diff` begins at infinity, while `result` is a placeholder. After each non-exact candidate, the method checks

```python
if abs(total - target) < min_diff:
    min_diff = abs(total - target)
    result = total
```

The first candidate always replaces the placeholder. Thereafter the two variables stay synchronized: `min_diff` is exactly the distance belonging to `result`.

Although pointer movement happens before this update in the source, `total` was already calculated and remains unchanged. The current candidate is still evaluated before the next loop iteration.

**Return an exact target immediately**

When `total == target`, the method returns `target`. Difference zero is unbeatable, so no unexamined triplet can improve it.

**Why each pointer move discards only worse candidates**

If `total < target`, holding the same `left` while decreasing `right` would use an equal or smaller value, producing a sum no larger than `total` and therefore no closer from below. Those pairs can be discarded, and `left += 1` is the only move that can approach the target.

If `total > target`, holding the same `right` while increasing `left` would produce an equal or larger sum, no closer from above. Decreasing `right` is the only useful direction.

The current `total` is evaluated for the best distance even though the pointer changes first. Thus the candidate that dominates the skipped pairs is retained in `result` if appropriate.

**Why duplicate largest values may be skipped**

The reverse scan processes the rightmost occurrence of a pivot value first. Its prefix includes every earlier occurrence and all values available to a later equal pivot. When the next `i` has the same value, its prefix is strictly smaller and cannot create a new sum that the earlier search lacked. Skipping it avoids repeated work without losing a possible closest sum.

Duplicates remain usable as separate elements inside the first search: two or three equal values occupy distinct indices even though repeated pivot iterations are skipped.

**Trace `[-4,-1,1,2]` for target `1`**

- Pivot `2`, pair `-4` and `1`: total `-1`, distance `2`; save it and raise `left`.
- Same pivot, pair `-1` and `1`: total `2`, distance `1`; save it and lower `right`.
- Later pivots yield no closer result.

The returned sum is `2`.

**Why the final result is globally closest**

For one pivot, the two-pointer proof shows that any skipped pair is dominated in distance by an already computed sum on the same side of the target. When pointers cross, no better pair for that pivot remains. The reverse outer loop processes every distinct pivot value with the largest available prefix, so every potentially unique triplet sum is evaluated or safely dominated.

The first real candidate initializes `result`, exact equality returns immediately, and every strict distance improvement replaces it. The final value is therefore the unique closest sum guaranteed by the contract.

**Why updating after the branch does not skip the last candidate**

The source changes `left` or `right` before comparing `total` with `min_diff`, but the loop condition is checked only at the start of the next iteration. The already computed integer `total` is independent of the newly changed indices. Even if the pointer move makes the pointers meet, the current sum still reaches the distance-update lines before the loop exits. Thus every examined pair is considered for `result` exactly once.

## Complexity detail

Let $n$ be `len(nums)`.

- **Time complexity: $O(n^2)$.** Sorting is $O(n\log n)$. Each of $O(n)$ pivots performs a linear inward pointer scan; duplicate skipping can reduce work but not worsen the bound.
- **Space complexity: $O(n)$ under the manifest's conservative sorting accounting.** The two-pointer state itself is $O(1)$. The source comment's $O(1)$ convention excludes output and sorting implementation workspace, while Python sorting may allocate temporary memory.

## Alternatives and edge cases

- **Forward pivot:** Fix the smallest value and search its suffix. It is equally correct and is used by the Optimal variant.
- **Do not skip duplicates:** Correct but repeats identical searches; asymptotic time remains quadratic.
- **Binary-search complement:** Fix two values and inspect neighbors around a binary-search insertion point, costing an extra logarithmic factor.
- **Exact match:** Returns before updating `min_diff`, which is safe because zero distance is final.
- **First candidate:** Finite distance always replaces infinity, so the placeholder `result = 0` cannot leak for legal arrays.
- **Three zeros:** Produces sum zero; for a nonzero target it becomes the initial and final closest candidate as appropriate.
- **Target beyond attainable range:** Monotonic movement finds the nearest extreme sum.
- **Repeated values:** Distinct pointer indices permit repeated values in a triplet; only redundant pivot searches are skipped.
- **Input mutation:** `nums.sort()` changes the input list order.
- **Update placement:** Pointer variables may change before the best-distance comparison, but the saved `total` still represents the just-evaluated triplet and is processed before another loop condition.
