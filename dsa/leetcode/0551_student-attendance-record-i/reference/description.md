## Description

You are given a string `s` representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

<ul>
	<li>`'A'`: Absent.</li>
	<li>`'L'`: Late.</li>
	<li>`'P'`: Present.</li>
</ul>

The student is eligible for an attendance award if they meet **both** of the following criteria:

<ul>
	<li>The student was absent (`'A'`) for **strictly** fewer than 2 days **total**.</li>
	<li>The student was **never** late (`'L'`) for 3 or more **consecutive** days.</li>
</ul>

Return `true`* if the student is eligible for an attendance award, or *`false`* otherwise*.
