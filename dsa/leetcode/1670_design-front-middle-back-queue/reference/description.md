## Description

Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBack` class:

<ul>
	<li>`FrontMiddleBack()` Initializes the queue.</li>
	<li>`void pushFront(int val)` Adds `val` to the **front** of the queue.</li>
	<li>`void pushMiddle(int val)` Adds `val` to the **middle** of the queue.</li>
	<li>`void pushBack(int val)` Adds `val` to the **back** of the queue.</li>
	<li>`int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `-1`.</li>
	<li>`int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `-1`.</li>
	<li>`int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `-1`.</li>
</ul>

**Notice** that when there are **two** middle position choices, the operation is performed on the **frontmost** middle position choice. For example:

<ul>
	<li>Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, <u>6</u>, 3, 4, 5]`.</li>
	<li>Popping the middle from `[1, 2, <u>3</u>, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.</li>
</ul>
