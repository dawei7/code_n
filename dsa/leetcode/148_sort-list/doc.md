# Sort List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 148 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-list/) |

## Problem Description
### Goal
Given the head of a linked list, sort it in ascending order. The result must contain the same nodes exactly once, including duplicates and negative values, and its final node must point to `null`.

Return the new head of the sorted chain, or `null` when the input list is empty. Meet the required $O(n \log n)$ running time and constant space target, which rules out quadratic comparison sorting and copying all values into a separate array. Sorting may change which original node becomes the head but must not replace the list with newly allocated value copies.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of integer values in app cases

**Return value**

The head node of the same linked-list nodes rearranged into sorted order.

### Examples
**Example 1**

- Input: `head = [4,2,1,3]`
- Output: `[1,2,3,4]`

**Example 2**

- Input: `head = [-1,5,3,4,0]`
- Output: `[-1,0,3,4,5]`

**Example 3**

- Input: `head = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Iterative run widths remove recursive stack space**

Count the list length, then treat every node as a sorted run of width one. In a pass of width `w`, merge adjacent runs of at most `w` nodes and double `w` afterward. Once $w \ge n$, one sorted run covers the complete list. Iteration avoids the $O(\log n)$ call stack of top-down merge sort.

**Cutting runs prevents one merge from consuming the next pair**

Starting from the unprocessed suffix, split off at most `w` nodes as `left`, then at most `w` nodes as `right`. Each split terminates its run with null and returns the first node after it. Save that remainder before merging so the next run pair stays reachable.

**Merge heads and return the merged tail for constant-time concatenation**

Compare run heads, append the smaller node to the pass output tail, and advance that run. When one run empties, append the other. Track or discover the merged tail once so the next pair can be connected without rescanning the entire accumulated output.

Choosing the left node on equality makes the merge stable, although only sorted values are required.

**Every width-doubling pass coalesces sorted adjacent runs**

At the start of a pass of width `w`, the list consists of sorted runs of length at most `w`. Each merge produces a sorted run of length at most `2w`, so doubling the width establishes the next pass's invariant.

**Merged run width doubles toward the whole list**

Each pass begins with sorted runs of at most the current width. Merging two adjacent runs always selects the smaller remaining head, preserving every node and producing one sorted run of at most twice that width.

One-node runs are trivially sorted. Doubling the width after every complete pass preserves the run invariant until a single run spans the list, at which point the entire chain is sorted.

#### Complexity detail

Each merge pass processes every node once, and there are $\lceil \log_2 n \rceil$ passes, giving $O(n \log n)$ time. Iteration uses only a dummy node and a constant number of pointers, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Top-down merge sort:** is natural but consumes $O(\log n)$ recursion stack space.
- **Insertion sort:** relinks in place but degrades to $O(n^2)$.
- **Array sorting:** is concise but requires $O(n)$ storage for node references or values.
- Empty and one-node lists return immediately. The final run in a pass may be shorter than the width or have no partner.
- Pointer splitting must null-terminate runs; otherwise the merge can cross into later nodes and duplicate or cycle links.

</details>
