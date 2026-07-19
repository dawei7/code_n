# Snapshot Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1146 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/snapshot-array/) |

## Problem Description

### Goal

Implement `SnapshotArray`, an array-like data structure of a requested `length` whose elements initially equal `0`. It must support changing one current element with `set(index, val)` and preserving the current state with `snap()`. Each call to `snap()` returns its snapshot ID, defined as the total number of snapshots taken so far minus `1`.

The operation `get(index, snap_id)` must return the value stored at `index` in the state identified by `snap_id`, even if that index has changed afterward. Calls arrive in order, every queried snapshot has already been created, and the implementation must retain the historical states needed by later reads.

### Function Contract

**Inputs**

- `length`: the constructor length, where $1 \le \texttt{length} \le 5 \cdot 10^4$.
- `operations`: an ordered list of at most $5 \cdot 10^4$ method calls represented in cOde(n) as `[method, args]` pairs.
- `set(index, val)`: requires $0 \le \texttt{index} < \texttt{length}$ and $0 \le \texttt{val} \le 10^9$.
- `snap()`: takes no arguments and returns the next consecutive snapshot ID beginning at `0`.
- `get(index, snap_id)`: requires a valid index and $0 \le \texttt{snap_id} < k$, where $k$ is the number of preceding `snap()` calls.
- Let $q$ be the number of operations, $s$ the number of stored value-change records, and $u$ the number of records retained for the index used by a particular `get` call.

**Return value**

For the cOde(n) adapter, return the ordered results of all operations: `null` for each `set`, the new ID for each `snap`, and the historical integer value for each `get`.

### Examples

**Example 1**

- Input: `length = 3, operations = [["set", [0, 5]], ["snap", []], ["set", [0, 6]], ["get", [0, 0]]]`
- Output: `[null, 0, null, 5]`
- Explanation: Snapshot `0` retains the value `5` at index `0` even after the current value becomes `6`.
