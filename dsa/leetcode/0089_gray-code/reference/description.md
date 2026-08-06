## Description

An **n-bit gray code sequence** is a sequence of `2^n` integers where:

<ul>
	<li>Every integer is in the **inclusive** range `[0, 2^n - 1]`,</li>
	<li>The first integer is `0`,</li>
	<li>An integer appears **no more than once** in the sequence,</li>
	<li>The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and</li>
	<li>The binary representation of the **first** and **last** integers differs by **exactly one bit**.</li>
</ul>

Given an integer `n`, return *any valid **n-bit gray code sequence***.
