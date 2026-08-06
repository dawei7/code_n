## Description

There is a circle of red and blue tiles. You are given an array of integers `colors`. The color of tile `i` is represented by `colors[i]`:

<ul>
	<li>`colors[i] == 0` means that tile `i` is **red**.</li>
	<li>`colors[i] == 1` means that tile `i` is **blue**.</li>
</ul>

Every 3 contiguous tiles in the circle with **alternating** colors (the middle tile has a different color from its **left** and **right** tiles) is called an **alternating** group.

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.
