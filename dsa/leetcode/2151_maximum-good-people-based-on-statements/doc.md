# Maximum Good People Based on Statements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2151 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-good-people-based-on-statements](https://leetcode.com/problems/maximum-good-people-based-on-statements/) |

## Problem Description

### Goal

A group contains good and bad people. Good people always tell the truth, while
a bad person's statements may be true or false. A square matrix `statements`
records what each person says about every other person: `0` means the target is
bad, `1` means the target is good, and `2` means no statement was made.

Classify every person as good or bad so that every statement made by each
person classified as good is true. Statements from people classified as bad
impose no restriction. Return the largest possible number of good people among
all consistent classifications. Nobody makes a statement about themselves, so
every diagonal entry is `2`.

### Function Contract

**Inputs**

- `statements`: An $n \times n$ matrix, where $2 \leq n \leq 15$, every entry
  is `0`, `1`, or `2`, and `statements[i][i] = 2`. Row `i` contains person
  `i`'s statements.

**Return value**

Return the maximum number of people that a classification can mark good
without contradicting any statement made by a good person.

### Examples

**Example 1**

- Input: `statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]`
- Output: `2`
- Explanation: People `0` and `1` can be good together while person `2` is
  bad. Marking person `2` good instead permits only one good person.

**Example 2**

- Input: `statements = [[2, 0], [0, 2]]`
- Output: `1`
- Explanation: Either person can be the sole good person, but they cannot both
  be good because each calls the other bad.
