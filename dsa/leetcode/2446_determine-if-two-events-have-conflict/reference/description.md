## Description

You are given two arrays of strings that represent two inclusive events that happened **on the same day**, `event1` and `event2`, where:

<ul>
	<li>`event1 = [startTime_1, endTime_1]` and</li>
	<li>`event2 = [startTime_2, endTime_2]`.</li>
</ul>

Event times are valid 24 hours format in the form of `HH:MM`.

A **conflict** happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return `true`* if there is a conflict between two events. Otherwise, return *`false`.
