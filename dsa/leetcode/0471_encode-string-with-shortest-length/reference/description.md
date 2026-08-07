## Description

Given a string `s`, encode the string such that its encoded length is the shortest.

The encoding rule is: $k[\text{encoded}_{string}]$, where the $\text{encoded}_{string}$ inside the square brackets is being repeated exactly `k` times. `k` should be a positive integer.

If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return **any of them**.
### Function Contract

**Inputs**

- `s`: the nonempty lowercase English string to encode

**Return value**

- Return a minimum-length valid encoding whose decoded value is exactly `s`.

An encoded region has the form $k[\text{encoded}_{string}]$, where positive integer `k` is the number of consecutive copies
of the decoded bracketed string. Do not use that form for a region unless it is strictly shorter than leaving the
same region literal.

### Examples

#### Example 1

- **Input:** `s = "aaa"`
- **Output:** `"aaa"`
- **Explanation:** There is no way to encode it such that it is shorter than the input string, so we do not encode it.
#### Example 2

- **Input:** `s = "aaaaa"`
- **Output:** $"5[a]"$
- **Explanation:** "5[a]" is shorter than "aaaaa" by 1 character.
#### Example 3

- **Input:** `s = "aaaaaaaaaa"`
- **Output:** $"\text{10}[a]"$
- **Explanation:** "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
### Constraints

- $1 \le \text{s.length} \le 150$

- `s` consists of only lowercase English letters.