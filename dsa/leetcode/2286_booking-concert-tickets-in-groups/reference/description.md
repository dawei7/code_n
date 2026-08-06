## Description

A concert hall has `n` rows numbered from `0` to `n - 1`, each with `m` seats, numbered from `0` to `m - 1`. You need to design a ticketing system that can allocate seats in the following cases:

<ul>
	<li>If a group of `k` spectators can sit **together** in a row.</li>
	<li>If **every** member of a group of `k` spectators can get a seat. They may or **may not** sit together.</li>
</ul>

Note that the spectators are very picky. Hence:

<ul>
	<li>They will book seats only if each member of their group can get a seat with row number **less than or equal** to `maxRow`. `maxRow` can **vary** from group to group.</li>
	<li>In case there are multiple rows to choose from, the row with the **smallest** number is chosen. If there are multiple seats to choose in the same row, the seat with the **smallest** number is chosen.</li>
</ul>

Implement the `BookMyShow` class:

<ul>
	<li>`BookMyShow(int n, int m)` Initializes the object with `n` as number of rows and `m` as number of seats per row.</li>
	<li>`int[] gather(int k, int maxRow)` Returns an array of length `2` denoting the row and seat number (respectively) of the **first seat** being allocated to the `k` members of the group, who must sit **together**. In other words, it returns the smallest possible `r` and `c` such that all `[c, c + k - 1]` seats are valid and empty in row `r`, and `r <= maxRow`. Returns `[]` in case it is **not possible** to allocate seats to the group.</li>
	<li>`boolean scatter(int k, int maxRow)` Returns `true` if all `k` members of the group can be allocated seats in rows `0` to `maxRow`, who may or **may not** sit together. If the seats can be allocated, it allocates `k` seats to the group with the **smallest** row numbers, and the smallest possible seat numbers in each row. Otherwise, returns `false`.</li>
</ul>
