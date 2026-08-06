## Description

You are given an integer array `ranks` and a character array `suits`. You have `5` cards where the `i^th` card has a rank of `ranks[i]` and a suit of `suits[i]`.

The following are the types of **poker hands** you can make from best to worst:

<ol>
	<li>`"Flush"`: Five cards of the same suit.</li>
	<li>`"Three of a Kind"`: Three cards of the same rank.</li>
	<li>`"Pair"`: Two cards of the same rank.</li>
	<li>`"High Card"`: Any single card.</li>
</ol>

Return *a string representing the **best** type of **poker hand** you can make with the given cards.*

**Note** that the return values are **case-sensitive**.
