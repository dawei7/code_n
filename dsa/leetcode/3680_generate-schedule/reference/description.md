## Description

You are given an integer `n` representing `n` teams. You are asked to generate a schedule such that:

<ul>
	<li>Each team plays every other team **exactly twice**: once at home and once away.</li>
	<li>There is **exactly one** match per day; the schedule is a list of **consecutive** days and `schedule[i]` is the match on day `i`.</li>
	<li>No team plays on **consecutive** days.</li>
</ul>

Return a 2D integer array `schedule`, where `schedule[i][0]` represents the home team and `schedule[i][1]` represents the away team. If multiple schedules meet the conditions, return **any** one of them.

If no schedule exists that meets the conditions, return an empty array.
