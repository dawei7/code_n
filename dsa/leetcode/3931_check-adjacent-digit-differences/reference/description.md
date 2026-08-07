## Description

You are given a string `s` consisting of digits.

Return `true` if the **absolute difference** between every pair of **adjacent** digits is at most 2, otherwise return `false`.

The absolute difference between `a` and `b` is defined as $abs(a - b)$.
### Function Contract

**Input**

- `s`: A string containing only the characters `0` through `9`.

Let $N=\lvert\texttt{s}\rvert$. Every index from $0$ through $N-2$ begins exactly one adjacent pair, namely `s[i]` and `s[i + 1]`. Leading zeroes are ordinary digits and remain part of the string.

**Return value**

Return a boolean that is `true` exactly when

$$
\left\lvert \operatorname{digit}(\texttt{s[i]})-
\operatorname{digit}(\texttt{s[i+1]})\right\rvert\le 2
$$

for every integer $i$ satisfying $0\le i<N-1$. Equality with $2$ is allowed.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "132"

**Output:** true

**Explanation:**

- The absolute difference between digits at $s[0]$ and $s[1]$ is $abs(1 - 3) = 2$.

- The absolute difference between digits at $s[1]$ and $s[2]$ is $abs(3 - 2) = 1$.

- Since both differences are at most 2, the answer is true.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "129"

**Output:** false

**Explanation:**

- The absolute difference between digits at $s[0]$ and $s[1]$ is $abs(1 - 2) = 1$.

- The absolute difference between digits at $s[1]$ and $s[2]$ is $abs(2 - 9) = 7$, which is greater than 2.

- Therefore, the answer is false.

</div>
### Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists only of digits.