# Next Greater Node In Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1019 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/next-greater-node-in-linked-list/) |

## Problem Description

### Goal

You are given the `head` of a singly linked list containing $N$ nodes. For each node, find the value of its next greater node: the first later node in list order whose value is strictly larger.

Return an integer array `answer` aligned with the list positions, where `answer[i]` is that next greater value for the node at position `i`. If no strictly larger node occurs later, set the corresponding result to `0`. Equal values do not satisfy the requirement.

### Function Contract

**Inputs**

- `head`: the first node of a nonempty singly linked list with $1\le N\le10^4$ nodes and $1\le\texttt{Node.val}\le10^9$.

**Return value**

- An $N$-element array containing each node's first strictly greater value to the right, or `0` when absent.

### Examples

**Example 1**

- Input: `head = [2, 1, 5]`
- Output: `[5, 5, 0]`
- Explanation: The final value `5` is the first greater value after both earlier nodes.

**Example 2**

- Input: `head = [2, 7, 4, 3, 5]`
- Output: `[7, 0, 5, 5, 0]`
- Explanation: No later value exceeds `7` or the final `5`.

**Example 3**

- Input: `head = [5, 4, 3]`
- Output: `[0, 0, 0]`
- Explanation: A strictly decreasing list has no next greater node.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Expose indexed values:** Traverse the linked list once and copy node values into an array. Initialize an equally sized answer array with zeroes and keep a stack of unresolved indices.

**Resolve smaller nodes at the first greater value:** Process values from left to right. While the stack is nonempty and `values[stack[-1]] < value`, pop that earlier index and set its answer to the current value. Then push the current index as unresolved.

**Preserve the nearest qualifying node:** Stack values are non-increasing. A node is popped at the first later value that exceeds it, so no closer qualifying node was skipped. Equal values remain on the stack because the comparison must be strictly larger.

Every index is eventually resolved by its first greater value or remains on the stack with its initialized zero. Since an index is pushed once and popped at most once, the method covers all positions without repeated suffix scans.

#### Complexity detail

Reading the $N$ nodes and processing the value array are linear. Each index enters and leaves the stack at most once, giving $O(N)$ time. The values, answer, and stack arrays use $O(N)$ space; the answer itself is required output.

#### Alternatives and edge cases

- **Scan every suffix:** Searching rightward independently from each node is direct but takes $O(N^2)$ time on a non-increasing list.
- **Reverse monotonic stack:** Processing copied values from right to left with a stack of candidate values also achieves $O(N)$ time.
- **Strictly decreasing list:** Every answer remains zero.
- **Equal values:** They do not resolve one another; only a strictly larger value qualifies.
- **Single node:** It has no later node, so return `[0]`.

</details>
