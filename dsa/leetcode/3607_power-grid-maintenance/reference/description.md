## Description

<p data-end="401" data-start="120">You are given an integer <code data-end="194" data-start="191">c</code> representing <code data-end="211" data-start="208">c</code> power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

<p data-end="401" data-start="120">These stations are interconnected via <code data-end="295" data-start="292">n</code> **bidirectional** cables, represented by a 2D array <code data-end="357" data-start="344">connections</code>, where each element <code data-end="430" data-start="405">connections[i] = [u_i, v_i]</code> indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

<p data-end="626" data-start="586">Initially, **all** stations are online (operational).

<p data-end="720" data-start="628">You are also given a 2D array <code data-end="667" data-start="658">queries</code>, where each query is one of the following *two* types:

<ul data-end="995" data-start="722">
	<li data-end="921" data-start="722">
	<p data-end="921" data-start="724"><code data-end="732" data-start="724">[1, x]</code>: A maintenance check is requested for station <code data-end="782" data-start="779">x</code>. If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** **operational** station *exists* in that grid, return -1.

	</li>
	<li data-end="995" data-start="923">
	<p data-end="995" data-start="925"><code data-end="933" data-start="925">[2, x]</code>: Station <code data-end="946" data-start="943">x</code> goes offline (i.e., it becomes non-operational).

	</li>
</ul>

<p data-end="1106" data-start="997">Return an array of integers representing the results of each query of type <code data-end="1080" data-start="1072">[1, x]</code> in the **order** they appear.

<p data-end="1106" data-start="997">**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
