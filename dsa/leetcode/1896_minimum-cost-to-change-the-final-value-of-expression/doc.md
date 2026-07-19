# Minimum Cost to Change the Final Value of Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1896 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/) |

## Problem Description

### Goal

A valid Boolean expression contains the literals `0` and `1`, the binary operators `&` and `|`, and properly matched, nonempty parentheses. Parentheses are evaluated first. Outside them, `&` has no precedence over `|`; operators at the same nesting depth are applied strictly from left to right.

One operation may flip a literal between `0` and `1`, or replace either operator with the other. Determine the fewest such operations needed to make the complete expression evaluate to the opposite Boolean value. Parentheses cannot be added, removed, or moved.

### Function Contract

**Inputs**

- `expression`: a valid string of length $N$, where $1 \le N \le 10^5$, containing only `0`, `1`, `&`, `|`, `(`, and `)`. All parentheses are matched and no pair is empty.

**Return value**

Return the minimum number of permitted single-character changes that makes the final value differ from the original expression's value.

### Examples

**Example 1**

- Input: `expression = "1&(0|1)"`
- Output: `1`
- Explanation: Replacing the inner `|` with `&` makes the expression false.

**Example 2**

- Input: `expression = "(0&0)&(0&0&0)"`
- Output: `3`

**Example 3**

- Input: `expression = "(0|(1|0&1))"`
- Output: `1`
- Explanation: Flipping the nested `1` to `0` changes the final result.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Keep both possible outcomes.** For every parsed subexpression, store a pair $(c_0,c_1)$: the minimum cost to make that subexpression evaluate to $0$ and to $1$. A literal `0` starts as $(0,1)$, while `1` starts as $(1,0)`.

When two pairs meet at an operator, consider the four combinations of left and right Boolean values. For each combination, evaluate both the written operator and its flipped form; changing the operator adds one to the cost. Taking the minimum for each resulting Boolean value produces the pair for the combined expression. This constant-size transition accounts for changing operands, changing the operator, or doing both.

**Parse the specified evaluation order.** Scan the string once. The current pair and pending operator describe the active parenthesis level. Because `&` and `|` have equal precedence, combine a new operand immediately with the current pair. On `(`, save the outer state on a stack and start a fresh frame. On `)`, restore the outer frame and treat the completed inner pair as its next operand.

For the complete expression, exactly one entry in the final pair is zero: it corresponds to the unchanged value. Return the other entry, which is the least cost to obtain the opposite value.

#### Complexity detail

Each of the $N$ characters is examined once. A combination checks only two Boolean values for each operand and two possible operators, so it takes constant time. The total time is $O(N)$. Nested parentheses may place $O(N)$ saved frames on the stack, giving $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive parsing:** A recursive descent parser can carry the same two-cost state, but an expression may nest far beyond Python's safe call depth.
- **Re-evaluate after candidate edits:** Trying changes and evaluating the whole expression again repeats work and quickly becomes exponential when the answer needs several edits.
- **Conventional precedence:** Treating `&` as stronger than `|` is incorrect here; unparenthesized operators are evaluated left to right.
- **Operator changes:** The cheapest solution may flip an operator even when neither operand changes, so transitions must include both possible operators.
- **Redundant parentheses:** Extra matched layers around a literal or group do not change its cost pair.
- **Single literal:** With no operator present, flipping the only character always costs exactly one.

</details>
