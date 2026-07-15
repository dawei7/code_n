# Minimum Add to Make Parentheses Valid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 921 |
| Difficulty | Medium |
| Topics | String, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) |

## Problem Description
### Goal

A parentheses string is valid exactly when it is empty, is a concatenation `AB` of two valid strings, or has the form `(A)` for a valid string `A`.

You are given a string `s` containing only opening and closing parentheses. In one move, insert either `'('` or `')'` at any position. Return the minimum number of insertions needed to make the resulting string valid.

### Function Contract
**Inputs**

- `s`: a parentheses string of length $n$, where $1 \le n \le 1000$ and every character is either `'('` or `')'`.

**Return value**

The minimum number of parenthesis characters that must be inserted anywhere in `s` to obtain a valid parentheses string.

### Examples
**Example 1**

- Input: `s = "())"`
- Output: `1`

**Example 2**

- Input: `s = "((("`
- Output: `3`

**Example 3**

- Input: `s = "()()"`
- Output: `0`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Match each closing parenthesis as it arrives**

Scan from left to right while maintaining `open_count`, the number of unmatched opening parentheses available to close. An opening parenthesis increases this balance. A closing parenthesis consumes one available opening when the balance is positive.

If a closing parenthesis arrives with balance zero, no later character can precede it, so it can never be matched by an existing opening parenthesis. One inserted opening parenthesis is therefore unavoidable; count that insertion and continue with balance zero.

**Account for openings left at the end**

After the scan, every unit of `open_count` is an opening parenthesis that never found a closing partner. Each requires one inserted closing parenthesis. The answer is the number of forced openings inserted during the scan plus this remaining balance.

Every counted insertion is necessary: unmatched closing parentheses require earlier openings, and unmatched opening parentheses require later closings. Adding exactly those characters produces a valid nesting, so the lower bound is achievable and the count is minimal.

#### Complexity detail

Let $n$ be the length of `s`. The scan processes each character once, giving $O(n)$ time. The balance and insertion count use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Explicit stack:** Pushing openings and popping them for closings is correct and linear, but stores up to $O(n)$ characters when a counter is sufficient.
- **Repeatedly remove matched pairs:** Removing every occurrence of `"()"` until none remain leaves exactly the unmatched characters, but nested input can require $O(n)$ full-string passes and $O(n^2)$ time.
- **All openings:** Every character needs a closing parenthesis appended, so the answer is $n$.
- **All closings:** Every character needs an opening parenthesis inserted before it, so the answer is $n$.
- **Already valid input:** The scan ends with no forced insertion and zero balance.
- **Balanced counts are insufficient:** A string such as `")("` has equal numbers of each character but still needs two insertions because prefix order matters.

</details>
