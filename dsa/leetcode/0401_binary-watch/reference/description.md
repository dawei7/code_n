## Description

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

<ul>
	<li>For example, the below binary watch reads `"4:51"`.</li>
</ul>

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" style="width: 500px; height: 500px;" />

Given an integer `turnedOn` which represents the number of LEDs that are currently on (ignoring the PM), return *all possible times the watch could represent*. You may return the answer in **any order**.

The hour must not contain a leading zero.

<ul>
	<li>For example, `"01:00"` is not valid. It should be `"1:00"`.</li>
</ul>

The minute must consist of two digits and may contain a leading zero.

<ul>
	<li>For example, `"10:2"` is not valid. It should be `"10:02"`.</li>
</ul>
