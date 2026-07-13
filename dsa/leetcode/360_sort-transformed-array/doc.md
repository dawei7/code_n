# Sort Transformed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 360 |
| Difficulty | Medium |
| Topics | Array, Math, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-transformed-array/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in ascending order and coefficients $a$, $b$, and $c$, transform every occurrence $x$ with the quadratic function $f(x)=ax^2+bx+c$. Preserve duplicate occurrences even when several inputs produce the same output.

Return all transformed values in ascending order. Use the input order and the parabola's direction to construct the result in linear time rather than transforming and comparison-sorting from scratch. Handle positive, zero, and negative `a`, including the linear-function case. The function returns values only and does not modify their multiplicities or omit points around the quadratic vertex.

### Function Contract
**Inputs**

- `nums`: a nondecreasing list of integers
- `a`: the quadratic coefficient
- `b`: the linear coefficient
- `c`: the constant coefficient

**Return value**

- A nondecreasing list containing `f(x)` for every `x` in `nums`, with multiplicities preserved.

### Examples
**Example 1**

- Input: `nums = [-4,-2,2,4], a = 1, b = 3, c = 5`
- Output: `[3,9,15,33]`

**Example 2**

- Input: `nums = [-4,-2,2,4], a = -1, b = 3, c = 5`
- Output: `[-23,-5,1,7]`

**Example 3**

- Input: `nums = [-4,-2,2,4], a = 0, b = -3, c = 5`
- Output: `[-7,-1,11,17]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use the parabola's shape to locate the next extreme**

A quadratic with $a > 0$ opens upward, so values farthest from its vertex are largest. Over a sorted input interval, the largest remaining transformed value must therefore come from one of the two endpoints. When $a < 0$, the parabola opens downward and the smallest remaining value must be at an endpoint. The linear case $a = 0$ is monotone and is also handled by the upward branch's endpoint comparison.

**Consume endpoints into the correct output direction**

Maintain pointers at both ends of `nums` and transform both pointed values. If $a \ge 0$, place the larger transform into the output from right to left. If $a < 0$, place the smaller transform from left to right. Advance only the pointer whose transform was used, then repeat until the pointers cross.

**Why no interior value can be the required extreme**

On either side of a quadratic's vertex the function is monotone. The remaining input values always form one contiguous sorted interval, and each monotone portion reaches its outward extreme at an interval endpoint. Thus the next largest value for an upward parabola, or next smallest value for a downward parabola, is one of the two candidates examined. Placing that value at the corresponding free output boundary preserves sorted order by induction.

**Trace a convex transform**

For `[-4,-2,2,4]` with $f(x)=x^{2}+3x+5$, the endpoint transforms are `9` and `33`, so `33` fills the last slot and the right pointer moves. Repeating endpoint comparisons fills the array backward as `[3,9,15,33]`.

#### Complexity detail

Each of the `n` input values is transformed a constant number of times and one pointer advances per output placement, giving $O(n)$ time. The returned array uses $O(n)$ space; beyond that output, the pointers and temporary transformed values use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Transform then comparison-sort:** is concise but discards the input order and costs $O(n \log n)$ time.
- **Find the vertex split and merge:** can transform the two monotone sides and merge them in $O(n)$, but requires more boundary bookkeeping.
- **Insert each transform into a sorted list:** can degrade to $O(n^2)$ because insertion shifts existing values.
- When $a = 0$, a positive `b` preserves input order and a negative `b` reverses it; endpoint filling handles both.
- Duplicate inputs or equal endpoint transforms must both be retained.
- A constant function produces `n` copies of `c`.
- Negative coefficients and values require ordinary signed integer arithmetic; comparing transforms avoids computing the vertex as a fraction.

</details>
