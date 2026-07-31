## General

Use 1-based fruit positions. Let `dp[i]` be the minimum additional cost when
fruit `i` is the next fruit that must be purchased to ensure all remaining
fruits can be acquired. Buying it covers positions through `2 * i` for free.
The next purchase may be any position from `i + 1` through `2 * i + 1`; buying
a fruit while it is free is allowed and may extend coverage. With sentinel
`dp[n + 1] = 0`, the recurrence is

$$
\texttt{dp[i]}=\texttt{prices[i-1]}+
\min_{i<j\le\min(n+1,2i+1)}\texttt{dp[j]}.
$$

Evaluate positions from right to left. The transition windows move
monotonically, so maintain their minimum in a deque. Deque indices decrease
from front to back, while their `dp` values increase. Add the newly available
left candidate after removing dominated values from the back, and remove
indices beyond the current right limit from the front. The front then supplies
the recurrence minimum in constant amortized time.

Every legal purchase plan chooses one transition from this range after buying
`i`, and every transition represents a legal choice of the next purchase.
Thus the recurrence considers exactly all plans. Monotonic-deque removals are
safe because a newer candidate with no greater cost remains eligible at least
as long as the dominated one.

## Complexity detail

Let $N=\lvert\texttt{prices}\rvert$. Each index enters and leaves the deque at
most once, so all transitions take $O(N)$ time. The dynamic-programming array
and deque use $O(N)$ space.

## Alternatives and edge cases

- **Scan every transition range:** Evaluating the recurrence with a fresh minimum scan is correct but takes $O(N^2)$ time.
- **Segment tree:** Range-minimum queries give $O(N\log N)$ time, but the monotone movement of these windows permits a simpler linear deque.
- **Buy a free fruit:** This is sometimes optimal because the new purchase can cover farther fruits.
- **First fruit:** It must be purchased; no earlier offer can cover it.
- **Sentinel state:** Position `n + 1` represents completion with zero additional cost and belongs to transition windows that cover the end.
- **Single fruit:** Buying it once is the only plan, so the answer is its price.
