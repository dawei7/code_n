## Description

You are given an `m x n` grid `grid` where:

<ul>
	<li>`'.'` is an empty cell.</li>
	<li>`'#'` is a wall.</li>
	<li>`'@'` is the starting point.</li>
	<li>Lowercase letters represent keys.</li>
	<li>Uppercase letters represent locks.</li>
</ul>

You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some `<font face="monospace">1 <= k <= 6</font>`, there is exactly one lowercase and one uppercase letter of the first `k` letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return *the lowest number of moves to acquire all keys*. If it is impossible, return `-1`.
