## General
**Maintain every still-possible hidden value**

Start with the inclusive interval `[1,n]`. Query its midpoint. If the midpoint is the hidden number, return it. If the response says the hidden value is lower, discard the midpoint and everything above it. If the response says it is higher, discard the midpoint and everything below it.

The offline app adapter performs the same three-way comparison directly against `pick`; the native submission calls LeetCode's oracle.

**Why each response safely removes half**

Before every query, the hidden number lies inside the maintained interval. A “lower” response proves all values at or above the midpoint are impossible, while a “higher” response proves all values at or below it are impossible. The remaining half therefore preserves the hidden value. The interval strictly shrinks on every non-matching query, so it must eventually query and return the unique hidden number.

**Use an overflow-safe midpoint form**

Compute the midpoint as `left + (right - left) // 2`. This is equivalent to averaging the boundaries but avoids overflow in fixed-width languages when `n` is large.

## Complexity detail
Every oracle response discards at least half of the remaining candidates, requiring $O(\log n)$ queries and time. The two boundaries, midpoint, and response use $O(1)$ space.

## Alternatives and edge cases
- **Linear guessing from one upward:** is correct but can require $O(n)$ oracle calls when the pick is near `n`.
- **Random guesses:** do not guarantee logarithmic progress or a bounded worst case comparable to binary search.
- The hidden value may be the first or last number in the range.
- When $n = 1$, the first midpoint is necessarily correct.
- Oracle signs are relative to the guess: negative means the guess is too high, positive means it is too low.
- The app-only `pick` parameter must not appear in the native LeetCode method declaration.
