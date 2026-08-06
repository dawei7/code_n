## Description

You are given two integer arrays `nums1` and `nums2` of size `n`.

You can perform the following two operations any number of times on these two arrays:

<ul>
	<li>**Swap within the same array**: Choose two indices `i` and `j`. Then, choose either to swap `nums1[i]` and `nums1[j]`, or `nums2[i]` and `nums2[j]`. This operation is **free of charge**.</li>
	<li>**Swap between two arrays**: Choose an index `i`. Then, swap `nums1[i]` and `nums2[i]`. This operation **incurs a cost of 1**.</li>
</ul>

Return an integer denoting the **minimum cost** to make `nums1` and `nums2` **identical**. If this is not possible, return -1.
