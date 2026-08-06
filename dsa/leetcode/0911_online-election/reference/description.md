## Description

You are given two integer arrays `persons` and `times`. In an election, the `i^th` vote was cast for `persons[i]` at time `times[i]`.

For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the `TopVotedCandidate` class:

<ul>
	<li>`TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.</li>
	<li>`int q(int t)` Returns the number of the person that was leading the election at time `t` according to the mentioned rules.</li>
</ul>
