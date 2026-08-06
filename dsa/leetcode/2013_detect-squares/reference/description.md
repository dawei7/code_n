## Description

You are given a stream of points on the X-Y plane. Design an algorithm that:

<ul>
	<li>**Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.</li>
	<li>Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.</li>
</ul>

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

<ul>
	<li>`DetectSquares()` Initializes the object with an empty data structure.</li>
	<li>`void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.</li>
	<li>`int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.</li>
</ul>
