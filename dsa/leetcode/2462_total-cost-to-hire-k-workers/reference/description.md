## Description

You are given a **0-indexed** integer array `costs` where `costs[i]` is the cost of hiring the `i^th` worker.

You are also given two integers `k` and `candidates`. We want to hire exactly `k` workers according to the following rules:

<ul>
	<li>You will run `k` sessions and hire exactly one worker in each session.</li>
	<li>In each hiring session, choose the worker with the lowest cost from either the first `candidates` workers or the last `candidates` workers. Break the tie by the smallest index.
	<ul>
		<li>For example, if `costs = [3,2,7,7,1,2]` and `candidates = 2`, then in the first hiring session, we will choose the `4^th` worker because they have the lowest cost `[<u>3,2</u>,7,7,<u>**1**,2</u>]`.</li>
		<li>In the second hiring session, we will choose `1^st` worker because they have the same lowest cost as `4^th` worker but they have the smallest index `[<u>3,**2**</u>,7,<u>7,2</u>]`. Please note that the indexing may be changed in the process.</li>
	</ul>
	</li>
	<li>If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.</li>
	<li>A worker can only be chosen once.</li>
</ul>

Return *the total cost to hire exactly *`k`* workers.*
