## Description

You are given an integer array `nums` of length `n`.

Alice and Bob are playing a game. Alice chooses:

- An integer `k` such that `k > 1`.

- Two integers `l` and `r` such that $0 \le l \le r < n$.

Initially, both Alice's and Bob's scores are 0.

For each index `i` in the range `[l, r]` (inclusive):

- If $\text{nums}[i]$ is divisible by `k`, Alice's score **increases** by $\text{nums}[i]$.

- Otherwise, Bob's score **increases** by $\text{nums}[i]$.

The **score difference** is Alice's score **minus** Bob's score.

Alice wants to **maximize** the score difference. If there are multiple values of `k` that achieve the **maximum** score difference, she chooses the **smallest** such `k`.

Return the **product** of the **maximum** score difference and the chosen value of `k`. Since the result can be large, return it **modulo** $10^{9} + 7$.
### Function Contract

`solve(nums) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A nonempty array of positive integers from which Alice must choose one inclusive range.

Alice also chooses an integer $k>1$. Within her selected range, each multiple of $k$ contributes positively to the difference and each nonmultiple contributes negatively. The range may contain one element.

**Output**

Return `(maximum score difference * smallest maximizing k) mod 1_000_000_007`. The maximum difference can be negative, but the returned residue is in the usual nonnegative modulo range.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,4,6,8]

**Output:** 36

**Explanation:**

- Alice can choose $k = 2$, $l = 1$, and $r = 3$.

- All values in `nums[1..3]` are divisible by 2, so Alice's score is $4 + 6 + 8 = 18$, while Bob's score is 0.

- The score difference is 18, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2.

- Therefore, the answer is $18 * 2 = 36$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,1,2]

**Output:** 6

**Explanation:**

- Alice can choose $k = 2$, $l = 0$, and $r = 2$.

- The values $\text{nums}[0]$ and $\text{nums}[2]$ are divisible by 2, so Alice's score is $2 + 2 = 4$. The value $\text{nums}[1]$ is not divisible by 2, so Bob's score is 1.

- The score difference is $4 - 1 = 3$, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2.

- Therefore, the answer is $3 * 2 = 6$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** 1000000005

**Explanation:**

- Alice must choose some `k > 1`. The smallest possible choice is $k = 2$.

- Since $\text{nums}[0]$ is not divisible by 2, Alice's score is 0, while Bob's score is 1.

- The score difference is -1, which is the maximum possible.

- Therefore, the answer is $-1 * 2 = -2$. Modulo $10^{9} + 7$, this equals 1000000005.

</div>
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{6}$