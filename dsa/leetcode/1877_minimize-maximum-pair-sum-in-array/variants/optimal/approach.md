## General

**Balance large values with small partners.** The objective is not to minimize the sum of all pair sums—that total is fixed because every number is used exactly once. The objective is to minimize the largest individual pair sum. Pairing large values together creates a dangerous peak, even if small values paired together look inexpensive. The reliable balancing rule is to pair the smallest value with the largest, the second smallest with the second largest, and continue inward.

**Sort to expose the extremes.** The source calls `nums.sort()`, modifying the list into nondecreasing order. If the sorted values are `a[0], a[1], ..., a[n - 1]`, the intended pairs are `a[i]` with `a[n - 1 - i]` for `0 <= i < n / 2`. Since `n` is even, the first half and reversed second half contain the same number of elements, and every index belongs to exactly one pair. No middle element is left over.

**Prove that an extreme pair can always be chosen optimally.** Let `a` be the smallest remaining value and `d` the largest. In any proposed pairing that does not pair them together, suppose `a` is paired with `x` and `d` is paired with `y`. Replace these two pairs with `(a, d)` and `(x, y)`. Because `a` is smallest and `d` is largest, `a <= y` and `x <= d`. Therefore,

$$
a+d\le y+d
$$

and

$$
x+y\le d+y.
$$

Both replacement sums are at most `d + y`, which was one of the original two sums. Hence the maximum among the replacement pairs is no greater than the maximum among the original pairs. This exchange never worsens the objective. There is consequently an optimal solution that pairs the current smallest and largest values.

After fixing that extreme pair, the same reasoning applies to the remaining sorted values. Repeating it pairs the next smallest with the next largest until no elements remain. This induction proves that the complete inward pairing minimizes the global maximum; it is not merely a heuristic that happens to spread values evenly.

**Read the exact generator carefully.** The slice `nums[: len(nums) >> 1]` contains the first half of the sorted list. The bit shift `len(nums) >> 1` is integer division by two for the nonnegative list length. `enumerate` produces each first-half value `x` together with its index `i`. The expression `nums[-i - 1]` addresses values from the right end: for `i = 0` it is the last and largest value, for `i = 1` it is the second-last, and so forth. Thus `x + nums[-i - 1]` computes exactly one extreme-pair sum.

**Take the bottleneck, not the total.** The generator emits all `n / 2` pair sums, and `max(...)` returns the largest one. The minimized objective is that bottleneck value. Replacing `max` with `sum` would answer a different and trivial question, because the sum over all pairs always equals the sum of the original array regardless of how elements are paired.

**Trace the second example.** Sorting `[3, 5, 4, 2, 4, 6]` gives `[2, 3, 4, 4, 5, 6]`. The first-half slice is `[2, 3, 4]`. Negative indexing supplies partners `6`, `5`, and `4`, producing sums `8`, `8`, and `8`. Their maximum is `8`. Pairing the largest `6` with anything greater than the minimum `2` would already make its pair exceed `8`, illustrating why protecting the largest element with the smallest partner is essential.

**Why all elements are used exactly once.** First-half indices range from `0` through `n / 2 - 1`. Their partner indices, expressed positively, range from `n - 1` down through `n / 2`. The ranges are disjoint, together cover every index, and contain equal numbers of positions. Duplicated values do not cause ambiguity because pairing is about element occurrences; two equal numbers at different sorted positions are still two different occurrences and each is consumed once.

**Mutation and return behavior.** `list.sort` rearranges the caller-provided `nums` list in place. The returned integer is correct under the challenge contract, which does not require retaining original order, but callers outside the challenge will observe the sorted list afterward. The first-half slice is a new list, while the generator itself is lazy.

## Complexity detail

Let $n$ be the even number of elements. Python's comparison sort costs $O(n\log n)$ time in the worst case. Creating the first-half slice copies $n/2$ references in $O(n)$ time, and the generator evaluates $n/2$ pair sums in another $O(n)$ time. The sort dominates, so total time is $O(n\log n)$.

The exact Python source uses $O(n)$ auxiliary space in the worst case. Timsort may allocate linear temporary storage, and `nums[: len(nums) >> 1]` definitely allocates a separate list of $n/2$ elements. The generator and `max` add only constant incremental state. This explains the manifest's $O(n)$ space bound; describing the code as constant-space merely because `sort` is in place would overlook the slice.

Each value is at most $10^5$, so a pair sum is at most $2\cdot10^5$. Python handles it safely. The input has at least two elements, so the generator given to `max` is never empty; no default value or special case is needed.

## Alternatives and edge cases

- **Two explicit pointers:** After sorting, set one pointer at each end, update a running maximum, and move both inward. This avoids the first-half slice and makes the pairing mechanics more direct while retaining $O(n\log n)$ time.
- **Counting frequencies:** Because values are bounded by $10^5$, counts plus two value pointers can form smallest-largest pairs in $O(n+V)$ time and $O(V)$ space, where $V$ is the value range. It is useful when the range is favorable but more elaborate than sorting.
- **Binary search on an answer threshold:** One could ask whether all values can be paired with sums at most a candidate limit, then binary-search the limit. After sorting, the feasibility condition still reduces to extreme pairs, so binary search adds unnecessary logarithmic work.
- **Pairing adjacent sorted values:** This leaves the largest values together and can increase the maximum. For `[1, 1, 2, 3]` it gives maximum `5`, while extreme pairing gives `4`.
- **Exactly two elements:** The slice contains the smaller element, negative indexing selects the larger, and their unavoidable sum is returned.
- **Duplicate values:** Sorting preserves all occurrences, and equal values can be paired in any occurrence order. The exchange proof uses non-strict inequalities, so duplicates require no special handling.
- **Even-length guarantee:** The index ranges cover all elements only because `n` is even. An odd-length generalization would need a rule for the unpaired element; the source intentionally assumes the stated contract.
- **Input preservation:** The exact implementation sorts `nums` in place. Use `sorted(nums)` or pass a copy if an external caller must retain the original ordering.
