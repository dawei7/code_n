## General

**Choose the next fruit that will be purchased.** Let `cost[i]` be the
minimum cost of a plan whose next paid fruit is the zero-based fruit `i`,
including its purchase price. After buying fruit `i`, its reward covers
indices through `2 * i + 1`. The next paid fruit may be any covered fruit
from `i + 1` onward, because paying for a free fruit is allowed, or it may be
the first uncovered fruit at `2 * i + 2`.

Add a sentinel state `cost[N] = 0` representing that no fruit remains. The
transition is therefore

$$
\texttt{cost[i]}
=
\texttt{prices[i]}
+
\min_{i+1\le j\le\min(N,2i+2)}
\texttt{cost[j]}.
$$

This considers every possible next purchase after fruit `i`. Fruits between
the two purchases are acquired free, and the chosen next state optimally
handles the remaining suffix, so backward induction proves that `cost[0]` is
the global minimum.

**Maintain each window minimum with a deque.** Evaluate indices from right to
left. Keep candidate indices in decreasing index order and nondecreasing cost
order from front to back. Before evaluating `i`, remove front indices beyond
the transition's right boundary. The front then has the minimum valid cost.
After computing `cost[i]`, remove back candidates whose cost is at least as
large: the new, smaller index is no more expensive and remains eligible for
future leftward windows at least as long, so it dominates them. Append `i`
for the next iteration.

## Complexity detail

Let $N=\lvert\texttt{prices}\rvert$. Every state enters the deque once and
leaves it at most once, so all transitions take $O(N)$ time. The dynamic
programming array and deque use $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Scan every transition window:** The direct recurrence is simple and correct but takes $O(N^2)$ time.
- **Min-heap of candidate states:** Lazy removal can provide $O(N\log N)$ time, but the monotonic deque exploits the ordered sliding boundaries more directly.
- **Always take a free fruit for free:** This greedy rule can be suboptimal because purchasing that fruit may unlock a valuable later reward.
- **Always buy the cheapest reachable fruit:** Price alone ignores how far the fruit's reward extends.
- **Single fruit:** It must be purchased, so the answer is its listed price.
- **Sentinel state:** Index `N` represents completion and permits a reward range that already covers the remaining suffix to add zero cost.

