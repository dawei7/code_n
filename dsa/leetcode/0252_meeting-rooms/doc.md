# Meeting Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 252 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/meeting-rooms/) |

## Problem Description
### Goal
Given a collection of meeting intervals `[start, end]`, determine whether one person can attend every meeting. Each interval is half-open: the meeting occupies its start time up to, but not including, its end time.

Return `True` when no two meetings overlap in time and `False` when any pair requires simultaneous attendance. A meeting ending exactly when another begins is compatible and does not count as an overlap. Input order does not indicate chronological order, so all intervals must be considered. Empty and one-meeting schedules are always attendable.

### Function Contract
**Inputs**

- `intervals`: meeting intervals `[start, end]`

**Return value**

`True` exactly when no two meetings overlap.

### Examples
**Example 1**

- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `false`

**Example 2**

- Input: `intervals = [[7,10],[2,4]]`
- Output: `true`

**Example 3**

- Input: `intervals = [[1,2],[2,3]]`
- Output: `true`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort starts so one adjacent conflict is enough**

Sort by start time. Any overlap must then appear between a meeting and its immediate predecessor; there is no need to compare every pair.

Before inspecting index `i`, all meetings through $i - 1$ are mutually compatible. The invariant continues exactly when `intervals[i].start >= intervals[i - 1].end`.

**A compatible prefix needs only its last meeting checked**

If the next meeting overlaps the previous sorted meeting, the schedule is immediately impossible. Otherwise, assume the earlier prefix was compatible. Its meetings finish in the same nonoverlapping sequence before the previous meeting starts, and the previous meeting finishes no later than the new start. The extended prefix is therefore also compatible. Induction makes the adjacent checks sufficient for the entire schedule.

#### Complexity detail

Sorting costs $O(n \log n)$ and the scan costs $O(n)$. Creating a sorted copy uses $O(n)$ space.

#### Alternatives and edge cases

- **Compare every pair:** is correct but takes $O(n^2)$ time.
- Empty and one-meeting schedules are valid; touching endpoints do not overlap.

</details>
