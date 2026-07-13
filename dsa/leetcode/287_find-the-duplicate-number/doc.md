# Find the Duplicate Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 287 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) |

## Problem Description
### Goal
Given an array of $n + 1$ integers whose values all lie in the inclusive range `1..n`, exactly one distinct value occurs more than once. That duplicate may appear twice or several times, while every other value follows the input guarantee.

Return the duplicated value itself. Do not modify or sort the input array, and use only constant extra space. Meet the required subquadratic running time rather than comparing every pair. Treat array entries as values under the contract even though their bounded range also permits an implicit pointer structure; no missing value or duplicate index needs to be returned.

### Function Contract
**Inputs**

- `nums`: an array containing exactly one distinct duplicated value

**Return value**

The duplicated value.

### Examples
**Example 1**

- Input: `nums = [1,3,4,2,2]`
- Output: `2`

**Example 2**

- Input: `nums = [3,1,3,4,2]`
- Output: `3`

**Example 3**

- Input: `nums = [3,3,3,3,3]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Array values define a functional graph**

Treat each array index as a node whose next node is `nums[index]`. Because values stay in `1..n`, following pointers from index zero eventually enters a cycle. The duplicated value is the cycle entrance.

**Floyd's two phases locate the cycle entrance**

Advance one pointer once and another twice until they meet inside the cycle. Then reset one pointer to index zero and advance both once; their next meeting is the entrance.

**The cycle entrance is the duplicated value**

Every visited index has one outgoing edge to its stored value. Because the path begins outside the value range at index zero and then stays within `1..n`, it consists of a noncyclic prefix followed by a cycle. The first node receiving an edge from both the prefix side and the cycle predecessor is exactly a value with multiple array occurrences—the duplicate.

Let the prefix length be $\mu$ and the cycle length be $\lambda$. At the first slow/fast meeting, the slow pointer's distance inside the cycle is congruent to $-\mu\pmod{\lambda}$. Resetting one pointer to zero and advancing both one step makes each travel $\mu$ steps to the entrance, one directly and one by completing the corresponding cycle remainder.

#### Complexity detail

Both phases traverse $O(n)$ pointers and store two indices, without changing `nums`.

#### Alternatives and edge cases

- **Set or frequency table:** uses $O(n)$ extra space.
- **Count every candidate by rescanning:** takes $O(n^2)$.
- The duplicate may occur more than twice; the cycle reasoning still holds.

</details>
