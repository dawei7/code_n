## Description

You are given an integer `n` and an **undirected** graph with `n` nodes labeled from 0 to `n - 1` and a 2D array `edges`, where `edges[i] = [u_i, v_i]` indicates an edge between nodes `u_i` and `v_i`.

You are also given a string `label` of length `n`, where `label[i]` is the character associated with node `i`.

You may start at any node and move to any adjacent node, visiting each node **at most** once.

Return the **maximum** possible length of a **<span data-keyword="palindrome-string">palindrome</span>** that can be formed by visiting a set of **unique** nodes along a valid path.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[1,2]], label = "aba"</span>

**Output:** <span class="example-io">3</span>

**Exp****lanation:**

![](images/screenshot-2025-06-13-at-230714.png)

	- The longest palindromic path is from node 0 to node 2 via node 1, following the path `0 → 1 → 2` forming string `"aba"`.

	- This is a valid palindrome of length 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, edges = [[0,1],[0,2]], label = "abc"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/screenshot-2025-06-13-at-230017.png)

	- No path with more than one node forms a palindrome.

	- The best option is any single node, giving a palindrome of length 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

![](images/screenshot-2025-06-13-at-230508.png)

	- The longest palindromic path is from node 0 to node 1, following the path `0 → 3 → 1`, forming string `"bcb"`.

	- This is a valid palindrome of length 3.

</div>

**Constraints:**

	- `1 <= n <= 14`

	- `n - 1 <= edges.length <= n * (n - 1) / 2`

	- `edges[i] == [u_i, v_i]`

	- `0 <= u_i, v_i <= n - 1`

	- `u_i != v_i`

	- `label.length == n`

	- `label` consists of lowercase English letters.

	- There are no duplicate edges.
