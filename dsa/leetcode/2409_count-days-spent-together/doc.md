# Count Days Spent Together

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2409 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-days-spent-together/) |

## Problem Description

### Goal

Alice and Bob travel to Rome for separate meetings during the same calendar year. Alice is present from `arriveAlice` through `leaveAlice`, and Bob is present from `arriveBob` through `leaveBob`. Both endpoints are inclusive, so an arrival or departure date can count as a shared day.

Each date is a valid five-character `"MM-DD"` string in a non-leap year, and each person's arrival is earlier than or equal to that person's departure. Determine how many calendar days belong to both stays. Return zero when the two inclusive intervals do not intersect.

### Function Contract

**Inputs**

- `arriveAlice`: Alice's arrival date in `"MM-DD"` format.
- `leaveAlice`: Alice's inclusive departure date.
- `arriveBob`: Bob's arrival date in `"MM-DD"` format.
- `leaveBob`: Bob's inclusive departure date.

All four dates belong to one non-leap year and are valid. The month lengths are `31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31`.

**Return value**

Return the number of days in the intersection of the two inclusive stays.

### Examples

**Example 1**

- Input: `arriveAlice = "08-15"`, `leaveAlice = "08-18"`, `arriveBob = "08-16"`, `leaveBob = "08-19"`
- Output: `3`

**Example 2**

- Input: `arriveAlice = "10-01"`, `leaveAlice = "10-31"`, `arriveBob = "11-01"`, `leaveBob = "12-31"`
- Output: `0`

**Example 3**

- Input: `arriveAlice = "02-28"`, `leaveAlice = "03-01"`, `arriveBob = "03-01"`, `leaveBob = "03-01"`
- Output: `1`
