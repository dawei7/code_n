## Description

You have `n` boxes labeled from `0` to `n - 1`. You are given four arrays: `status`, `candies`, `keys`, and `containedBoxes` where:

<ul>
	<li>`status[i]` is `1` if the `i^th` box is open and `0` if the `i^th` box is closed,</li>
	<li>`candies[i]` is the number of candies in the `i^th` box,</li>
	<li>`keys[i]` is a list of the labels of the boxes you can open after opening the `i^th` box.</li>
	<li>`containedBoxes[i]` is a list of the boxes you found inside the `i^th` box.</li>
</ul>

You are given an integer array `initialBoxes` that contains the labels of the boxes you initially have. You can take all the candies in **any open box** and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return *the maximum number of candies you can get following the rules above*.
