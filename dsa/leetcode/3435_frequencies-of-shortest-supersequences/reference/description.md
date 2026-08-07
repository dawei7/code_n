### 1. Description

You are given an array of strings `words`. Find all **shortest common supersequences (SCS)** of `words` that are not permutations of each other.

A **shortest common supersequence** is a string of **minimum** length that contains each string in `words` as a subsequence.

Return a 2D array of integers `freqs` that represent all the SCSs. Each $\text{freqs}[i]$ is an array of size 26, representing the frequency of each letter in the lowercase English alphabet for a single SCS. You may return the frequency arrays in any order.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** words = ["ab","ba"]

**Output: **[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**Explanation:**

The two SCSs are `"aba"` and `"bab"`. The output is the letter frequencies for each one.

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["aa","ac"]

**Output: **[[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**Explanation:**

The two SCSs are `"aac"` and `"aca"`. Since they are permutations of each other, keep only `"aac"`.

</div>
#### Example 3

<div class="example-block">
**Input:** words = ["aa","bb","cc"]

**Output: **[[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**Explanation:**

`"aabbcc"` and all its permutations are SCSs.

</div>

### 4. Constraints

- $1 \le \text{words.length} \le 256$

- $\text{words}[i].length = 2$

- All strings in `words` will altogether be composed of no more than 16 unique lowercase letters.

- All strings in `words` are unique.