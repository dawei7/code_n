## Description

You are given an integer array ​​​​​​​`nums`.

Define a **frequency balance <span data-keyword="subarray-nonempty">subarray</span>** as follows:

<ul>
	<li>If the subarray contains only one distinct value, it is frequency balanced.</li>
	<li>Otherwise, there must exist a positive integer `f` such that every distinct value in the subarray occurs either `f` or `2 * f` times, and both <span data-keyword="frequency-array">frequencies</span> occur among the distinct values.</li>
</ul>

Return an integer denoting the length of the **longest** frequency balance subarray.
