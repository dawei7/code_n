## Description

You are given the `head` of a linked list.

The nodes in the linked list are **sequentially** assigned to **non-empty** groups whose lengths form the sequence of the natural numbers (`1, 2, 3, 4, ...`). The **length** of a group is the number of nodes assigned to it. In other words,

<ul>
	<li>The `1^st` node is assigned to the first group.</li>
	<li>The `2^nd` and the `3^rd` nodes are assigned to the second group.</li>
	<li>The `4^th`, `5^th`, and `6^th` nodes are assigned to the third group, and so on.</li>
</ul>

Note that the length of the last group may be less than or equal to `1 + the length of the second to last group`.

**Reverse** the nodes in each group with an **even** length, and return *the* `head` *of the modified linked list*.
