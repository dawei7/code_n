## Description

You are given a **0-indexed** integer array `nums` of **even** length and there is also an empty array `arr`. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

<ul>
	<li>Every round, first Alice will remove the **minimum** element from `nums`, and then Bob does the same.</li>
	<li>Now, first Bob will append the removed element in the array `arr`, and then Alice does the same.</li>
	<li>The game continues until `nums` becomes empty.</li>
</ul>

Return *the resulting array *`arr`.
