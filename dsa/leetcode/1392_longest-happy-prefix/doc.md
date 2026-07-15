# Longest Happy Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1392 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-happy-prefix/) |

## Problem Description

### Goal

A string prefix consists of one or more characters taken from its beginning, while a suffix consists of one or more characters taken from its end. A prefix is called happy when the same sequence is also a suffix, but it must be a proper prefix: it cannot equal the entire string.

Given a lowercase English string `s`, return its longest happy prefix. If no nonempty proper prefix also occurs as a suffix, return the empty string.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 10^5$.

**Return value**

- The longest nonempty proper prefix of `s` that is also a suffix, or `""` when no such prefix exists.

### Examples

**Example 1**

- Input: `s = "level"`
- Output: `"l"`

**Example 2**

- Input: `s = "ababab"`
- Output: `"abab"`

**Example 3**

- Input: `s = "leetcodeleet"`
- Output: `"leet"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Record the best border ending at every position.** Build the prefix-function array used by Knuth-Morris-Pratt string matching. For each position `i`, let `prefix[i]` be the length of the longest prefix of `s` that equals a suffix of `s[:i + 1]` and is shorter than that substring.

Begin with the candidate length `prefix[i - 1]`. If `s[i]` does not extend that candidate, replace the candidate by `prefix[candidate - 1]`, which is the next-longest border of the already matched prefix. Continue through this chain until the new character matches or the candidate becomes zero. A match extends the border by one.

Every fallback remains a possible border because a border of a border is also a border of the current prefix. Any skipped length cannot work: it is not itself a border of the portion already matched. Thus the final value at each position is the longest valid border there. At the last position, `prefix[n - 1]` is exactly the longest proper prefix that is also a suffix of the complete string; return that many leading characters.

#### Complexity detail

Although a mismatch can trigger several fallbacks, each successful extension increases the candidate length and the total number of decreases across the scan is $O(n)$. The prefix function is therefore built in $O(n)$ time. Its $n$ integer entries use $O(n)$ space.

#### Alternatives and edge cases

- **Test every prefix length:** Comparing every prefix with the corresponding suffix is simple but requires $O(n^2)$ character work in the worst case.
- **Rolling hash:** Prefix and suffix hashes can find matching lengths in $O(n)$ expected time, but collision avoidance requires either verification or multiple robust hashes.
- **Whole string:** The prefix function always describes a proper border, so the complete string is never returned.
- **Single character:** It has no nonempty proper prefix, so the result is `""`.
- **Repeated characters:** For `"aaaaa"`, the answer is `"aaaa"`; overlapping prefix and suffix occurrences are allowed.
- **No border:** Return the empty string rather than an arbitrary character or the whole input.

</details>
