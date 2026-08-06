## Description

Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

<ul>
	<li>`i + 1` where: `i + 1 < arr.length`.</li>
	<li>`i - 1` where: `i - 1 >= 0`.</li>
	<li>`j` where: `arr[i] == arr[j]` and `i != j`.</li>
</ul>

Return *the minimum number of steps* to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.
