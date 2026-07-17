# Goal Parser Interpretation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1678 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/goal-parser-interpretation/) |

## Problem Description
### Goal

A Goal Parser receives a command formed by concatenating tokens from the fixed alphabet `"G"`, `"()"`, and `"(al)"`. The input is guaranteed to be a valid sequence of those complete tokens, so parentheses never appear in any other form and no validation or error recovery is required.

Interpret each `"G"` as `"G"`, each `"()"` as `"o"`, and each `"(al)"` as `"al"`. Concatenate the decoded pieces in the same order in which their tokens occur and return the resulting string. Token boundaries matter only while reading the command; they do not appear in the output.

### Function Contract
**Inputs**

- `command`: a string of length $n$ formed by concatenating one or more valid tokens from `"G"`, `"()"`, and `"(al)"`

**Return value**

The string obtained by decoding every token in order.

### Examples
**Example 1**

- Input: `command = "G()(al)"`
- Output: `"Goal"`

**Example 2**

- Input: `command = "G()()()()(al)"`
- Output: `"Gooooal"`

**Example 3**

- Input: `command = "(al)G(al)()()G"`
- Output: `"alGalooG"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The next character identifies the token family**

Scan `command` from left to right with an index. If the current character is `G`, the next token is unambiguously `"G"`; append `"G"` and advance one position. Otherwise the current character is an opening parenthesis. The validity guarantee leaves only `"()"` and `"(al)"`.

**One lookahead separates the parenthesized tokens**

Inspect the character immediately after `(`. A closing parenthesis identifies `"()"`, so append `"o"` and advance two positions. Otherwise the only legal possibility is `"(al)"`; append `"al"` and advance four positions. No substring search or backtracking is necessary.

After each iteration, the accumulated pieces are exactly the interpretation of the consumed prefix, and the index points to the first character of the next complete token. Each branch appends that token's prescribed interpretation and skips exactly its source length, preserving this property. Because the command is a concatenation of valid tokens, the index eventually reaches its length without entering the middle of a token. Joining the pieces therefore yields precisely the full interpretation in original order.

#### Complexity detail

Every input character belongs to one token and is skipped once, giving $O(n)$ scanning time. The decoded pieces and final string contain $O(n)$ characters, so the explicit output-building storage is $O(n)$.

#### Alternatives and edge cases

- **Two global replacements:** replacing `"()"` with `"o"` and `"(al)"` with `"al"` is concise and remains $O(n)$ because the token dictionary has constant size, though it hides the parser's token-boundary reasoning.
- **Repeated prefix removal:** decoding the first token and slicing it from the remaining string is correct, but repeated copying can take $O(n^2)$ time.
- **Only one token kind:** commands made entirely of `"G"`, `"()"`, or `"(al)"` require the same branch on every iteration and must still preserve multiplicity.
- **Adjacent parenthesized tokens:** the closing parenthesis of one token must not be confused with any part of the next token.
- **Minimum command:** each of the three token forms is independently valid when it is the entire input.

</details>
