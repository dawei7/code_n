# Remove All Adjacent Duplicates In String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1047 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) |

## Problem Description

### Goal

The string `s` consists of lowercase English letters. One duplicate removal chooses two letters that are both adjacent and equal, then removes that pair from the string.

Keep making duplicate removals until no adjacent equal pair remains. Removing one pair may bring another equal pair together, so those newly adjacent letters must also be considered. Return the final string after every possible removal. The final result is guaranteed to be unique regardless of which available pair is removed first.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $N$, where $1 \le N \le 10^5$.

**Return value**

- The unique string remaining after repeatedly deleting adjacent equal-letter pairs until no such pair exists.

### Examples

**Example 1**

- Input: `s = "abbaca"`
- Output: `"ca"`
- Explanation: Removing `"bb"` gives `"aaca"`; the newly exposed `"aa"` is then removed.

**Example 2**

- Input: `s = "azxxzy"`
- Output: `"ay"`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Store the fully reduced prefix:** Maintain a list as a stack. Before processing the next character, the stack contains the unique fully reduced result for the prefix already read, so no equal adjacent pair exists inside it.

**Resolve the only possible new pair:** Compare the next character with the stack top. If they are equal, pop the top because those two letters form a removable adjacent pair. Otherwise push the character. No other part of the reduced prefix changes, and a pop automatically exposes the earlier stack character for comparison with a later input character.

**Establish the final reduction:** Each input character is pushed at most once and popped at most once. After processing a prefix, the push-or-pop rule produces exactly the result of reducing that prefix: an unequal character extends it, while an equal character cancels its final letter. By induction, the invariant holds for all prefixes. When the scan ends, the stack has no adjacent equal pair and represents a sequence of valid removals from the original string, so its joined contents are the guaranteed unique answer.

#### Complexity detail

The scan processes $N$ characters once, and every stack operation is constant time, giving $O(N)$ time. At most $N$ characters remain in the stack, so space is $O(N)$.

#### Alternatives and edge cases

- **Repeated string scans:** Find one removable pair, rebuild the string without it, and restart. This is correct but can take $O(N^2)$ time.
- **Regular-expression replacement:** Repeatedly replace every adjacent equal pair until stable. It obscures cascading behavior and may require many full-string passes.
- **In-place write pointer:** Use a mutable character array and treat its written prefix as the stack, achieving the same $O(N)$ time and space bounds.
- **Single character:** No pair exists, so the input is returned unchanged.
- **Complete cancellation:** An even run such as `"aaaa"` reduces to the empty string.
- **Cascading removal:** In `"abba"`, removing `"bb"` exposes `"aa"`, which must also be removed.
- **No duplicates:** A string with no adjacent equal letters remains unchanged.
- **Odd run length:** Repeated cancellation leaves one copy from an odd-length run.

</details>
