## Description

You are given two arrays, `instructions` and `values`, both of size `n`.

You need to simulate a process based on the following rules:

<ul>
	<li>You start at the first instruction at index `i = 0` with an initial score of 0.</li>
	<li>If `instructions[i]` is `"add"`:
	<ul>
		<li>Add `values[i]` to your score.</li>
		<li>Move to the next instruction `(i + 1)`.</li>
	</ul>
	</li>
	<li>If `instructions[i]` is `"jump"`:
	<ul>
		<li>Move to the instruction at index `(i + values[i])` without modifying your score.</li>
	</ul>
	</li>
</ul>

The process ends when you either:

<ul>
	<li>Go out of bounds (i.e., `i < 0 or i >= n`), or</li>
	<li>Attempt to revisit an instruction that has been previously executed. The revisited instruction is not executed.</li>
</ul>

Return your score at the end of the process.
