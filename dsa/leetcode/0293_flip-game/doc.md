# Flip Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 293 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-game/) |

## Problem Description
### Goal
Given a string containing only `+` and `-`, one legal move selects two adjacent plus signs and changes that pair from `"++"` to `"--"`. Every other character remains in its original position and state.

Return all states reachable by making exactly one legal move, in any order. Overlapping pairs represent different choices and may produce different states. Do not include the unchanged input or states requiring several moves. When no adjacent plus pair exists, return an empty list. The output strings retain the same length as the input.

### Function Contract
**Inputs**

- `currentState`: the current row of plus and minus symbols

**Return value**

A list containing one next-state string for each flippable adjacent pair, in left-to-right pair order.

### Examples
**Example 1**

- Input: `currentState = "++++"`
- Output: `["--++", "+--+", "++--"]`

**Example 2**

- Input: `currentState = "+"`
- Output: `[]`

**Example 3**

- Input: `currentState = "++"`
- Output: `["--"]`
