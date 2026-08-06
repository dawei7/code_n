## Description

You are given a string `s`. Simulate events at each second `i`:

<ul>
	<li>If `s[i] == 'E'`, a person enters the waiting room and takes one of the chairs in it.</li>
	<li>If `s[i] == 'L'`, a person leaves the waiting room, freeing up a chair.</li>
</ul>

Return the **minimum **number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially **empty**.
