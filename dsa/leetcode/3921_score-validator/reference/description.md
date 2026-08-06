## Description

You are given a string array `events`.

Initially, `score = 0` and `counter = 0`. Each element in `events` is one of the following:

<ul>
	<li>`"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`: Add that value to the total score.</li>
	<li>`"W"`: Increase the counter by 1. No score is added.</li>
	<li>`"WD"`: Add 1 to the total score.</li>
	<li>`"NB"`: Add 1 to the total score.</li>
</ul>

Process the array from left to right. Stop processing when either:

<ul>
	<li>All elements in `events` have been processed, or</li>
	<li>The counter becomes 10.</li>
</ul>

Return an integer array `[score, counter]`, where:

<ul>
	<li>`score` is the final total score.</li>
	<li>`counter` is the final counter value.</li>
</ul>
