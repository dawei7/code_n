## Description

You are given `n` individuals at a base camp who need to cross a river to reach a destination using a single boat. The boat can carry at most `k` people at a time. The trip is affected by environmental conditions that vary **cyclically** over `m` stages.

Each stage `j` has a speed multiplier `mul[j]`:

<ul>
	<li>If `mul[j] > 1`, the trip slows down.</li>
	<li>If `mul[j] < 1`, the trip speeds up.</li>
</ul>

Each individual `i` has a rowing strength represented by `time[i]`, the time (in minutes) it takes them to cross alone in neutral conditions.

**Rules:**

<ul>
	<li>A group `g` departing at stage `j` takes time equal to the **maximum** `time[i]` among its members, multiplied by `mul[j]` minutes to reach the destination.</li>
	<li>After the group crosses the river in time `d`, the stage advances by `floor(d) % m` steps.</li>
	<li>If individuals are left behind, one person must return with the boat. Let `r` be the index of the returning person, the return takes `time[r] × mul[current_stage]`, defined as `return_time`, and the stage advances by `floor(return_time) % m`.</li>
</ul>

Return the **minimum** total time required to transport all individuals. If it is not possible to transport all individuals to the destination, return `-1`.
