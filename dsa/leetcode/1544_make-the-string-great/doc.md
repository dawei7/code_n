# Make The String Great

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1544 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-the-string-great/) |

## Problem Description
### Goal
A string is considered good when it has no adjacent pair formed by the same English letter in opposite cases. In other words, a lowercase letter directly beside its uppercase version, in either order, makes the string invalid.

You may repeatedly remove any such adjacent pair. Continue until no invalid pair remains, then return the resulting good string. The input contains only uppercase and lowercase English letters, and the removal process is guaranteed to lead to a unique final string.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 100$, containing only uppercase and lowercase English letters.

**Return value**

The unique good string obtained after repeatedly deleting adjacent equal letters whose cases differ. The answer may be empty.

### Examples
**Example 1**

- Input: `s = "leEeetcode"`
- Output: `"leetcode"`
- Explanation: Removing the adjacent `"eE"` leaves a string with no opposite-case equal neighbors.

**Example 2**

- Input: `s = "abBAcC"`
- Output: `""`
- Explanation: Removing `"bB"` makes `"aA"` adjacent, and the final `"cC"` also disappears.

**Example 3**

- Input: `s = "s"`
- Output: `"s"`
- Explanation: A one-character string cannot contain an invalid adjacent pair.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Treat the current result as a stack**

Scan the input from left to right while storing the characters that have survived so far. Only the newest survivor can form a newly exposed invalid pair with the next input character. If the stack is empty or the two characters are not opposite-case versions of the same letter, push the new character.

**Cancel exactly when the boundary is invalid**

When the stack top and current character are different as characters but equal after case normalization, they form a removable pair. Pop the stack top and do not push the current character. This also exposes the previous survivor, allowing a later input character to trigger a chain of cancellations without rescanning the prefix.

After every step, the stack is the fully reduced result of the prefix processed so far. A push preserves goodness because the new boundary is valid; a pop removes the only new invalid boundary, and the remaining stack was already good. Thus, after the final character, the stack is good and represents a legal sequence of removals. Since the contract guarantees a unique final result, joining the stack returns exactly that result.

#### Complexity detail

Each of the $n$ characters is pushed at most once and popped at most once. Every comparison and stack operation is constant time, so the scan takes $O(n)$ time. In the worst case no pair cancels, and the stack stores all $n$ characters, requiring $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Repeated search and splice:** finding one bad pair, deleting it, and restarting is straightforward, but repeated scans and string rebuilding can take $O(n^2)$ time.
- **Recursive reduction:** recursion can mirror the cancellation process, but it adds call-stack overhead and can still rescan unchanged text unless it carries explicit stack state.
- A single character is already good.
- The entire string may cancel, so an empty answer is valid.
- Equal adjacent characters with the same case, such as `"aa"`, do not cancel.
- Different letters never cancel merely because their cases differ, so `"aB"` remains unchanged.
- Removing one pair can expose another invalid pair across the removed boundary.
- Either order, lowercase-uppercase or uppercase-lowercase, must be recognized.

</details>
