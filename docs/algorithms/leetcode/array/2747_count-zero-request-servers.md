# Count Zero Request Servers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2747 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window, Sorting |
| Official Link | [count-zero-request-servers](https://leetcode.com/problems/count-zero-request-servers/) |

## Problem Description & Examples
### Goal
Given a total of `n` servers (labeled from `1` to `n`) and a list of request logs where each log contains `[server_id, time]`, we want to answer multiple queries. Each query specifies a time `q`. For each query, we need to determine how many servers did not receive any requests in the closed time interval `[q - x, q]`, where `x` is a constant window size.

### Function Contract
**Inputs**

- `n`: `int` - The total number of servers.
- `logs`: `List[List[int]]` - A 2D list where `logs[i] = [server_id, time]` indicates that the server `server_id` received a request at `time`.
- `x`: `int` - The duration of the query time window.
- `queries`: `List[int]` - A list of query times.

**Return value**

- `List[int]` - An array of the same length as `queries`, where the $i$-th element is the number of servers that received zero requests in the interval `[queries[i] - x, queries[i]]`.

### Examples
**Example 1**

- Input:
  - `n = 3`
  - `logs = [[1, 3], [2, 6], [1, 5]]`
  - `x = 5`
  - `queries = [10, 11]`
- Output: `[1, 2]`
- Explanation:
  - For the query at time `10`, the interval is `[5, 10]`. Logs in this interval are `[1, 5]` and `[2, 6]`. Servers `1` and `2` received requests. Server `3` did not. Thus, `1` server has zero requests.
  - For the query at time `11`, the interval is `[6, 11]`. The only log in this interval is `[2, 6]`. Server `2` received a request. Servers `1` and `3` did not. Thus, `2` servers have zero requests.

**Example 2**

- Input:
  - `n = 3`
  - `logs = [[2, 4], [2, 1], [1, 1], [3, 1]]`
  - `x = 2`
  - `queries = [3, 4]`
- Output: `[0, 2]`
- Explanation:
  - For the query at time `3`, the interval is `[1, 3]`. Logs in this interval are `[2, 1]`, `[1, 1]`, and `[3, 1]`. All servers `1`, `2`, and `3` received requests. Thus, `0` servers have zero requests.
  - For the query at time `4`, the interval is `[2, 4]`. The only log in this interval is `[2, 4]`. Only server `2` received a request. Servers `1` and `3` did not. Thus, `2` servers have zero requests.

**Example 3**

- Input:
  - `n = 4`
  - `logs = [[1, 1], [2, 2], [3, 3], [4, 4]]`
  - `x = 1`
  - `queries = [1, 2, 5]`
- Output: `[3, 2, 4]`
- Explanation:
  - For the query at time `1`, the interval is `[0, 1]`. Server `1` is active. Zero request servers: `3`.
  - For the query at time `2`, the interval is `[1, 2]`. Servers `1` and `2` are active. Zero request servers: `2`.
  - For the query at time `5`, the interval is `[4, 5]`. Server `4` is active. Zero request servers: `3`.

---

## Underlying Base Algorithm(s)
The problem can be solved efficiently using **Offline Queries** combined with a **Sliding Window (Two Pointers)** approach:

1. **Offline Processing**: Since the queries can be answered in any order, we sort the queries chronologically while keeping track of their original indices. This allows us to process the time windows monotonically from left to right.
2. **Sorting Logs**: We sort the logs by their request times.
3. **Sliding Window**: We maintain a sliding window of logs that fall within the interval `[q - x, q]` for the current query `q`.
   - As the query time `q` increases, both the start `q - x` and end `q` of the window move to the right.
   - We expand the window by incrementing a `right_ptr` and adding logs whose times are $\le q$.
   - We shrink the window by incrementing a `left_ptr` and removing logs whose times are $< q - x$.
4. **Frequency Tracking**: We maintain an array tracking the frequency of requests for each server within the current window. We also maintain a count of unique active servers.
5. **Result Calculation**: For each query, the number of servers with zero requests is simply `n - unique_active_servers`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(M \log M + Q \log Q)$ where $M$ is the number of logs and $Q$ is the number of queries. Sorting the logs takes $\mathcal{O}(M \log M)$ time, and sorting the queries takes $\mathcal{O}(Q \log Q)$ time. The sliding window pointers traverse the logs array at most once, taking $\mathcal{O}(M)$ time.
- **Space Complexity**: $\mathcal{O}(N + Q)$ where $N$ is the number of servers and $Q$ is the number of queries. We use $\mathcal{O}(N)$ space for the server frequency array and $\mathcal{O}(Q)$ space to store the sorted queries and the final result array.
