# Remove Invalid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 301 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/) |

## Problem Description
### Goal
Given a string containing letters and parentheses, delete some parenthesis characters so every opening parenthesis in the result has a later matching close and no prefix contains more closes than opens. Non-parenthesis characters cannot be removed or reordered.

Use the minimum possible number of deletions, then return every unique valid string obtainable with exactly that minimum. Return the answer in any order, and do not repeat text produced by different deletion choices. The empty string is a valid parenthesis structure when all parentheses must be removed, while an already valid input should be returned unchanged as the sole result.

### Function Contract
**Inputs**

- `s`: a string containing letters and parentheses

**Return value**

A list of all distinct valid strings obtainable with the minimum number of removals, in any order.

### Examples
**Example 1**

- Input: `s = "()())()"`
- Output: `["(())()", "()()()"]`

**Example 2**

- Input: `s = "(a)())()"`
- Output: `["(a())()", "(a)()()"]`

**Example 3**

- Input: `s = ")("`
- Output: `[""]`

### Required Complexity

- **Time:** $O(2^p \cdot n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**First determine the exact removal budget**

Scan from left to right. An opening parenthesis increases the unmatched-open count. A closing parenthesis consumes one unmatched opening when possible; otherwise it must be removed, so it increases the required closing-removal count. After the scan, every unmatched opening must also be removed.

These two counts are lower bounds forced by prefix balance and total balance. Removing exactly them is also sufficient, so backtracking can search only minimum-removal candidates rather than generating valid strings at deeper deletion levels.

**Backtrack with balance and both remaining budgets**

At each parenthesis, branch between removing it—only when its corresponding budget remains—and keeping it. A kept opening increments the balance. A closing parenthesis may be kept only when balance is positive, after which it decrements the balance. Letters have no removal branch and are always appended.

Prune a state when the unprocessed suffix is shorter than the total remaining removal budget. At the end, accept only states with zero balance and both budgets exhausted. Store completed strings in a set because removing identical parentheses at different indices can produce the same text.

For `"()())()"`, the preliminary scan requires one closing removal. Backtracking can remove either of the two closing parentheses that cause the repeated middle shape, yielding `"(())()"` and `"()()()"`; other removals either violate prefix balance or retain the extra closing parenthesis.

**The budgets prove minimality; the branches prove completeness**

Every valid result must remove at least the computed number of unmatched closings and openings. Every accepted branch removes exactly those budgets, so no returned string uses more than the minimum.

Conversely, consider any minimum-removal valid result. At each parenthesis its choice is either keep or remove, and the backtracking includes that choice while its corresponding budget remains. Validity guarantees that its kept prefixes never have negative balance, and its final balance is zero, so that branch is never incorrectly pruned and reaches the result. Deduplication changes multiplicity only, not the set of obtainable strings.

#### Complexity detail

With `p` parentheses there can be up to $2^{p}$ keep/remove decision paths, and materializing or hashing a completed length-`n` string costs $O(n)$, giving the conservative output-sensitive bound $O(2^p \cdot n)$. Removal budgets and balance prune many inputs substantially. The recursion path and character buffer use $O(n)$ auxiliary space, excluding returned strings.

#### Alternatives and edge cases

- **Breadth-first deletion:** is correct and stops at the first valid level, but may retain a large frontier of strings.
- **Generate every subsequence and validate afterward:** ignores forced-removal and prefix-balance pruning and repeats many equivalent candidates.
- Letters are never removed. An already valid string returns itself; a string containing only unmatched parentheses may return the empty string.

</details>
