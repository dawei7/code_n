## Description

You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

<ol>
	<li>**Add** a positive integer to an element of a given index in the array `nums2`.</li>
	<li>**Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).</li>
</ol>

Implement the `FindSumPairs` class:

<ul>
	<li>`FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.</li>
	<li>`void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply `nums2[index] += val`.</li>
	<li>`int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.</li>
</ul>
