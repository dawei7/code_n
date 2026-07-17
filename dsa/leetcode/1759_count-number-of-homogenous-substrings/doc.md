# Count Number of Homogenous Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1759 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-homogenous-substrings/) |

## Problem Description

### Goal

You are given a string `s` of lowercase English letters. A substring is homogenous when every character in that contiguous, nonempty segment is the same.

Count all homogenous substrings of `s`. Each occurrence is identified by its start and end positions, so occurrences at different positions count separately even when their text is identical. Because the count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: a lowercase English string with $1 \le n \le 10^5$, where $n=\lvert s\rvert$.

Let $M=10^9+7$.

**Return value**

- Return the number of nonempty contiguous substrings whose characters are all equal, reduced modulo $M$.

### Examples

**Example 1**

- Input: `s = "abbcccaa"`
- Output: `13`
- Explanation: Runs of lengths $1$, $2$, $3$, and $2$ contribute $1$, $3$, $6$, and $3$ homogenous substrings.

**Example 2**

- Input: `s = "xy"`
- Output: `2`
- Explanation: Only the two one-character substrings are homogenous.

**Example 3**

- Input: `s = "zzzzz"`
- Output: `15`
- Explanation: A length-five uniform run contains $5+4+3+2+1=15$ homogenous substrings.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count substrings by their ending position**

When a character extends a current run to length $r$, exactly $r$ homogenous substrings end at that position: the suffixes of the run having lengths $1$ through $r$. Every homogenous substring has one unique ending position, so adding these contributions counts every valid occurrence exactly once.

**Maintain the current equal-character run**

Scan from left to right. If the current character equals the preceding run's character, increment the run length. Otherwise begin a new run of length one. No earlier character outside the current run can participate in a homogenous substring ending at this position.

**Accumulate with the modulus**

Add the current run length to the total at every position and reduce modulo $M$. For a maximal run of length $L$, the accumulated contributions are $1+2+\cdots+L=L(L+1)/2$, matching the number of ways to choose a nonempty interval inside that run.

The maximal equal-character runs partition `s`, and a homogenous substring cannot cross a boundary between distinct characters. Summing the exact ending-position contributions within every run therefore gives the complete answer.

#### Complexity detail

The algorithm performs one constant-time update for each of the $n$ characters, taking $O(n)$ time. It stores only the previous character, current run length, total, and modulus, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sum completed runs:** Detect each maximal run and add $L(L+1)/2$ when it ends. This is also linear but requires explicitly flushing the final run.
- **Enumerate all substrings:** Extending from every starting position and stopping at the first different character is correct, but takes $O(n^2)$ time for a uniform string.
- **Single character:** The only substring is homogenous, so the answer is one.
- **All characters distinct:** Every run has length one, and the answer is $n$.
- **All characters equal:** The answer before reduction is $n(n+1)/2$.
- **Repeated text at different positions:** Equal substring values still count separately because their intervals are different.
- **Run boundaries:** A substring containing both sides of a character change is never homogenous.
- **Large count:** Apply the modulus during accumulation so implementations with fixed-width integers do not overflow.

</details>
