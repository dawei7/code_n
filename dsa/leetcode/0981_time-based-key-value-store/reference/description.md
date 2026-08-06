## Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

<ul>
	<li>`TimeMap()` Initializes the object of the data structure.</li>
	<li>`void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.</li>
	<li>`String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.</li>
</ul>
