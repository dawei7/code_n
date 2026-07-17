# Delivering Boxes from Storage to Ports

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1687 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Segment Tree, Queue, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) |

## Problem Description
### Goal

A single ship must deliver a queue of boxes from storage. Each entry `boxes[i] = [port_i, weight_i]` gives the destination and weight of the next box. The ship may load a nonempty prefix of the remaining queue, but one load may contain at most `maxBoxes` boxes and have total weight at most `maxWeight`. Consequently, every load is a consecutive segment of the original order; boxes cannot be skipped or rearranged.

For each load, the ship leaves storage and visits the loaded boxes' destination ports in order. Consecutive boxes for the port where the ship is already located require no additional movement. After unloading the batch, the ship returns to storage before loading again, and it must also end at storage after the final delivery. Return the minimum total number of movements between storage and ports or between distinct ports. `portsCount` specifies the available port identifiers but does not change a batch's travel cost by itself.

### Function Contract
**Inputs**

- `boxes`: a length-$n$ list of `[port, weight]` pairs in mandatory delivery order
- `portsCount`: the number of destination ports, numbered from 1 through this value
- `maxBoxes`: the largest number of boxes one load may contain
- `maxWeight`: the largest total weight one load may contain

**Return value**

The minimum number of location-to-location trips required to deliver every box and finish back at storage.

### Examples
**Example 1**

- Input: `boxes = [[1,1], [2,1], [1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3`
- Output: `4`

Loading all boxes visits port 1, port 2, port 1, and then storage.

**Example 2**

- Input: `boxes = [[1,2], [3,3], [3,1], [3,1], [2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6`
- Output: `6`

The optimal loads contain the first box, the middle three boxes, and the final box.

**Example 3**

- Input: `boxes = [[1,4], [1,2], [2,1], [2,1], [3,2], [3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7`
- Output: `6`

The weight limit makes three same-port batches optimal.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express the final load as a prefix transition**

Let `dp[i]` be the minimum travel count after delivering the first `i` boxes and returning to storage. A final load that begins at index `j` and ends just before `i` is legal exactly when $i-j \le \texttt{maxBoxes}$ and its prefix-sum weight does not exceed `maxWeight`.

Create `changes[k]` for box index `k`: the number of adjacent destination changes from box 0 through box `k`, with `changes[0] = 0`. The loaded segment from `j` through `i-1` crosses `changes[i - 1] - changes[j]` port boundaries. It also needs one movement from storage to its first port and one back to storage, so

$$
\texttt{dp[i]} = \texttt{changes[i-1]} + 2
  + \min_j\left(\texttt{dp[j]} - \texttt{changes[j]}\right)
$$

over all capacity-feasible starts `j`. Subtracting `changes[j]` correctly excludes the boundary between box `j - 1` and the new load's first box; the ship returned to storage at that split.

**Turn feasibility into a sliding interval**

As `i` increases, legal starts form a contiguous suffix of earlier indices. A start falls out forever once the box count is too large. Because every weight is positive, it also falls out forever once the prefix-weight difference exceeds `maxWeight`. Remove such indices from the front of a deque.

**Keep only undominated transition values**

Among feasible starts, the recurrence needs the minimum `dp[j] - changes[j]`. Store candidate indices in non-decreasing order of that value. Before appending a new index, remove candidates from the back while their value is at least the new value: they can never be preferable, and they expire no later because they are older. The deque front is therefore the best legal start for the next state.

Every possible schedule ends with some capacity-feasible consecutive load, so the recurrence considers its preceding optimal prefix. Conversely, combining a recorded prefix schedule with any feasible transition constructs a legal schedule whose added travel is counted exactly. The deque removes only expired starts or starts dominated in both value and lifetime, so its front preserves the recurrence minimum. Induction over `i` proves `dp[n]` is optimal.

#### Complexity detail

Prefix arrays and DP states take $O(n)$ space. Each candidate index enters the deque once, leaves its front at most once, and leaves its back at most once. All prefix and transition work is therefore $O(n)$ time, with $O(n)$ auxiliary space overall.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** scan every feasible start for every prefix; it uses the same recurrence but takes $O(n^2)$ time when capacities allow long batches.
- **Segment tree or heap:** range-minimum or lazy-expiration structures can evaluate transitions in $O(n \log n)$ time, but the feasible interval's monotone movement permits a linear deque.
- **Greedily fill every load:** maximizing each batch size can miss a better split at a port-run boundary and is not generally optimal.
- **Repeated destination:** consecutive boxes for the same port add weight and box count but no port-to-port movement.
- **Both limits apply:** a candidate start must satisfy the box-count and weight constraints simultaneously.
- **Single box:** its only schedule moves storage to its port and back, for a result of two.
- **Final return:** the last batch must return to storage just like every earlier batch.

</details>
