## Description

You are given an integer array `gifts` denoting the number of gifts in various piles. Every second, you do the following:

<ul>
	<li>Choose the pile with the maximum number of gifts.</li>
	<li>If there is more than one pile with the maximum number of gifts, choose any.</li>
	<li>Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.</li>
</ul>

Return *the number of gifts remaining after *`k`* seconds.*
