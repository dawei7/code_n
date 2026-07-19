## General
An invalid parenthesis has one of two causes: a closing parenthesis appears before any unmatched opening parenthesis, or an opening parenthesis remains unmatched after the entire string. These cases can be removed in two directional passes without searching among combinations.

**Discarding closings that can never be matched**

Scan from left to right while tracking the number of unmatched `"("` characters retained so far. Keep every letter and opening parenthesis. Keep a closing parenthesis only when the balance is positive, decrementing the balance when it is kept. If the balance is zero, that `")"` cannot be paired with any earlier opening parenthesis, so every valid subsequence must remove it.

**Removing only the surplus openings**

After the first pass, every retained closing parenthesis has a partner, while `balance` openings may remain unmatched. Scan the retained characters from right to left and skip exactly that many `"("` characters. Choosing them from the right preserves every already matched pair. Reverse the remaining characters to restore their original order.

Every removed parenthesis is provably unusable: the first-pass closings lack an earlier partner, and the second-pass openings lack a later partner. Any valid result must remove all of them, so retaining everything else achieves the minimum number of removals.

## Complexity detail
Each of the $n$ characters is examined a constant number of times, giving $O(n)$ time. The retained character lists and final output occupy $O(n)$ space.

## Alternatives and edge cases
- **Stack of opening indices:** Record each `"("` index and mark unmatched closings plus openings for deletion; this is also $O(n)$ time and space but needs an explicit deletion set or mask.
- **Breadth-first deletion search:** Trying every one-character removal can certify minimum removals, but generates exponentially many strings and is infeasible at the input limit.
- **No parentheses:** The original lowercase string is already valid and must be returned unchanged.
- **Only unmatched parentheses:** Every character is removed, so the valid result is the empty string.
- **Multiple valid answers:** Different unmatched openings may sometimes be removed; any result with minimum removals is accepted.
