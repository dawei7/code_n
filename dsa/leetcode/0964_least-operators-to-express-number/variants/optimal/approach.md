## General
**View the expression as signed powers of `x`.** A copy of $x^k$ for $k\ge1$ requires `k` operators inside its multiplication chain, while $x^0=1$ is written as `x / x` and costs two. Addition and subtraction between terms are accounted for by these per-copy costs; one final operator is removed because the first term needs no leading sign.

**Process the base-$x$ digits with a carry choice.** Read `target` from its least significant base-$x$ digit upward. At position $k$, keep two costs: `positive`, the least cost for representing the processed suffix exactly, and `negative`, the least cost for representing it as one unit of $x^{k+1}$ minus that suffix. For digit `digit`, the exact state may use `digit` copies of $x^k$ without a carry or `digit + 1` copies when resolving a prior negative state. The negative state similarly uses `x - digit` copies, with one fewer copy when a carry is already present.

**Initialize the special unit cost.** At $k=0$, each positive unit costs two operators because it is `x / x`; initialize the exact cost as `digit * 2` and the complement cost as `(x - digit) * 2`. At higher positions, one copy of $x^k$ costs $k$. Update both states from the previous pair without storing earlier digits.

**Close the highest carry.** After all $L$ digits, the exact state is already complete. The negative state needs one additional $x^L$, costing $L$, to cancel its deficit. Take the cheaper of those choices and subtract one for the absent leading `+` or `-`. These two states cover both possible carry decisions at every digit, so the result is minimal.

## Complexity detail
Each iteration removes one base-$x$ digit from `target`, so there are $L$ iterations and $O(L)$ time. Only the digit position and two dynamic-programming costs are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Memoized recursion around powers:** Recurse on using the largest power below `target` or overshooting with the next power, then memoize remainders. This is correct but uses $O(L)$ call and cache space.
- **Recompute every prefix:** Solve the digit dynamic program again for each longer base-$x$ prefix. It preserves correctness but takes $O(L^2)$ time.
- **Breadth-first expression search:** Generating expression values by operator count has an enormous state space and does not respect the constraints efficiently.
- **Target equals `x`:** The expression is simply `x`, so the answer is `0`.
- **Target equals one:** The expression `x / x` uses one operator.
- **Exact power:** When `target` is $x^k$, a multiplication chain uses $k-1$ operators after the leading copy.
- **Rational intermediates:** Division is exact rational arithmetic; it is not integer truncation.
