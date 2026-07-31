# Percentage of Letter in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2278 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/percentage-of-letter-in-string/) |

## Problem Description
### Goal
You are given a nonempty lowercase English string `s` and one lowercase
English character `letter`. Determine what percentage of the positions in `s`
contain exactly `letter`.

If `letter` occurs $c$ times in a string of length $n$, its exact percentage
is

$$
\frac{100c}{n}.
$$

Round this value down to the nearest whole percent and return that integer.
Thus any fractional part is discarded rather than rounded to the nearest
integer.

### Function Contract
**Inputs**

- `s`: a lowercase English string with length between 1 and 100
- `letter`: one lowercase English character

Let $n=\lvert\texttt{s}\rvert$.

**Return value**

The integer

$$
\left\lfloor
\frac{100\cdot\operatorname{count}(\texttt{letter in s})}{n}
\right\rfloor.
$$

### Examples
**Example 1**

- Input: `s = "foobar", letter = "o"`
- Output: `33`

Two of six positions match, and $\lfloor 200/6\rfloor=33$.

**Example 2**

- Input: `s = "jjjj", letter = "k"`
- Output: `0`

**Example 3**

- Input: `s = "abc", letter = "a"`
- Output: `33`

One third is rounded down from approximately $33.33\%$.
