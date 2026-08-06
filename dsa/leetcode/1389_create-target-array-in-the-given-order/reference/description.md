## Description

Given two arrays of integers `nums` and `index`. Your task is to create *target* array under the following rules:

<ul>
	<li>Initially *target* array is empty.</li>
	<li>From left to right read nums[i] and index[i], insert at index `index[i]` the value `nums[i]` in *target* array.</li>
	<li>Repeat the previous step until there are no elements to read in `nums` and `index.`</li>
</ul>

Return the *target* array.

It is guaranteed that the insertion operations will be valid.
