## General

**Read the condition as independent output pairs**

A beautiful array has even length, and every even output index must differ from the following odd output index. In other words, the kept elements can be grouped as

`(answer[0], answer[1])`, `(answer[2], answer[3])`, and so on,

with unequal values inside each pair. There is no restriction between the second element of one pair and the first element of the next. That local pair structure is what permits a greedy scan.

Deleting an element shifts later elements left, so the parity of an original index is not what matters. What matters is how many elements have already been deleted or kept. The solution tracks original-array position `i` and deletion count `ans` in a way that always treats `nums[i]` as the candidate for the next even position of the resulting array.

Initially, `i = 0` and `ans = 0`. The difference `i - ans` is zero, an even position in the conceptual array after deletions. Every loop action preserves the fact that the next unresolved kept position is even:

- if two candidates are equal, the solution records one deletion and advances one original position, so both `i` and `ans` increase by one and `i - ans` stays even;
- if they differ, it keeps them as a complete pair and advances by two, so `i - ans` increases by two and remains even.

This invariant explains why the code can inspect adjacent entries of the original list without physically deleting anything.

**When adjacent candidates are equal**

At the start of a pair, suppose `nums[i] == nums[i + 1]`. Keeping both would place equal values at the next even and odd output positions, immediately violating beauty. At least one of these two occurrences must therefore be deleted before a valid pair can be completed.

The code performs the conceptual deletion by incrementing `ans` and moving `i` forward by one. It can be viewed as deleting `nums[i]` and allowing the equal-valued `nums[i + 1]` to remain the first candidate for the pair. Because the two values are identical, choosing the other occurrence instead would expose the same value to all later elements. Deleting one now is unavoidable and does not sacrifice a better future option.

If a long run contains several copies of the same value, this action repeats. For `[1, 1, 1, 2]`, the first comparison deletes one `1`, the second comparison deletes another `1`, and the remaining `1, 2` forms a valid pair. The scan keeps exactly one useful representative from the run at the pair's first position.

**When adjacent candidates differ**

If `nums[i] != nums[i + 1]`, these two elements already form a valid next pair. The solution keeps both and advances `i` by two without increasing `ans`.

Keeping them is optimal. They are the earliest available two elements, they satisfy the only constraint applying within their pair, and completing this pair imposes no value restriction on the next pair. Deleting either element could not increase the number kept in the processed portion: the greedy choice keeps two elements using zero deletions, which is the maximum possible contribution of a complete pair.

An exchange argument makes this precise. Consider any optimal result for the current suffix. If the first two available values differ but that result deletes one of them, replace its first eventual valid pair with these two earliest values. They are already unequal, preserve original order, and do not constrain later pairs. The replacement keeps at least as many elements and uses no more deletions. Therefore, some optimum agrees with the greedy choice.

Together, the two cases are safe at every iteration. Equal candidates force at least one deletion, and the greedy method pays exactly that unavoidable cost. Unequal candidates can safely be kept as the next complete pair. Applying these choices repeatedly minimizes deletions needed to build as many valid pairs as possible.

**Why no actual deletion is needed**

Physically removing list elements would shift the remaining list and can make a repeated series of deletions expensive in an array-backed structure. The algorithm instead counts deletions and changes its index. Its comparisons are exactly the comparisons that would appear at the front of the unresolved suffix after the conceptual deletions.

The loop condition is `i < n - 1` because forming a pair requires both `nums[i]` and `nums[i + 1]`. When the condition fails, all possible complete pairs have been resolved. There may be no unpaired element, or exactly one candidate may remain.

**Enforce even final length**

Valid unequal pairs alone are not enough; the final length must also be even. After the scan, `n - ans` is the number of elements conceptually kept. The expression

`(n - ans) % 2`

is zero when that count is even and one when it is odd. Adding it to `ans` deletes a final unpaired element if necessary.

This last deletion is unavoidable when the kept count is odd. Every beautiful array consists entirely of two-element pairs, so one leftover element cannot remain. Removing it is sufficient because all preceding pairs were already established as unequal.

For `nums = [1, 1, 2, 3, 5]`, the first equal comparison forces one deletion. The scan then keeps `[1, 2]` and `[3, 5]` as unequal pairs. The kept length is four, already even, so the parity correction adds nothing and the answer is one.

For `nums = [1, 2, 3]`, the scan keeps `1, 2` as a valid pair and stops with `3` unpaired. No equality deletion was needed, but `(3 - 0) % 2 = 1`, so the method deletes the trailing element and returns one.

**Why the total is minimum**

During the main loop, every counted deletion arises only when two equal values compete for the two positions of a required unequal pair. Any valid subsequence must discard at least one before it can complete that pair, and the greedy scan discards exactly one. When it keeps an unequal pair, an optimum can be chosen to keep that same pair without extra cost.

After those locally optimal decisions, the only possible violation is odd length. If present, one more deletion is mathematically necessary and makes the length even. Thus, every deletion charged by the algorithm is forced by either an equality conflict or the even-length rule, while the constructed conceptual subsequence is beautiful. No solution can use fewer deletions.

## Complexity detail

Let `n = len(nums)`. Each loop iteration advances `i` by either one or two, and `i` never moves backward. Every input position participates in only a constant amount of work, so the main scan takes `O(n)` time. The final parity expression takes `O(1)` time.

The solution stores only `n`, `i`, and `ans` in addition to loop temporaries. It does not build the kept subsequence and does not mutate or copy `nums`. Its auxiliary space complexity is therefore `O(1)`.

The answer itself is a single integer, so there is no output collection to add to the space bound. The one-pass time and constant-space usage match the Optimal manifest.

## Alternatives and edge cases

- **Construct a separate kept array:** Append a value when it can legally occupy the next position, then remove a trailing element if the result is odd. This can express the state clearly but uses `O(n)` extra space; the index-and-count method represents the same choices in `O(1)` space.
- **Physically delete equal elements:** Repeated deletion from the middle of a Python list shifts later elements and can lead to `O(n^2)` time. Counting conceptual deletions avoids all movement.
- **Dynamic programming over index and parity:** A DP can decide whether to keep or delete every value while remembering the previous kept value and parity. It is much more state than this pair-local condition requires, and the greedy exchange argument gives a linear constant-space solution.
- **Only remove adjacent duplicates once:** Deleting a single member of each original equal adjacency is not enough because earlier deletions change which values become paired. The scan's current pair position, not original parity alone, must guide comparisons.
- **Single element:** The loop never runs. The kept count is odd, so the parity correction returns one, leaving the empty array, which is beautiful.
- **Two equal elements:** One equality deletion is counted, leaving one conceptual element; the parity correction deletes that last element too. The answer is two, and the empty array is the only beautiful result.
- **Two unequal elements:** The scan keeps the pair, the kept length is even, and the answer is zero.
- **All values equal:** Repeated equality handling leaves at most one conceptual element, and the parity correction removes it. No nonempty unequal pair can be formed.
- **Already beautiful input:** Every scanned pair is unequal and the length is even, so `ans` remains zero.
- **Equal values across a pair boundary:** Values at output indices `1` and `2` may be equal because the rule applies only when the left index is even. The algorithm correctly advances by two after completing a pair and does not compare across that boundary.
- **Final unpaired candidate:** Its value does not matter. Even if it differs from the previous element, it cannot remain because a beautiful array must have even length.
- **Input preservation:** All deletions are conceptual. The original `nums` list is unchanged after the method returns.
