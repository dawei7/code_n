## Description

You are given an integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return *a list *`answer`* of size *`2`* where:*

<ul>
	<li>`answer[0]` is a list of all players that have **not** lost any matches.</li>
	<li>`answer[1]` is a list of all players that have lost exactly **one** match.</li>
</ul>

The values in the two lists should be returned in **increasing** order.

**Note:**

<ul>
	<li>You should only consider the players that have played **at least one** match.</li>
	<li>The testcases will be generated such that **no** two matches will have the **same** outcome.</li>
</ul>
