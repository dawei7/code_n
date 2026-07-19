# People Whose List of Favorite Companies Is Not a Subset of Another List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1452 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) |

## Problem Description
### Goal

`favoriteCompanies[i]` lists the favorite companies of person $i$, where
people are indexed from zero. A person should be excluded when every company
in that person's list also appears in some other person's list—that is, when
their list is a subset of another list.

Return the indices of exactly those people whose favorite-company list is not
a subset of any other person's list. The indices must appear in increasing
order. Company order inside an input list has no semantic meaning.

### Function Contract
**Inputs**

- `favoriteCompanies`: a list containing $P$ favorite-company lists, with
  $1 \le P \le 100$.
- Each person's list contains between $1$ and $500$ distinct company names.
- Every company name contains between $1$ and $20$ lowercase English letters.
- All favorite-company lists are distinct as sets, even if their input orders
  differ.

Let $C$ be the maximum number of companies in one person's list.

**Return value**

Return the qualifying person indices in increasing order. Index $i$ qualifies
exactly when there is no $j\ne i$ for which every company in
`favoriteCompanies[i]` belongs to `favoriteCompanies[j]`.

### Examples
**Example 1**

- Input: `favoriteCompanies = [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]`
- Output: `[0, 1, 4]`
- Explanation: Lists at indices `2` and `3` are contained in larger lists;
  the other three are not contained in any person's list.

**Example 2**

- Input: `favoriteCompanies = [["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]`
- Output: `[0, 1]`

**Example 3**

- Input: `favoriteCompanies = [["leetcode"], ["google"], ["facebook"], ["amazon"]]`
- Output: `[0, 1, 2, 3]`
- Explanation: The four distinct singleton sets are mutually disjoint, so none
  is a subset of another.
