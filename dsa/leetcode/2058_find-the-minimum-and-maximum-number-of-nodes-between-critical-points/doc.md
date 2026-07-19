# Find the Minimum and Maximum Number of Nodes Between Critical Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2058 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) |

## Problem Description

### Goal

A critical point in a singly linked list is an internal node that is either a strict local maximum or a strict local minimum. Its value must be strictly greater than both neighboring values or strictly less than both. The head and tail cannot be critical because each lacks one neighbor.

Among all distinct critical-point pairs, find the minimum and maximum distances between their zero-based list positions. Return `[minDistance, maxDistance]`. If the list contains fewer than two critical points, neither distance exists, so return `[-1, -1]`.

### Function Contract

**Inputs**

- `head`: the first node of a singly linked list containing $n$ nodes, where $2 \le n \le 10^5$ and every node value is from $1$ through $10^5$.

**Return value**

- Return the minimum and maximum index differences among pairs of critical points.
- Return `[-1, -1]` when fewer than two critical points exist.

### Examples

**Example 1**

- Input: `head = [3,1]`
- Output: `[-1,-1]`
- Explanation: Neither endpoint can be critical.

**Example 2**

- Input: `head = [5,3,1,2,5,1,2]`
- Output: `[1,3]`
- Explanation: Critical positions are `2`, `4`, and `5`.

**Example 3**

- Input: `head = [1,3,2,2,3,2,2,2,7]`
- Output: `[3,3]`
- Explanation: The two critical positions are `1` and `4`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognizing critical nodes with three pointers**

Traverse using `previous`, `current`, and `next_node`. The current node is critical when its value is strictly above both neighbors or strictly below both. Starting with the second node and stopping before the tail automatically excludes the endpoints; equal neighboring values satisfy neither strict comparison.

**Keeping only the positions that determine the answers**

Record the first critical position, the immediately previous critical position, and the current minimum gap. When a new critical point appears, its distance from the previous one is a candidate minimum. The maximum distance is always between the first and last critical points because those are the extreme positions.

Consecutive critical points yield every candidate for the minimum: inserting an intermediate critical point can only split a wider gap into no-larger adjacent gaps. The most widely separated pair must use the earliest and latest positions. Thus the retained state is sufficient for both requested extrema.

#### Complexity detail

The traversal visits every node once and performs constant work per node, giving $O(n)$ time. It stores a fixed number of pointers, indices, and distances, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Store all critical positions:** A second pass over the position array makes the distance calculations simple but uses $O(n)$ extra space.
- **Compare every critical pair:** This directly finds both extrema but can take $O(n^2)$ time when values alternate.
- The head and tail are never critical, even if their values exceed their sole neighbors.
- Comparisons are strict; a plateau cannot contain a local maximum or minimum.
- Exactly two critical points produce equal minimum and maximum distances.

</details>
