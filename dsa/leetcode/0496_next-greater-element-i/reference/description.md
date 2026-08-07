## Description

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each $0 \le i < \text{nums1.length}$, find the index `j` such that $\text{nums1}[i] = \text{nums2}[j]$ and determine the **next greater element** of $\text{nums2}[j]$ in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array *`ans`* of length *`nums1.length`* such that *$\text{ans}[i]$* is the **next greater element** as described above.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $nums1 = [4,1,2], nums2 = [1,3,4,2]$
- **Output:** `[-1,3,-1]`
- **Explanation:** The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,<u>4</u>,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [<u>1</u>,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,<u>2</u>]. There is no next greater element, so the answer is -1.
#### Example 2

- **Input:** $nums1 = [2,4], nums2 = [1,2,3,4]$
- **Output:** `[3,-1]`
- **Explanation:** The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,<u>2</u>,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,<u>4</u>]. There is no next greater element, so the answer is -1.
### Constraints

- $1 \le \text{nums1.length} \le \text{nums2.length} \le 1000$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 10^{4}$

- All integers in `nums1` and `nums2` are **unique**.

- All the integers of `nums1` also appear in `nums2`.

**Follow up:** Could you find an $O(\text{nums1.length} + \text{nums2.length})$ solution?