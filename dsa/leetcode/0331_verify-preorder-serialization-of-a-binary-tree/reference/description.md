## Description

One way to serialize a binary tree is to use **preorder traversal**. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `'#'`.

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/pre-tree.jpg" style="width: 362px; height: 293px;" />
For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `'#'` represents a null node.

Given a string of comma-separated values `preorder`, return `true` if it is a correct preorder traversal serialization of a binary tree.

It is **guaranteed** that each comma-separated value in the string must be either an integer or a character `'#'` representing null pointer.

You may assume that the input format is always valid.

<ul>
	<li>For example, it could never contain two consecutive commas, such as `"1,,3"`.</li>
</ul>

**Note: **You are not allowed to reconstruct the tree.
