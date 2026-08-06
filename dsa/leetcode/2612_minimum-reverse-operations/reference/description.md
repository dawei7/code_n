## Description

You are given an integer `n` and an integer `p` representing an array `arr` of length `n` where all elements are set to 0's, except position `p` which is set to 1. You are also given an integer array `banned` containing restricted positions. Perform the following operation on `arr`:

<ul>
	<li>Reverse a <span data-keyword="subarray-nonempty">**subarray**</span> with size `k` if the single 1 is not set to a position in `banned`.</li>
</ul>

Return an integer array `answer` with `n` results where the `i^th` result is* *the **minimum** number of operations needed to bring the single 1 to position `i` in `arr`, or -1 if it is impossible.
