## Description

You are given two 2D integer arrays `series1` and `series2`.

Each element in both series is of the form `[timestamp, value]`, where:

<ul>
	<li>`timestamp` is an integer representing the time.</li>
	<li>`value` is an integer representing the value at that timestamp.</li>
</ul>

Each array is sorted in <span data-keyword="strictly-increasing-array">strictly increasing</span> order of `timestamp`.

For any timestamp **not present** in a series, its value is taken from the **next available timestamp** in the same series if one exists. Otherwise, its value is considered 0.

The **aggregated series** is formed by summing the corresponding values from both series at every timestamp that appears in either series.

Return the **aggregated series** as a 2D integer array of `[timestamp, summedValue]` pairs, sorted in **strictly increasing** order of timestamp.
