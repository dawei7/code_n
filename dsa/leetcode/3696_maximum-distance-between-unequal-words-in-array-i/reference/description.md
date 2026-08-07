## Description

You are given a string array `words`.

Find the **maximum distance** between two **distinct** indices `i` and `j` such that:

- $\text{words}[i] \neq \text{words}[j]$, and

- the distance is defined as $j - i + 1$.

Return the maximum distance among all such pairs. If no valid pair exists, return 0.
### Function Contract

**Inputs**

- `words`: A nonempty array of lowercase English strings.

A candidate uses two distinct indices $i<j$. The candidate is valid only when `words[i] != words[j]`, and its distance is $j-i+1$, not merely the index difference.

**Return value**

Return the maximum distance among all valid pairs, or `0` when no unequal pair exists.

### Examples
#### Example 1

<div class="example-block">
**Input:** words = ["leetcode","leetcode","codeforces"]

**Output:** 3

**Explanation:**

In this example, $\text{words}[0]$ and $\text{words}[2]$ are not equal, and they have the maximum distance $2 - 0 + 1 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["a","b","c","a","a"]

**Output:** 4

**Explanation:**

In this example $\text{words}[1]$ and $\text{words}[4]$ have the largest distance of $4 - 1 + 1 = 4$.

</div>
#### Example 3

<div class="example-block">
**Input:** words = ["z","z","z"]

**Output:** 0

**Explanation:**

In this example all the words are equal, thus the answer is 0.

</div>
### Constraints

- $1 \le \text{words.length} \le 100$

- $1 \le \text{words}[i].length \le 10$

- $\text{words}[i]$ consists of lowercase English letters.