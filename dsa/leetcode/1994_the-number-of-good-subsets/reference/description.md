## Description

You are given an integer array `nums`. We call a subset of `nums` **good** if its product can be represented as a product of one or more **distinct prime** numbers.

<ul>
	<li>For example, if `nums = [1, 2, 3, 4]`:

	<ul>
		<li>`[2, 3]`, `[1, 2, 3]`, and `[1, 3]` are **good** subsets with products `6 = 2*3`, `6 = 2*3`, and `3 = 3` respectively.</li>
		<li>`[1, 4]` and `[4]` are not **good** subsets with products `4 = 2*2` and `4 = 2*2` respectively.</li>
	</ul>
	</li>
</ul>

Return *the number of different **good** subsets in *`nums`***modulo***`10^9 + 7`.

A **subset** of `nums` is any array that can be obtained by deleting some (possibly none or all) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.
