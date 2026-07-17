# Longest Nice Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1763 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-nice-substring/) |

## Problem Description

### Goal

You are given a string `s` containing uppercase and lowercase English letters. A string is nice when every alphabetic letter that appears in it is represented in both cases: if lowercase `a` occurs, uppercase `A` must also occur, and conversely.

Find the longest contiguous substring of `s` that is nice. When several qualifying substrings have the same maximum length, return the one that begins earliest. If no nonempty nice substring exists, return the empty string.

### Function Contract

**Inputs**

- `s`: a string of uppercase and lowercase English letters with $1 \le n \le 100$, where $n=\lvert s\rvert$.

**Return value**

- Return the longest contiguous substring in which every appearing letter has both its lowercase and uppercase forms.
- Resolve equal maximum lengths by choosing the earliest starting position, and return `""` if none exists.

### Examples

**Example 1**

- Input: `s = "YazaAay"`
- Output: `"aAa"`
- Explanation: The returned substring contains both `a` and `A`; no longer substring satisfies the paired-case condition.

**Example 2**

- Input: `s = "Bb"`
- Output: `"Bb"`
- Explanation: Both cases of `b` occur, so the complete string is nice.

**Example 3**

- Input: `s = "c"`
- Output: `""`
- Explanation: The only appearing letter lacks its uppercase counterpart.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Test the current region as a whole**

Collect the characters present in the current substring. It is nice exactly when every character's `swapcase()` form is also present. If this holds, the complete region is necessarily the longest answer available inside itself.

**Use an unpaired character as a separator**

Suppose character `s[i]` appears in the region but its opposite case does not. No nice substring contained in this region can include `s[i]`: that smaller substring cannot contain a counterpart that is absent from the entire region. Every valid candidate must therefore lie wholly to the left or wholly to the right of this position.

**Solve both independent sides**

Recursively find the longest nice substring on each side of the first unpaired character. Returning the longer result is safe because the separator proof excludes every candidate crossing that position.

**Preserve the earliest tie**

The left recursive result begins before every right result. When their lengths are equal, choose the left result with `>=`; this implements the required earliest-start rule at every split and therefore in the final answer.

A region shorter than two characters cannot contain both cases of any letter and returns empty. Otherwise recursion either proves the entire region nice or splits at a character that no valid answer may cross, so induction over region length establishes completeness and correctness.

#### Complexity detail

In the worst case, each recursive level builds a set and slices a substring only one character shorter than its parent, producing the series $n+(n-1)+\cdots+1=O(n^2)$ time. Python substring slices and character sets retained across a maximally unbalanced recursion can likewise total $O(n^2)$ space; recursion depth is $O(n)$.

#### Alternatives and edge cases

- **Enumerate all substrings:** Building a character set and checking every candidate directly is simple but can take $O(n^3)$ time.
- **Incremental case masks:** Extending each start position while maintaining lowercase and uppercase bitmasks reduces exhaustive enumeration to $O(n^2)$ time and can compare masks in constant time.
- **Sliding windows by distinct-letter count:** Trying each possible number of distinct letters can also achieve quadratic time but requires more bookkeeping.
- **Single character:** It cannot be nice because only one case is present.
- **Entire string nice:** Return it immediately; no contained substring can be longer.
- **No paired cases:** Repeated splitting eventually returns the empty string.
- **Equal-length answers:** Choose the leftmost occurrence, not the lexicographically smallest text.
- **Repeated characters:** Multiplicity is irrelevant; only the presence of both cases matters.
- **Several letters:** Every letter appearing in the candidate must satisfy the condition independently.

</details>
