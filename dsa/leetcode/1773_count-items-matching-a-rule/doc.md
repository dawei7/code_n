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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate the rule key into one column**

The item schema fixes type at index `0`, color at index `1`, and name at index `2`. Map `ruleKey` to that index once before scanning instead of checking the key separately for every row.

**Inspect exactly the selected attribute**

For each item, compare `item[field_index]` with `ruleValue` using exact string equality. Add one to the count when they match. The other two fields are deliberately ignored, so a requested value appearing in the wrong attribute cannot cause a false match.

**Accumulate one complete count**

Each row is visited once and contributes either zero or one according to the rule's definition. The fixed mapping selects the contractually correct field, so the final sum includes every matching item and no nonmatching item.

#### Complexity detail

The scan performs one constant-time field access and bounded-length string comparison for each of the $n$ items, giving $O(n)$ time. Apart from the returned integer, the field index and running count use $O(1)$ space.

#### Alternatives and edge cases

- **Branch on `ruleKey` inside the loop:** This is correct but repeats the same three-way decision for every item.
- **Build dictionaries for every item:** Named fields may improve readability, but allocating transformed rows adds unnecessary $O(n)$ space.
- **Value in the wrong field:** A name equal to `ruleValue` does not match a type rule.
- **No matches:** The accumulator remains zero.
- **Every item matches:** The result equals the number of item rows.
- **Repeated identical rows:** Each row is a separate item and contributes independently.
- **Exact string comparison:** Prefixes, substrings, and different attribute values do not match.
- **Single item:** The same field mapping and comparison apply without a special case.

</details>
