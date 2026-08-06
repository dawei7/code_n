## Description

`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

Implement the `RandomizedCollection` class:

<ul>
	<li>`RandomizedCollection()` Initializes the empty `RandomizedCollection` object.</li>
	<li>`bool insert(int val)` Inserts an item `val` into the multiset, even if the item is already present. Returns `true` if the item is not present, `false` otherwise.</li>
	<li>`bool remove(int val)` Removes an item `val` from the multiset if present. Returns `true` if the item is present, `false` otherwise. Note that if `val` has multiple occurrences in the multiset, we only remove one of them.</li>
	<li>`int getRandom()` Returns a random element from the current multiset of elements. The probability of each element being returned is **linearly related** to the number of the same values the multiset contains.</li>
</ul>

You must implement the functions of the class such that each function works on **average** `O(1)` time complexity.

**Note:** The test cases are generated such that `getRandom` will only be called if there is **at least one** item in the `RandomizedCollection`.
