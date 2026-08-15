# Create Object from Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2794 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [2794. Create Object from Two Arrays](https://leetcode.com/problems/create-object-from-two-arrays/) |

## Problem Description

### Goal

Build a new JavaScript object from two parallel arrays, `keysArr` and `valuesArr`. For every index $i$, the element `keysArr[i]` proposes the property whose value is `valuesArr[i]`.

Convert each proposed key by calling `String()`. When multiple input elements convert to the same property name, keep only the pair at the earliest index and ignore every later collision. The result must therefore preserve the first value associated with each converted key, including names that already have special meaning on ordinary JavaScript objects.

The two arrays always have equal length. Empty arrays produce an empty object.

### Function Contract

**Inputs**

- `keysArr`: A valid JSON array containing the proposed property keys.
- `valuesArr`: A valid JSON array of equal length containing the corresponding property values.

Let $n = \texttt{keysArr.length}$. Each array's JSON serialization has length between $2$ and $5 \cdot 10^5$, inclusive.

**Return value**

Return a new object containing one own enumerable property for each distinct value of `String(keysArr[i])`. Its value must come from that converted key's first occurrence.

### Examples

#### Example 1

- **Input:** `keysArr = ["a", "b", "c"], valuesArr = [1, 2, 3]`
- **Output:** `{"a": 1, "b": 2, "c": 3}`
- **Explanation:** Every converted key is distinct, so all three pairs are retained.

#### Example 2

- **Input:** `keysArr = ["1", 1, false], valuesArr = [4, 5, 6]`
- **Output:** `{"1": 4, "false": 6}`
- **Explanation:** Both of the first two keys convert to `"1"`; the earlier value `4` wins.

#### Example 3

- **Input:** `keysArr = [], valuesArr = []`
- **Output:** `{}`
- **Explanation:** There are no pairs from which to create a property.
