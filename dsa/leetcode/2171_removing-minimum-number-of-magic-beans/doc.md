# Removing Minimum Number of Magic Beans

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2171 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/) |

## Problem Description
### Goal

Each positive integer in `beans` is the number of magic beans in one bag.
From every bag, remove any non-negative number of beans, possibly emptying the
bag completely. Removed beans cannot be placed back into that bag or moved to
another bag.

After the removals, every bag that remains nonempty must contain the same
number of beans. Empty bags do not need to match that amount. Return the
smallest total number of beans that must be removed to meet this condition.

### Function Contract
**Inputs**

- `beans`: an array of $n$ positive integers, where $1\le n\le 10^5$ and each
  count is between $1$ and $10^5$, inclusive.

Only removal is allowed; no bag's count may increase.

**Return value**

Return the minimum total number of beans removed across all bags so that all
remaining nonempty bags have equal counts.

### Examples
**Example 1**

- Input: `beans = [4, 1, 6, 5]`
- Output: `4`

Empty the one-bean bag, reduce `6` to `4`, and reduce `5` to `4`. The nonempty
bags then all hold four beans after four removals.

**Example 2**

- Input: `beans = [2, 10, 3, 2]`
- Output: `7`

Empty the two two-bean bags and the three-bean bag, leaving the ten-bean bag
unchanged.

**Example 3**

- Input: `beans = [5, 5]`
- Output: `0`

The nonempty bags already contain the same amount.
