# Resulting String After Adjacent Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3561 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/resulting-string-after-adjacent-removals/) |

## Problem Description

### Goal

Start with a string `s` containing only lowercase English letters. While a removable pair exists, find the **leftmost** two adjacent characters that are consecutive in the alphabet, remove both characters, and close the resulting gap. The two letters may appear in either order, so both `ab` and `ba` are removable.

The alphabet is circular for this operation: `a` and `z` are also consecutive, in either order. Removing one pair can bring previously separated characters together and create another removable pair. Continue until the string contains no eligible adjacent pair, then return that final string.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters.

Its length satisfies $1 \le \lvert s \rvert \le 10^5$.

**Return value**

Return the string remaining after repeatedly deleting the leftmost adjacent alphabetically consecutive pair, including the circular pair `az` or `za`, until no operation is possible.

### Examples

#### Example 1

- **Input:** `s = "abc"`
- **Output:** `"c"`
- **Explanation:** The leftmost removable pair is `ab`, leaving `c`.

#### Example 2

- **Input:** `s = "adcb"`
- **Output:** `""`
- **Explanation:** Removing `dc` leaves `ab`, which is then removed.

#### Example 3

- **Input:** `s = "zadb"`
- **Output:** `"db"`
- **Explanation:** The circular pair `za` is removed; the remaining `db` is stable.

---
