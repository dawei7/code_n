### 1. Description

You are given a string `s` and an integer `k`.

First, you are allowed to change **at most** **one** index in `s` to another lowercase English letter.

After that, do the following partitioning operation until `s` is **empty**:

- Choose the **longest** **prefix** of `s` containing at most `k` **distinct** characters.

- **Delete** the prefix from `s` and increase the number of partitions by one. The remaining characters (if any) in `s` maintain their initial order.

Return an integer denoting the **maximum** number of resulting partitions after the operations by optimally choosing at most one index to change.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "accca", k = 2

**Output:** 3

**Explanation:**

The optimal way is to change $s[2]$ to something other than a and c, for example, b. then it becomes `"acbca"`.

Then we perform the operations:

- The longest prefix containing at most 2 distinct characters is `"ac"`, we remove it and `s` becomes `"bca"`.

- Now The longest prefix containing at most 2 distinct characters is `"bc"`, so we remove it and `s` becomes `"a"`.

- Finally, we remove `"a"` and `s` becomes empty, so the procedure ends.

Doing the operations, the string is divided into 3 partitions, so the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aabaab", k = 3

**Output:** 1

**Explanation:**

Initially `s` contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "xxyz", k = 1

**Output:** 4

**Explanation:**

The optimal way is to change $s[0]$ or $s[1]$ to something other than characters in `s`, for example, to change $s[0]$ to `w`.

Then `s` becomes `"wxyz"`, which consists of 4 distinct characters, so as `k` is 1, it will divide into 4 partitions.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists only of lowercase English letters.

- $1 \le k \le 26$