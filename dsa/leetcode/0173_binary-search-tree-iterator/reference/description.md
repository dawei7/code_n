## Description

Implement the `BSTIterator` class that represents an iterator over the **<a href="https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)" target="_blank">in-order traversal</a>** of a binary search tree (BST):

<ul>
	<li>`BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.</li>
	<li>`boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.</li>
	<li>`int next()` Moves the pointer to the right, then returns the number at the pointer.</li>
</ul>

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.
