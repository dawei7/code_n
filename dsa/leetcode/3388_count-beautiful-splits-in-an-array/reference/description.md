## Description

You are given an array `nums`.

A split of an array `nums` is **beautiful** if:

<ol>
	<li>The array `nums` is split into three <span data-keyword="subarray-nonempty">subarrays</span>: `nums1`, `nums2`, and `nums3`, such that `nums` can be formed by concatenating `nums1`, `nums2`, and `nums3` in that order.</li>
	<li>The subarray `nums1` is a <span data-keyword="array-prefix">prefix</span> of `nums2` **OR** `nums2` is a <span data-keyword="array-prefix">prefix</span> of `nums3`.</li>
</ol>

Return the **number of ways** you can make this split.
