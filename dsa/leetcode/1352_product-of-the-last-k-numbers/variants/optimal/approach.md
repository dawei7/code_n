## General
**Store prefix products after the latest zero.** Keep a list beginning with the sentinel product `1`. For a nonzero addition, append the previous prefix product multiplied by the new number. If the current zero-free segment has values $x_1,\ldots,x_a$, the list stores $1,x_1,x_1x_2,\ldots,x_1\cdots x_a$.

**Reset at zero.** When zero is added, replace the list with just `[1]`. The list length minus one is therefore exactly the number of consecutive nonzero values after the most recent zero.

For `getProduct(k)`, if $k$ is at least the current list length, the requested suffix crosses the latest zero and its product is zero. Otherwise, divide the full segment prefix by the prefix immediately before the requested suffix: `prefix[-1] // prefix[-1 - k]`. All stored factors are integers and the denominator is an exact factor of the numerator, so this quotient is precisely the suffix product.

## Complexity detail
Each `add` and `getProduct` performs a constant number of list and arithmetic operations in the standard unit-cost model, so $q$ operations take $O(q)$ time. At most one prefix product is stored per addition after the latest zero, bounded by $O(q)$ space.

## Alternatives and edge cases
- **Store raw values:** Appending is constant time, but multiplying the last $k$ values makes a query $O(k)$ and repeated growing queries quadratic overall.
- **Keep every historical prefix across zeroes:** Division cannot recover a suffix that crosses a zero, so zero positions still need special handling; resetting makes that boundary explicit.
- **Query crosses a zero:** The prefix-list length detects this immediately and the answer is zero.
- **Consecutive zeroes:** Each zero simply resets the same sentinel state.
- **Product of one value:** Dividing adjacent prefixes returns the latest number.
