## Description

You are given an array `items`, where each $\text{items}[i] = [\text{type}_{i}, \text{color}_{i}, \text{name}_{i}]$ describes the type, color, and name of the $$i^{\text{th}}$$ item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The $$i^{\text{th}}$$ item is said to match the rule if **one** of the following is true:

- $ruleKey = "type"$ and $ruleValue = \text{type}_{i}$.

- $ruleKey = "color"$ and $ruleValue = \text{color}_{i}$.

- $ruleKey = "name"$ and $ruleValue = \text{name}_{i}$.

Return *the number of items that match the given rule*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"$
- **Output:** `1`
- **Explanation:** There is only one item matching the given rule, which is ["computer","silver","lenovo"].
#### Example 2

- **Input:** $items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"$
- **Output:** `2`
- **Explanation:** There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
### Constraints

- $1 \le \text{items.length} \le 10^{4}$

- $1 \le \text{type}_{i}.length, \text{color}_{i}.length, \text{name}_{i}.length, \text{ruleValue.length} \le 10$

- `ruleKey` is equal to either `"type"`, `"color"`, or `"name"`.

- All strings consist only of lowercase letters.