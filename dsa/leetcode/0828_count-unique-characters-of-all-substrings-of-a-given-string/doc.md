# Count Unique Characters of All Substrings of a Given String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 828 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) |

## Problem Description

### Goal

For any string `t`, define `countUniqueChars(t)` as the number of characters that occur exactly once in `t`. For example, `countUniqueChars("LEETCODE")` is `5` because `L`, `T`, `C`, `O`, and `D` each appear once, while `E` appears three times.

Given an uppercase English string `s`, consider every nonempty substring selected by a pair of start and end positions. Return the sum of `countUniqueChars(t)` over all those substrings. Equal substring values arising at different positions are separate substrings and must each contribute. The input guarantees that the final sum fits in a 32-bit integer.

### Function Contract

**Inputs**

- `s`: a string of $n$ uppercase English letters, where $1 \le n \le 10^5$
- Let $A=26$ be the alphabet size.

**Return value**

- The sum, over every nonempty positional substring of `s`, of the number of characters occurring exactly once in that substring

### Examples

**Example 1**

- Input: `s = "ABC"`
- Output: `10`
- Explanation: Every character in every substring is unique, so the six substrings contribute `1 + 1 + 1 + 2 + 2 + 3`.

**Example 2**

- Input: `s = "ABA"`
- Output: `8`
- Explanation: The complete substring has only `B` as a unique character, while the shorter positional substrings contribute the remaining `7`.

**Example 3**

- Input: `s = "LEETCODE"`
- Output: `92`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Reverse the counting from substrings to occurrences**

Enumerating substrings repeats the same question many times. Instead, ask how many substrings count one particular occurrence of a character as unique. Suppose an occurrence is at index $i$, the previous occurrence of that same character is at $p$, and the next is at $q$. Use the virtual boundaries $p=-1$ when there is no previous occurrence and $q=n$ when there is no next occurrence.

For the occurrence at $i$ to be the only copy in a substring, the left boundary may be any position from $p+1$ through $i$, giving $i-p$ choices. Independently, the right boundary may be any position from $i$ through $q-1$, giving $q-i$ choices. This occurrence therefore contributes

$$
(i-p)(q-i)
$$

to the final sum.

**Finalize a contribution when its next occurrence arrives**

Maintain the last two indices for each of the $A$ letters. When the current index becomes the next occurrence $q$, the immediately preceding occurrence $i$ now has both boundaries known, so add its contribution and shift the two saved indices. After scanning the string, use the virtual boundary $q=n$ to finalize the last occurrence of every letter.

**Why summing occurrence contributions equals the requested total**

Every unique character counted inside a particular substring corresponds to exactly one occurrence position in `s`. That substring's boundaries lie between the adjacent equal-character occurrences precisely when the formula counts it. Conversely, every boundary pair counted by the formula contains the chosen occurrence and no other copy of its character, so it contributes one to `countUniqueChars` for that substring. Summing over occurrences therefore counts every requested substring-character contribution once, including equal substring values at different positions.

#### Complexity detail

Let $n$ be the string length and $A=26$ the alphabet size. The scan performs constant work per character, and finalizing the alphabet costs $O(A)$, for $O(n+A)=O(n)$ time. Two index arrays of length $A$ use $O(A)$ auxiliary space.

#### Alternatives and edge cases

- **Expand every substring with frequency counts:** Updating a count and current unique total for every start/end pair takes $O(n^2)$ time and $O(A)$ space.
- **Recount each materialized substring:** Constructing every substring and counting its characters independently can take $O(n^3)$ time.
- **Store all positions per character:** Sentinel-augmented occurrence lists support the same contribution formula in $O(n)$ time but retain $O(n)$ indices instead of only the last two per letter.
- **First occurrence:** The virtual previous index `-1` permits every left boundary from the start of the string through that occurrence.
- **Last occurrence:** The virtual next index $n$ permits every right boundary from that occurrence through the end of the string.
- **Repeated substring values:** Positions define substrings, so two equal strings from different ranges both contribute.
- **All characters equal:** Only length-one substrings have a unique character, and each occurrence contributes exactly once.
- **All characters distinct:** Every character is unique in every substring containing it, making the sum equal to the total lengths of all substrings.

</details>
