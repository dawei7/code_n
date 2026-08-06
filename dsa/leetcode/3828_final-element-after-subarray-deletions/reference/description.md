## Description

You are given an integer array `nums`.

Two players, Alice and Bob, play a game in turns, with Alice playing first.

<ul>
	<li>In each turn, the current player chooses any **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l..r]` such that `r - l + 1 < m`, where `m` is the **current length** of the array.</li>
	<li>The selected **subarray is removed**, and the remaining elements are **concatenated** to form the new array.</li>
	<li>The game continues until **only one** element remains.</li>
</ul>

Alice aims to **maximize** the final element, while Bob aims to **minimize** it. Assuming both play optimally, return the value of the final remaining element.
