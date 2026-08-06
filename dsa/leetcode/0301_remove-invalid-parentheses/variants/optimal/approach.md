## General
**First determine the exact removal budget**

Scan from left to right. An opening parenthesis increases the unmatched-open count. A closing parenthesis consumes one
unmatched opening when possible; otherwise it must be removed, so it increases the required closing-removal count.
After the scan, every unmatched opening must also be removed.

These two counts are lower bounds forced by prefix balance and total balance. Removing exactly them is also
sufficient, so backtracking can search only minimum-removal candidates rather than generating valid strings at deeper
deletion levels.

**Backtrack with balance and both remaining budgets**

The candidate's state records position `i`, the current balance, and both remaining budgets. At each parenthesis,
branch between removing it—only when its corresponding budget remains—and keeping it. A kept opening increments the
balance. A closing parenthesis may be kept only when balance is positive, after which it decrements the balance.
Letters have no removal branch and are always appended.

Prune when the `len(s) - i` unprocessed characters cannot satisfy the total remaining removal budget. At the end,
accept only states with zero balance and both budgets exhausted. Store completed strings in a set because removing
identical parentheses at different positions can produce the same text.

For `"()())()"`, the preliminary scan requires one closing removal. Backtracking can remove either of the two closing
parentheses that cause the repeated middle shape, yielding `"(())()"` and `"()()()"`; other removals either violate
prefix balance or retain the extra closing parenthesis.

**The budgets prove minimality; the branches prove completeness**

Every valid result must remove at least the computed number of unmatched closings and openings. Every accepted branch
removes exactly those budgets, so no returned string uses more than the minimum.

Conversely, consider any minimum-removal valid result. At each parenthesis its choice is either keep or remove, and
the backtracking includes that choice while its corresponding budget remains. Validity guarantees that its kept
prefixes never have negative balance, and its final balance is zero, so that branch is never incorrectly pruned and
reaches the result. Deduplication changes multiplicity only, not the set of obtainable strings.

## Complexity detail
Let $p$ be the number of parentheses and $n$ the complete string length. There can be up to $2^p$ keep/remove paths,
and materializing or hashing a completed string costs $O(n)$, giving the conservative output-sensitive bound
$O(2^p \cdot n)$. Removal budgets and balance prune many inputs substantially. The recursion path and character
buffer use $O(n)$ auxiliary space, excluding returned strings.

## Alternatives and edge cases
- **Breadth-first deletion:** is correct and stops at the first valid level, but may retain a large frontier of
  strings.
- **Generate every subsequence and validate afterward:** ignores forced-removal and prefix-balance pruning and repeats
  many equivalent candidates.
- **Letters:** are always retained because only parentheses may be removed.
- **Already valid input:** exhausts both zero budgets and returns itself.
- **Only unmatched parentheses:** may require every symbol to be removed and therefore return the empty string.
