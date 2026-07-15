# The Earliest Moment When Everyone Become Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) |

## Problem Description

### Goal

A social group contains `n` people labeled from `0` through `n - 1`. Each entry `logs[i] = [timestamp_i, x_i, y_i]` says that two different people become friends at that timestamp. Friendship is symmetric.

Two people are acquainted when they are direct friends or connected through a chain of friendships. Return the earliest timestamp at which every person is acquainted with every other person. If the events never connect the entire group, return `-1`. All timestamps are unique, and each friendship pair occurs at most once.

### Function Contract

**Inputs**

- `logs`: a list of $m$ triples `[timestamp, x, y]`, where $1 \leq m \leq 10^4$, $0 \leq \texttt{timestamp} \leq 10^9$, and `x` and `y` are distinct labels in $[0,n-1]`. Timestamps and unordered friendship pairs are unique.
- `n`: the number of people, where $2 \leq n \leq 100$.

**Return value**

The earliest timestamp when the friendship graph is connected, or `-1` if it never becomes connected.

### Examples

**Example 1**

- Input: `logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6`
- Output: `20190301`

At that event, the components containing `{0,1,5}` and `{2,3,4}` merge.

**Example 2**

- Input: `logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4`
- Output: `3`

### Required Complexity

- **Time:** $O(m \log m + m\alpha(n))$
- **Space:** $O(m + n)$

<details>
<summary>Approach</summary>

#### General

**Process events in temporal order.** The input need not be sorted, so first order the logs by timestamp. Connectivity only gains edges over time; the first chronological prefix that forms one component determines the answer.

**Represent friendship circles with union-find.** Start with each person as a separate parent and maintain `components = n`. For every log, find the roots of its two people. If the roots differ, join the smaller tree beneath the larger one and decrement the component count. Path compression keeps later root searches short.

**Stop at the first single component.** An event whose endpoints already share a root changes nothing, even if the two people were never direct friends before. When a successful union reduces `components` to 1, every label belongs to the same transitive friendship group, so return that event's timestamp immediately.

Before processing a log, union-find's sets are exactly the connected components formed by earlier events. A successful union adds the current edge between two such components; a redundant edge leaves them unchanged. This invariant means the first moment the count becomes one is both sufficient for universal acquaintance and earlier than any later possible answer.

#### Complexity detail

Sorting $m$ logs costs $O(m \log m)$. With path compression and union by size, the $m$ union-find operations cost $O(m\alpha(n))$, where $\alpha$ is the inverse Ackermann function. The sorted log copy uses $O(m)$ space and the parent and size arrays use $O(n)$.

#### Alternatives and edge cases

- **Graph traversal after every event:** Rebuilding reachability is correct but can require $O(m(m+n))$ time.
- **Binary search over timestamps:** Test connectivity for chronological prefixes, but repeated graph construction is more work than the one-pass union-find method.
- **Redundant transitive edge:** If both endpoints already have the same root, the component count must not change.
- **Unsorted logs:** Returning during input order rather than timestamp order can produce the wrong moment.
- **Never connected:** Remaining with more than one component after all logs requires `-1`.
- **Two people:** Their first and only connecting event immediately supplies the answer.

</details>
