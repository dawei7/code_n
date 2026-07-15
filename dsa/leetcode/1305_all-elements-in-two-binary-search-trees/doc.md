# All Elements in Two Binary Search Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1305 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Search Tree, Sorting, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) |

## Problem Description
### Goal
Two binary search trees are given by their roots, `root1` and `root2`. Collect every node value from both trees and return those values together in ascending order.

Values that occur in both trees are not deduplicated: each node contributes one entry to the result. Either root may be null because each tree is allowed to contain no nodes, so the answer may come entirely from one tree or may be empty when both roots are null.

### Function Contract
**Inputs**

- `root1`: the root of the first binary search tree, or null.
- `root2`: the root of the second binary search tree, or null.
- Each tree contains between 0 and 5000 nodes.
- Every node value lies in the inclusive range $[-10^5,10^5]$.

Let $n$ and $m$ be the numbers of nodes in the first and second trees, respectively, and let $N=n+m$.

**Return value**

An array of length $N$ containing every node value from both trees in ascending order, with multiplicities preserved.

### Examples
**Example 1**

- Input: `root1 = [2,1,4]`, `root2 = [1,0,3]`
- Output: `[0,1,1,2,3,4]`
- Explanation: Both nodes with value 1 remain in the merged result.

**Example 2**

- Input: `root1 = [1,null,8]`, `root2 = [8,1]`
- Output: `[1,1,8,8]`

**Example 3**

- Input: `root1 = []`, `root2 = []`
- Output: `[]`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Expose the ordering already present in each tree**

An in-order traversal visits a binary search tree's values in ascending order. Traverse each tree iteratively with a stack, producing two sorted arrays `first` and `second`. The iterative form also handles a valid tree that degenerates into a chain without depending on the language's recursion limit.

**Merge instead of sorting again**

Maintain one index into each sorted array. At every step, append the smaller current value; when the values are equal, either side may be chosen because the other equal value remains available for a later step. Once one array is exhausted, append the unused suffix of the other.

Every node enters exactly one traversal array. During the merge, the smallest value not yet returned must be at the front of one of the two remaining suffixes, so choosing the smaller front preserves ascending order. Advancing exactly one index per append also preserves duplicates and places all $N$ node values in the answer.

#### Complexity detail

The two traversals visit $n+m=N$ nodes, and the merge processes $N$ values, for $O(N)$ time. The traversal arrays, result, and explicit stacks use $O(N)$ space in the worst case. If only auxiliary space beyond the returned array is counted, the two stored traversal arrays still require $O(N)$.

#### Alternatives and edge cases

- **Collect then sort:** Traversing both trees into one unsorted array and applying a comparison sort is simpler, but it takes $O(N\log N)$ time instead of using the BST ordering.
- **Two lazy in-order iterators:** Keeping one stack per tree and merging their next values avoids the two complete traversal arrays; auxiliary space becomes $O(h_1+h_2)$ beyond the output, where $h_1$ and $h_2$ are tree heights.
- **Repeated sorted insertion:** Inserting each visited value into its position in a growing array is correct but can take $O(N^2)$ time because later insertions may scan and shift many entries.
- **Empty input trees:** If one root is null, return the other tree's in-order sequence; if both are null, return an empty array.
- **Repeated values:** Equal values from different nodes must appear separately in the result.
- **Skewed trees:** An explicit traversal stack avoids recursion-depth failures on long chains.

</details>
