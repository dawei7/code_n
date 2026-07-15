# Group the People Given the Group Size They Belong To

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1282 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) |

## Problem Description
### Goal
There are $n$ people with unique identifiers from $0$ through $n-1$, partitioned into groups whose membership is not yet known. The array `groupSizes` describes the required group of every person: `groupSizes[i]` is exactly the number of people that must be in the same group as person `i`.

Construct a grouping that contains every person exactly once and makes the size of each person's group equal to that person's requested value. A valid grouping is guaranteed to exist. The ordering of groups and the ordering of people within them are unrestricted, so any valid answer may be returned.

### Function Contract
**Inputs**

- `groupSizes`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{groupSizes[i]} \le n$.

**Return value**

A list of groups. Every index from $0$ through $n-1$ must occur exactly once, and each returned group must contain exactly `groupSizes[i]` people for every member `i` of that group.

### Examples
**Example 1**

- Input: `groupSizes = [3,3,3,3,3,1,3]`
- Output: `[[5],[0,1,2],[3,4,6]]`
- Explanation: Person 5 forms the required singleton; the other six people form two groups of three.

**Example 2**

- Input: `groupSizes = [2,1,3,3,3,2]`
- Output: `[[1],[0,5],[2,3,4]]`

**Example 3**

- Input: `groupSizes = [1,1,1]`
- Output: `[[0],[1],[2]]`
- Explanation: Each request for size one must become a separate group.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Use a hash table whose key is a requested group size and whose value is the not-yet-complete bucket of people requesting that size. Process people in identifier order. Append person `i` to the bucket keyed by `groupSizes[i]`.

A bucket with key $s$ becomes a complete valid group exactly when it contains $s$ people. Move that bucket into the answer immediately and replace it with an empty bucket so later people requesting $s$ start another group. Every person enters exactly one bucket and a completed bucket contains only people who requested its exact size. Because the input guarantees a solution, no partial bucket remains after all people have been processed; consequently the emitted groups cover every person exactly once and satisfy every requested size.

#### Complexity detail

Let $n$ be the number of people. Each index is appended once and transferred into the answer once, while expected hash-table access is constant time, for $O(n)$ total time. The incomplete buckets and returned grouping together store $n$ indices, so auxiliary construction space is $O(n)$ including the returned answer.

#### Alternatives and edge cases

- **Sort by requested size:** Sorting pairs of size and identifier makes equal requests contiguous, but costs $O(n \log n)$ time and requires careful chunking.
- **Repeated search among people:** Building each group by scanning for compatible unassigned people can take $O(n^2)$ time.
- **Several groups of one size:** Filling and clearing a bucket is essential; a size may require multiple distinct groups.
- **Singleton requests:** Every person requesting size one must be emitted immediately in a separate group.
- **Non-unique output:** Tests must validate the partition rather than require one particular ordering of otherwise valid groups.

</details>
