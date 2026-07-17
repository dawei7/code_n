# Number of Different Integers in a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-different-integers-in-a-string/) |
| Frontend ID | 1805 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A string `word` contains lowercase English letters and decimal digits. Treat every maximal consecutive run of digits as one nonnegative integer; letters separate neighboring runs.

Two digit runs represent the same integer when they differ only by leading zeros. For example, `"1"`, `"01"`, and `"001"` are one value, and every run consisting only of zeros represents zero. Return how many distinct integers occur in the string.

### Function Contract

**Inputs**

- `word`: a string of length $n$, where $1 \le n \le 1000$ and every character is a lowercase English letter or a decimal digit.

**Return value**

- Return the number of distinct integer values represented by maximal digit runs in `word`.

### Examples

**Example 1**

- Input: `word = "a123bc34d8ef34"`
- Output: `3`

The digit runs represent `123`, `34`, `8`, and `34`.

**Example 2**

- Input: `word = "leet1234code234"`
- Output: `2`

The two represented values are `1234` and `234`.

**Example 3**

- Input: `word = "a1b01c001"`
- Output: `1`

All three runs normalize to the integer value one.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Extract maximal digit runs**

Scan from left to right. Skip letters. When a digit is found, advance a second pointer through every consecutive digit so that the substring is one complete integer token rather than several pieces.

**Normalize without converting to an integer**

Remove leading zeros from the token. If nothing remains, use the canonical representation `"0"`; otherwise use the remaining digit string. This makes numerically equal runs identical even when they contain many more digits than a fixed-width integer can hold.

**Count canonical strings in a set**

Insert each normalized token into a set and return its size. Every represented integer contributes its canonical decimal form, equal integers share one form, and distinct integers have different forms. The set size is therefore exactly the requested count.

#### Complexity detail

The scanning pointers advance through each of the $n$ characters once. Normalizing and hashing all digit runs processes at most $n$ digits in total, giving $O(n)$ expected time. The canonical strings stored in the set contain at most $O(n)$ total characters, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Convert every run with `int`:** It is concise in arbitrary-precision languages, but string normalization is portable and avoids constructing large numeric objects.
- **Compare against a list of prior tokens:** It is correct but may compare every new value with every earlier distinct value and take $O(n^2)$ time.
- **No digits:** The set remains empty and the answer is zero.
- **One run spanning the string:** It contributes exactly one integer, regardless of its length.
- **All-zero runs:** Normalize `"0"`, `"00"`, and longer zero runs to the same `"0"`.
- **Letters between digits:** Each letter terminates the current run, even when the neighboring digit characters would otherwise form one number.
- **Repeated normalized value:** Leading-zero variants do not increase the set size.

</details>
