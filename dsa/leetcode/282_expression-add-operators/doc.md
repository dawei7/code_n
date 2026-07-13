# Expression Add Operators

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 282 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/expression-add-operators/) |

## Problem Description
### Goal
Given a string of decimal digits `num` and an integer `target`, insert any of the binary operators `+`, `-`, and `*` between selected adjacent digits. Digits that are not separated form one multi-digit operand, and their original order may not change.

Return every distinct valid expression whose standard arithmetic value equals `target`, in any order. Multiplication has its usual precedence over addition and subtraction. An operand may be exactly `0`, but no multi-digit operand may begin with zero. Operators cannot be placed before the first digit, after the last digit, or twice without an operand between them; use every input digit exactly once.

### Function Contract
**Inputs**

- `num`: a decimal digit string
- `target`: the desired integer value

**Return value**

All valid expressions reaching the target, in any order; operands may not contain leading zeros.

### Examples
**Example 1**

- Input: `num = "123", target = 6`
- Output: `["1+2+3","1*2*3"]`

**Example 2**

- Input: `num = "232", target = 8`
- Output: `["2+3*2","2*3+2"]`

**Example 3**

- Input: `num = "105", target = 5`
- Output: `["1*0+5","10-5"]`

### Required Complexity

- **Time:** $O(4^n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Operand boundaries and operators form the search tree**

At each digit position, try every following substring as the next operand, stopping after a leading zero. The first operand has no operator; later operands branch over addition, subtraction, and multiplication.

**Carry the final additive term to enforce precedence**

Track the expression's current value and the most recent signed operand. Addition and subtraction update both directly. Multiplication replaces the last operand inside the total with `last * current`, which enforces multiplication precedence without reparsing.

At every recursion state, `value` equals the displayed expression's arithmetic value and `last` is its final additive term. The expression uses exactly the consumed digit prefix with valid operand formatting.

For multiplication, if the current expression value is `value = prefix + last`, replacing the final term gives `prefix + last * operand`, computed as `value - last + last * operand`. This handles chains such as `2+3*4*5` without reparsing or storing an operator stack.

**Every valid expression follows one recursion path**

An expression uniquely determines where each operand ends and which operator follows it, so exhaustive branching reaches it exactly once. The carried state evaluates every branch with normal precedence, and only branches that consume all digits and equal the target are emitted. Stopping a multi-digit operand after an initial zero removes exactly the syntactically invalid choices.

#### Complexity detail

Each gap can continue the current operand or introduce one of three operators, producing $O(4^n)$ search states. The recursion path and expression builder use $O(n)$ auxiliary space, excluding output.

#### Alternatives and edge cases

- **Generate strings then call `eval`:** repeatedly reparses expressions and complicates safe validation.
- Zero may be a standalone operand, but `05` is invalid; multiplication by zero still requires retaining the previous additive term correctly.

</details>
