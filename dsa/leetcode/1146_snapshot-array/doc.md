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

### Required Complexity

- **Time:** $O(\log u)$
- **Space:** $O(\texttt{length}+s)$

<details>
<summary>Approach</summary>

#### General

**Store histories by index rather than arrays by snapshot.** Give every index a chronological list of `[snap_id, value]` records, initialized with value `0` at snapshot ID `0`. Unchanged indices then consume no additional storage when a snapshot is taken.

**Coalesce changes made before the same snapshot.** `set(index, val)` associates the new value with the current snapshot counter. If the last record for that index already has this counter, replace its value; otherwise append a new record. Calling `snap()` merely returns the current counter and increments it, so both operations take constant time.

**Find the last change visible to a historical read.** Records for an index have increasing snapshot IDs. Binary search for the rightmost record whose ID is at most the requested `snap_id`; that record is exactly the most recent assignment included in the snapshot. The initial zero record guarantees that this predecessor always exists. Later assignments carry larger IDs and therefore cannot affect the result.

#### Complexity detail

Each `set` and `snap` takes $O(1)$ time, while `get` takes $O(\log u)$ time for the queried index's $u$ records. Across $q$ operations this is $O(q\log u)$ in the worst case. The initial history for every array position uses $O(\texttt{length})$ space, and the effective change records add $O(s)$ space.

#### Alternatives and edge cases

- **Copy the full current array on every snapshot:** Historical reads become $O(1)$, but each `snap` costs $O(\texttt{length})$ time and total storage can grow to the product of the length and number of snapshots.
- **Store a full map for every snapshot:** Sparse maps still duplicate unchanged state unless they are linked through a persistent structure, making the simple per-index histories more direct.
- **Repeated sets before `snap`:** Only the last value belongs to that snapshot, so overwriting one record prevents redundant history entries.
- **Never-set index:** Its initial record returns `0` for every valid snapshot.
- **Empty snapshots:** Consecutive `snap` calls without updates receive distinct IDs but share all previously stored values.
- **Read after later updates:** Binary search ignores records whose IDs exceed the requested `snap_id`.

</details>
