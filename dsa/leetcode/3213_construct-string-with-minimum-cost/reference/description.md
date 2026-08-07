### 1. Description

You are given a string `target`, an array of strings `words`, and an integer array `costs`, both arrays of the same length.

Imagine an empty string `s`.

You can perform the following operation any number of times (including **zero**):

- Choose an index `i` in the range `[0, words.length - 1]`.

- Append $\text{words}[i]$ to `s`.

- The cost of operation is $\text{costs}[i]$.

Return the **minimum** cost to make `s` equal to `target`. If it's not possible, return `-1`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]

**Output:** 7

**Explanation:**

The minimum cost can be achieved by performing the following operations:

- Select index 1 and append `"abc"` to `s` at a cost of 1, resulting in `s = "abc"`.

- Select index 2 and append `"d"` to `s` at a cost of 1, resulting in `s = "abcd"`.

- Select index 4 and append `"ef"` to `s` at a cost of 5, resulting in `s = "abcdef"`.

</div>
#### Example 2

<div class="example-block">
**Input:** target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]

**Output:** -1

**Explanation:**

It is impossible to make `s` equal to `target`, so we return -1.

</div>

### 4. Constraints

- $1 \le \text{target.length} \le 5 * 10^{4}$

- $1 \le \text{words.length} = \text{costs.length} \le 5 * 10^{4}$

- $1 \le \text{words}[i].length \le \text{target.length}$

- The total sum of $\text{words}[i].length$ is less than or equal to $5 * 10^{4}$.

- `target` and $\text{words}[i]$ consist only of lowercase English letters.

- $1 \le \text{costs}[i] \le 10^{4}$