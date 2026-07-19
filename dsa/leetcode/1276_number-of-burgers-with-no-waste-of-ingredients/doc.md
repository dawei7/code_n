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

- `tomato_slices`: the available tomato-slice count, where $0 \le \texttt{tomato_slices} \le 10^7$.
- `cheese_slices`: the available cheese-slice count, where $0 \le \texttt{cheese_slices} \le 10^7$.

**Return value**

- Return `[jumbo, small]` when nonnegative integers satisfy both $4\,\textit{jumbo}+2\,\textit{small}=\texttt{tomato_slices}$ and $\textit{jumbo}+\textit{small}=\texttt{cheese_slices}$. Return `[]` if no such counts exist.

### Examples

**Example 1**

- Input: `tomato_slices = 16, cheese_slices = 7`
- Output: `[1,6]`

**Example 2**

- Input: `tomato_slices = 17, cheese_slices = 4`
- Output: `[]`

**Example 3**

- Input: `tomato_slices = 4, cheese_slices = 17`
- Output: `[]`
