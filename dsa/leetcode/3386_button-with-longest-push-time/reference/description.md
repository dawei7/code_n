## Description

You are given a 2D array `events` which represents a sequence of events where a child pushes a series of buttons on a keyboard.

Each `events[i] = [index_i, time_i]` indicates that the button at index `index_i` was pressed at time `time_i`.

<ul>
	<li>The array is **sorted** in increasing order of `time`.</li>
	<li>The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed.</li>
</ul>

Return the `index` of the button that took the **longest** time to push. If multiple buttons have the same longest time, return the button with the **smallest** `index`.
