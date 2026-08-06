## Description

You are given an integer `n` representing the number of tasks in a project, numbered from 0 to `n - 1`. These tasks are connected as a **tree** rooted at task 0. This is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that task `u_i` is the parent of task `v_i`.

You are also given an array `baseTime` of length `n`, where `baseTime[i]` represents the time to complete task `i`.

The **finish time** of each task is calculated as follows:

<ul>
	<li>Leaf task: The finish time is `baseTime[i]`.</li>
	<li>Non-leaf task:
	<ul>
		<li>Let `earliest` be the **minimum** finish time among its children, and `latest` be the **maximum** finish time among its children.</li>
		<li>Let `ownDuration` be `(latest - earliest) + baseTime[i]`.</li>
		<li>The finish time of task `i` is `latest + ownDuration`.</li>
	</ul>
	</li>
</ul>

Return the finish time of the root task 0.
