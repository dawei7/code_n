# Open the Lock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 752 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/open-the-lock/) |

## Problem Description

### Goal

A lock has four circular decimal wheels and begins at `"0000"`. In one move, rotate exactly one wheel by one slot forward or backward; digits wrap between `0` and `9`.

The listed `deadends` are forbidden combinations: if the lock displays one, its wheels can no longer turn. Return the minimum number of legal moves needed to display `target`, or `-1` if the target cannot be reached without entering a deadend. The starting combination also obeys the deadend restriction.

### Function Contract

**Inputs**

- `deadends`: a list of forbidden four-character digit combinations.
- `target`: the four-character digit combination to reach.

**Return value**

- The minimum number of single-wheel turns from `"0000"` to `target`, or `-1` when unreachable.

### Examples

**Example 1**

- Input: `deadends = ["0201", "0101", "0102", "1212", "2002"]`, `target = "0202"`
- Output: `6`
- Explanation: A shortest legal route avoids the forbidden combinations and uses six wheel turns.

**Example 2**

- Input: `deadends = ["8888"]`, `target = "0009"`
- Output: `1`
- Explanation: Rotate the last wheel backward once, wrapping from `0` to `9`.

### Required Complexity

- **Time:** $O(d + 10^w w)$
- **Space:** $O(d + 10^w)$

<details>
<summary>Approach</summary>

#### General

**Model combinations as an unweighted graph**

Each lock combination is a vertex. Rotating one of the $w = 4$ wheels in either direction creates at most `2w` neighboring vertices. Every legal edge costs one move, so the problem asks for an unweighted shortest path from `"0000"` to `target` after removing the deadend vertices.

**Meet in the middle by distance layers**

Put all deadends in a hash set and reject a blocked endpoint immediately. Maintain one frontier and visited set from `"0000"` and another from `target`. On each layer, expand whichever frontier is smaller. Generate both wrapped digits for every wheel, skip blocked states, and stop when a generated neighbor has already been reached from the opposite side.

Each side is an ordinary breadth-first search and therefore reaches its states with minimum distance from its own endpoint. When an edge first joins the two reached sets, the accumulated layer count is a valid path length. Any shorter path would have made the two breadth-first layers meet earlier, so that length is minimum. If either frontier becomes empty, the endpoints lie in different legal components.

#### Complexity detail

Let `d` be the deadend count and `w` the number of wheels. There are at most $10^{w}$ states, and generating a state's neighbors costs $O(w)$. Building the blocked set and running BFS take $O(d + 10^w w)$ time. The blocked set, visited set, and queue use $O(d + 10^w)$ space. Here `w` is fixed at four, so the state space is bounded by 10,000 combinations.

#### Alternatives and edge cases

- **One-ended breadth-first search:** It has the same worst-case bound and is simpler, but it may explore nearly the entire 10,000-state graph before resolving a deep or unreachable target.
- **Rebuild or linearly scan deadends per neighbor:** Reconstructing a set or using list membership inside the search adds $O(d)$ work to each lookup; build one hash set before BFS instead.
- **Depth-first search:** It can determine reachability, but it does not produce a shortest path without additional distance machinery.
- **Blocked start:** If `"0000"` is a deadend, no move is legal and the answer is `-1`.
- **Target equals the start:** Return `0` provided the start is not blocked.
- **Blocked target:** It cannot be entered, so the search returns `-1`.
- **Wheel wraparound:** The predecessor of `0` is `9`, and the successor of `9` is `0`.

</details>
