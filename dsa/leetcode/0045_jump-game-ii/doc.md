# Jump Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 45 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-ii/) |

## Problem Description
### Goal
You begin at index zero of a nonempty array. At position `i`, the nonnegative value `nums[i]` is the greatest number of indices that one jump may move forward; any shorter positive jump within the array is also allowed.

Return the minimum number of jumps needed to reach the final index. The input guarantees that some legal sequence reaches it, so no impossible-result marker is needed. A one-element array already starts at its destination and therefore requires zero jumps.

### Function Contract
**Inputs**

- `nums`: non-empty `List[int]` of non-negative maximum jump lengths

**Return value**

The minimum jump count as an `int`.

### Examples
**Example 1**

- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `2`

**Example 2**

- Input: `nums = [2, 3, 0, 1, 4]`
- Output: `2`

**Example 3**

- Input: `nums = [0]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compress breadth-first-search layers into index boundaries**

Every index reachable with the same number of jumps forms a contiguous range. Maintain `current_end`, the last index of the current range, and `farthest`, the greatest endpoint reachable by one jump from any position scanned in that range.

When the scan reaches `current_end`, every possible departure point for the current jump count has been considered. Reaching a later index requires one additional jump, so increment the count and set `current_end = farthest`. This is breadth-first search over implicit jump edges without storing individual neighbors or a queue.

Scan only through the penultimate index. The final index needs to be reached, not used as the start of another jump; processing it could add a spurious extra jump.

**Finish a whole layer before committing to the next jump**

Before scanning a layer, every index through `current_end` is reachable in at most `jumps` moves, and no later index is reachable in fewer moves. While scanning that layer, `farthest` is the maximum endpoint of one additional jump from any departure index seen so far.

Choosing a jump before the layer ends could miss a later departure point with a much longer reach. Waiting until `current_end` ensures the next boundary is the union of all one-jump possibilities, exactly as breadth-first search expands an entire frontier before increasing distance.

**Trace the frontier expansion**

For `[2, 3, 1, 1, 4]`, the first layer contains only index 0 and reaches through index 2, so jump count becomes 1. Scanning indices 1 and 2 discovers reach through index 4; closing that layer increments the count to 2, which reaches the end.

**Contiguous BFS layers certify the minimum jump count**

Indices reachable with the same number of jumps form a contiguous layer ending at `current_end`. Scanning every index in that layer and taking the greatest `i + nums[i]` computes the union of all positions reachable with one additional jump, whose boundary is `farthest`.

The jump count advances only after the complete current layer has contributed, exactly as breadth-first search finishes one distance before entering the next. A shorter route cannot be hidden in a later layer. Therefore the first new boundary that reaches the final index uses the minimum possible number of jumps.

#### Complexity detail

The scan visits each departure index once and performs constant work, so time is $O(n)$. Three integer boundaries/counters are sufficient, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Dynamic programming over prior indices:** computes minimum jumps but can require $O(n^2)$ time and $O(n)$ space.
- **Explicit BFS queue:** preserves minimum-path reasoning but stores many indices that contiguous layer boundaries summarize.
- **Always jump from the locally largest value:** ignores how far into the array that value occurs and is not generally optimal.
- A one-element array needs zero jumps. The reachability guarantee ensures `farthest` advances whenever another layer is required; variants without that guarantee should detect a stalled frontier.
- Reaching or passing the last index is equivalent because jump lengths are maxima and a shorter landing distance may be chosen.

</details>
