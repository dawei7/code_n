## General

**Recover the sum that the missing rolls must have**

There are `m = len(rolls)` known observations and `n` missing observations. If the average across all `m+n` rolls must be exactly `mean`, then their required total sum is

$$
(m+n)\cdot\textit{mean}.
$$

The known observations already contribute `sum(rolls)`. Therefore the missing observations must contribute

$$
s=(m+n)\cdot\textit{mean}-\sum\texttt{rolls}.
$$

This is the value calculated by the source. Once `s` is known, the original average requirement becomes a simpler construction problem: produce exactly `n` legal die values whose sum is `s`.

**Determine whether that sum is possible**

Every six-sided die value is at least one. Consequently, `n` missing dice have minimum possible sum `n`. Every value is at most six, so their maximum possible sum is `6n`.

The necessary condition is therefore

$$
n\le s\le6n.
$$

It is also sufficient. Every integer sum in this inclusive range can be distributed among `n` values from one through six. The source checks both boundaries and immediately returns an empty list when `s<n` or `s>6n`.

This test handles both directions of impossibility. A very large known sum can make the required missing sum too small, while a small known sum combined with a high requested mean can make it too large.

**Distribute the sum as evenly as possible**

On feasible input, divide `s` by `n`:

$$
q=\left\lfloor\frac{s}{n}\right\rfloor,\qquad r=s\bmod n.
$$

The source first creates `n` copies of `q`. Their current total is `nq`. By the division algorithm,

$$
s=nq+r
$$

with `0\le r<n`. The construction then increments the first `r` entries by one. That adds exactly the missing remainder, so the final sum is `s`.

The resulting list contains `r` copies of `q+1` and `n-r` copies of `q`. The order is irrelevant because the task accepts any valid set of missing observations.

**Why every constructed value is a legal die face**

Feasibility gives `s>=n`, hence `s/n>=1` and `q>=1`.

It also gives `s<=6n`, hence `q<=6`. If `q=6`, then `s=6n` and the remainder must be zero, so no value is incremented to seven. If the remainder is positive, `q` must be at most five, making `q+1<=6`.

Thus every output entry lies between one and six inclusive. The average-like distribution is not merely aesthetically balanced; it makes the range proof immediate.

**Trace the first example**

For `rolls = [3,2,4,3]`, `mean=4`, and `n=2`, there are six observations in total. Their required sum is `6 * 4 = 24`, while the known rolls sum to 12. Therefore `s=12`.

The feasible interval for two missing dice is from two through twelve, so twelve is possible. Division gives `q=6` and `r=0`. The source returns `[6,6]`, and all six rolls sum to 24 as required.

**Trace a nonzero remainder**

For `rolls = [1,5,6]`, `mean=3`, and `n=4`, the required total is `7 * 3 = 21`. The known sum is 12, leaving `s=9`.

Here `q=9 // 4=2` and `r=9 % 4=1`. Four copies of two initially sum to eight. Incrementing the first one produces `[3,2,2,2]`, whose sum is nine. This differs in order from another valid example output, but the problem explicitly permits any valid array.

**Why the construction is correct**

If the source returns empty, `s` lies outside `[n,6n]`. No collection of `n` legal die values can have such a sum, so no answer exists.

Otherwise, quotient-and-remainder distribution creates exactly `n` integers. The range argument proves each is a legal face, and the sum argument proves they total `s`. Adding their total to the known-roll sum yields `(m+n) * mean`. Dividing by the total number of rolls gives exactly `mean`.

Those two cases cover every input, establishing that the source returns a valid construction exactly when one exists.

**Why integer arithmetic is preferable**

The algorithm never computes a floating-point average. It works entirely with totals, so it cannot introduce rounding error. Since the desired mean is an integer, equality of the total to `(m+n) * mean` is exactly equivalent to equality of the average to `mean`.

The input list is read only for its length and sum; it is not rearranged or modified.

## Complexity detail

Let $M$ be the number of known rolls and $N$ the number of missing rolls. Computing `sum(rolls)` takes $O(M)$ time. Allocating the answer takes $O(N)$ time, and incrementing the first remainder entries takes at most $N-1$ additional operations. Total time is $O(M+N)$.

The returned list contains $N$ integers, so total output storage is $O(N)$. Excluding that required output, the algorithm uses only a constant number of scalar variables, or $O(1)$ auxiliary space. On an impossible input, it returns after the sum and bounds check without allocating the length-$N$ answer.

## Alternatives and edge cases

- **Start every die at one:** Distribute `s-n` extra points, at most five per die; this is equivalent but requires a slightly more explicit capacity loop.
- **Backtracking over die faces:** It explores many unnecessary combinations even though only the total matters.
- **Random valid distribution:** It can work but complicates reproducibility and range enforcement without improving complexity.
- **Required sum exactly `n`:** Every missing roll must be one.
- **Required sum exactly `6n`:** Every missing roll must be six.
- **Required sum below `n`:** Return empty because even all ones are too large.
- **Required sum above `6n`:** Return empty because even all sixes are too small.
- **Remainder zero:** Every output value is the quotient.
- **Positive remainder:** Exactly that many entries receive one extra point.
- **One missing roll:** It must equal `s`, provided `1<=s<=6`.
- **Many valid answers:** The source returns a balanced one; output order has no semantic importance.
- **Exact average:** Total-sum arithmetic avoids floating-point comparison.
- **Input preservation:** `rolls` is never changed.
