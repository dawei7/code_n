## General
**Count factors of five**

Every trailing zero pairs one factor `5` with an abundant factor `2`. Therefore $z(x) = \operatorname{floor}(x / 5) + \operatorname{floor}(x / 25) + \operatorname{floor}(x / 125) + \ldots$. Repeatedly divide by five to evaluate this monotone function in logarithmic time.

**Find the first candidate with binary search**

Search for the smallest `x` with $z(x) \ge k$ in the half-open range from zero through $5k + 5$. If this first candidate has $z(x) = k$, return five; otherwise the monotone function skipped `k`, so return zero.

**Why a present value has five preimages**

Within each block $5q, 5q + 1, \ldots, 5q + 4$, multiplying by the extra nonmultiples of five introduces no new factor of five, so `z` is constant across all five values. At the next multiple of five it increases by at least one. Consequently a zero count is either skipped entirely or occupies exactly one five-integer block. The lower-bound check distinguishes those two cases.

## Complexity detail
The binary search performs $O(\log(k + 1))$ iterations over a range proportional to `k`. Each trailing-zero evaluation uses $O(\log(k + 1))$ divisions by five, for $O(\\log^{2} (k + 1))$ time. Only scalar bounds and counters are stored, using $O(1)$ space.

## Alternatives and edge cases
- **Two lower bounds:** Compute the first `x` with $z(x) \ge k$ and with $z(x) \ge k + 1$; their difference is the preimage size.
- **Base-five characterization:** Missing values can be characterized through the cumulative powers of five, but binary search is simpler and less error-prone.
- **Linear scan:** Increment `x` until `z(x)` reaches `k`; this is correct but takes time proportional to `k`.
- **Zero target:** The five values `0` through `4` form the first complete block.
- **Jump at a multiple of twenty-five:** Extra factors of five can make `z` skip one or more target counts.
- **Search upper bound:** $5k + 5$ is safely beyond the first possible preimage because every block of five contributes at least one zero.
- **Large target:** The arithmetic stays bounded and no factorial is ever constructed.
