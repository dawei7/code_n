# Alert Using Same Key-Card Three or More Times in a One Hour Period

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1604 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/) |

## Problem Description
### Goal
An office records every use of an employee key card. For each event, `keyName[i]` identifies the employee and `keyTime[i]` gives that event's time during one particular day in 24-hour `"HH:MM"` format. Every `(name, time)` pair is unique.

An employee triggers an alert when their card appears at least three times during one one-hour period. Both endpoints count: events at `"10:00"` and `"11:00"` are exactly one hour apart and may belong to the same alerting window, whereas events 61 minutes apart do not.

Return every alerted employee name exactly once, sorted in ascending alphabetical order.

### Function Contract
**Inputs**

- `keyName`: an array of $n$ lowercase employee names, where $1 \le n \le 10^5$ and each name has length from 1 through 10.
- `keyTime`: an array of $n$ corresponding access times in 24-hour `"HH:MM"` format. All records belong to one day, and each paired name and time is unique.

**Return value**

Return the unique names for which some three access times span at most 60 minutes, in ascending lexicographic order.

### Examples
**Example 1**

- Input: `keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]`, `keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]`
- Output: `["daniel"]`
- Explanation: Daniel's uses at `"10:00"`, `"10:40"`, and `"11:00"` span exactly 60 minutes.

**Example 2**

- Input: `keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]`, `keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]`
- Output: `["bob"]`
- Explanation: Alice has no qualifying triple, while Bob has three uses between `"21:00"` and `"21:30"`.

### Required Complexity
- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate each employee's timeline.** Convert every `"HH:MM"` timestamp to minutes after midnight and append it to a list keyed by the corresponding name. Because all events belong to the same day, ordinary integer order is chronological order; there is no wraparound interval across midnight.

**Only consecutive triples need inspection.** Sort each employee's times. For a sorted list, examine every index $i \ge 2$ and compare the third time with the time two positions earlier. If `uses[i] - uses[i - 2] <= 60`, those three consecutive uses fit in an inclusive one-hour window, so that employee must be reported.

This test is also sufficient when an alerting window contains more than three uses: any three consecutive members of that window still span at most 60 minutes. Conversely, if every consecutive triple spans more than 60 minutes, any non-consecutive triple spans at least as much as the consecutive triple between its endpoints and cannot qualify. Sort the names found by this test to satisfy the output contract.

#### Complexity detail

Grouping all $n$ events takes $O(n)$ time and space. If employee $j$ has $k_j$ uses, sorting their list costs $O(k_j \log k_j)$. Since $\sum_j k_j=n$, the combined sorting cost is at most $O(n \log n)$. The consecutive-triple scans take another $O(n)$ time, and the grouped timestamps occupy $O(n)$ space.

#### Alternatives and edge cases

- **Globally sort `(name, time)` records:** This also places each employee's events together and has the same $O(n \log n)$ time bound, but grouping first makes the per-name reasoning more direct.
- **Try every triple of uses:** Exhaustive combination checking is correct but can require cubic work for one employee; sorting reveals that consecutive triples are sufficient.
- **Scan all records again for every distinct name:** This can take $O(un)$ time for $u$ employees and repeat nearly the entire input scan for every name.
- A span of exactly 60 minutes triggers an alert; use `<= 60`, not `< 60`.
- Times such as `"23:58"` and `"00:01"` are far apart within the stated single day; the interval does not wrap through midnight.
- An employee with fewer than three events can never be reported, while four or more events still produce that name only once.
- The input order is arbitrary, and the final list must be sorted independently of record order or hash-map iteration order.

</details>
