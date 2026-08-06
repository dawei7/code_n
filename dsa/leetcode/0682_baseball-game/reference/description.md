## Description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the `i^th` operation you must apply to the record and is one of the following:

<ul>
	<li>An integer `x`.

	<ul>
		<li>Record a new score of `x`.</li>
	</ul>
	</li>
	<li>`'+'`.
	<ul>
		<li>Record a new score that is the sum of the previous two scores.</li>
	</ul>
	</li>
	<li>`'D'`.
	<ul>
		<li>Record a new score that is the double of the previous score.</li>
	</ul>
	</li>
	<li>`'C'`.
	<ul>
		<li>Invalidate the previous score, removing it from the record.</li>
	</ul>
	</li>
</ul>

Return *the sum of all the scores on the record after applying all the operations*.

The test cases are generated such that the answer and all intermediate calculations fit in a **32-bit** integer and that all operations are valid.
