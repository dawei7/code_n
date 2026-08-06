## Description

An ant is on a boundary. It sometimes goes **left** and sometimes **right**.

You are given an array of **non-zero** integers `nums`. The ant starts reading `nums` from the first element of it to its end. At each step, it moves according to the value of the current element:

<ul>
	<li>If `nums[i] < 0`, it moves **left** by<!-- notionvc: 55fee232-4fc9-445f-952a-f1b979415864 --> `-nums[i]` units.</li>
	<li>If `nums[i] > 0`, it moves **right** by `nums[i]` units.</li>
</ul>

Return *the number of times the ant **returns** to the boundary.*

**Notes:**

<ul>
	<li>There is an infinite space on both sides of the boundary.</li>
	<li>We check whether the ant is on the boundary only after it has moved `|nums[i]|` units. In other words, if the ant crosses the boundary during its movement, it does not count.<!-- notionvc: 5ff95338-8634-4d02-a085-1e83c0be6fcd --></li>
</ul>
