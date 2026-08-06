## Description

You are given two **2D** integer arrays `nums1` and `nums2.`

<ul>
	<li>`nums1[i] = [id_i, val_i]` indicate that the number with the id `id_i` has a value equal to `val_i`.</li>
	<li>`nums2[i] = [id_i, val_i]` indicate that the number with the id `id_i` has a value equal to `val_i`.</li>
</ul>

Each array contains **unique** ids and is sorted in **ascending** order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

<ul>
	<li>Only ids that appear in at least one of the two arrays should be included in the resulting array.</li>
	<li>Each id should be included **only once** and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be `0`.</li>
</ul>

Return *the resulting array*. The returned array must be sorted in ascending order by id.
