# Break a Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1328 |
| Difficulty | Medium |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/break-a-palindrome/) |

## Problem Description
### Goal
Given a palindromic string `palindrome` of lowercase English letters, replace exactly one character with another lowercase letter so the resulting string is not a palindrome.

Among all valid results, return the lexicographically smallest. For equal-length strings, lexicographic order is determined by the first position where they differ. If no one-character replacement can break the palindrome, return the empty string.

The replacement character may be any lowercase English letter, but it must differ from the character it replaces because the operation is an actual change.

### Function Contract
**Inputs**

- `palindrome`: a lowercase palindromic string of length $n$, where $1\le n\le1000$.

**Return value**

The lexicographically smallest non-palindrome obtainable by replacing exactly one character, or `""` if no such string exists.

### Examples
**Example 1**

- Input: `palindrome = "abccba"`
- Output: `"aaccba"`
- Explanation: Replacing the first non-`a` in the left half yields the smallest possible differing prefix.

**Example 2**

- Input: `palindrome = "a"`
- Output: `""`
- Explanation: Every one-character string is a palindrome after any replacement.

**Example 3**

- Input: `palindrome = "aa"`
- Output: `"ab"`
- Explanation: No left-half character can be reduced, so increasing the final character minimally is optimal.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Prefer the earliest possible decrease**

Only positions before the midpoint need to be considered for a lexicographic decrease. If a character there is not `a`, replace the first such character with `a`. The mirrored character remains unchanged, so the result is not a palindrome, and changing the earliest reducible position dominates every change at a later position.

**Fall back to the smallest final increase**

If the entire left half is already `a`, no character before or at the decisive prefix can be decreased. Change the last character to `b`. This breaks symmetry while postponing the first difference as far right as possible and using the smallest increase from `a`.

For length 1, every replacement still produces a one-character palindrome, so return empty. Excluding the middle position from the first-half scan is essential for odd lengths: changing only the center would preserve the palindrome.

#### Complexity detail

The scan examines at most half of the $n$ characters, and constructing the modified string copies $n$ characters. Time is $O(n)$ and the mutable character list uses $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every replacement:** Testing candidates and checking each for symmetry is correct but takes $O(n^2)$ time even when only the first useful position matters.
- **Single-character input:** No valid result exists, so return the empty string.
- **Odd-length center:** Never choose it as the only change because the string remains palindromic.
- **All `a` characters:** Change the last character to `b`.
- **First character reducible:** Replacing it with `a` gives the greatest possible lexicographic improvement.
- **Exactly one replacement:** Even when the input is all `a`, returning it unchanged is not permitted.

</details>
