## General

**The initial minimum separates the two outcomes.** Let $m$ be the smallest
input value and let $C$ be its frequency. If some value is not divisible by
$m$, taking its remainder modulo $m$ creates a positive value strictly smaller
than $m$. Euclidean-style reductions can then consolidate the positive values
until only one array element remains, so the answer is 1.

**Divisibility makes zeros unavoidable.** Suppose instead that every input is
divisible by $m$. Modulo preserves divisibility by $m$, so no operation can
create a positive value below $m$. A larger multiple can be removed without
losing a copy of the minimum by evaluating `m % larger`, which produces $m$
again. After all larger values are removed, pair equal minima. Each pair
becomes one zero, and an unpaired minimum remains when $C$ is odd.

Zeros cannot be selected again. Therefore the $C$ copies of the minimum leave
exactly

$$
\left\lceil\frac{C}{2}\right\rceil
$$

elements. No operation can do better in the all-divisible case because one
new frozen zero can account for at most two copies of the minimum.

## Complexity detail

Finding the minimum, counting it, and checking divisibility each scan at most
$N$ values. The method uses $O(N)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort the array:** Sorting exposes the minimum and its run but costs $O(N\log N)$ time unnecessarily.
- **Search all operand pairs:** Testing which pairwise remainders fall below the minimum is correct but can cost $O(N^2)$ time.
- **Single element:** No operation is possible, and the formula returns 1.
- **Unique minimum:** Whether or not every value is divisible by it, the minimum achievable length is 1.
- **Odd minimum frequency:** One positive minimum remains alongside the zeros produced by the other pairs.
- **Created zeros:** They count toward the final length and can never be selected as either operand.
