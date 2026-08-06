## Description

You are given two integer arrays `nums1` and `nums2`, and a 2D integer array `queries`.

Each `queries[i]` is one of the following types:

<ul>
	<li>`[1, x, y, val]` – **Add** `val` to every element in `nums2[x..y]`.</li>
	<li>`[2, tot]` – **Compute** the number of pairs `(j, k)` such that `nums1[j] + nums2[k] == tot`.</li>
</ul>

Return an integer array `answer`, where `answer[j]` is the number of pairs for the `j^th` query of type 2.
