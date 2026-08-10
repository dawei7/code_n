## General

Every zero must be replaced by a strictly positive integer, so its smallest contribution is $1$. For an array `nums`,

`sum(nums) + nums.count(0)`

is its minimum attainable sum: existing positive values stay fixed, and every zero becomes one.

Call the two minima $s_1$ and $s_2$. An array containing a zero can attain every integer at or above its minimum. Set all zeros to one, then add any desired extra amount to one replacement. An array without zeros is fixed and can attain only its current sum.

The problem is therefore determined by two lower bounds and whether the lower-sum side is adjustable.

**Normalize the order of the minima**

If `s1 > s2`, the source recursively calls the method with the arrays swapped. The problem is symmetric, so exchanging their names preserves the answer. In the swapped call the minima satisfy `s1 <= s2`, which prevents another swap; recursion depth is at most two calls.

This normalization lets the remaining branches analyze only equality or a strictly smaller first minimum.

**Equal minima give the optimum immediately**

If `s1 == s2`, replace every zero in both arrays by one. Both sums equal the shared minimum. No smaller common sum can exist because neither array can fall below its minimum, so returning `s1` is optimal.

**Raise the smaller side when the minima differ**

After normalization, the remaining case is `s1 < s2`. The second array reaches $s_2$ by replacing every zero with one. To match it, the first array must gain $s_2-s_1$.

If the first array has a zero, make one replacement

$$
1+(s_2-s_1)
$$

and replace its other zeros with one. Its sum becomes $s_2$. This common sum is minimal because any equality must be at least the larger lower bound $s_2$.

If the first array has no zero, it is permanently fixed at $s_1$. It cannot rise, and the other array cannot fall below $s_2$. Equality is impossible, so the method returns `-1`.

This yields the exact final expression:

`return -1 if nums1.count(0) == 0 else s2`.

**Why flexibility on the larger side does not matter**

The larger-minimum array already attains $s_2$ at its cheapest replacements. Only the smaller side must close a gap. If that side is fixed, choosing a target above $s_2$ cannot help because the fixed sum cannot increase at all. If it is adjustable, matching exactly $s_2$ is already best.

For `[2,0,2,0]` and `[1,4]`, the minima are $6$ and $5$. The recursive swap places the fixed array first with $5<6$. It contains no zero, so the answer is `-1`.

For `[3,2,0,1,0]` and `[6,5,0]`, minima are $8$ and $12$. The first side has zeros and can absorb the gap of four, producing the minimum common sum $12$.

## Complexity detail

Let $n$ and $m$ be the lengths. Each call runs `sum` and `count` on both arrays, and the final branch may count the normalized first array's zeros again. These are linear scans.

At most one swapped call occurs, so total time remains $O(n+m)$ despite the constant repeated scans. Recursion depth is bounded by two calls and only scalar values are stored, giving $O(1)$ auxiliary space.

The arrays are not modified and actual replacement values are not constructed because only the minimum sum is requested.

## Alternatives and edge cases

- **Simulate replacement choices:** Replacements are unbounded positive integers, so explicit search is unnecessary. A minimum and an adjustability flag describe all attainable totals.
- **Both arrays contain zeros:** Both can rise above their minima, making `max(s1, s2)` always attainable.
- **Neither contains a zero:** Both sums are fixed; equality is possible only if they already match.
- **Only the lower-minimum side has a zero:** It can rise to the larger minimum, producing the optimal result.
- **Only the larger-minimum side has a zero:** The lower fixed side cannot rise and the larger side cannot fall, so equality is impossible.
- **Several zeros:** One zero can absorb the entire gap while all remaining zeros become one.
- **All zeros:** An array of length $q$ has minimum $q$ and can attain every integer at least $q$.
- **Strict positivity:** Replacing a zero by zero is forbidden. Adding the zero count enforces the correct lower bound.
- **Recursive swap:** It does not mutate inputs and terminates after one swap because it reverses a strict inequality.
- **Repeated scans:** Saving zero counts could improve constants, but the exact `count(0)` calls remain linear overall.
- **Gap absorbed by one replacement:** There is no upper bound on the positive integer replacing a zero, so a gap of any legal size can be assigned to one position. No divisibility or distribution restriction exists.
- **Minimum proof:** Returning the larger lower bound is not merely feasible when the smaller side is adjustable; every common total below it is impossible for the larger-minimum array.
- **Large sums:** Python integers avoid overflow when arrays contain many values near $10^6$.
