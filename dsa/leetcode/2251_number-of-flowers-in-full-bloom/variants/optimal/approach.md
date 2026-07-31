## General

**Count starts and completed blooms separately**

At arrival time `time`, every flower whose start is at most `time` has begun
blooming. From that number, remove flowers whose end is strictly less than
`time`. An end equal to the arrival is not removed because bloom intervals are
inclusive.

Store all starts in one sorted array and all ends in another. `bisect_right`
on the starts counts values at most `time`; `bisect_left` on the ends counts
values strictly less than `time`. Their difference is exactly the number of
active intervals.

Apply these two searches independently to every person in input order. Each
flower falls into exactly one of three states at a query time—unstarted,
active, or already ended—so the subtraction neither misses nor double-counts
an active flower.

## Complexity detail

Let $F=\lvert\texttt{flowers}\rvert$ and
$P=\lvert\texttt{people}\rvert$. Sorting the endpoint arrays costs
$O(F\log F)$ time. Two binary searches per person cost $O(P\log F)$, for
$O((F+P)\log F)$ total time. The two endpoint arrays use $O(F)$ auxiliary
space, excluding the returned list.

## Alternatives and edge cases

- **Check every flower for every person:** Direct containment tests are correct but require $O(FP)$ time.
- **Event sweep with sorted queries:** Processing starts, ends, and indexed arrivals in chronological order also works, but requires restoring the original query order.
- **Difference map on every time:** Coordinates reach $10^9$, so a dense time array is not viable without compression.
- **Arrival at a start:** The flower is active because starts use an inclusive comparison.
- **Arrival at an end:** The flower is still active; subtract only ends strictly before the arrival.
- **Single-time flower:** `[t, t]` contributes exactly at `t`.
- **Repeated arrival times:** Each occurrence retains its own output position and receives the same count.
- **No active flowers:** The two endpoint counts are equal, yielding `0`.
