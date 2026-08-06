## Description

There are two types of persons:

<ul>
	<li>The **good person**: The person who always tells the truth.</li>
	<li>The **bad person**: The person who might tell the truth and might lie.</li>
</ul>

You are given a **0-indexed** 2D integer array `statements` of size `n x n` that represents the statements made by `n` people about each other. More specifically, `statements[i][j]` could be one of the following:

<ul>
	<li>`0` which represents a statement made by person `i` that person `j` is a **bad** person.</li>
	<li>`1` which represents a statement made by person `i` that person `j` is a **good** person.</li>
	<li>`2` represents that **no statement** is made by person `i` about person `j`.</li>
</ul>

Additionally, no person ever makes a statement about themselves. Formally, we have that `statements[i][i] = 2` for all `0 <= i < n`.

Return *the **maximum** number of people who can be **good** based on the statements made by the *`n`* people*.
