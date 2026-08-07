## Description

You are given an array of strings `words` and an integer `k`.

Two words `a` and `b` at **distinct indices** are **prefix-connected** if $a[0..k-1] = b[0..k-1]$.

A **connected group** is a set of words such that each pair of words is prefix-connected.

Return the **number of connected groups** that contain **at least** two words, formed from the given words.

**Note:**

- Words with length less than `k` cannot join any group and are ignored.

- Duplicate strings are treated as separate words.
### Function Contract

**Inputs**

- `words`: The array whose words may form prefix-connected groups.
- `k`: The exact prefix length used for every connectivity comparison.

Let $N=\lvert\texttt{words}\rvert$ and $K=\texttt{k}$. Only a word of length at least $K$ has a valid length-$K$ prefix. For every such prefix $p$, define

$$
C(p)=\left\lvert\left\{i\mid \lvert\texttt{words}[i]\rvert\ge K
\text{ and }\texttt{words}[i][0..K-1]=p\right\}\right\rvert.
$$

All indices with the same prefix form one maximal connected group. The requested groups are exactly the prefixes $p$ for which $C(p)\ge 2$.

**Return value**

Return the number of distinct valid length-$K$ prefixes that occur at two or more indices.

### Examples

#### Example 1

<div class="example-block">
**Input:** words = ["apple","apply","banana","bandit"], k = 2

**Output:** 2

**Explanation:**

Words sharing the same first $k = 2$ letters are grouped together:

- $\text{words}[0] = "apple"$ and $\text{words}[1] = "apply"$ share prefix `"ap"`.

- $\text{words}[2] = "banana"$ and $\text{words}[3] = "bandit"$ share prefix `"ba"`.

Thus, there are 2 connected groups, each containing at least two words.

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["car","cat","cartoon"], k = 3

**Output:** 1

**Explanation:**

Words are evaluated for a prefix of length $k = 3$:

- $\text{words}[0] = "car"$ and $\text{words}[2] = "cartoon"$ share prefix `"car"`.

- $\text{words}[1] = "cat"$ does not share a 3-length prefix with any other word.

Thus, there is 1 connected group.

</div>
#### Example 3

<div class="example-block">
**Input:** words = ["bat","dog","dog","doggy","bat"], k = 3

**Output:** 2

**Explanation:**

Words are evaluated for a prefix of length $k = 3$:

- $\text{words}[0] = "bat"$ and $\text{words}[4] = "bat"$ form a group.

- $\text{words}[1] = "dog"$, $\text{words}[2] = "dog"$ and $\text{words}[3] = "doggy"$ share prefix `"dog"`.

Thus, there are 2 connected groups, each containing at least two words.

</div>
### Constraints

- $1 \le \text{words.length} \le 5000$

- $1 \le \text{words}[i].length \le 100$

- $1 \le k \le 100$

- All strings in `words` consist of lowercase English letters.