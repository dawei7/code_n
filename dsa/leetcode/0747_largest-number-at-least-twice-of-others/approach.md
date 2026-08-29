## General

**Only the largest competitor matters**

Let `x` be the unique largest value and `y` be the second-largest value. Every other array value is at most `y`.

Therefore:

- If `x >= 2 * y`, then `x` is at least twice every other value.
- If `x < 2 * y`, the condition already fails for `y`.

Checking the largest against the second largest is both necessary and sufficient. There is no need to compare `x` separately with all remaining smaller values after those two have been identified.

This argument uses the nonnegative-value constraint. Multiplying preserves the ordering among competitors.

**Extract the two largest values**

The exact solution calls

`x, y = nlargest(2, nums)`.

`heapq.nlargest` returns the requested number of elements in descending order, so `x` is the largest and `y` the second largest. It internally maintains only a fixed-size selection structure for two values rather than sorting the entire input.

The array length is at least two, so unpacking exactly two results is always safe.

**Test the dominance condition**

The comparison `x >= 2 * y` directly represents “at least twice.” Equality qualifies. For example, largest six and second largest three pass.

If the test fails, `y` is a concrete other element for which the largest is less than twice its value, so the method returns `-1`.

**Recover the original index**

`nlargest` returns values, not positions. When the dominance condition passes, the solution calls `nums.index(x)` to locate the largest value in the original array.

The problem guarantees that the largest integer is unique, so there is exactly one correct index. `list.index` returns that index.

Without uniqueness, returning the first occurrence might still be one largest index, but the problem’s singular-index wording and proof are simplest under the guarantee.

**Trace `[3, 6, 1, 0]`**

The two largest values are six and three. Since `6 >= 2 * 3`, six is at least twice the strongest competitor. All remaining values are at most three, so they also satisfy the inequality. Looking up six returns index one.

For `[1, 2, 3, 4]`, the two largest are four and three. `4 < 6`, so value three disproves dominance and the result is `-1`.

**Why comparing with an average or sum is wrong**

The requirement is universal: the largest must dominate each individual other value. An average could be small even while one competitor is too large, and a sum imposes a different, much stronger or differently shaped condition. The maximum competitor is the exact critical statistic.

**Why selecting two values is enough even though the answer is an index**

The mathematical decision depends only on the two largest values, so index bookkeeping does not need to complicate the selection step. The exact solution first settles whether dominance holds and only then performs the index lookup. Because the maximum is unique, that lookup cannot accidentally choose a different occurrence.

This two-stage structure is also safe when the second-largest value occurs several times. `y` is used only as the greatest competing value; its index and multiplicity do not matter. If `x` dominates that value, the same inequality automatically holds for every copy and every smaller competitor.

**Why the method is correct**

`nlargest` identifies the unique maximum `x` and maximum value `y` among all other positions. If `x` is at least twice `y`, it is at least twice every value no larger than `y`, so returning its index is correct. If it is not twice `y`, the required universal condition is false, so returning `-1` is correct.

The two branches cover every input.

## Complexity detail

Let `n` be the array length. Selecting the two largest values with a heap of fixed size two costs `O(n log 2) = O(n)` time. Finding `x`’s index performs another linear scan, so total time remains `O(n)`.

The selection heap contains only two values, a constant independent of `n`. Auxiliary space is `O(1)`. The input is not sorted or modified.

Sorting the full array would cost `O(n log n)` and would also require extra care to preserve the original index.

## Alternatives and edge cases

- **One-pass largest and second-largest tracking:** Maintain both values and the largest index while scanning. This achieves the same `O(n)` time and `O(1)` space without a second index scan.

- **Find maximum, then scan all others:** Obtain the maximum and index, then verify `max >= 2 * value` for every other position. This is also linear but performs explicit repeated checks instead of using the second-largest reduction.

- **Sort value-index pairs:** The last two pairs reveal the needed values and preserve the index, but sorting costs `O(n log n)`.

- **Compare only with an arbitrary other value:** The second largest is the strongest constraint. A smaller chosen value cannot prove dominance over all others.

- **Equality at twice:** “At least twice” includes equality, so the comparison must use `>=`.

- **Two-element array:** The two extracted values are the maximum and the only competitor, making the test direct.

- **Zero competitors:** If all nonmaximum values are zero, any positive unique maximum passes because it is at least twice zero.

- **Unique-largest guarantee:** It makes `nums.index(x)` unambiguous and ensures the second returned value belongs to another position.

- **Nonnegative values:** The second-largest sufficiency proof relies on all values being ordered normally under multiplication by two, as guaranteed.
