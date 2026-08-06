## Description

A **peak** in an array `arr` is an element that is **greater** than its previous and next element in `arr`.

You are given an integer array `nums` and a 2D integer array `queries`.

You have to process queries of two types:

<ul>
	<li>`queries[i] = [1, l_i, r_i]`, determine the count of **peak** elements in the <span data-keyword="subarray">subarray</span> `nums[l_i..r_i]`.<!-- notionvc: 73b20b7c-e1ab-4dac-86d0-13761094a9ae --></li>
	<li>`queries[i] = [2, index_i, val_i]`, change `nums[index_i]` to `<font face="monospace">val_i</font>`.</li>
</ul>

Return an array `answer` containing the results of the queries of the first type in order.<!-- notionvc: a9ccef22-4061-4b5a-b4cc-a2b2a0e12f30 -->

**Notes:**

<ul>
	<li>The **first** and the **last** element of an array or a subarray<!-- notionvc: fcffef72-deb5-47cb-8719-3a3790102f73 --> **cannot** be a peak.</li>
</ul>
