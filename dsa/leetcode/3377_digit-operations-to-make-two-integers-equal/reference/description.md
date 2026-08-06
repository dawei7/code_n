## Description

You are given two integers `n` and `m` that consist of the **same** number of digits.

You can perform the following operations **any** number of times:

<ul>
	<li>Choose **any** digit from `n` that is not 9 and **increase** it by 1.</li>
	<li>Choose **any** digit from `n` that is not 0 and **decrease** it by 1.</li>
</ul>

The integer `n` must not be a <span data-keyword="prime-number">prime</span> number at any point, including its original value and after each operation.

The cost of a transformation is the sum of **all** values that `n` takes throughout the operations performed.

Return the **minimum** cost to transform `n` into `m`. If it is impossible, return -1.
