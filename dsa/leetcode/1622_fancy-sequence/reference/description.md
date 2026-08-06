## Description

Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations.

Implement the `Fancy` class:

<ul>
	<li>`Fancy()` Initializes the object with an empty sequence.</li>
	<li>`void append(val)` Appends an integer `val` to the end of the sequence.</li>
	<li>`void addAll(inc)` Increments all existing values in the sequence by an integer `inc`.</li>
	<li>`void multAll(m)` Multiplies all existing values in the sequence by an integer `m`.</li>
	<li>`int getIndex(idx)` Gets the current value at index `idx` (0-indexed) of the sequence **modulo** `10^9 + 7`. If the index is greater or equal than the length of the sequence, return `-1`.</li>
</ul>
