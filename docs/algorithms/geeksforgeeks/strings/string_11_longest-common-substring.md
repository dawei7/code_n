# Longest Common Prefix

| | |
|---|---|
| **ID** | `string_11` |
| **Category** | strings |
| **Complexity (required)** | $O(N \times M)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |

## Problem statement

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

**Input:** An array of strings `strs`.
**Output:** A string representing the longest common prefix.

**Example 1:**
`strs = ["flower", "flow", "flight"]`
Output: `"fl"`.

**Example 2:**
`strs = ["dog", "racecar", "car"]`
Output: `""`. (There is no common prefix among the input strings).

## When to use it

- To find shared directory paths, namespace prefixes, or auto-complete boundaries.
- A highly popular, straightforward interview question to test your ability to avoid index-out-of-bounds exceptions.

## Approach

**1. Horizontal Scanning (The Intuitive Way):**
1. Treat the very first string in the array as your initial "prefix".
2. Iterate through the rest of the strings one by one.
3. For each string, compare it to your running "prefix".
4. If the current string does not start with the prefix, chop off the last character of the prefix and try again!
5. If the prefix ever becomes empty (`""`), it means there is absolutely no common prefix. Return `""` immediately.
6. Return the prefix after all strings have been checked.

**2. Vertical Scanning (The Optimal Way):**
Horizontal scanning can be slow if there is a massive array of very long identical strings, but the very last string in the array is just `"a"`. We would scan millions of characters before finally chopping the prefix down to `"a"`.
Instead, we scan vertically!
We look at the 0th character of all strings. If they match, we move to the 1st character of all strings. We continue until we find a character mismatch, or we reach the end of one of the strings!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_11: Longest Common Substring.

Length of the longest common substring (consecutive, not
subsequence) of s1 and s2. Standard DP: dp[i][j] = length
of the common suffix of s1[..i] and s2[..j]. The answer
is the max over the table.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    best = 0
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best = dp[i][j]
            else:
                dp[i][j] = 0
    return best
```

</details>

## Walk-through (Vertical Scanning)

`strs = ["flower", "flow", "flight"]`.

**`i = 0` (Checking 0th character):**
- `strs[0][0]` is `'f'`.
- `strs[1][0]` is `'f'`. Match.
- `strs[2][0]` is `'f'`. Match.

**`i = 1` (Checking 1st character):**
- `strs[0][1]` is `'l'`.
- `strs[1][1]` is `'l'`. Match.
- `strs[2][1]` is `'l'`. Match.

**`i = 2` (Checking 2nd character):**
- `strs[0][2]` is `'o'`.
- `strs[1][2]` is `'o'`. Match.
- `strs[2][2]` is `'i'`. Mismatch! (`'i' != 'o'`).

Return `strs[0][:2]`, which is `"fl"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \times \min(M)$) | $O(1)$ |
| **Average** | $O(N \times M)$ | $O(1)$ |
| **Worst** | $O(N \times M)$ | $O(1)$ |

Let N be the number of strings, and M be the maximum length of a string.
In the worst case, all strings are identical. The algorithm compares every character of every string. The total number of comparisons is N x M. Therefore, time complexity is $O(N \times M)$ (or $O(S)$ where S is the sum of all characters).
Space complexity is $O(1)$ constant extra space, assuming substring slicing `strs[0][:i]` is optimized or returning string pointers.

## Variants & optimizations

- **Sorting $O(S log N)$:** If you sort the array of strings lexicographically (alphabetically), you only need to compare the *first* string and the *last* string in the sorted array! The longest common prefix between them is guaranteed to be the longest common prefix for the entire array. However, sorting takes $O(S log N)$, making it mathematically slower than linear scanning.
- **Trie $O(S)$:** Insert all strings into a Trie. Then traverse down the Trie. As long as a node only has exactly 1 child (and isn't the end of a word), it is part of the common prefix!

## Real-world applications

- **Command Line Auto-Complete:** When you hit the `TAB` key in a Unix terminal, the shell calculates the Longest Common Prefix of all valid executable files matching your current typing to fill in the rest of the command!

## Related algorithms in cOde(n)

- **[trie_01 - Trie Insert/Search](../trie/trie_01_trie-insert-search.md)** — The data structure heavily optimized for answering prefix-based queries dynamically.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
