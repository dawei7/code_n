# Removing Minimum Number of Magic Beans

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2171 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [removing-minimum-number-of-magic-beans](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/).

### Goal
Remove the fewest beans so every nonempty bag contains the same number. Any number of beans may be removed from a bag, including all of them.

### Function Contract
**Inputs**

- `beans`: positive bean counts for the bags.

**Return value**

The minimum total number of beans to remove.

### Examples
**Example 1**

- Input: `beans = [4, 1, 6, 5]`
- Output: `4`

**Example 2**

- Input: `beans = [2, 10, 3, 2]`
- Output: `7`

**Example 3**

- Input: `beans = [5, 5]`
- Output: `0`

---

## Solution
### Approach
Sort the bag counts. If sorted value `beans[i]` is chosen as the common nonzero amount, bags before `i` must be emptied and every bag from `i` onward can retain exactly that amount. Thus the retained total is `beans[i] * (n - i)`. Maximize retained beans and subtract from the original total.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
