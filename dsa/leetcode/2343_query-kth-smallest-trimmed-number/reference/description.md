## Description

You are given a **0-indexed** array of strings `nums`, where each string is of **equal length** and consists of only digits.

You are also given a **0-indexed** 2D integer array `queries` where `queries[i] = [k_i, trim_i]`. For each `queries[i]`, you need to:

<ul>
	<li>**Trim** each number in `nums` to its **rightmost** `trim_i` digits.</li>
	<li>Determine the **index** of the `k_i^th` smallest trimmed number in `nums`. If two trimmed numbers are equal, the number with the **lower** index is considered to be smaller.</li>
	<li>Reset each number in `nums` to its original length.</li>
</ul>

Return *an array *`answer`* of the same length as *`queries`,* where *`answer[i]`* is the answer to the *`i^th`* query.*

**Note**:

<ul>
	<li>To trim to the rightmost `x` digits means to keep removing the leftmost digit, until only `x` digits remain.</li>
	<li>Strings in `nums` may contain leading zeros.</li>
</ul>
