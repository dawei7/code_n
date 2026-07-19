# Count Items Matching a Rule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1773 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-items-matching-a-rule/) |

## Problem Description

### Goal

Each row in `items` describes one item as `[type, color, name]`. A rule consists of `ruleKey`, which selects one of those three attributes, and `ruleValue`, which supplies the exact value that attribute must equal.

When `ruleKey` is `"type"`, compare the first field; when it is `"color"`, compare the second; and when it is `"name"`, compare the third. In every case, matching uses exact string equality.

Count and return the items matching the rule. Values in unselected attributes do not affect the result.

### Function Contract

**Inputs**

- `items`: between $1$ and $10^4$ triples `[type, color, name]`.
- `ruleKey`: exactly one of `"type"`, `"color"`, or `"name"`.
- `ruleValue`: the lowercase string required in the selected field.
- Every item attribute and `ruleValue` has length between $1$ and $10$.

Let $n=\lvert\texttt{items}\rvert$.

**Return value**

- Return the number of rows whose field selected by `ruleKey` equals `ruleValue`.

### Examples

**Example 1**

- Input: `items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"`
- Output: `1`
- Explanation: Only the computer has `"silver"` in its color field.

**Example 2**

- Input: `items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"`
- Output: `2`
- Explanation: The computer's name is `"phone"`, but its type is not, so it does not match this rule.

**Example 3**

- Input: `items = [["a","b","c"]], ruleKey = "name", ruleValue = "c"`
- Output: `1`
- Explanation: The selected name field equals the requested value.
