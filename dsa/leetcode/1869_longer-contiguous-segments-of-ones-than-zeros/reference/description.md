## Description

Given a binary string `s`, return `true`* if the **longest** contiguous segment of *`1`'*s is **strictly longer** than the **longest** contiguous segment of *`0`'*s in *`s`, or return `false`* otherwise*.

- For example, in `s = "<u>11</u>01<u>000</u>10"` the longest continuous segment of `1`s has length `2`, and the longest continuous segment of `0`s has length `3`.

Note that if there are no `0`'s, then the longest continuous segment of `0`'s is considered to have a length `0`. The same applies if there is no `1`'s.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `s = "1101"`
- **Output:** `true`
- **Explanation:**
The longest contiguous segment of 1s has length 2: "<u>11</u>01"
The longest contiguous segment of 0s has length 1: "11<u>0</u>1"
The segment of 1s is longer, so return true.
#### Example 2

- **Input:** `s = "111000"`
- **Output:** `false`
- **Explanation:**
The longest contiguous segment of 1s has length 3: "<u>111</u>000"
The longest contiguous segment of 0s has length 3: "111<u>000</u>"
The segment of 1s is not longer, so return false.
#### Example 3

- **Input:** `s = "110100010"`
- **Output:** `false`
- **Explanation:**
The longest contiguous segment of 1s has length 2: "<u>11</u>0100010"
The longest contiguous segment of 0s has length 3: "1101<u>000</u>10"
The segment of 1s is not longer, so return false.
### Constraints

- $1 \le \text{s.length} \le 100$

- $s[i]$ is either `'0'` or `'1'`.