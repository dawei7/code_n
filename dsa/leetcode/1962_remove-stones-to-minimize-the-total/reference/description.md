## Description

You are given a **0-indexed** integer array `piles`, where `piles[i]` represents the number of stones in the `i^th` pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

<ul>
	<li>Choose any `piles[i]` and **remove** `floor(piles[i] / 2)` stones from it.</li>
</ul>

**Notice** that you can apply the operation on the **same** pile more than once.

Return *the **minimum** possible total number of stones remaining after applying the *`k`* operations*.

`floor(x)` is the **largest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).
