# Different Ways to Add Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 241 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Recursion, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/) |

## Problem Description
### Goal
Given a valid expression containing nonnegative decimal integers and the binary operators `+`, `-`, and `*`, insert parentheses in every possible way that fully determines the order of operations. The input contains no existing parentheses, and multi-digit numbers remain indivisible operands.

Return one integer result for every structurally distinct full parenthesization. Different evaluation structures must be retained even when they produce the same numeric value, so duplicate results are meaningful and must not be removed. Return the results in any order. Apply each operator to the complete result sets of its left and right subexpressions rather than assuming ordinary multiplication precedence.

### Function Contract
**Inputs**

- `expression`: a valid operator-separated arithmetic expression without existing parentheses

**Return value**

A list containing one result for every full parenthesization; duplicate numeric results are retained and order is unrestricted.

### Examples
**Example 1**

- Input: `expression = "2-1-1"`
- Output: `[0,2]`

**Example 2**

- Input: `expression = "2*3-4*5"`
- Output: `[-34,-14,-10,-10,10]`

**Example 3**

- Input: `expression = "11"`
- Output: `[11]`

### Required Complexity

- **Time:** $O(C_n \cdot n)$
- **Space:** $O(C_n \cdot n)$

<details>
<summary>Approach</summary>

#### General

**Every expression tree chooses one final operator**

Every full parenthesization has one root operator. Split at each operator, recursively obtain every left and right result, and combine their Cartesian product using that operator.

For `2*3-4*5`, choosing the subtraction as the root combines every interpretation of `2*3` with every interpretation of `4*5`. Choosing either multiplication instead covers the trees whose final operation is that multiplication. No precedence rule is imposed because the parenthesization itself determines evaluation order.

**Cache the complete multiset for each interval**

Different split choices request the same subexpressions repeatedly. Cache the complete result list for each substring so its parenthesizations are generated once.

The cached value must remain a list rather than a set. Distinct parenthesizations may evaluate to the same integer, and the output requires one entry for each structure. A substring containing no operator is the base case and contributes its parsed integer once.

**Root decomposition generates every parenthesization exactly once**

For any cached interval, consider a complete parenthesization tree. Its root is one specific operator in that interval; its left and right children are complete parenthesizations of the corresponding two substrings. The recursion reaches that split, and the Cartesian product includes exactly that child pair.

Conversely, selecting an operator and one valid result structure from each side creates a valid full parenthesization with that operator as its unique root. Different root splits or child structures represent different trees, so the generated multiset is neither missing structures nor inventing invalid ones.

#### Complexity detail

With `n` operators there are Catalan-number `C_n` output structures, each requiring combination work across its tree, giving output-sensitive $O(C_n \cdot n)$ time and stored results of the same order.

#### Alternatives and edge cases

- **Recursion without memoization:** recomputes identical substrings.
- **Precedence evaluation:** produces only one interpretation, not all trees.
- A number-only expression has one result; multi-digit numbers and duplicate results must be preserved.

</details>
