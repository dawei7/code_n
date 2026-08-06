## Description

You are given a string `num`, representing a large integer, and an integer `k`.

We call some integer **wonderful** if it is a **permutation** of the digits in `num` and is **greater in value** than `num`. There can be many wonderful integers. However, we only care about the **smallest-valued** ones.

<ul>
	<li>For example, when `num = "5489355142"`:

	<ul>
		<li>The 1^st smallest wonderful integer is `"5489355214"`.</li>
		<li>The 2^nd smallest wonderful integer is `"5489355241"`.</li>
		<li>The 3^rd smallest wonderful integer is `"5489355412"`.</li>
		<li>The 4^th smallest wonderful integer is `"5489355421"`.</li>
	</ul>
	</li>
</ul>

Return *the **minimum number of adjacent digit swaps** that needs to be applied to *`num`* to reach the *`k^th`*** smallest wonderful** integer*.

The tests are generated in such a way that `k^th` smallest wonderful integer exists.
