## Description

You are given the `root` of a binary tree with **unique** values, and an integer `start`. At minute `0`, an **infection** starts from the node with value `start`.

Each minute, a node becomes infected if:

<ul>
	<li>The node is currently uninfected.</li>
	<li>The node is adjacent to an infected node.</li>
</ul>

Return *the number of minutes needed for the entire tree to be infected.*
