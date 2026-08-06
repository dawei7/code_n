## Description

For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are **equal** to `value`.

Implement the **DataStream** class:

<ul>
	<li>`DataStream(int value, int k)` Initializes the object with an empty integer stream and the two integers `value` and `k`.</li>
	<li>`boolean consec(int num)` Adds `num` to the stream of integers. Returns `true` if the last `k` integers are equal to `value`, and `false` otherwise. If there are less than `k` integers, the condition does not hold true, so returns `false`.</li>
</ul>
