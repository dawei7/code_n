## Description

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

- $i + minJump \le j \le min(i + maxJump, \text{s.length} - 1)$, and

- $s[j] = '0'$.

Return `true`* if you can reach index *$\text{s.length} - 1$* in *`s`*, or *`false`* otherwise.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `s = "<u>0</u>11<u>0</u>1<u>0</u>", minJump = 2, maxJump = 3`
- **Output:** `true`
- **Explanation:**
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.
#### Example 2

- **Input:** `s = "01101110", minJump = 2, maxJump = 3`
- **Output:** `false`
### Constraints

- $2 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'0'` or `'1'`.

- $s[0] = '0'$

- $1 \le minJump \le maxJump < \text{s.length}$