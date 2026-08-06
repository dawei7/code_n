## Description

You are given an integer `n` and an undirected tree with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between `u_i` and `v_i`.

You are also given three **distinct** target nodes `x`, `y`, and `z`.

For any node `u` in the tree:

<ul>
	<li>Let `dx` be the distance from `u` to node `x`</li>
	<li>Let `dy` be the distance from `u` to node `y`</li>
	<li>Let `dz` be the distance from `u` to node `z`</li>
</ul>

The node `u` is called **special** if the three distances form a **Pythagorean Triplet**.

Return an integer denoting the number of special nodes in the tree.

A **Pythagorean triplet** consists of three integers `a`, `b`, and `c` which, when sorted in **ascending** order, satisfy `a^2 + b^2 = c^2`.

The **distance** between two nodes in a tree is the number of edges on the unique path between them.
