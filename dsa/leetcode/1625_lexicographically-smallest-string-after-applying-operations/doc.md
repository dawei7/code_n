# Lexicographically Smallest String After Applying Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1625 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Depth-First Search, Breadth-First Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/) |

## Problem Description
### Goal
You are given an even-length decimal string `s` and integers `a` and `b`. Starting from `s`, either of two operations may be applied any number of times and in any order.

The addition operation increases every digit at an odd 0-indexed position by `a`, wrapping modulo 10. For example, adding 5 to `"3456"` produces `"3951"`. The rotation operation moves the final `b` characters to the front, which is a right rotation by exactly `b` positions.

Return the lexicographically smallest string reachable under these operations. Strings have equal length, so lexicographic order is decided by the first position at which their digits differ.

### Function Contract
**Inputs**

- `s`: an even-length string of $n$ decimal digits, where $2 \le n \le 100$.
- `a`: the amount added modulo 10 to odd-indexed digits, where $1 \le a \le 9$.
- `b`: the right-rotation distance, where $1 \le b \le n-1$.

**Return value**

Return the lexicographically smallest length-$n$ string reachable from `s` by any finite sequence of the two permitted operations.

### Examples
**Example 1**

- Input: `s = "5525", a = 9, b = 2`
- Output: `"2050"`

**Example 2**

- Input: `s = "74", a = 5, b = 1`
- Output: `"24"`

**Example 3**

- Input: `s = "0011", a = 4, b = 2`
- Output: `"0011"`

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Treat reachable strings as a finite graph.** Each distinct string is a state. It has two outgoing edges: one to the result of adding `a` at every odd index, and one to the result of rotating right by `b`. Because both operations are deterministic and all strings have fixed length over ten digits, repeated operations eventually revisit a state.

**Visit every state once.** Start a depth-first or breadth-first traversal at `s`. For each removed state, compare it with the smallest string seen so far, construct both neighboring strings, and add only previously unseen neighbors to the worklist. A hash set prevents cycles from causing unbounded exploration.

**Why the graph is small enough.** Rotation can create at most $n$ distinct alignments. Let $c=10/\gcd(a,10)$ be the number of additions needed for an affected digit to return to its starting value. If `b` is even, rotations preserve index parity, so only the digits originally at odd positions change and there are at most $c$ additive phases. If `b` is odd, rotations swap the parities, allowing the two original parity classes to receive independent phases, for at most $c^2$ combinations. Since $c\le 10$, there are at most $100n$ reachable states.

Every permitted operation sequence follows edges in this graph, so every reachable string is visited. Conversely, each generated neighbor is the result of one permitted operation and is therefore reachable. The minimum over the visited set is consequently exactly the requested lexicographic minimum.

#### Complexity detail

There are $O(n)$ reachable states because the factor of at most 100 additive configurations is constant. Constructing, hashing, and comparing each length-$n$ state costs $O(n)$ time, giving $O(n^2)$ total time. The visited set can retain $O(n)$ strings of length $n$, so it uses $O(n^2)$ space; the worklist is no larger asymptotically.

#### Alternatives and edge cases

- **Direct phase enumeration:** Enumerate reachable rotations and the one or two modular addition phases without graph traversal. This reaches the same $O(n^2)$ bound but requires careful parity reasoning, especially when `b` is odd.
- **Search without a visited set:** The operation graph contains cycles, so unrestricted DFS or BFS may never terminate and repeatedly recomputes the same strings.
- **Linear visited-state lookup:** Keeping visited strings in a list preserves correctness but can add another factor from repeated full-string comparisons, worsening the bound to $O(n^3)$.
- If `b` is even, rotations never move an original even-position digit into an odd position; those digits cannot be changed by addition.
- If `b` is odd, a rotation swaps parity, so both original parity classes can eventually be changed.
- The original `s` is itself reachable by applying no operations and must remain a candidate.
- Addition wraps each digit independently modulo 10; it never carries into a neighboring digit.

</details>
