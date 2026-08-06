## Description

Bob is stuck in a dungeon and must break `n` locks, each requiring some amount of **energy** to break. The required energy for each lock is stored in an array called `strength` where `strength[i]` indicates the energy needed to break the `i^th` lock.

To break a lock, Bob uses a sword with the following characteristics:

<ul>
	<li>The initial energy of the sword is 0.</li>
	<li>The initial factor `<font face="monospace">x</font>` by which the energy of the sword increases is 1.</li>
	<li>Every minute, the energy of the sword increases by the current factor `x`.</li>
	<li>To break the `i^th` lock, the energy of the sword must reach **at least** `strength[i]`.</li>
	<li>After breaking a lock, the energy of the sword resets to 0, and the factor `x` increases by a given value `k`.</li>
</ul>

Your task is to determine the **minimum** time in minutes required for Bob to break all `n` locks and escape the dungeon.

Return the **minimum **time required for Bob to break all `n` locks.
