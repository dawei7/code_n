## Description

You are given an integer `n` representing the dimensions of an `n x n`<!-- notionvc: fa9fe4ed-dff8-4410-8196-346f2d430795 --> grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates `rectangles`, where `rectangles[i]` is in the form `[start_x, start_y, end_x, end_y]`, representing a rectangle on the grid. Each rectangle is defined as follows:

<ul>
	<li>`(start_x, start_y)`: The bottom-left corner of the rectangle.</li>
	<li>`(end_x, end_y)`: The top-right corner of the rectangle.</li>
</ul>

**Note **that the rectangles do not overlap. Your task is to determine if it is possible to make **either two horizontal or two vertical cuts** on the grid such that:

<ul>
	<li>Each of the three resulting sections formed by the cuts contains **at least** one rectangle.</li>
	<li>Every rectangle belongs to **exactly** one section.</li>
</ul>

Return `true` if such cuts can be made; otherwise, return `false`.
