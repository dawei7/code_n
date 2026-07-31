## General

At processing position `i`, zero-based from the first selected element, the current multiplier is `mul - i`. Because every array value is positive, multiplication is preferable to ordinary addition exactly when this current multiplier is greater than one. If it equals one, the two choices tie; if it is zero or negative, ordinary addition is strictly better. The effective contribution factor at position `i` is therefore `max(1, mul - i)`.

These effective factors never increase. The first

$$
t = \min(k, \texttt{mul} - 1)
$$

positions have factors `mul, mul - 1, ..., mul - t + 1`, all greater than one. Every remaining selected element has effective factor one.

All $k$ factors are positive, so an optimal selection must contain the largest `k` values in `nums`. If a selected value were smaller than an unselected value, replacing the former by the latter at the same processing position would only increase the total.

The selected values should also be processed from largest to smallest. For values $x \ge y$ and factors $a \ge b$, assigning the larger value to the larger factor changes the contribution by

$$
(ax + by) - (ay + bx) = (a-b)(x-y) \ge 0.
$$

Repeated exchanges therefore transform any order into descending value order without reducing the total.

Maintain the largest `k` array values with a size-`k` heap, then arrange those retained values in descending order. Multiply the first `t` selected values by `mul - i` at their positions, then add the remaining selected values unchanged. This realizes both exchange arguments simultaneously and is optimal.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Heap-based top-`k` selection and ordering take $O(n\log(k+1))$ time; the `+1` states the bound uniformly for `k = 1`, whose selection scan is linear. The contribution scan costs $O(k)$ more. The retained values use $O(k)$ auxiliary space.

## Alternatives and edge cases

- **Full descending sort:** Sorting every input value and taking the first `k` gives the same greedy result in $O(n\log n)$ time and $O(n)$ auxiliary space. It is concise but retains and orders values that cannot be selected.
- **Repeatedly extract the current maximum:** This produces the correct value but can take $O(nk)$ time when extraction scans or shifts a list at every step.
- **Multiplier equal to one:** Multiplication and addition tie immediately, so the answer is simply the sum of the largest `k` values.
- **Multiplier becomes nonpositive:** Continue processing until exactly `k` elements have been used, choosing ordinary addition for every factor at most one.
- **More profitable factors than selections:** When `k < mul - 1`, every selected value is multiplied; the factor sequence stops after exactly `k` positions.
- **Duplicate values:** Equal elements at different indices are distinct selections, although swapping equal values does not alter the total.
- **Wide totals:** Values and multipliers can make the answer exceed 32-bit range, so fixed-width implementations need 64-bit arithmetic.
