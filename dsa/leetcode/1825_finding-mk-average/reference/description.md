## Description

You are given two integers, `m` and `k`, and a stream of integers. You are tasked to implement a data structure that calculates the **MKAverage** for the stream.

The **MKAverage** can be calculated using these steps:

<ol>
	<li>If the number of the elements in the stream is less than `m` you should consider the **MKAverage** to be `-1`. Otherwise, copy the last `m` elements of the stream to a separate container.</li>
	<li>Remove the smallest `k` elements and the largest `k` elements from the container.</li>
	<li>Calculate the average value for the rest of the elements **rounded down to the nearest integer**.</li>
</ol>

Implement the `MKAverage` class:

<ul>
	<li>`MKAverage(int m, int k)` Initializes the **MKAverage** object with an empty stream and the two integers `m` and `k`.</li>
	<li>`void addElement(int num)` Inserts a new element `num` into the stream.</li>
	<li>`int calculateMKAverage()` Calculates and returns the **MKAverage** for the current stream **rounded down to the nearest integer**.</li>
</ul>
