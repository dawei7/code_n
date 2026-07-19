# Two Out of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2032 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/two-out-of-three/) |

## Problem Description

### Goal

Given three integer arrays `nums1`, `nums2`, and `nums3`, identify every value
that occurs in at least two different arrays. Repeated copies inside a single
array still establish presence in only that one array; they do not satisfy the
two-array requirement by themselves.

Return each qualifying value exactly once. The result may list those distinct
values in any order. Values appearing in only one array must be omitted, while
a value shared by all three arrays qualifies as usual.

### Function Contract

Define

$$
S = \lvert \texttt{nums1} \rvert
  + \lvert \texttt{nums2} \rvert
  + \lvert \texttt{nums3} \rvert.
$$

**Inputs**

- `nums1`, `nums2`, and `nums3`: nonempty integer lists, each of length at
  most $100$, whose values lie from $1$ through $100$.

**Return value**

- A distinct list containing exactly the values present in at least two input
  arrays, in any order.

### Examples

**Example 1**

- Input: `nums1 = [1, 1, 3, 2], nums2 = [2, 3], nums3 = [3]`
- Output: `[3, 2]`
- Explanation: `3` appears in all three arrays and `2` appears in the first
  two.

**Example 2**

- Input: `nums1 = [3, 1], nums2 = [2, 3], nums3 = [1, 2]`
- Output: `[2, 3, 1]`

**Example 3**

- Input: `nums1 = [1, 2, 2], nums2 = [4, 3, 3], nums3 = [5]`
- Output: `[]`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Deduplicate each array before counting**

Convert one input array at a time to a set. For each value in that set,
increment a map recording the number of distinct arrays in which the value has
appeared. This prevents duplicates such as two copies of `2` in `nums1` from
being mistaken for presence in two arrays.

**Select values with at least two appearances**

After all three sets have contributed, return every map key whose count is two
or three. Each key occurs only once in the map, so the output is automatically
distinct.

A value receives one increment for each and only each input array containing
it. Its final count is therefore exactly its number of source arrays, making
the threshold test equivalent to the problem condition. Iterating map keys
once also ensures no qualifying value is duplicated in the result.

#### Complexity detail

Building the three sets and processing their members reads $S$ input elements,
so the expected time is $O(S)$. The per-array sets, appearance map, and result
store at most $O(S)$ distinct values in the general bound, using $O(S)$ space.
The stated value domain is even smaller, but the bound remains source-size
based.

#### Alternatives and edge cases

- **Bit masks per value:** Associate one bit with each input array and OR that
  bit into a value's mask. A mask with at least two set bits qualifies and
  gives the same $O(S)$ bounds.
- **Repeated membership scans:** For every encountered value, search all three
  arrays directly. This remains correct but can take $O(S^2)$ time.
- Duplicates inside one array count as only one array appearance.
- A value present in all three arrays must still appear only once in output.
- If the three arrays are pairwise disjoint, the result is empty.
- Output order is unconstrained and must not affect correctness.

</details>
