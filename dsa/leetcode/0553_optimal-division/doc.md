# Optimal Division

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 553 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/optimal-division/) |

## Problem Description
### Goal
Given an array of positive integers `nums`, insert division operators between every adjacent pair while keeping all values in their original order. Add parentheses wherever needed to choose the evaluation grouping; division uses the represented numerical expression rather than integer truncation.

Return an expression whose value is as large as possible. The string must use every number exactly once and contain no redundant parentheses. For one number, return that number alone; for two numbers, simple division needs no parentheses. When more values are present, grouping denominators differently can change the result even though operand order cannot change.

### Function Contract
**Inputs**

- `nums`: a non-empty list of positive integers

**Return value**

- A string representing a maximum-value division expression

### Examples
**Example 1**

- Input: `nums = [1000, 100, 10, 2]`
- Output: `"1000/(100/10/2)"`

**Example 2**

- Input: `nums = [2]`
- Output: `"2"`

**Example 3**

- Input: `nums = [2, 3]`
- Output: `"2/3"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep the first number in the numerator**

Every complete expression splits as `nums[0] / denominator` because the original order cannot change. With positive values, maximizing the result is therefore equivalent to minimizing the value represented by all remaining numbers.

**Make every later number multiply against the first divisor**

For at least three numbers, write the denominator as `nums[1] / nums[2] / ... / nums[n - 1]`. Division is evaluated left to right inside the parentheses, so this denominator equals `nums[1] / (nums[2] * ... * nums[n - 1])`. Dividing the first number by it places every value after `nums[1]` effectively in the outer numerator.

**Use parentheses only when they change grouping**

One number needs no operator. Two numbers have only one possible division and need no parentheses. With three or more numbers, wrap the entire tail once so it becomes the denominator of the first value; no inner parentheses are necessary.

**Why no other grouping can produce a larger value**

In any division expression over positive ordered values, `nums[1]` must remain in the denominator of `nums[0]`. Each later value can affect the result either as an effective numerator factor or as an effective denominator factor, depending on nesting. The proposed grouping makes every one of those later positive values a numerator factor. Moving any such value to a denominator cannot increase the result because every input is at least one. Thus the single wrapped tail attains the maximum.

#### Complexity detail

Converting and joining the `n` values writes each output token once, taking $O(n)$ time in the number-of-values model. The returned expression contains $O(n)$ tokens and therefore uses $O(n)$ space.

#### Alternatives and edge cases

- **Interval dynamic programming:** can track minimum and maximum values for every subarray in $O(n^3)$ time and $O(n^2)$ space, but positivity makes that machinery unnecessary.
- **Enumerate all parenthesizations:** eventually finds an optimum but explores a Catalan number of expressions.
- **One value:** return the number alone.
- **Two values:** return their direct quotient without parentheses.
- **Three or more values:** exactly one pair of parentheses around the complete tail is sufficient.
- **Values equal to one:** may create several numerically tied expressions; the direct form remains optimal and follows the required nonredundant format.
- **Original order:** numbers may not be rearranged even when another ordering would produce a larger quotient.

</details>
