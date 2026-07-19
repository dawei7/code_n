# Maximum Number of People That Can Be Caught in Tag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1989 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/) |

## Problem Description
### Goal
People stand at the indexed positions of the binary array `team`. A value of
`1` marks a person who is “it,” while `0` marks someone who may be caught. A
person who is “it” at index `i` may catch one person at an index from
`i - dist` through `i + dist`, including both endpoints.

Each catcher may catch at most one other person, and each non-catcher may be
caught at most once. Choose the pairings to maximize the total number of caught
people, and return that maximum.

### Function Contract
**Inputs**

- `team`: a binary list of length $N$, where $1 \le N \le 10^5$; `1` denotes
  a catcher and `0` denotes a person who can be caught.
- `dist`: the inclusive maximum index distance $D$, where $1 \le D \le N$.

**Return value**

- The maximum number of disjoint catcher–person pairs whose index difference is
  at most $D$.

### Examples
**Example 1**

- Input: `team = [0, 1, 0, 1, 0], dist = 3`
- Output: `2`

The two catchers can be paired with any two of the three other people.

**Example 2**

- Input: `team = [1], dist = 1`
- Output: `0`

**Example 3**

- Input: `team = [0], dist = 1`
- Output: `0`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Separate both teams in position order**

Collect the indices containing `1` into `catchers` and the indices containing
`0` into `people`. Both lists are automatically increasing because the input is
scanned from left to right. Maintain one pointer to the earliest unmatched
index in each list.

**Discard an index that can no longer match**

Let the current indices be `catcher` and `person`. If
`person < catcher - dist`, that person lies too far left for the current
catcher and for every later catcher, so advance only the person pointer.
Symmetrically, if `catcher < person - dist`, the current catcher lies too far
left to reach the current or any later person, so advance only the catcher
pointer.

**Greedily match the earliest feasible pair**

Otherwise the two current indices are within the inclusive distance bound.
Match them and advance both pointers. This cannot reduce the optimum: in any
maximum matching that uses either earliest index, replacing its partner with
the other earliest feasible index leaves every later index at least as much
room to match to the right. If neither is used, adding their feasible pair
would improve the matching.

Thus the greedy step preserves a maximum completion after every pointer
advance. The number of matched pairs when either list is exhausted is the
largest possible number of catches.

#### Complexity detail

Building the two index lists scans all $N$ positions once. Each pointer then
advances monotonically and never retreats, so matching also takes $O(N)$ time.
The two lists together store exactly $N$ indices, using $O(N)$ space.

#### Alternatives and edge cases

- **Direct streaming queues:** Maintain unmatched indices while scanning the
  original array. This can also achieve linear time but makes the symmetric
  expiration logic less direct.
- **General bipartite matching:** Connect every catcher to every reachable
  person and run augmenting paths. This is correct but ignores interval order
  and may require quadratic edges and superlinear matching work.
- **Choose the nearest person independently:** Local nearest-distance choices
  can consume the only partner reachable by a later catcher; left-to-right
  order, not raw distance, provides the safe greedy rule.
- If either team is absent, no pair can be formed.
- A pair at distance exactly `dist` is valid because the interval is inclusive.
- When `dist` spans the whole array, the answer is the smaller of the counts of
  zeros and ones.
- Extra people on either team remain unmatched once the opposite index list is
  exhausted.

</details>
