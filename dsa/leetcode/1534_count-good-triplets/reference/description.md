## Description

Given an array of integers `arr`, and three integers `a`, `b` and `c`. You need to find the number of good triplets.



A triplet `(arr[i], arr[j], arr[k])` is **good** if the following conditions are true:



<ul>
	<li>`0 <= i < j < k < arr.length`</li>
	<li>`|arr[i] - arr[j]| <= a`</li>
	<li>`|arr[j] - arr[k]| <= b`</li>
	<li>`|arr[i] - arr[k]| <= c`</li>
</ul>

Where `|x|` denotes the absolute value of `x`.



Return* the number of good triplets*.
