## Description

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `i^th` friend brings you to the `(i+1)^th` friend for `1 <= i < n`, and moving clockwise from the `n^th` friend brings you to the `1^st` friend.

The rules of the game are as follows:

<ol>
	<li>**Start** at the `1^st` friend.</li>
	<li>Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.</li>
	<li>The last friend you counted leaves the circle and loses the game.</li>
	<li>If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.</li>
	<li>Else, the last friend in the circle wins the game.</li>
</ol>

Given the number of friends, `n`, and an integer `k`, return *the winner of the game*.
