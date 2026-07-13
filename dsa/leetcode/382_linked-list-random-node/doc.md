# Linked List Random Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 382 |
| Difficulty | Medium |
| Topics | Linked List, Math, Reservoir Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-random-node/) |

## Problem Description
### Goal
Initialize a selector from the head of a nonempty singly linked list whose total length need not be supplied separately. Each `getRandom()` call must choose one node position from the complete list with equal probability.

Return the selected node's stored value. Nodes with equal values remain separate equally likely positions, so their shared value may appear with correspondingly greater probability. Successive calls perform new random selections and must not consume or rearrange the list. Support the intended constant-extra-space reservoir behavior when the list size is not pre-indexed; the app adapter performs the requested number of draws.

### Function Contract
**Inputs**

- `head`: the head of a nonempty singly linked list
- `draws`: for the app adapter, the number of successive random selections to perform

**Return value**

- The app adapter returns a list containing `draws` selected values. Native LeetCode calls `getRandom()` once per requested selection.

### Examples
**Example 1**

- Input: `head = [1,2,3], draws = 4`
- Output: one valid result is `[2,1,3,2]`

**Example 2**

- Input: `head = [7], draws = 3`
- Output: `[7,7,7]`

**Example 3**

- Input: `head = [-2,5,-2], draws = 2`
- Output: one valid result is `[-2,5]`

### Required Complexity

- **Time:** $O(n + draws)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn node positions into equally likely array positions**

Traverse the linked list once during initialization and append every node value to a dense array. This preserves occurrences rather than only distinct values: if the same value appears in several nodes, it occupies several array positions, exactly matching the greater probability contributed by those nodes.

**Choose a fresh uniform index for every call**

For each request, select one array position uniformly at random and return its value. Every one of the `n` node positions maps to exactly one of the `n` equally likely array indices, so each node has probability $1 / n$. Repeating the random choice independently supplies the requested sequence of draws.

**Separate semantic validation from one random sample**

A finite run cannot prove that a generator is uniformly distributed, and it should not be compared with one predetermined sequence. The package therefore checks that the solution returns the requested number of values and that every result occurs in the input list. The implementation's uniform-index rule establishes the stronger probability requirement.

#### Complexity detail

Materializing `n` node values costs $O(n)$ time and $O(n)$ space. Each random selection is $O(1)$, so `draws` requests take $O(draws)$ additional time and the whole app-adapter call costs $O(n + draws)$.

#### Alternatives and edge cases

- **Reservoir sampling per call:** traverses the list using $O(1)$ extra space and still selects every node uniformly, but costs $O(n)$ time for every draw.
- **Store nodes instead of values:** also supports constant-time draws but retains node objects when only their values are needed.
- **Sample distinct values:** is incorrect when duplicate values occupy different numbers of nodes because it changes their required probabilities.
- A one-node list must return that node's value on every draw.
- Duplicate values must retain one array entry per occurrence.
- Negative and zero values require no special handling.
- Zero app-adapter draws return an empty result without making a random call.

</details>
