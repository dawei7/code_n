# Maximum Nesting Depth of the Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1614 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) |

## Problem Description
### Goal
A valid parentheses string may contain digits, arithmetic operators, and matched pairs of parentheses. Its nesting depth at a position is the number of opening parentheses whose matching closing parentheses have not yet appeared.

Given such a valid string `s`, return its maximum nesting depth: the greatest number of parenthesis pairs simultaneously surrounding any position. A string with no parentheses has depth zero, while adjacent parenthesized groups do not add to one another unless one group is inside another.

### Function Contract
**Inputs**

- `s`: a valid parentheses string of length $n$, where $1 \le n \le 100$.
- Every character is a digit, one of `+`, `-`, `*`, or `/`, or a parenthesis.
- The parentheses in `s` are balanced and properly nested.

**Return value**

Return the largest number of open parenthesis pairs present at the same point while scanning `s`.

### Examples
**Example 1**

- Input: `s = "(1+(2*3)+((8)/4))+1"`
- Output: `3`

**Example 2**

- Input: `s = "(1)+((2))+(((3)))"`
- Output: `3`

**Example 3**

- Input: `s = "()(())((()()))"`
- Output: `3`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the currently open pairs.** Scan `s` from left to right with a counter `depth`. An opening parenthesis begins one more enclosing pair, so increment `depth` when `(` is encountered. A closing parenthesis ends the innermost active pair, so decrement `depth` when `)` is encountered. Digits and operators do not affect nesting.

**Record a new maximum after opening.** Immediately after processing `(`, `depth` equals the number of parenthesis pairs that contain the next position. Compare it with `maximum` at that moment. Updating before a later closing parenthesis ensures that even the innermost level of a run such as `((()))` is observed.

The validity guarantee means `depth` never becomes negative and returns to zero after the scan. Every possible nesting level begins at an opening parenthesis, so examining `depth` after every opening observes the global maximum. Conversely, the counter counts only unmatched openings, so no recorded value can exceed the true nesting depth.

#### Complexity detail

The scan examines each of the $n$ characters once, giving $O(n)$ time. The two integer counters use $O(1)$ auxiliary space; no explicit stack is needed because the task asks only for the number of active pairs, not their positions or contents.

#### Alternatives and edge cases

- **Explicit stack:** Pushing each `(` and popping for each `)` also finds the maximum stack size, but it uses $O(n)$ space for information that a counter already captures.
- **Repeated prefix counting:** Counting opens and closes again for every prefix is correct, but rescans characters and takes $O(n^2)$ time.
- A string containing no parentheses has maximum depth zero.
- Adjacent groups such as `()()` each return to depth zero; their depths are not added together.
- A run of opening parentheses may establish the maximum before any digit or operator appears.
- Because `s` is guaranteed valid, the algorithm does not need separate rejection logic for unmatched parentheses.

</details>
