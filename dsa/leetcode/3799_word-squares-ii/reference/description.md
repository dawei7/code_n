## Description

You are given a string array `words`, consisting of **distinct** 4-letter strings, each containing lowercase English letters.

A **word square** consists of 4 **distinct** words: `top`, `left`, `right` and `bottom`, arranged as follows:

<ul>
	<li>`top` forms the **top row**.</li>
	<li>`bottom` forms the **bottom row**.</li>
	<li>`left` forms the **left column** (top to bottom).</li>
	<li>`right` forms the **right column** (top to bottom).</li>
</ul>

It must satisfy:

<ul>
	<li>`top[0] == left[0]`, `top[3] == right[0]`</li>
	<li>`bottom[0] == left[3]`, `bottom[3] == right[3]`</li>
</ul>

Return all valid **distinct** word squares, sorted in **ascending lexicographic** order by the 4-tuple `(top, left, right, bottom)​​​​​​​`.
