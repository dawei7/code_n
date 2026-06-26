# Count Items Matching a Rule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1773 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [count-items-matching-a-rule](https://leetcode.com/problems/count-items-matching-a-rule/) |

## Problem Description & Examples
### Goal
Each item has a type, color, and name. Count how many items match a rule on one of those fields.

### Function Contract
**Inputs**

- `items`: a list of `[type, color, name]` triples.
- `ruleKey`: one of `"type"`, `"color"`, or `"name"`.
- `ruleValue`: the value that must match.

**Return value**

Return the number of items whose selected field equals `ruleValue`.

### Examples
**Example 1**

- Input: `items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"`
- Output: `1`

**Example 2**

- Input: `items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"`
- Output: `2`

**Example 3**

- Input: `items = [["a","b","c"]], ruleKey = "name", ruleValue = "c"`
- Output: `1`

---

## Underlying Base Algorithm(s)
Map the rule key to its column index: type `0`, color `1`, name `2`. Scan all items and count rows where that column equals the requested value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
