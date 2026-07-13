# Cracking the Safe

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 753 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Depth-First Search, Graph Theory, Eulerian Circuit |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cracking-the-safe/) |

## Problem Description

### Goal

A safe password consists of `n` digits, each chosen from `0` through $k - 1$. After each typed digit, the safe tests the most recent `n` entered digits as a password candidate.

Return a shortest string that is guaranteed to try every one of the $k^{n}$ possible passwords as a contiguous length-`n` substring. Overlapping candidates may share typed digits, and any minimum-length string with complete coverage is acceptable. The entered alphabet must use only the allowed `k` digits.

### Function Contract

**Inputs**

- `n`: the positive password length.
- `k`: the alphabet size, using digit characters from `0` through $k - 1$.

**Return value**

- Any minimum-length string containing each of the $k^{n}$ possible passwords at least once.

### Examples

**Example 1**

- Input: `n = 1`, `k = 2`
- Output: `"10"`
- Explanation: Both one-digit passwords occur once; `"01"` would be equally valid.

**Example 2**

- Input: `n = 2`, `k = 2`
- Output: `"01100"`
- Explanation: Its length-two windows are `01`, `11`, `10`, and `00`, covering all four passwords.

### Required Complexity

- **Time:** $O(k^n)$
- **Space:** $O(k^n)$

<details>
<summary>Approach</summary>

#### General

**Turn passwords into edges of an overlap graph**

Represent every length-$n - 1$ digit string as a vertex. Each password is a directed edge from its first $n - 1$ digits to its last $n - 1$ digits; appending the edge's final digit moves between those vertices. Every vertex has exactly `k` incoming and `k` outgoing edges, and the overlap graph is connected through the all-zero vertex, so it has an Eulerian circuit using every password edge once.

**Traverse every edge with iterative Hierholzer search**

Encode a vertex as an integer modulo $k^{(n - 1)}$. For each vertex, remember the next outgoing digit not yet used. From the vertex at the top of a stack, take that digit, compute `(vertex * k + digit) % k ** ((n - 1))`, and push the next vertex together with the digit used to enter it. When a vertex has no unused outgoing edge, pop it and append its incoming digit to the answer.

The digits are appended during backtracking, which is exactly Hierholzer's Eulerian output order. Finish by appending $n - 1$ zeros for the starting vertex.

**Why the length is minimum**

The traversal uses every one of the $k^{n}$ edges exactly once, so the returned string has $k^{n} + n - 1$ characters and its consecutive length-`n` windows are precisely all passwords. Any string of length `L` has only $L - n + 1$ such windows. Covering $k^{n}$ distinct passwords therefore requires $L \ge k^{n} + n - 1$, and the construction meets that lower bound.

#### Complexity detail

There are $k^{n}$ password edges. Each edge is pushed and popped once with constant-time integer transitions, giving $O(k^n)$ time. The per-vertex outgoing counters, traversal stack, and output each use at most $O(k^n)$ space.

#### Alternatives and edge cases

- **Recursive Hierholzer traversal:** The same edge-postorder idea is concise, but its recursion depth can reach $k^{n}$ and exceed Python's call-stack limit.
- **Backtracking over candidate strings:** Trying digits and repeatedly checking which passwords remain can revisit exponentially many partial strings.
- **Store visited password strings:** A set-based Euler traversal is correct and still linear in the number of edges, but integer vertices and per-vertex next-digit counters avoid repeated string construction.
- **$n = 1$:** The graph has one empty-suffix vertex with `k` self-loop edges; any permutation of all digits is valid.
- **$k = 1$:** There is one password, and the minimum sequence is `n` zero characters.
- **Multiple valid outputs:** Edge order can produce different Eulerian circuits; validation must check coverage and minimum length rather than one exact string.

</details>
