## Description

Design an iterator that supports the `peek` operation on an existing iterator in addition to the `hasNext` and the `next` operations.

Implement the `PeekingIterator` class:

<ul>
	<li>`PeekingIterator(Iterator<int> nums)` Initializes the object with the given integer iterator `iterator`.</li>
	<li>`int next()` Returns the next element in the array and moves the pointer to the next element.</li>
	<li>`boolean hasNext()` Returns `true` if there are still elements in the array.</li>
	<li>`int peek()` Returns the next element in the array **without** moving the pointer.</li>
</ul>

**Note:** Each language may have a different implementation of the constructor and `Iterator`, but they all support the `int next()` and `boolean hasNext()` functions.
