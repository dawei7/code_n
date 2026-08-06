## Description

There are `n` uniquely-sized sticks whose lengths are integers from `1` to `n`. You want to arrange the sticks such that **exactly** `k` sticks are **visible** from the left. A stick is **visible** from the left if there are no **longer** sticks to the **left** of it.

<ul>
	<li>For example, if the sticks are arranged `[<u>1</u>,<u>3</u>,2,<u>5</u>,4]`, then the sticks with lengths `1`, `3`, and `5` are visible from the left.</li>
</ul>

Given `n` and `k`, return *the **number** of such arrangements*. Since the answer may be large, return it **modulo** `10^9 + 7`.
