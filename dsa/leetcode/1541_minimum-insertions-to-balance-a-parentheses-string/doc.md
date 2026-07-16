# Minimum Insertions to Balance a Parentheses String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1541 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) |

## Problem Description
### Goal
You are given a nonempty string containing only `(` and `)`. Under this problem's balancing rule, every opening parenthesis must be matched by two consecutive closing parentheses `))`, and the opening parenthesis must occur before its matching pair. Thus `(` acts as one opening token while `))` acts as one closing token.

You may insert either parenthesis character at any position without deleting or rearranging existing characters. Return the minimum number of insertions required to make the entire string balanced, including repairs for unmatched closing pairs, incomplete pairs of closing parentheses, and openings left unmatched at the end.

### Function Contract
**Inputs**

- `s`: a string of `(` and `)` with length $n$, where $1 \le n \le 10^5$.

**Return value**

The minimum number of inserted parentheses needed to satisfy the two-consecutive-closing rule.

### Examples
**Example 1**

- Input: `s = "(()))"`
- Output: `1`
- Explanation: One final `)` completes the closing pair for the first opening parenthesis.

**Example 2**

- Input: `s = "())"`
- Output: `0`
- Explanation: One opening parenthesis is already followed by its required `))` token.

**Example 3**

- Input: `s = "))())("`
- Output: `3`
- Explanation: Insert one `(` before the initial `))` and two `)` after the final `(`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track required closing characters rather than a stack**

Scan from left to right while `needed` records how many closing-parenthesis characters the openings already seen still require. Each `(` adds two to `needed`. Each `)` satisfies one requirement and subtracts one.

The count encodes both nesting and the special paired-close rule. A completed valid prefix has `needed = 0`, while a positive value describes exactly how many future `)` characters would finish all pending openings if no new opening appeared.

**Finish an odd closing requirement before a new opening**

When a new `(` arrives while `needed` is odd, the previous closing token has consumed only its first `)`. The required pair must be consecutive, so the second `)` has to be inserted before this new opening. Count that insertion and decrease `needed` by one, making it even, before adding the new opening's two requirements.

This repair is forced: placing the missing `)` anywhere after the encountered `(` would separate the two characters of the previous closing token and could not fix that prefix.

**Supply an opening for an excess close**

When processing `)` makes `needed` negative, no earlier opening exists for it. Insert `(` immediately before this close. That new opening needs two closing characters; the current `)` supplies the first, so reset `needed` to one and count one insertion.

After the scan, every remaining requirement can only be fulfilled by appending `)` characters. Adding `needed` to the insertions is both sufficient and necessary. Every repair made during the scan addresses a prefix violation at the first point it becomes unavoidable, so postponing it cannot use fewer characters.

#### Complexity detail

The scan performs constant work for each of the $n$ input characters, taking $O(n)$ time. The insertion count and outstanding-close count use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Literal list insertion:** can repair the string in place and obtain the same minimum, but repeated middle insertions can take $O(n^2)$ time.
- **Explicit stack of openings:** works, but stores up to $O(n)$ indices even though only the number and parity of outstanding closes matter.
- A single `(` needs two appended `)` characters, while a single `)` needs an inserted `(` and one additional `)`.
- The string `))` needs only one opening parenthesis inserted before it.
- A lone `)` immediately before `(` forces the missing second `)` to be inserted before that new opening.
- Already balanced strings such as `())` require no insertion.
- Long runs of openings leave two required closing characters per opening at the end.

</details>
