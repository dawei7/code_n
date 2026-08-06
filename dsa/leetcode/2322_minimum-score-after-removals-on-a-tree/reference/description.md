## Description

There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given a **0-indexed** integer array `nums` of length `n` where `nums[i]` represents the value of the `i^th` node. You are also given a 2D integer array `edges` of length `n - 1` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Remove two **distinct** edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

<ol>
	<li>Get the XOR of all the values of the nodes for **each** of the three components respectively.</li>
	<li>The **difference** between the **largest** XOR value and the **smallest** XOR value is the **score** of the pair.</li>
</ol>

<ul>
	<li>For example, say the three components have the node values: `[4,5,7]`, `[1,9]`, and `[3,3,3]`. The three XOR values are `4 ^ 5 ^ 7 = <u>**6**</u>`, `1 ^ 9 = <u>**8**</u>`, and `3 ^ 3 ^ 3 = <u>**3**</u>`. The largest XOR value is `8` and the smallest XOR value is `3`. The score is then `8 - 3 = 5`.</li>
</ul>

Return *the **minimum** score of any possible pair of edge removals on the given tree*.
