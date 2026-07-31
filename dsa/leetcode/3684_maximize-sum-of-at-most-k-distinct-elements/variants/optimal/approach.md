## General

**Deduplicate before choosing.** First remove duplicate values because a valid choice can contain each number at most once. Since every remaining value is positive, an optimal solution chooses exactly $\min(k,U)$ values: adding any unused distinct positive value increases the sum while staying within the limit.

**Keep the largest distinct values.** Among choices of that fixed size, suppose a selected value is smaller than an unselected value. Exchanging them strictly increases the sum, so no optimum can omit a larger value in favor of a smaller one. Therefore the chosen set consists precisely of the largest $\min(k,U)$ distinct values.

Sort the deduplicated values in descending order and return its first `k` entries. The slice naturally returns all entries when there are fewer than `k` distinct values, and the sort supplies the required strict descending order.

## Complexity detail

Creating the set takes $O(n)$ expected time. Sorting its $U$ values takes $O(U\log U)$ time, and the set plus sorted result uses $O(U)$ space.

The complete legal input contains at most 100 elements, which is too small for stable timing to distinguish sorting, heap selection, and repeated maximum selection. The package therefore uses a reviewed `bounded_domain` certificate. Its bounded-work proof limits deduplication and sorting to 100 values, while property tests compare the reference against independent repeated-maximum selection over exhaustive small arrays, every legal length, and extrema.

## Alternatives and edge cases

- **Min-heap of size `k`:** It can reduce ordering work when `k` is small, but the bounded input makes full sorting simpler and clear.
- **Repeated maximum selection:** It is correct but may repeatedly scan the remaining distinct values.
- **Duplicate values:** Multiple occurrences never allow multiple selections of the same number.
- **Fewer than `k` distinct values:** Return all distinct values; the result is allowed to contain fewer than `k` entries.
- **`k = 1`:** Return only the maximum array value.
- **All values positive:** This guarantee is why selecting an additional available distinct value can never hurt the sum.
- **Output order:** The selected values must be strictly descending, not kept in their input order.
