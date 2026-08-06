## Description

You are given an integer `n` and a **directed** graph with `n` nodes labeled from 0 to `n - 1`. This is represented by a 2D array `edges`, where `edges[i] = [u_i, v_i, start_i, end_i]` indicates an edge from node `u_i` to `v_i` that can **only** be used at any integer time `t` such that `start_i <= t <= end_i`.

You start at node 0 at time 0.

In one unit of time, you can either:

<ul>
	<li>Wait at your current node without moving, or</li>
	<li>Travel along an outgoing edge from your current node if the current time `t` satisfies `start_i <= t <= end_i`.</li>
</ul>

Return the **minimum** time required to reach node `n - 1`. If it is impossible, return `-1`.
