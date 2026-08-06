## Description

You are given an integer array `nums` of length `n` and an integer `numSlots` such that `2 * numSlots >= n`. There are `numSlots` slots numbered from `1` to `numSlots`.

You have to place all `n` integers into the slots such that each slot contains at **most** two numbers. The **AND sum** of a given placement is the sum of the **bitwise** `AND` of every number with its respective slot number.

<ul>
	<li>For example, the **AND sum** of placing the numbers `[1, 3]` into slot <u>`1`</u> and `[4, 6]` into slot <u>`2`</u> is equal to `(1 AND <u>1</u>) + (3 AND <u>1</u>) + (4 AND <u>2</u>) + (6 AND <u>2</u>) = 1 + 1 + 0 + 2 = 4`.</li>
</ul>

Return *the maximum possible **AND sum** of *`nums`* given *`numSlots`* slots.*
