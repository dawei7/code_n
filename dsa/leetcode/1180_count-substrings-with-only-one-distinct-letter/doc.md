# Count Substrings with Only One Distinct Letter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1180 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/) |

## Problem Description

### Goal

You are given a non-empty lowercase English string `s`. Count its non-empty substrings that contain only one distinct letter. A substring is a contiguous sequence, and occurrences at different index ranges count separately even when their text is identical.

Every single-character substring qualifies, while a longer substring qualifies exactly when all of its positions hold the same letter. Return the total number of qualifying substrings across every possible start and end position in `s`.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert s\rvert \leq 1000$.
- Let $n=\lvert s\rvert$.

**Return value**

- The number of non-empty contiguous substrings whose characters are all equal.

### Examples

**Example 1**

- Input: `s = "aaaba"`
- Output: `8`

The text `"aaa"` occurs once, `"aa"` occurs twice, `"a"` occurs four times, and `"b"` occurs once, for a total of eight occurrences.

**Example 2**

- Input: `s = "aaaaaaaaaa"`
- Output: `55`

**Example 3**

- Input: `s = "abc"`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition the string into maximal equal-character runs.** Scan from left to right while tracking the length of the current run. When the character changes, the previous run ends and a new length-one run begins. No qualifying substring can cross that boundary because it would contain both neighboring character values.

**Count by the ending position.** When the current run has length $L$, exactly $L$ valid substrings end at its newest character: the length-one suffix, the length-two suffix, and so on through the entire run. Add $L$ immediately at each position. Over a completed run of length $L$, these contributions total

$$
1+2+\cdots+L=\frac{L(L+1)}{2}.
$$

Every single-distinct-letter substring lies wholly within one maximal run and has one unique ending position, so this accumulation counts every valid occurrence exactly once.

#### Complexity detail

The scan visits each of the $n$ characters once, giving $O(n)$ time. The answer, current run length, and previous character use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every start and extend while equal:** This is correct, but an all-equal string makes it examine $O(n^2)$ start-end pairs.
- **Materialize maximal runs first:** Splitting or grouping the runs and then summing $L(L+1)/2$ is also linear, but storing all run lengths can use $O(n)$ space.
- **Single character:** The only substring qualifies, so the answer is `1`.
- **All characters equal:** Every non-empty substring qualifies, yielding $n(n+1)/2$.
- **All adjacent characters differ:** Only the $n$ length-one substrings qualify.
- **Repeated text at different positions:** Each index interval is a separate substring occurrence and must be counted.

</details>
