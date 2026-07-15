# Perform String Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1427 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/perform-string-shifts/) |

## Problem Description

### Goal

Apply a sequence of cyclic shifts to the string `s`. Each operation is `[direction, amount]`: direction `0` moves the first `amount` characters to the end, while direction `1` moves the last `amount` characters to the front.

Process the operations in their given order and return the resulting string. Shift amounts wrap around the string length, and left and right shifts may partially or completely cancel one another.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 100$.
- `shift`: an array of $q$ operations, where $1 \le q \le 100$.
- Each operation is `[direction, amount]`, with `direction` equal to `0` or `1` and $1 \le \texttt{amount} \le 100$.

**Return value**

- The string obtained after applying every cyclic shift in order.

### Examples

**Example 1**

- Input: `s = "abc", shift = [[0,1],[1,2]]`
- Output: `"cab"`

**Example 2**

- Input: `s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]`
- Output: `"efgabcd"`

**Example 3**

- Input: `s = "abcd", shift = [[0,4],[1,8]]`
- Output: `"abcd"`

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Combine shifts algebraically.** Represent a right shift as a positive amount and a left shift as a negative amount. Sum those signed amounts across all operations. Cyclic rotations compose by adding their offsets, so only the final net value matters even though the operations are presented sequentially.

**Apply one normalized rotation.** Reduce the net right shift modulo $n$. If the result is zero, return `s` unchanged. Otherwise, split before the last `net` characters and concatenate the suffix before the prefix.

**Why composition is equivalent.** Each operation changes every character's cyclic index by its signed amount. Adding all changes gives the same final index as applying them one at a time, and modulo reduction preserves that cyclic destination. The single rotation therefore produces exactly the sequential result.

#### Complexity detail

Reading the $q$ operations takes $O(q)$ time, and constructing the rotated string copies $O(n)$ characters, for $O(n+q)$ total time. The returned string uses $O(n)$ space.

#### Alternatives and edge cases

- **Execute each operation directly:** Slice and concatenate after every shift. It is correct but repeatedly copies the string and takes $O(nq)$ time.
- **Shift one character at a time:** Repeating unit rotations for every amount can take $O(n\sum a_i)$ time.
- **Opposite directions:** Signed amounts naturally cancel.
- **Amount at least n:** Reduce only the final total modulo $n$; individual large amounts need no special case.
- **Net zero:** Return the original ordering.
- **Single character:** Every rotation produces the same string.
- **Direction sign:** Direction `0` is left and must subtract; direction `1` is right and must add.

</details>
