## Description

You are given a positive integer `n`, that is initially placed on a board. Every day, for `10^9` days, you perform the following procedure:

<ul>
	<li>For each number `x` present on the board, find all numbers `1 <= i <= n` such that `x % i == 1`.</li>
	<li>Then, place those numbers on the board.</li>
</ul>

Return* the number of **distinct** integers present on the board after* `10^9` *days have elapsed*.

**Note:**

<ul>
	<li>Once a number is placed on the board, it will remain on it until the end.</li>
	<li>`%` stands for the modulo operation. For example, `14 % 3` is `2`.</li>
</ul>
