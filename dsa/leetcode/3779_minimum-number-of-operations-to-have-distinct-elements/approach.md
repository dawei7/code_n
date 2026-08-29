## General

**View every possible result as a retained suffix**

Each operation removes the first three current elements, except that a final shorter remainder is removed completely. After $m$ operations, the surviving array—if any—starts at original index $3m$.

There is no choice about which elements an operation removes. The only question is how many three-element prefix blocks must disappear before the remaining suffix has no duplicate.

**Scan from the end to find the longest distinct suffix**

The source maintains a set `st` while moving from right to left. Before processing index `i`, the set contains exactly the values in suffix `nums[i+1:]`, and that suffix is pairwise distinct.

If `nums[i]` is not in the set, adding it extends the distinct suffix one position left. The invariant remains true.

If `nums[i]` is already in the set, then `nums[i:]` is not distinct: the current occurrence duplicates a later occurrence. This is the first duplicate encountered during the reverse scan, so `nums[i+1:]` is the longest suffix known to be distinct.

For `[3,8,3,6,5,8]`, the scan stores 8, 5, and 6. It then sees 3 and stores it. At index one it finds 8 already present, so any valid retained suffix must begin after index one.

**Convert the duplicate index into whole operations**

To eliminate the duplicate at index `i` while retaining a suffix, the removed prefix length must be strictly greater than `i`. After $m$ operations that length is $3m$, so the requirement is

$$
3m>i.
$$

The smallest integer satisfying it is

$$
m=\left\lfloor\frac{i}{3}\right\rfloor+1,
$$

implemented as `i // 3 + 1`.

This formula handles block boundaries correctly. A duplicate at index two disappears after one operation because indices zero through two are removed. A duplicate at index three survives one operation and needs a second.

**Why removing through the first reverse duplicate is sufficient**

The returned operation count removes at least indices zero through `i`. The remaining array begins somewhere inside or after `nums[i+1:]`.

That latter suffix is already pairwise distinct by the scan invariant, and any suffix of a distinct sequence is also distinct. The computed number of operations therefore always reaches a valid stopping state, possibly the empty array.

**Why fewer operations cannot work**

With one fewer operation, at most `3(m-1)` elements are removed. By minimality of `m`, that prefix ends at or before index `i`, so the occurrence at `i` remains. Its matching occurrence lies later and also remains because prefix deletion preserves every later element.

The retained suffix still contains a duplicate. Therefore no smaller operation count can satisfy the stopping condition.

Together, sufficiency and necessity prove that the rounded block count is exact.

**Return zero when the whole array is already distinct**

If the reverse loop finishes without a membership hit, every value was inserted once and the complete array is pairwise distinct. The process must stop before performing an operation, so the source returns zero.

The array is nonempty, but no special small-length logic is required. A length-one array is distinct. A length-two duplicated array finds a hit at index zero and returns one, which removes all remaining elements under the operation rule.

## Complexity detail

Let $N$ be the array length. The reverse scan visits each occurrence at most once. Set membership and insertion take expected $O(1)$ time, giving expected $O(N)$ total time.

In the worst distinct case, `st` stores all $N$ values, so auxiliary space is $O(N)$. The source does not mutate or copy the array.

The operation count is computed arithmetically; it does not simulate individual prefix removals.

## Alternatives and edge cases

- **Simulate removals and rebuild a set each time:** Rechecking every remaining suffix can become quadratic.
- **Scan candidate suffixes from the left:** A reverse set finds the maximal distinct suffix in one pass.
- **Return `ceil(i/3)`:** Index `i` itself must be removed, so the prefix length must be greater than `i`; `i//3+1` is the correct rounding.
- **Stop at the first duplicate from the left:** Later duplicates determine whether the retained suffix is distinct; left-to-right discovery does not directly identify the longest distinct suffix.
- **Already distinct input:** No operation is allowed or needed before the stopping condition, so return zero.
- **Two equal elements:** One operation removes the entire shorter-than-three remainder.
- **Duplicate at index two:** One three-element removal eliminates it.
- **Duplicate at index three:** One operation leaves it at the new front, so two are required.
- **Many repeated values:** The first membership hit from the right is enough; anything retained after removing it lies inside the established distinct suffix.
- **Final removal past the array end:** The rule explicitly removes all remaining elements when fewer than three exist.
- **Empty result:** It is a valid stopping state.
- **Relative order:** Prefix removal never rearranges survivors, matching the suffix reasoning.
- **Input preservation:** Only a set and loop index are changed.
