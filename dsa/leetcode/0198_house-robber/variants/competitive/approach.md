## General

**Build optimal answers for prefixes**

The competitive method scans houses from left to right and keeps only two
dynamic-programming values. Before processing the current amount `i`, `now` is
the maximum money obtainable from all already processed houses, and `last` is
the maximum obtainable from the prefix that ends one house earlier than that.

In index notation before house $h$, `now` represents the best result through
$h-1$, while `last` represents the best result through $h-2$. These are exactly
the two earlier states needed to decide whether to include house $h$.

**Compare robbing and skipping the current house**

If the robber skips the current house, the best total remains old `now`.

If the robber takes the current amount `i`, the immediately previous house
cannot have been taken. The compatible earlier optimum is old `last`, so this
candidate is `last + i`.

The new prefix optimum is `max(last + i, now)`. This one comparison represents
all legal subsets of the processed prefix because every such subset either
includes the current house or excludes it.

**Use simultaneous assignment correctly**

The update is:

`last, now = now, max(last + i, now)`

Python evaluates every right-hand expression using the old values before it
assigns either left-hand variable. New `last` therefore receives the previous
prefix optimum, ready to serve as the two-back state on the next iteration.
New `now` receives the best total including or excluding the current house.

Sequentially assigning `last = now` before computing the maximum would be
wrong: `last + i` would then use the immediately preceding optimum, which may
already include the adjacent house. A temporary variable or Python's parallel
assignment is essential to preserve the old states.

**Initialize the empty prefixes**

Both variables start at zero. Before any house, the best obtainable total is
zero. The conceptual prefix two steps back is also empty and has value zero.

For the first house, the update compares taking its nonnegative amount with
skipping for zero. The result becomes that amount. Afterward, the invariant has
the ordinary meanings needed for all later iterations.

This initialization also makes the method return zero for an empty list, even
though the Reference guarantees at least one house.

**Trace `[2,7,9,3,1]`**

Start with `(last, now) = (0, 0)`.

- Amount 2 gives `(0, 2)`.
- Amount 7 compares `0 + 7` with 2, giving `(2, 7)`.
- Amount 9 compares `2 + 9` with 7, giving `(7, 11)`.
- Amount 3 compares `7 + 3` with 11, giving `(11, 11)`.
- Amount 1 compares `11 + 1` with 11, giving `(11, 12)`.

The returned 12 corresponds to houses with amounts 2, 9, and 1. The variables
store totals, not the actual chosen indices, which is sufficient for the
requested scalar answer.

**Why the invariant proves the result**

Initially, both empty-prefix optima are zero, so the invariant is true. Assume
it holds before a house. Every legal selection for the enlarged prefix either
skips this house, in which case its maximum is old `now`, or takes it, in which
case the prior house is excluded and its maximum is old `last + current`.

The computed maximum is therefore the exact optimum for the enlarged prefix.
Parallel assignment shifts old `now` into the role required for the next house,
so the invariant is preserved. After the final house, `now` is the optimum for
the entire array and is returned.

**Why no explicit robbed-state flag is needed**

Some formulations store separate values for “rob current” and “skip current.”
Here the recurrence has already maximized those possibilities into prefix
totals. Keeping the best one-back and two-back values retains all information
needed by the next decision, so an array or boolean state would be redundant.

**Nonnegative values and optional selection**

All amounts are nonnegative. Nevertheless, the recurrence includes the skip
candidate because taking a small house can block a larger adjacent one. If
negative amounts were allowed, the same initialization and maximum would still
permit skipping all harmful houses and return at least zero.

## Complexity detail

The loop visits each of the $n$ amounts once and performs constant arithmetic
and comparison per visit, so time is $O(n)$.

Only the loop value and two running totals are retained, independent of input
length. Auxiliary space is $O(1)$, exactly matching the manifest. Python's
iteration does not create a proportional recursion stack or DP table.

## Alternatives and edge cases

- **Memoized suffix recursion:** The optimal variant uses the same recurrence conceptually but stores $O(n)$ cached states and stack frames.
- **Bottom-up array:** Store `dp[h] = max(dp[h-1], dp[h-2] + nums[h])`; clear but unnecessary for a total-only result.
- **Separate take/skip states:** Maintain best totals ending with each choice; equivalent constant-space DP.
- **Greedy largest-first selection:** Can fail because choosing one house changes availability of two neighbors.
- **One house:** First update chooses its amount.
- **Two houses:** Second update chooses the greater amount.
- **All zeros:** Running total remains zero.
- **Empty list:** Returns zero as a safe generalized behavior.
- **Duplicate amounts:** Decisions depend on positions and totals, not uniqueness.
- **Parallel assignment:** Must use old `last` and old `now` together; careless sequential updates break adjacency safety.
