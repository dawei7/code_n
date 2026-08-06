## Description

Given a binary tree with the following rules:

<ol>
	<li>`root.val == 0`</li>
	<li>For any `treeNode`:
	<ol type="a">
		<li>If `treeNode.val` has a value `x` and `treeNode.left != null`, then `treeNode.left.val == 2 * x + 1`</li>
		<li>If `treeNode.val` has a value `x` and `treeNode.right != null`, then `treeNode.right.val == 2 * x + 2`</li>
	</ol>
	</li>
</ol>

Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.

Implement the `FindElements` class:

<ul>
	<li>`FindElements(TreeNode* root)` Initializes the object with a contaminated binary tree and recovers it.</li>
	<li>`bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.</li>
</ul>
