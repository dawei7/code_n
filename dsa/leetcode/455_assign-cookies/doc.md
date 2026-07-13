# Assign Cookies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 455 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/assign-cookies/) |

## Problem Description
### Goal
Each child has a greed requirement `g[i]`, and each available cookie has a size `s[j]`. A child is satisfied only when assigned one cookie whose size is at least that child's requirement.

Assign each cookie to at most one child and each child at most one cookie. Return the maximum number of satisfied children. Unused cookies and unsatisfied children are allowed, and a larger cookie may satisfy a less greedy child but then cannot be reused. The function returns only the optimal count rather than a concrete assignment. An empty cookie list yields zero satisfied children.

### Function Contract
**Inputs**

- `g`: greed requirements for the children
- `s`: sizes of the available cookies

**Return value**

- The maximum number of children that can be satisfied by a one-to-one assignment

### Examples
**Example 1**

- Input: `g = [1, 2, 3], s = [1, 1]`
- Output: `1`

**Example 2**

- Input: `g = [1, 2], s = [1, 2, 3]`
- Output: `2`

**Example 3**

- Input: `g = [10, 9, 8, 7], s = [5, 6, 7, 8]`
- Output: `2`

### Required Complexity

- **Time:** $O(g \log g + s \log s)$
- **Space:** $O(g + s)$

<details>
<summary>Approach</summary>

#### General

**Consider the least demanding child first**

Sort greed requirements and cookie sizes. Maintain one pointer to the smallest unsatisfied greed. Scan cookies from smallest to largest, discarding a cookie when it is too small and assigning it when it meets the current requirement.

**Use the smallest cookie that can work**

When a cookie can satisfy the least greedy remaining child, assigning it is safe. Any feasible assignment that gives this child a larger cookie can swap in the current smaller cookie; the larger cookie remains available for a child with an equal or greater requirement. Thus the greedy assignment cannot reduce the number achievable by an optimum.

**Why an undersized cookie can be skipped**

If a cookie is smaller than the least remaining greed, it is also too small for every later child because the requirements are sorted. No future assignment can use it, so advancing only the cookie pointer loses nothing.

#### Complexity detail

Sorting takes $O(g \log g + s \log s)$ time for `g` children and `s` cookies. The two-pointer scan is $O(g + s)$. Sorted copies use $O(g + s)$ auxiliary space; in-place sorting reduces explicit copy space.

#### Alternatives and edge cases

- **Match from largest to largest:** satisfying the greediest child with the largest adequate cookie is the symmetric greedy strategy.
- **Repeatedly search for the smallest adequate cookie:** is correct but removing one match at a time can cost $O(g \cdot s)$.
- **Maximum bipartite matching:** models all valid assignments but is unnecessary because the threshold relation is totally ordered.
- **No children or no cookies:** the answer is zero.
- **Extra cookies:** once every child is satisfied, remaining cookies do not change the result.
- **Equal sizes and requirements:** each cookie can satisfy only one child, so duplicates retain their multiplicity.
- **Exact boundary:** a cookie whose size equals the greed requirement is sufficient.

</details>
