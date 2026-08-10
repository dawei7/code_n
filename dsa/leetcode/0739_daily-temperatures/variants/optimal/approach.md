## General

**Scan backward so the future is already summarized**

For each day, we need the nearest later day with a strictly higher temperature. A direct forward search from every day repeats comparisons and can become quadratic.

The exact solution scans indices from right to left. When processing day `i`, all future days have already been considered. A stack of future indices keeps only the days that could still be the nearest warmer answer for some earlier day.

The answer array begins with zeroes. Zero is already correct for any day that has no warmer future day, so the code writes a positive distance only when a candidate exists.

**What the monotonic stack represents**

The stack stores indices, not temperatures, because the answer needs a day difference. Their temperatures can be read through `temperatures[index]`.

Before answering day `i`, the solution removes stack tops whose temperatures are less than or equal to `temperatures[i]`:

`while stk and temperatures[stk[-1]] <= temperatures[i]:`

After these removals, any remaining top is strictly warmer than the current day.

The top is also the nearest surviving future candidate because indices were pushed during a right-to-left scan. More recently pushed indices lie closer to the current position and appear at the top.

**Why colder or equal future days can be discarded forever**

Suppose future day `j` has temperature no greater than current day `i`. For the current day, `j` is not strictly warmer and cannot be the answer.

For any still-earlier day `h`, day `i` is closer than `j`. If `j` would be warm enough for `h`, then `i` is at least as warm as `j` and is also warm enough, while occurring sooner. Therefore `j` can never be the preferred answer for any earlier day.

This domination argument makes popping permanent and is the source of linear time.

Equal temperatures are popped as well because the problem requires a strictly warmer day. An equal day cannot answer the current index, and the closer equal-temperature current day dominates it for earlier indices.

**Read the nearest warmer day**

After popping, if the stack is nonempty, its top index `j` has temperature greater than the current temperature. All closer future indices that could block it were either popped as too cool or remain above it; since none remain above it after the loop, `j` is the nearest warmer day.

The wait is `j - i`, stored as

`ans[i] = stk[-1] - i`.

If the stack is empty, no future day is warmer, so the prefilled zero remains correct.

Finally, the current index is pushed. It may become a useful warmer candidate for days farther to the left.

**Trace the beginning of the standard example**

For `[73, 74, 75, 71, 69, 72, 76, 73]`, scanning begins at the final 73. Its stack is empty, so its answer stays zero and index 7 is pushed.

At 76, the 73 is popped because it is not warmer. The stack becomes empty, so 76 also receives zero and index 6 is pushed.

At 72, the top is 76, which is warmer. The difference is one day. Later, at 69, the top 72 is warmer, again giving one. At 71, the nearest warmer top is the 72 two positions later, producing two.

When processing 75, intervening temperatures at or below 75 are popped until 76 remains. The distance to that index is four.

**The stack invariant**

After processing a suffix, stack indices are possible nearest-warmer witnesses for earlier positions. From top toward bottom, indices move farther into the future, and temperatures are strictly increasing because a new index removes all tops no warmer than itself before being pushed.

This structure ensures the first surviving top is both sufficiently warm and closest among candidates.

**Why the answers are correct**

Every popped day is dominated by a closer day with an equal or higher temperature, so removing it cannot erase a future answer for any unprocessed index. After popping for day `i`, the stack top, if present, is strictly warmer. No closer warmer day is absent: such a day would not have been dominated by a temperature incapable of answering `i` and would remain above the farther candidate.

Therefore the stored difference is exactly the minimum positive wait. If the stack is empty, no qualifying future day exists. Processing all indices yields the complete correct array.

## Complexity detail

Let `n` be the number of days. Each index is pushed once. An index can also be popped at most once because popped indices never return. Thus all while-loop iterations across the entire scan total at most `n`.

Time complexity is `O(n)`, even though one individual day may pop many stack entries.

In a strictly decreasing scan direction that causes no pops, the stack may contain all `n` indices. Auxiliary stack space is `O(n)`. The returned answer array also contains `n` integers and is required output.

## Alternatives and edge cases

- **Forward monotonic stack:** Scan left to right and keep unresolved days with decreasing temperatures. When a warmer day arrives, pop and fill their waits. This is equally optimal and may feel more event-driven.

- **Nested forward searches:** For every day, scan later days until finding a warmer one. Worst-case decreasing or constant temperatures cause `O(n^2)` comparisons.

- **Jump using already computed answers:** Scan backward and skip through future days by their known waits. This can achieve linear behavior with careful zero handling, but the monotonic stack has a clearer domination proof.

- **Pop only strictly colder days:** This would leave an equal-temperature top, which is not a valid warmer answer. The condition must remove `<=` current temperature.

- **Strictly increasing temperatures:** Every day except the last waits one day.

- **Strictly decreasing temperatures:** Each new current temperature pops all lower candidates as appropriate, and every answer remains zero.

- **All temperatures equal:** Equal values are popped, so no day falsely points to an equal-temperature future day.

- **Last day:** It has no future day and keeps its initialized zero.

- **Indices rather than values:** Storing only temperatures would lose the position needed to calculate the wait.

- **Large input:** Every index enters and leaves the stack at most once, making the method suitable for the `10^5`-day constraint.
