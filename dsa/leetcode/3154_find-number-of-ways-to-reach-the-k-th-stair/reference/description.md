## Description

You are given a **non-negative** integer `k`. There exists a staircase with an infinite number of stairs, with the **lowest** stair numbered 0.

Alice has an integer `jump`, with an initial value of 0. She starts on stair 1 and wants to reach stair `k` using **any** number of **operations**. If she is on stair `i`, in one **operation** she can:

<ul>
	<li>Go down to stair `i - 1`. This operation **cannot** be used consecutively or on stair 0.</li>
	<li>Go up to stair `i + 2^jump`. And then, `jump` becomes `jump + 1`.</li>
</ul>

Return the *total* number of ways Alice can reach stair `k`.

**Note** that it is possible that Alice reaches the stair `k`, and performs some operations to reach the stair `k` again.
