## Description

You are given the `root` of a binary tree.

A ZigZag path for a binary tree is defined as follow:

<ul>
	<li>Choose **any **node in the binary tree and a direction (right or left).</li>
	<li>If the current direction is right, move to the right child of the current node; otherwise, move to the left child.</li>
	<li>Change the direction from right to left or from left to right.</li>
	<li>Repeat the second and third steps until you can't move in the tree.</li>
</ul>

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return *the longest **ZigZag** path contained in that tree*.
