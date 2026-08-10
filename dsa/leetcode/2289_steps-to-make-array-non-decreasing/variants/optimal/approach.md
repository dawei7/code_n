## General

**Why literal round-by-round simulation repeats work**

In each step, all currently offending elements are removed simultaneously. Removing them can expose new offending pairs for the next step. Rebuilding the array and rescanning after every round can take quadratic time: one new element may disappear per round.

The solution instead computes how long each right-side block takes to be eliminated when dominated by a larger value on its left. A right-to-left monotonic stack combines already-solved blocks without simulating every global round.

**Interpret the dynamic-programming value**

`dp[i]` represents the number of deletion rounds required for `nums[i]` to finish eliminating the contiguous blocks of smaller values that it can eventually dominate to its right.

It is also the latest deletion round created within that dominated region. Taking `max(dp)` therefore gives the number of global steps until no decreasing adjacent pair remains.

An element with no smaller block that it can expose and remove has `dp[i] = 0`.

**Scan from right to left**

When processing index `i`, all indices to its right already have their own deletion-chain lengths. The stack stores representatives of unresolved right-side blocks.

While the top represents a smaller value,

`nums[i] > nums[stk[-1]]`,

the current value can eventually cause that block to disappear. The top index is popped and merged into the block controlled by `i`.

Values greater than or equal to `nums[i]` stop the popping. The current value cannot delete across such a surviving barrier.

**Why merging needs two timing constraints**

Suppose index `j` is popped into the current index's dominated region.

First, blocks are exposed in order from near to far. If `dp[i]` rounds are already needed for previously merged material, reaching and removing the next exposed block needs one additional round. That gives `dp[i] + 1`.

Second, `j` may itself control a deletion cascade farther right. That internal work can take `dp[j]` rounds and cannot be ignored merely because `j` has now been merged. The combined region cannot finish before that cascade finishes.

Both constraints must hold, producing

`dp[i] = max(dp[i] + 1, dp[j])`.

The source writes `dp[stk.pop()]` directly as the second argument, combining the pop and lookup.

**A simple cascade**

Consider `[5, 3, 4]`. Processing from the right gives zero-time blocks for four and three. At five:

- three is the nearest smaller value, so merging it sets `dp[0]` to one;
- four is then exposed and is also smaller, so merging it sets `dp[0]` to two.

The real process matches this: three disappears in step one, exposing five next to four; four disappears in step two. The answer is two.

**Why equal values are not popped**

The removal rule is strict: the left neighbor must be greater. Equal adjacent values are already non-decreasing and do not delete one another. Accordingly, the stack loop uses `>`, not `>=`.

An equal or larger value remains a barrier and the current index is pushed above it for a possible larger value farther left to process later.

**The monotonic-stack invariant**

After all smaller tops have been popped, either the stack is empty or its top value is at least `nums[i]`. Pushing `i` preserves the ordering of block representatives needed by the next leftward element.

Every index is pushed exactly once and popped at most once. A popped block's timing has already summarized all of its internal interactions, so no deleted region must be traversed again.

**Why the maximum DP value is the global step count**

Every removal chain is attached to some surviving left boundary whose `dp` value records the last round in that chain. The recurrence models simultaneous deletion by taking a maximum when independent internal work overlaps, while the `+1` models sequential exposure of farther blocks.

Thus, the largest `dp[i]` is the latest round on which any deletion occurs. After that many rounds, every dominated block has finished; no decreasing adjacent pair remains. Before it, the chain attaining that maximum is still active.

**Already non-decreasing input**

If `nums` is non-decreasing, scanning from right to left never finds `nums[i] > nums[stk[-1]]`. Every `dp` entry stays zero, and `max(dp)` returns zero.

The local variable `ans` in the source is initialized but never used. The returned value comes directly from the DP array.

## Complexity detail

Let `n` be the array length. Every index is pushed once and popped at most once, so all executions of the nested `while` total `O(n)`. The outer scan is therefore `O(n)` time.

The `dp` array and stack each hold at most `n` entries, using `O(n)` auxiliary space. No modified copy of the array is constructed, and `nums` is not changed.

The nonempty-input guarantee makes `max(dp)` safe.

## Alternatives and edge cases

- **Simulate every round:** Repeated filtering is easy to understand but can take `O(n^2)` time and allocate many intermediate arrays.
- **Forward monotonic stack:** A valid formulation exists with deletion times attached differently; the exact source uses right-to-left block merging.
- **Pop equal values:** That would contradict the strict-greater deletion rule and can overstate the number of steps.
- **Single element:** No deletion is possible, so its sole DP entry and the answer are zero.
- **Already non-decreasing:** No stack pop occurs and the answer is zero.
- **Strictly decreasing:** All offending elements are removed simultaneously in one step, and the recurrence produces a maximum of one.
- **One large value followed by increasing smaller values:** They are exposed one per round, producing a long chain such as `[5,3,4]`.
- **Nested right-side cascade:** `dp[j]` can dominate `dp[i]+1`, which is why the recurrence takes a maximum.
- **Duplicate values:** Equals remain as non-deleting barriers until a strictly larger left value potentially dominates their blocks.
- **Large element values:** Only comparisons are used; their magnitude does not affect complexity.
- **Unused** `ans`: It has no role in the returned result and should not be mistaken for the maintained answer.
- **Input preservation:** The method stores indices and times without removing from `nums`.
