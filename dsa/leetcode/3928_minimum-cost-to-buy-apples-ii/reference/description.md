## Description

You are given an integer `n` and an integer array `prices` of length `n`, where `prices[i]` is the price of apples at shop `i`.

You are also given a 2D integer array `roads`, where `roads[i] = [u_i, v_i, cost_i, tax_i]` represents a **bidirectional** road:

<ul>
	<li>`u_i` and `v_i` are the shops connected by the road.</li>
	<li>`cost_i` is the cost to travel the road **without** carrying apples.</li>
	<li>`tax_i` is the multiplier applied to `cost_i` when traveling **with** apples.</li>
</ul>

For each shop `i`, you can either:

<ul>
	<li>Buy apples locally at shop `i` for `prices[i]`.</li>
	<li>Travel **empty** to any shop `j` using **any** number of roads, buy apples for `prices[j]`, and return to shop `i` while carrying apples, paying `cost * tax` on each road used for the return trip.</li>
</ul>

The forward path, where you travel empty, and the return path may be **different**.

Return an integer array `ans` of length `n`, where `ans[i]` is the **minimum** total cost to buy apples starting from shop `i`.
