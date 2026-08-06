## Description

You are given a 2D integer array `units` of size `m × n` where `units[i][j]` represents the capacity of the `j^th` unit in the `i^th` device. Each device contains **exactly** `n` units.

The **rating** of a device is the **minimum** capacity among all its units.

You may perform the following operation any number of times (including zero):

<ul>
	<li>Choose a device `i` that has **not been** used as a source before.</li>
	<li>Remove **exactly** one unit from device `i` and add it to **any** different device.</li>
	<li>Then mark device `i` as used, so it cannot be chosen again as a source.</li>
</ul>

Return the **maximum** possible sum of the ratings of all devices after any number of such operations.

**Note:**

<ul>
	<li>Devices can receive units from multiple devices, regardless of whether they have been selected.</li>
	<li>The rating of an empty device is 0.</li>
</ul>
