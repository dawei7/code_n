## General

**Reducing a route to one interval**

Any route that harvests more than one pile visits every coordinate between its leftmost and rightmost harvested positions. Reversing direction more than once only repeats distance without reaching a new extreme, so an optimal route covers one contiguous interval of the sorted fruit positions and changes direction at most once.

For interval endpoints $L$ and $R$, define

$$
d_L = \max(0,\texttt{startPos}-L)
\quad\text{and}\quad
d_R = \max(0,R-\texttt{startPos}).
$$

Going left first costs $2d_L+d_R$, while going right first costs $d_L+2d_R$. The minimum steps needed to cover the interval are therefore

$$
\min(2d_L+d_R,\ d_L+2d_R).
$$

This formula also handles an interval entirely on one side: the distance on the other side is zero, leaving the direct distance to its far endpoint.

**Maintaining every maximal reachable window**

Advance `right` through the already sorted piles and add its amount to `window_total`. If the interval from `fruits[left][0]` through the new right position costs more than `k`, remove the left pile and increment `left` until the route becomes feasible.

For a fixed right endpoint, moving `left` rightward can only decrease both the covered distance and the collected amount. Thus the first feasible `left` produces the largest sum among feasible windows ending at `right`, because all fruit amounts are positive. Record that sum and continue.

The left pointer never moves backward. Every reachable contiguous interval that could be optimal appears as the maintained maximal window for some right endpoint, while the route formula proves that every retained window can actually be harvested within the step budget. The largest recorded sum is consequently the optimum.

## Complexity detail

Both pointers move from left to right at most once, and each pile is added to and removed from the running sum at most once. The time complexity is $O(n)$. Apart from the input and a constant number of counters, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all endpoint pairs:** Carry a sum while trying every contiguous interval and test its route cost. This is correct but requires $O(n^2)$ time.
- **Prefix sums plus binary search:** For each possible turning boundary, binary-search the opposite reachable endpoint and query its interval sum. This can achieve $O(n\log n)$ time with $O(n)$ prefix storage, but the sliding window is simpler and faster.
- **Fruit at `startPos`:** It is harvested at zero cost whenever its position lies in the selected interval.
- **Zero steps:** Only a pile exactly at `startPos` can contribute.
- An interval entirely left or entirely right is handled by one zero endpoint distance in the route formula.
- Positions outside every feasible window must be removed even when their fruit amount is large; value cannot compensate for an unreachable route.
- Unique ascending positions make every sliding-window interval unambiguous, and positive amounts justify keeping the widest feasible window for each right endpoint.
