## Description

You are given an array `nums` consisting of positive integers.

Starting with `score = 0`, apply the following algorithm:

<ul>
	<li>Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.</li>
	<li>Add the value of the chosen integer to `score`.</li>
	<li>Mark **the chosen element and its two adjacent elements if they exist**.</li>
	<li>Repeat until all the array elements are marked.</li>
</ul>

Return *the score you get after applying the above algorithm*.
