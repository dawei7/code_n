# HTML Entity Parser

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1410 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/html-entity-parser/) |

## Problem Description

### Goal

HTML represents certain reserved characters with named character entities. Parse a given string by replacing each recognized entity with the single character it denotes: `&quot;` with `"`, `&apos;` with `'`, `&amp;` with `&`, `&gt;` with `>`, `&lt;` with `<`, and `&frasl;` with `/`.

Preserve every character that is not part of one of those six complete spellings. Interpret the original input from left to right: replacement characters are output, not scanned again as fresh entity syntax. Return the fully parsed string.

### Function Contract

**Inputs**

- `text`: a string of length $n$, where $1 \le n \le 10^5$, containing printable ASCII characters.

**Return value**

- The string produced by replacing every recognized HTML entity while leaving all other text unchanged.

### Examples

**Example 1**

- Input: `text = "&amp; is an HTML entity but &ambassador; is not."`
- Output: `"& is an HTML entity but &ambassador; is not."`

**Example 2**

- Input: `text = "x &gt; y &amp;&amp; x &lt; y is false"`
- Output: `"x > y && x < y is false"`

**Example 3**

- Input: `text = "leetcode.com&frasl;problemset&frasl;all"`
- Output: `"leetcode.com/problemset/all"`
