## General

**Parameterize a plan by the number of shared items**

Suppose exactly `x` type-3 items are bought. They contribute `x` units to both requirements. Any remaining shortage is filled most directly with one-sided items:

$$
C(x)=x\cdot\texttt{costBoth}
+\max(0,\texttt{need1}-x)\cdot\texttt{cost1}
+\max(0,\texttt{need2}-x)\cdot\texttt{cost2}.
$$

Because all costs are positive, buying more than `max(need1,need2)` shared items cannot help: both requirements are already met, and every extra item only increases cost.

The problem is to minimize this function over an enormous integer range, potentially up to $10^9$. The source evaluates only three meaningful breakpoints.

For a fixed `x`, the remaining one-sided purchase counts in the formula are forced in an optimum. Buying fewer would leave a requirement unmet, while buying more contributes beyond an already met requirement at positive cost. Thus `C(x)` really is the minimum plan among all plans with exactly `x` shared items.

**Candidate A: buy no shared items**

`a = need1 * cost1 + need2 * cost2`

is $C(0)$. Each requirement is met independently by its dedicated item type.

This is best when shared items are expensive compared with buying one item of each one-sided type.

**Candidate B: use shared items for the larger requirement**

`b = costBoth * max(need1, need2)`

buys enough type-3 items to satisfy both requirements by itself. The smaller requirement may be exceeded, which is explicitly allowed.

This candidate matters when a shared item is even cheaper than satisfying the remaining one-sided units after the smaller requirement is filled.

**Candidate C: share only the overlapping demand**

Let `mn = min(need1, need2)`. Buying `mn` shared items fills the portion required by both sides. Only the larger requirement can have a remainder:

`c = costBoth * mn + (need1-mn)*cost1 + (need2-mn)*cost2`.

This is $C(\min(need1,need2))$ and represents shared coverage without deliberate oversupply.

**Why no intermediate count can be better**

Assume for illustration that `need1 <= need2`.

For $0\le x\le need1$, increasing `x` by one replaces one type-1 item and one type-2 item with one shared item. Every step changes cost by the constant

$$
\texttt{costBoth}-\texttt{cost1}-\texttt{cost2}.
$$

The cost over this interval is therefore linear and reaches its minimum at an endpoint: `x=0` or `x=need1`.

For $need1\le x\le need2$, requirement one is already satisfied. Increasing `x` replaces only one type-2 item and changes cost by

$$
\texttt{costBoth}-\texttt{cost2}.
$$

This interval is also linear, so its minimum occurs at `x=need1` or `x=need2`.

Those endpoints are exactly the three source candidates: zero, minimum need, and maximum need. The case `need2<need1` is symmetric.

If a slope is zero, every point in that interval ties with its endpoints, so checking the endpoints remains sufficient.

This piecewise-linear view also explains why merely comparing three item prices is not enough. The economic meaning of one shared item changes after the smaller requirement is filled: before that point it replaces two purchases, while afterward it replaces only one.

**Trace expensive and cheap shared items**

With costs 3, 2, and 1 and needs 3 and 2:

- independent plan costs $3\cdot3+2\cdot2=13$;
- all-shared plan costs $3\cdot1=3$;
- overlap-only plan costs $2\cdot1+1\cdot3=5$.

The minimum is three.

With costs 5, 4, and 15 and needs 2 and 3, the independent plan costs 22. Shared items are more expensive than the one-sided replacements, so both other candidates cost more.

**Zero requirements need no branch**

If both needs are zero, all three expressions evaluate to zero and the source returns zero.

If only one need is zero, the overlap candidate equals the independent one, while the all-shared candidate allows direct comparison between the one-sided and shared price for that requirement.

## Complexity detail

The method performs a fixed number of multiplications, additions, minimums, and maximums independent of requirement sizes. Time is $O(1)$ and auxiliary space is $O(1)$.

The costs may reach roughly $10^{15}$ under the constraints; Python integers handle them without overflow.

## Alternatives and edge cases

- **Loop over every shared-item count:** Requirements reach $10^9$, so enumeration is far too slow.
- **Always buy `min(need1,need2)` shared items:** This ignores whether shared items are too expensive or cheap enough to justify oversupplying the smaller side.
- **Compare `costBoth` only with `cost1+cost2`:** That decides the overlap interval but not whether shared items should cover the larger-side remainder.
- **Require exact contributions:** The contract permits exceeding a need, which is why the all-shared candidate is legal.
- **Both needs zero:** Buying nothing gives cost zero.
- **One need zero:** Shared and one-sided items compete only for the nonzero requirement.
- **Equal needs:** The overlap and all-shared candidates coincide.
- **Shared cost equals both one-sided costs combined:** Every overlap count ties across the first interval; endpoint evaluation remains exact.
- **Shared cost equals one remaining side's cost:** Every oversupply count in the second interval ties.
- **Very expensive shared item:** The independent candidate wins.
- **Very cheap shared item:** Buying `max(need1,need2)` shared items may win.
- **Positive prices:** Buying beyond the larger need is never beneficial.
- **No input mutation:** All five arguments remain unchanged.
