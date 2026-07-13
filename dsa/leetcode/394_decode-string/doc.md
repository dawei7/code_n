# Decode String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 394 |
| Difficulty | Medium |
| Topics | String, Stack, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-string/) |

## Problem Description
### Goal
Given a valid encoded string, each construct `k[encoded]` represents the bracketed substring repeated exactly positive integer `k` times. Encoded regions may nest, and decimal repeat counts may contain several digits; letters outside brackets appear once in their original order.

Return the fully expanded lowercase string. Inner bracketed expressions must be decoded before their enclosing repetition is applied, and neighboring literal or repeated pieces concatenate. Digits serve only as repeat counts under the grammar, brackets are balanced, and no extra separators appear in the output. Consume the complete input rather than decoding only its first top-level component.

### Function Contract
**Inputs**

- `s`: a valid encoding containing lowercase letters, positive decimal repeat counts, and balanced square brackets

**Return value**

- Return the fully expanded lowercase string.

### Examples
**Example 1**

- Input: `s = "3[a]2[bc]"`
- Output: `"aaabcbc"`

**Example 2**

- Input: `s = "3[a2[c]]"`
- Output: `"accaccacc"`

**Example 3**

- Input: `s = "2[abc]3[cd]ef"`
- Output: `"abcabccdcdcdef"`

### Required Complexity

- **Time:** $O(n + m)$
- **Space:** $O(n + m)$

<details>
<summary>Approach</summary>

#### General

**Accumulate a possibly multi-digit repeat count**

While reading digits, update `repeat = repeat * 10 + digit`. The following opening bracket consumes that complete count, so push it together with the chunks belonging to the enclosing level.

**Give each open bracket its own chunk list**

After a push, start an empty chunk list for the bracketed substring. Plain letters are appended as chunks rather than repeatedly concatenated into an immutable string. The stack therefore stores exactly the unfinished outer contexts needed when nested groups close.

**Collapse one completed group at a closing bracket**

Join the current chunks once, multiply that substring by its saved repeat count, restore the parent's chunk list, and append the expanded group as one chunk. Nested groups are already decoded before their parent closes, matching the inside-out meaning of the grammar.

**Why the stack produces the specified expansion**

For every open group, its chunk list contains the decoded concatenation of all tokens read inside it. Letters are correct base tokens, and closing a nested group appends exactly its required repetition. By induction over closing brackets, each completed group is decoded correctly; the final join concatenates the complete top-level sequence in source order.

#### Complexity detail

Let `n` be the encoded input length and `m` the decoded output length. Parsing visits `n` characters, and joining or repeating chunks materializes output characters for $O(n + m)$ total work under the bounded valid encoding. Stack contexts, chunks, and the required decoded result occupy $O(n + m)$ space.

#### Alternatives and edge cases

- **Recursive descent with a shared index:** follows the grammar naturally and has the same output-sensitive work, using call-stack depth proportional to nesting.
- **Store individual characters on one stack:** is easy to implement but may repeatedly reverse or rebuild groups at closing brackets.
- **Append through full-string rebuilding:** preserves correctness but can copy a growing decoded prefix repeatedly and take $O(m^2)$ time.
- Repeat counts can contain more than one digit.
- A group may contain nested groups and plain-letter prefixes or suffixes.
- Several encoded groups may be adjacent at the same level.
- Letters outside brackets remain once in their original positions.

</details>
