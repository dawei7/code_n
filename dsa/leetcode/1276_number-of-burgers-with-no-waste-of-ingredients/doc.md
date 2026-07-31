# Number of Burgers with No Waste of Ingredients

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1276 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) |

## Problem Description

### Goal

Two burger sizes consume ingredients differently. Each jumbo burger requires four tomato slices and one cheese slice, while each small burger requires two tomato slices and one cheese slice.

Given the available numbers of tomato and cheese slices, determine nonnegative counts of jumbo and small burgers that use every slice of both ingredients, leaving no waste. Return the counts with jumbo burgers first. If no such combination exists, return an empty list.

### Function Contract

**Inputs**

- `tomatoSlices`: the available tomato-slice count, where $0 \le \texttt{tomatoSlices} \le 10^7$.
- `cheeseSlices`: the available cheese-slice count, where $0 \le \texttt{cheeseSlices} \le 10^7$.

**Return value**

- Return `[jumbo, small]` when nonnegative integers satisfy both $4\,\textit{jumbo}+2\,\textit{small}=\texttt{tomatoSlices}$ and $\textit{jumbo}+\textit{small}=\texttt{cheeseSlices}$. Return `[]` if no such counts exist.

### Examples

**Example 1**

- Input: `tomatoSlices = 16, cheeseSlices = 7`
- Output: `[1,6]`

**Example 2**

- Input: `tomatoSlices = 17, cheeseSlices = 4`
- Output: `[]`

**Example 3**

- Input: `tomatoSlices = 4, cheeseSlices = 17`
- Output: `[]`
