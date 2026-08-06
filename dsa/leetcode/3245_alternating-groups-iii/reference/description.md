## Description

There are some red and blue tiles arranged circularly. You are given an array of integers `colors` and a 2D integers array `queries`.

The color of tile `i` is represented by `colors[i]`:

<ul>
	<li>`colors[i] == 0` means that tile `i` is **red**.</li>
	<li>`colors[i] == 1` means that tile `i` is **blue**.</li>
</ul>

An **alternating** group is a contiguous subset of tiles in the circle with **alternating** colors (each tile in the group except the first and last one has a different color from its **adjacent** tiles in the group).

You have to process queries of two types:

<ul>
	<li>`queries[i] = [1, size_i]`, determine the count of **alternating** groups with size `size_i`.</li>
	<li>`queries[i] = [2, index_i, color_i]`, change `colors[index_i]` to `color<font face="monospace">_i</font>`.</li>
</ul>

Return an array `answer` containing the results of the queries of the first type *in order*.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.
