### 1. Description

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor $g[i]$, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size $s[j]$. If $s[j] \ge g[i]$, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

### 2. Function Contract

**Inputs**

- `g`: The nonempty list of children's greed factors.
- `s`: The list of available cookie sizes, which may be empty.

**Return value**

- Return the maximum number of children that can be made content by a one-to-one cookie assignment.

A cookie whose size exactly equals a child's greed factor is sufficient.

### 3. Examples

#### Example 1

- **Input:** $g = [1,2,3], s = [1,1]$
- **Output:** `1`
- **Explanation:** You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

#### Example 2

- **Input:** $g = [1,2], s = [1,2,3]$
- **Output:** `2`
- **Explanation:** You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

### 4. Constraints

- $1 \le \text{g.length} \le 3 * 10^{4}$

- $0 \le \text{s.length} \le 3 * 10^{4}$

- $1 \le g[i], s[j] \le 2^{31} - 1$

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/" target="_blank"> 2410: Maximum Matching of Players With Trainers.</a>
