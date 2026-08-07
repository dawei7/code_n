## Description

You are given the `head` of a linked list containing unique integer values and an integer array `nums` that is a subset of the linked list values.

Return the number of **connected** **components** in `nums`. A connected component is a non-empty, maximal sequence of **consecutive** nodes in the linked list such that every node's value belongs to nums.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/lc-linkedlistcom1.jpg)

- **Input:** $head = [0,1,2,3], nums = [0,1,3]$
- **Output:** `2`
- **Explanation:** 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
#### Example 2

![](images/lc-linkedlistcom2.jpg)

- **Input:** $head = [0,1,2,3,4], nums = [0,3,1,4]$
- **Output:** `2`
- **Explanation:** 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
### Constraints

- The number of nodes in the linked list is `n`.

- $1 \le n \le 10^{4}$

- $0 \le \text{Node.val} < n$

- All the values `Node.val` are **unique**.

- $1 \le \text{nums.length} \le n$

- $0 \le \text{nums}[i] < n$

- All the values of `nums` are **unique**.