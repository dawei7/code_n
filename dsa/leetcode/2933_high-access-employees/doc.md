# High-Access Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2933 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/high-access-employees/) |

## Problem Description

### Goal

Each entry in `access_times` contains an employee name and one system-access
time from a single day. Times use four-digit 24-hour notation such as `"0800"`
or `"2250"`. An employee is high-access when at least three of that employee's
recorded accesses occur within a period shorter than one hour.

Return all high-access employee names in any order. Accesses exactly 60 minutes
apart do not belong to the same one-hour period. The day is not circular:
times near midnight at its beginning and end must not be joined across the day
boundary.

### Function Contract

**Inputs**

- `access_times`: Pairs `[employee_name, timestamp]` for accesses made during one day.

Let $n=\lvert\texttt{access\_times}\rvert$. The constraints are $1\le n\le100$;
names contain 1 through 10 lowercase English letters; and every timestamp is a
valid four-digit 24-hour time.

**Return value**

- The names of all employees with at least three accesses spanning fewer than 60 minutes, in any order.

### Examples

#### Example 1

- **Input:** `access_times = [["a", "0549"], ["b", "0457"], ["a", "0532"], ["a", "0621"], ["b", "0540"]]`
- **Output:** `["a"]`
- **Explanation:** Employee `a` accesses at 05:32, 05:49, and 06:21, spanning 49 minutes.

#### Example 2

- **Input:** `access_times = [["d", "0002"], ["c", "0808"], ["c", "0829"], ["e", "0215"], ["d", "1508"], ["d", "1444"], ["d", "1410"], ["c", "0809"]]`
- **Output:** `["c", "d"]`
- **Explanation:** Both `c` and `d` have a qualifying triple; `e` has only one access.

#### Example 3

- **Input:** `access_times = [["cd", "1025"], ["ab", "1025"], ["cd", "1046"], ["cd", "1055"], ["ab", "1124"], ["ab", "1120"]]`
- **Output:** `["ab", "cd"]`
- **Explanation:** Each employee has three accesses whose earliest and latest times differ by 59 minutes or less.
