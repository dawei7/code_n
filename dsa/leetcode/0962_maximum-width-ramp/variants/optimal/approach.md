## General

**A wide ramp wants an early small left endpoint**

A ramp `(i, j)` needs `i < j` and `nums[i] <= nums[j]`. Its width grows when `i` is farther left and `j` farther right.

Not every index is useful as a left endpoint. If an earlier index has a value less than or equal to a later candidate, the earlier index dominates it: any right endpoint valid for the later candidate is also valid for the earlier one and gives at least as much width.

The first pass keeps only indices that establish a new strict prefix minimum.

**Building the decreasing stack**

The stack stores indices in increasing index order, while their values are strictly decreasing.

At index `i` with value `v`, the code appends when:

- the stack is empty; or
- `nums[stk[-1]] > v`.

If `v` is equal to or larger than the last stored minimum, some earlier stacked index has value at most `v` and dominates `i` as a left endpoint. Skipping `i` loses no maximum ramp.

For `[6, 0, 8, 2, 1, 5]`, the stack becomes indices `[0, 1]` with values `[6, 0]`. Every later value is at least zero, so none can be a better left candidate than index one.

**Scan right endpoints from farthest right**

The second loop visits indices `i` from the end toward zero. For current right value `nums[i]`, it checks the most recently stored left candidate.

While:

`nums[stk[-1]] <= nums[i]`,

that left index and current right index form a valid ramp. The code updates width with `i - stk.pop()`.

The non-strict comparison is required because equal values are allowed in a ramp.

**Why a matched left endpoint can be popped forever**

The right scan moves from largest index to smaller indices. The first right endpoint that can match a particular left candidate is therefore the farthest-right possible match for that candidate.

Any later iteration uses a smaller right index and cannot produce a larger width with the same left endpoint. Once its width is recorded, the left index never needs consideration again and can be popped.

This is what makes the total second-pass work linear rather than comparing every left candidate with every right endpoint.

**Why checking the stack top is sufficient**

Stack values decrease from bottom to top. The top is the smallest and latest prefix minimum.

If the top value is at most current right value, it is matchable and is popped. This may reveal an earlier left index with a larger value that might also match.

If the top value is greater than current right value, every earlier stack entry below it has an even greater value, so none can match this right endpoint. The while loop correctly stops.

**Trace**

For `[6, 0, 8, 2, 1, 5]`, candidates are indices zero and one.

Start right scan at index five, value five. Stack top index one has value zero, so ramp `(1, 5)` is valid with width four. Pop index one.

The new top index zero has value six, which is greater than five, so it cannot match index five.

At index two, value eight, index zero now matches and gives width two. The maximum remains four. The stack becomes empty and scanning stops.

**Why empty stack permits early termination**

After every candidate left endpoint has been popped, its farthest valid right match was already processed. No unrecorded useful left endpoint exists, so later right indices cannot improve the answer.


The first pass retains every nondominated left endpoint: for any skipped index, an earlier retained index has a no-greater value and gives no-smaller width.

The reverse pass matches each retained left endpoint with the farthest right index that can satisfy it, because right indices are considered in descending order. Popping after that match is safe.

Therefore, every possible optimal ramp is represented by an equal-or-better retained ramp, and its maximum width is recorded.

## Complexity detail

Let `N` be array length.

Each index is pushed at most once and popped at most once. Both scans are linear, so time is `O(N)`.

In a strictly decreasing array, every index becomes a prefix minimum and the stack holds `O(N)` indices. Auxiliary space is `O(N)`.

## Alternatives and edge cases

- **Check every pair:** It costs `O(N^2)` time.
- **Sort indices by value:** Processing indices in value order can track a minimum index in `O(N log N)` time.
- **Prefix minima and suffix maxima arrays:** A two-pointer scan gives linear time but uses two auxiliary arrays.
- **Strictly increasing array:** Only index zero is stacked, and it matches the last index for width `N - 1`.
- **Strictly decreasing array:** No positive-width ramp exists, so the answer stays zero.
- **Equal values:** Equality forms a valid ramp and must use `<=`.
- **Duplicate prefix minimum:** The later equal value is dominated and is not stacked.
- **Two elements:** The method returns one if the first value is at most the second, otherwise zero.
- **Early empty stack:** It means every candidate already received its best possible right endpoint.
- **Input preservation:** The algorithm stores indices and does not modify `nums`.
