## Description

Given a string `s`, return *the number of substrings that have only **one distinct** letter*.
### Function Contract

**Inputs**

- `s`: The non-empty string whose contiguous substrings are counted.

Let $n = \lvert s\rvert$. Each candidate substring is identified by an interval with start and end positions inside `s`; the interval qualifies only when its set of characters has size one.

**Return value**

- Return the integer number of qualifying non-empty intervals. Occurrences at different positions count separately even when their substring text is identical.

### Examples

#### Example 1

- **Input:** `s = "aaaba"`
- **Output:** `8`
- **Explanation:** The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
#### Example 2

- **Input:** `s = "aaaaaaaaaa"`
- **Output:** `55`
### Constraints

- $1 \le \text{s.length} \le 1000$

- $s[i]$ consists of only lowercase English letters.