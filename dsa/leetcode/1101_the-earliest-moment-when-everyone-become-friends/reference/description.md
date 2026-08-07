## Description

There are n people in a social group labeled from `0` to $n - 1$. You are given an array `logs` where $\text{logs}[i] = [\text{timestamp}_{i}, x_{i}, y_{i}]$ indicates that $x_{i}$ and $y_{i}$ will be friends at the time $\text{timestamp}_{i}$.

Friendship is **symmetric**. That means if `a` is friends with `b`, then `b` is friends with `a`. Also, person `a` is acquainted with a person `b` if `a` is friends with `b`, or `a` is a friend of someone acquainted with `b`.

Return *the earliest time for which every person became acquainted with every other person*. If there is no such earliest time, return `-1`.
### Function Contract

**Inputs**

- `logs`: friendship events `[timestamp_i, x_i, y_i]`; the input order need not be chronological.
- `n`: the number of people, labeled consecutively from `0` to `n - 1`.

At each timestamp, the event adds an undirected friendship between its two distinct people. Existing friendships persist. After any chronological prefix of the events, acquaintance groups are the connected components formed by all friendships in that prefix.

**Return value**

Return the earliest event timestamp whose chronological prefix leaves exactly one acquaintance group containing all `n` people. Return `-1` if more than one group remains after every event.

### Examples
#### Example 1

- **Input:** $logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6$
- **Output:** `20190301`
- **Explanation:**
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
#### Example 2

- **Input:** $logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4$
- **Output:** `3`
- **Explanation:** At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
### Constraints

- $2 \le n \le 100$

- $1 \le \text{logs.length} \le 10^{4}$

- $\text{logs}[i].length = 3$

- $0 \le \text{timestamp}_{i} \le 10^{9}$

- $0 \le x_{i}, y_{i} \le n - 1$

- $x_{i} \neq y_{i}$

- All the values $\text{timestamp}_{i}$ are **unique**.

- All the pairs $(x_{i}, y_{i})$ occur at most one time in the input.