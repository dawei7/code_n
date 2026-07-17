# Minimum Changes To Make Alternating Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1758 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) |

## Problem Description

### Goal

You are given a binary string `s`. In one operation, choose any position and change its character from `"0"` to `"1"` or from `"1"` to `"0"`.

A binary string is alternating when every pair of adjacent characters differs. Determine the minimum number of operations required to transform `s` into an alternating string of the same length, and return that minimum.

### Function Contract

**Inputs**

- `s`: a string containing only `"0"` and `"1"`, with $1 \le n \le 10^4$, where $n=\lvert s\rvert$.

**Return value**

- Return the minimum number of single-character changes needed so that `s[i] != s[i + 1]` for every valid adjacent pair.

### Examples

**Example 1**

- Input: `s = "0100"`
- Output: `1`
- Explanation: Changing the final character produces `"0101"`.

**Example 2**

- Input: `s = "10"`
- Output: `0`
- Explanation: The two existing adjacent characters already differ.

**Example 3**

- Input: `s = "1111"`
- Output: `2`
- Explanation: Either `"0101"` or `"1010"` can be reached with two changes.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize the only two valid targets**

Once the first character of an alternating binary string is chosen, every later character is forced. For length $n$, the only possibilities are the prefix of `"0101..."` that starts with zero and the complementary prefix of `"1010..."` that starts with one.

**Count mismatches against one target**

At zero-based index `i`, the zero-starting target expects `str(i % 2)`. Scan `s` once and count positions whose characters differ from this expectation. Each mismatch needs one change, and changing all such positions is sufficient, so the count is exactly the cost of reaching that target.

**Derive the complementary cost**

At every position, exactly one of the two target strings matches the current binary character. If $x$ positions mismatch the zero-starting target, the remaining $n-x$ positions mismatch the one-starting target. The answer is therefore $\min(x,n-x)$.

These are the only alternating strings of the required length, and the calculation gives the exact number of changes for each. Taking their smaller cost is consequently globally optimal.

#### Complexity detail

The scan examines each of the $n$ characters once, taking $O(n)$ time. It stores only the mismatch count and loop state, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Build both target strings:** Comparing against explicit `"0101..."` and `"1010..."` strings is correct but allocates $O(n)$ additional space.
- **Count equal adjacent pairs:** The number of adjacent violations alone is not sufficient because one changed character can affect two neighboring pairs; compare positions with complete targets instead.
- **Single character:** A length-one string has no adjacent pair and is already alternating.
- **Already alternating:** One mismatch count is zero and the method returns zero.
- **All characters equal:** The best target changes exactly half the positions, rounded down.
- **Odd length:** The two targets contain different counts of zeros and ones, but complementary mismatch counts still sum to $n$.
- **Even length:** The two targets contain equal symbol counts; their positional mismatch costs may still differ.
- **Choose either starting bit:** The minimum explicitly considers both possible first characters.

</details>
