## General
**Sum complete weeks as an arithmetic progression**

Write `n = 7 * w + d`, where $w$ is the number of complete weeks and $0 \le d < 7$. Week zero deposits `1` through `7`, totaling 28. Every later week adds one dollar to each of seven days, so complete-week totals are

$$
28, 35, 42, \ldots, 28+7(w-1).
$$

Their sum is

$$
28w+\frac{7w(w-1)}{2}.
$$

**Add the incomplete week**

After $w$ complete weeks, the next Monday deposit is $w+1$. The first $d$ days of that week form

$$
w+1,w+2,\ldots,w+d.
$$

Their sum is

$$
d(w+1)+\frac{d(d-1)}{2}.
$$

Adding the two formulas covers each of the first `n` days exactly once. Integer division and remainder recover $w$ and $d$ directly, so no simulation is required.

## Complexity detail
The calculation uses a fixed number of divisions, multiplications, additions, and subtractions regardless of `n`, giving $O(1)$ time. It stores only the week count, remainder, and partial totals, for $O(1)$ space.

## Alternatives and edge cases
- **Simulate every day:** following the deposit pattern directly is correct but takes $O(n)$ time.
- **Loop over complete weeks:** summing seven-day blocks reduces constants but still takes $O(n/7)$ time.
- **First day:** `n = 1` returns the first Monday deposit of one dollar.
- **Exact week:** when `d = 0`, the incomplete-week contribution is zero.
- **First day of a later week:** the new Monday is one dollar greater than the previous Monday, not the previous Sunday.
- **Maximum day count:** the same closed form applies at `n = 1000` without accumulation error.
