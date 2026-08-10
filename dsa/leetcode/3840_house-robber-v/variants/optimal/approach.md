## General

**Only the immediately previous house affects a new choice**

The restriction applies when two selected houses are both adjacent and have the same color. When deciding whether to rob house `i`, every earlier choice except house `i - 1` is non-adjacent to it and cannot conflict.

Therefore a prefix solution needs only two states:

- `f`: the maximum money from the processed prefix when its last house is not robbed;
- `g`: the maximum money from the processed prefix when its last house is robbed.

The states do not need to remember a set of prior colors. A matching color two or more positions away is allowed.

**Initialize the first house**

Before processing beyond index 0:

- skipping house 0 gives `f = 0`;
- taking house 0 gives `g = nums[0]`.

Both are legal. Keeping the zero state is important even though all amounts are positive, because it can enable taking a same-colored adjacent house with a larger amount.

**Skipping the current house**

If house `i` is not robbed, the preceding house may have been skipped or robbed. Neither choice conflicts with a skipped current house.

Thus the new skip state is always:

$$
f_{\text{new}}=\max(f_{\text{old}},g_{\text{old}}).
$$

The source uses this same expression in both color branches.

**Taking when adjacent colors are equal**

If

`colors[i - 1] == colors[i]`,

houses `i - 1` and `i` cannot both be robbed.

To take house `i`, the previous state must be `f_old`, where house `i - 1` was skipped. The new take value is:

$$
g_{\text{new}}=f_{\text{old}}+\texttt{nums}[i].
$$

This is the familiar House Robber restriction, but it applies only at same-color boundaries.

**Taking when adjacent colors differ**

If the colors differ, robbing both adjacent houses is allowed. House `i` can extend either previous state:

$$
g_{\text{new}}
=
\max(f_{\text{old}},g_{\text{old}})
+
\texttt{nums}[i].
$$

This may select consecutive houses. The problem does not ban adjacency by itself; it bans only adjacent selections sharing a color.

**Simultaneous assignment preserves the old states**

The source writes assignments such as:

`f, g = max(f, g), f + nums[i]`.

Python evaluates the entire right-hand side before assigning either left-hand variable. The second expression therefore uses `f_old`, not the newly computed skip state.

This detail is essential in the equal-color branch. Sequentially overwriting `f` first and then using it for `g` would incorrectly allow the best previous take state to feed a forbidden adjacent take.

**Trace a mixed-color example**

For `nums = [3,1,2,4]` and `colors = [2,3,2,2]`:

After house 0, states are `f = 0` and `g = 3`.

House 1 has a different color from house 0. Skipping gives 3, while taking can extend the best old state, giving $3+1=4$. States become `(3,4)`, representing that houses 0 and 1 can both be robbed.

House 2 also differs from house 1. New states become skip 4 and take $4+2=6$.

House 3 has the same color as house 2. Taking it must extend the old skip state 4, giving 8, while skipping keeps 6. The result is 8, achieved by houses 0, 1, and 3.

**Why two states are sufficient and exact**

Assume `f` and `g` are optimal for the prefix ending at `i - 1`.

Every valid selection for the next prefix either skips house `i` or takes it. If it skips, removing the unused current house leaves one of the two optimal predecessor categories, so the best value is their maximum.

If it takes, legality depends only on whether house `i - 1` was taken and whether the adjacent colors match. The source allows exactly the legal predecessor state or states in each color case.

Every transition constructs a legal selection, and every legal selection belongs to one transition. The states remain optimal by induction. After the final house, the best overall solution may end in either state, so the source returns `max(f, g)`.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The loop processes each house after the first once and performs constant comparisons and arithmetic. Total time is $O(N)$.

Only `n`, `f`, `g`, and the loop index are stored. The DP rolls the prefix states instead of allocating arrays, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Two DP arrays:** Store skip and take values for every index. This gives the same recurrence and $O(N)$ time but uses unnecessary $O(N)$ space.
- **Standard House Robber recurrence:** Always forbidding adjacent houses is too restrictive when neighboring colors differ.
- **Rob every positive house:** Amounts are positive, but this is invalid across a same-color adjacent pair.
- **Greedy larger of a same-color pair:** Local choices can affect which later houses combine, so a two-state DP is safer than pairwise greedy decisions.
- **One house:** Initialization covers the entire input, and the positive amount is returned.
- **All adjacent colors equal:** The problem reduces to standard House Robber, forbidding every adjacent pair.
- **Every adjacent color differs:** All positive-value houses may be robbed, and the take transition accumulates them.
- **Same color at non-adjacent positions:** It creates no restriction; only `colors[i - 1]` is compared with `colors[i]`.
- **Skipping a positive house:** It can be optimal when that enables a more valuable same-colored neighbor.
- **Simultaneous assignment:** Both new values must read the old states; changing evaluation order can break the equal-color transition.
