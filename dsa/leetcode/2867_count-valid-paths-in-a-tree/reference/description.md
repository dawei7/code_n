## Description

There is an undirected tree with `n` nodes labeled from `1` to `n`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree.

Return *the **number of valid paths** in the tree*.

A path `(a, b)` is **valid** if there exists **exactly one** prime number among the node labels in the path from `a` to `b`.

**Note** that:

<ul>
	<li>The path `(a, b)` is a sequence of **distinct** nodes starting with node `a` and ending with node `b` such that every two adjacent nodes in the sequence share an edge in the tree.</li>
	<li>Path `(a, b)` and path `(b, a)` are considered the **same** and counted only **once**.</li>
</ul>
