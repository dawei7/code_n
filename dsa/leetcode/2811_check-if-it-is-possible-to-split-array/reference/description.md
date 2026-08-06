## Description

You are given an array `nums` of length `n` and an integer `m`. You need to determine if it is possible to split the array into `n` arrays of size 1 by performing a series of steps.

An array is called **good** if:

<ul>
	<li>The length of the array is **one**, or</li>
	<li>The sum of the elements of the array is **greater than or equal** to `m`.</li>
</ul>

In each step, you can select an existing array (which may be the result of previous steps) with a length of **at least two** and split it into **two **arrays, if both resulting arrays are good.

Return true if you can split the given array into `n` arrays, otherwise return false.
