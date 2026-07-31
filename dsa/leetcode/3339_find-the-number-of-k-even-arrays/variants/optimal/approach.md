## General

Only the parity of two neighboring values determines whether their expression is even. Modulo two, subtraction and addition are identical, so

$$
xy-x-y \equiv xy+x+y \pmod 2.
$$

Checking the four parity combinations shows that this value is even only when both $x$ and $y$ are even. Every other combination is odd. The range `[1,m]` contains $\lfloor m/2\rfloor$ even values and $\lceil m/2\rceil$ odd values, so individual values can be aggregated into these two multiplicities.

Maintain two arrays. `end_even[j]` counts prefixes with exactly $j$ qualifying adjacent pairs whose last value is even, and `end_odd[j]` counts those ending in an odd value. For the first position, initialize index zero with the number of choices of the corresponding parity.

When appending an odd value, the new adjacent pair never qualifies, regardless of the previous parity:

`next_odd[j] = (end_even[j] + end_odd[j]) * odd_values`.

When appending an even value, a prefix ending odd keeps the same count, while a prefix ending even creates one new qualifying pair:

`next_even[j] = end_odd[j] * even_values + end_even[j - 1] * even_values`.

The second term is omitted when $j=0$. Use fresh arrays for every position and reduce all counts modulo $10^9+7$. After `n` positions, add the two states at index `k`.

Initially the states enumerate every one-element array, all with zero adjacent pairs. Each transition appends every legal next value exactly once, updates the qualifying-pair count according to the complete parity analysis, and records the new last parity. Induction therefore shows that the final states partition all length-`n` arrays by the exact required count and last parity.

## Complexity detail

There are $n-1$ extension steps and $k+1$ count states for each of two parities. The time complexity is $O(nk)$. Four arrays of length $k+1$ are used across the current and next layers, giving $O(k)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all arrays:** Trying all $m^n$ value sequences is infeasible even at moderate constraints.
- **Track the exact last value:** Values of equal parity have identical transition behavior; retaining all $m$ possibilities wastes a factor of $m$.
- **Two-dimensional position table:** Storing every completed layer uses $O(nk)$ space even though only the previous layer is needed.
- **Length one:** There are no adjacent positions, so all $m$ arrays qualify when `k = 0`.
- **`m = 1`:** Every value is odd, hence no adjacent pair can qualify.
- **`k = n - 1`:** Every value must be even, producing $\lfloor m/2\rfloor^n$ arrays.
- **Odd `m`:** There is one more odd choice than even choices; using `m // 2` for both parities is incorrect.
- **Exact count:** Prefixes that already exceed `k` never need to be stored because future extensions cannot decrease the count.
