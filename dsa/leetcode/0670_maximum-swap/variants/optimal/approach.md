## General
**Improve the earliest possible digit**

Decimal place value makes the leftmost changed position decisive. If a digit can be replaced by any larger digit occurring to its right, the optimal swap must improve the earliest such position; no later improvement can compensate for leaving a smaller digit there. Scan positions from left to right and stop after making the first beneficial swap.

**Record where each replacement digit last appears**

Store the last index of each digit `0` through `9`. At a position containing digit `d`, test replacement digits from `9` down to $d + 1$. The first digit whose last occurrence lies to the right is the largest possible replacement for this position.

**Why the rightmost equal replacement is best**

When the chosen larger digit occurs more than once, swapping with its rightmost occurrence keeps that larger digit in every earlier suffix position where it already appeared. Moving the original smaller digit as far right as possible therefore maximizes the remaining suffix. The scan first fixes the earliest improvable position, chooses its largest available replacement, and uses the best occurrence of that replacement, so no other single swap can produce a larger number.

## Complexity detail
Let `D` be the number of decimal digits, so $D = O(\log N)$ for positive `N`. Building last-occurrence positions and scanning for the swap each take $O(D)$ time. The mutable digit list uses $O(D)$ space, while the ten-entry position table is constant-sized. For `num = 0`, the representation has one digit and the same bounds apply.

## Alternatives and edge cases
- **Suffix-maximum indices:** precompute the position of the greatest digit in every suffix, then find the first improving swap; it has the same asymptotic bounds but needs another $O(D)$ array.
- **Try every pair of positions:** directly evaluates all legal swaps and is easy to verify, but takes $O(D^2)$ time.
- **Arithmetic digit extraction:** avoids string conversion and can use fixed digit storage, but place-value manipulation makes the greedy choice less transparent.
- An already nonincreasing digit sequence cannot be improved and must be returned unchanged.
- For repeated replacement digits, use the rightmost occurrence; `1993` becomes `9913`, not `9193`.
- Zero and every one-digit number remain unchanged.
