## Description

You are given an integer array `nums` and two **distinct** integers `target1` and `target2`.

A **partition** of `nums` splits it into one or more **contiguous, non-empty** blocks that cover the entire array without overlap.

A partition is **valid** if the **bitwise XOR** of elements in its blocks **alternates** between `target1` and `target2`, starting with `target1`.

Formally, for blocks `b1`, `b2`, …:

<ul>
	<li>`XOR(b1) = target1`</li>
	<li>`XOR(b2) = target2` (if it exists)</li>
	<li>`XOR(b3) = target1`, and so on.</li>
</ul>

Return the number of valid partitions of `nums`, modulo `10^9 + 7`.

**Note:** A single block is valid if its **XOR** equals `target1`.
