## Description

You are given an integer array `nums` of length `n`.

You start at index 0, and your goal is to reach index `n - 1`.

From any index `i`, you may perform one of the following operations:

<ul>
	<li>**Adjacent Step**: Jump to index `i + 1` or `i - 1`, if the index is within bounds.</li>
	<li>**Prime Teleportation**: If `nums[i]` is a <span data-keyword="prime-number">prime number</span> `p`, you may instantly jump to any index `j != i` such that `nums[j] % p == 0`.</li>
</ul>

Return the **minimum** number of jumps required to reach index `n - 1`.
