# High-Access Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2933 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [high-access-employees](https://leetcode.com/problems/high-access-employees/) |

## Problem Description & Examples
### Goal
Identify "high-access" employees who have accessed a secure system at least three times within a single one-hour window. Access times are provided in 24-hour HHMM format. An employee is considered high-access if there exist three timestamps $t_1, t_2, t_3$ for that employee such that they all fall within a range of strictly less than 60 minutes.

### Function Contract
**Inputs**

- `access_times`: A list of lists, where each inner list contains two strings: the employee name and their access time in "HHMM" format.

**Return value**

- A list of strings representing the names of all high-access employees, sorted in any order.

### Examples
**Example 1**

- Input: `access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0615"],["a","0559"]]`
- Output: `["a"]`

**Example 2**

- Input: `access_times = [["d","0002"],["c","0808"],["c","0809"],["c","0810"]]`
- Output: `["c"]`

**Example 3**

- Input: `access_times = [["cd","1025"],["ig","1025"],["cd","1026"],["cd","1027"],["ig","1028"],["ig","1029"]]`
- Output: `["cd","ig"]`

---

## Underlying Base Algorithm(s)
The solution utilizes a Hash Map (dictionary) to group access times by employee. For each employee, the access times are converted into integer minutes from the start of the day and sorted. A sliding window approach (or checking index `i` and `i+2`) is then used to determine if any three timestamps fall within a 60-minute interval.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N + N \cdot K \log K)$, where $N$ is the number of access records and $K$ is the average number of access records per employee. Sorting the records per employee dominates the complexity.
- **Space Complexity**: $O(N)$, required to store the grouped access times in the hash map.
