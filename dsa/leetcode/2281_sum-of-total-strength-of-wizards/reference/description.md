## Description

As the ruler of a kingdom, you have an army of wizards at your command.

You are given a **0-indexed** integer array `strength`, where `strength[i]` denotes the strength of the `i^th` wizard. For a **contiguous** group of wizards (i.e. the wizards' strengths form a **subarray** of `strength`), the **total strength** is defined as the **product** of the following two values:

<ul>
	<li>The strength of the **weakest** wizard in the group.</li>
	<li>The **total** of all the individual strengths of the wizards in the group.</li>
</ul>

Return *the **sum** of the total strengths of **all** contiguous groups of wizards*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.
