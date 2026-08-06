## Description

You are given the `root` of a **binary tree** with `n` nodes. Each node is uniquely assigned a value from `1` to `n`. You are also given an integer `startValue` representing the value of the start node `s`, and a different integer `destValue` representing the value of the destination node `t`.

Find the **shortest path** starting from node `s` and ending at node `t`. Generate step-by-step directions of such path as a string consisting of only the **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:

<ul>
	<li>`'L'` means to go from a node to its **left child** node.</li>
	<li>`'R'` means to go from a node to its **right child** node.</li>
	<li>`'U'` means to go from a node to its **parent** node.</li>
</ul>

Return *the step-by-step directions of the **shortest path** from node *`s`* to node* `t`.
