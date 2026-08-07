## Description

You are given two integers `red` and `blue` representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1^st row will have 1 ball, the 2^nd row will have 2 balls, the 3^rd row will have 3 balls, and so on.

All the balls in a particular row should be the **same** color, and adjacent rows should have **different** colors.

Return the **maximum*** height of the triangle* that can be achieved.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">red = 2, blue = 4</span>

**Output:** 3

**Explanation:**

![](images/brb.png)

The only possible arrangement is shown above.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">red = 2, blue = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/br.png)

The only possible arrangement is shown above.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">red = 1, blue = 1</span>

**Output:** <span class="example-io">1</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">red = 10, blue = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/br.png)

The only possible arrangement is shown above.

</div>

**Constraints:**

	- `1 <= red, blue <= 100`
