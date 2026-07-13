# License Key Formatting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 482 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/license-key-formatting/) |

## Problem Description
### Goal
Given a license-key string `s` containing English letters, digits, and dashes, ignore the existing group boundaries by removing every dash. Convert all lowercase letters among the remaining alphanumeric characters to uppercase without changing any digit or character order.

Reformat the cleaned characters into groups separated by one dash. Every group except the first must contain exactly `k` characters; the first may be shorter than `k` but must contain at least one character. Return the reformatted key with no leading or trailing dash and no empty group.

### Function Contract
**Inputs**

- `s`: letters, digits, and dashes
- `k`: the required size of every group after the first

**Return value**

- The reformatted uppercase key with single dashes between groups

### Examples
**Example 1**

- Input: `s = "5F3Z-2e-9-w", k = 4`
- Output: `"5F3Z-2E9W"`

**Example 2**

- Input: `s = "2-5g-3-J", k = 2`
- Output: `"2-5G-3J"`

**Example 3**

- Input: `s = "---", k = 3`
- Output: `""`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Normalize the meaningful characters**

Scan the input once, skip every dash, and append the uppercase form of each remaining character. Existing group boundaries have no effect on the new layout.

**Determine the first group from the remainder**

If `length % k` is nonzero, that remainder is the first group length. Otherwise the first group also has length `k`. After it, slice consecutive groups of exactly `k` characters and join all groups with one dash.

**Why this layout is unique**

The normalized character order cannot change. Requiring every group except possibly the first to have size `k` fixes all boundaries when counted backward from the end, and the remainder fixes the only shorter prefix.

#### Complexity detail

Normalization and grouping each process `n` characters at most once, giving $O(n)$ time. The cleaned characters, groups, and returned string use $O(n)$ space.

#### Alternatives and edge cases

- **Build backward:** scan from right to left, insert a dash after every `k` retained characters, then reverse the result.
- **Repeated string prepending:** is correct but can copy the growing output on every character and take $O(n^2)$ time.
- **All dashes:** produces an empty key without a leading or trailing dash.
- **$k = 1$:** every retained character becomes its own group.
- **Exact multiple of `k`:** the first group has full size rather than zero length.
- **Digits:** remain unchanged while letters are uppercased.
- **Consecutive input dashes:** are all discarded and never create empty groups.

</details>
