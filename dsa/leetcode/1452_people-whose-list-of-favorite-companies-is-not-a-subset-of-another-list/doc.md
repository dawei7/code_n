# People Whose List of Favorite Companies Is Not a Subset of Another List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1452 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/).

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

## Solution
### Approach
Set containment checks. Convert each list to a set, then compare each set against all others with larger or equal size.

### Complexity Analysis
- **Time Complexity**: `O(n^2 * c)` where `c` is the average company-list size.
- **Space Complexity**: `O(nc)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(favorite_companies):
    sets = []
    for companies in favorite_companies:
        if isinstance(companies, list):
            sets.append(set(companies))
        else:
            sets.append({companies})
    result = []
    for index, companies in enumerate(sets):
        if not any(index != other and companies <= other_companies for other, other_companies in enumerate(sets)):
            result.append(index)
    return result
```
</details>
