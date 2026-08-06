## Description

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

We define the **right** direction as positive x-axis (**increasing x-coordinate**) and the **left** direction as negative x-axis (**decreasing x-coordinate**). Similarly, we define the **up** direction as positive y-axis (**increasing y-coordinate**) and the **down** direction as negative y-axis (**decreasing y-coordinate**)

You have to place `n` people, including Alice and Bob, at these points such that there is **exactly one** person at every point. Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the **upper left corner** and Bob's position as the **lower right corner** of the fence (**Note** that the fence **might not** enclose any area, i.e. it can be a line). If any person other than Alice and Bob is either **inside** the fence or **on** the fence, Alice will be sad.

Return *the number of **pairs of points** where you can place Alice and Bob, such that Alice **does not** become sad on building the fence*.

**Note** that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. For example, Alice cannot build either of the fences in the picture below with four corners `(1, 1)`, `(1, 3)`, `(3, 1)`, and `(3, 3)`, because:

<ul>
	<li>With Alice at `(3, 3)` and Bob at `(1, 1)`, Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.</li>
	<li>With Alice at `(1, 3)` and Bob at `(1, 1)` (as the rectangle shown in the image instead of a line), Bob's position is not the lower right corner of the fence.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/example0alicebob-1.png" style="width: 750px; height: 308px;padding: 10px; background: #fff; border-radius: .5rem;" />
