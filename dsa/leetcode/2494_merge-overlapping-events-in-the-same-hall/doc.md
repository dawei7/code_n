# Merge Overlapping Events in the Same Hall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2494 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-overlapping-events-in-the-same-hall/) |

## Problem Description

### Goal

The `HallEvents` table records the hall and inclusive start and end dates of scheduled events. Duplicate rows may be present.

Merge every set of overlapping events held in the same hall. Two events overlap when their inclusive date ranges share at least one day, so events ending and starting on the same date belong to one merged interval. Overlap is transitive: if one event connects two otherwise separate ranges, all three form a single interval. Events belonging to different halls never affect one another.

Return one row for each resulting merged interval. The rows may appear in any order.

### Function Contract

**Inputs**

- `HallEvents(hall_id, start_day, end_day)`: Event intervals identified by hall; the table may contain duplicate rows.

Each interval includes both `start_day` and `end_day`.

**Return value**

Return a relation with these columns:

- `hall_id`: The hall containing the merged event range.
- `start_day`: The earliest date in that merged range.
- `end_day`: The latest date in that merged range.

### Examples

**Example 1**

- Input: Hall 1 contains `[2023-01-13, 2023-01-14]`, `[2023-01-14, 2023-01-17]`, and `[2023-01-18, 2023-01-25]`; hall 2 contains a large interval enclosing a smaller one; hall 3 contains one event.
- Output: Hall 1 produces `[2023-01-13, 2023-01-17]` and `[2023-01-18, 2023-01-25]`; halls 2 and 3 each produce one interval.
- Explanation: The first two hall-1 events share January 14, while the third does not share a day with either one.

**Example 2**

- Input: One hall contains `[2024-01-01, 2024-01-02]`, `[2024-01-05, 2024-01-06]`, and `[2024-01-02, 2024-01-05]`.
- Output: One interval `[2024-01-01, 2024-01-06]`.
- Explanation: The third event bridges the first two ranges, so transitive overlap merges all of them.

**Example 3**

- Input: Two identical rows describe `[2024-03-10, 2024-03-12]` in hall 7.
- Output: One row for hall 7 with `[2024-03-10, 2024-03-12]`.
- Explanation: Duplicate source rows do not create duplicate merged intervals.
