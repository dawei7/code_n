# Substrings of Size Three with Distinct Characters

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) |
| Frontend ID | 1876 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A substring is a contiguous portion of a string. Call a substring good when none of its characters repeat. Given a lowercase English string `s`, count the good substrings whose length is exactly three.

Every starting position defines a separate occurrence. Consequently, if the same three-character text appears at several positions, each occurrence is counted. Windows may overlap, and a string shorter than three contributes no qualifying substring because it contains no window of the required size.

### Function Contract

**Inputs**

- `s`: a lowercase English string with $1 \le \lvert s\rvert \le 100$.
- Let $N = \lvert s\rvert$.

**Return value**

- Return the number of indices $i$ for which `s[i:i+3]` exists and its three characters are pairwise distinct.

### Examples

**Example 1**

- Input: `s = "xyzzaz"`
- Output: `1`

Among `"xyz"`, `"yzz"`, `"zza"`, and `"zaz"`, only `"xyz"` has three distinct characters.

**Example 2**

- Input: `s = "aababcabc"`
- Output: `4`

The good occurrences are `"abc"`, `"bca"`, `"cab"`, and the later `"abc"`.

**Example 3**

- Input: `s = "abca"`
- Output: `2`

Both overlapping windows, `"abc"` and `"bca"`, are good.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Enumerate only windows of the required length**

A length-three substring starts at each index from `0` through `N - 3`. Scan exactly those starts. There is no reason to generate substrings of any other length.

**Test pairwise distinctness directly**

Three characters are all distinct precisely when the first differs from the second, the first differs from the third, and the second differs from the third. Add the Boolean result of these three comparisons to the count for each window.

**Why occurrences are counted correctly**

Each possible length-three occurrence has one unique starting index and is examined once, including occurrences that overlap or contain the same text as another window. The pairwise test accepts exactly the good windows, so the accumulated total equals the requested occurrence count.

#### Complexity detail

There are at most $N-2$ candidate windows, and each uses three constant-time comparisons. Total time is therefore $O(N)$. The scan stores only an index and count, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Three-character set:** Checking `len(set(s[i:i+3])) == 3` is clear and remains $O(N)$ because the window size is fixed, though it allocates tiny temporary objects.
- **Enumerate every substring:** It eventually finds the correct length-three windows but performs $O(N^2)$ unnecessary enumeration.
- **String shorter than three:** The answer is zero.
- **Exactly three distinct characters:** The sole window contributes one.
- **Repeated first and third characters:** A window such as `"aba"` is not good even though adjacent characters differ.
- **Overlapping windows:** Each valid start is counted independently.
- **Repeated text:** Separate occurrences of the same good substring all count.

</details>
