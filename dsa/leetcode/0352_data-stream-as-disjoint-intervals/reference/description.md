## Description

Given a data stream input of non-negative integers `a_1, a_2, ..., a_n`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:

<ul>
	<li>`SummaryRanges()` Initializes the object with an empty stream.</li>
	<li>`void addNum(int value)` Adds the integer `value` to the stream.</li>
	<li>`int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[start_i, end_i]`. The answer should be sorted by `start_i`.</li>
</ul>
