## Description

You are given an undirected tree with `n` nodes labeled 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given a string `s` of length `n` consisting of lowercase English letters, where `s[i]` represents the character assigned to node `i`.

You are also given a string array `queries`, where each `queries[i]` is either:

<ul>
	<li>`"update u_i c"`: Change the character at node `u_i` to `c`. Formally, update `s[u_i] = c`.</li>
	<li>`"query u_i v_i"`: Determine whether the string formed by the characters on the **unique** path from `u_i` to `v_i` (inclusive) can be **rearranged** into a **<span data-keyword="palindrome-string">palindrome</span>**.</li>
</ul>

Return a boolean array `answer`, where `answer[j]` is `true` if the `j^th` query of type `"query u_i v_i"​​​​​​​` can be rearranged into a **palindrome**, and `false` otherwise.
