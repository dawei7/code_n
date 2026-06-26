# People Whose List of Favorite Companies Is Not a Subset of Another List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1452 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) |

## Problem Description & Examples
### Goal
Return the indices of people whose favorite-company list is not a subset of any other person's list.

### Function Contract
**Inputs**

- `favoriteCompanies`: a list where each entry is one person's favorite companies.

**Return value**

The qualifying indices in increasing order.

### Examples
**Example 1**

- Input: `favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]`
- Output: `[0,1,4]`

**Example 2**

- Input: `favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]`
- Output: `[0,1]`

**Example 3**

- Input: `favoriteCompanies = [["a"],["a"],["a","b"]]`
- Output: `[2]`

---

## Underlying Base Algorithm(s)
Set containment checks. Convert each list to a set, then compare each set against all others with larger or equal size.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 * c)` where `c` is the average company-list size.
- **Space Complexity**: `O(nc)`
