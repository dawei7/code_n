## Description

Given an integer array `arr` and a filtering function `fn`, return a filtered array `filteredArr`.

The `fn` function takes one or two arguments:

<ul>
	<li>`arr[i]` - number from the `arr`</li>
	<li>`i` - index of `arr[i]`</li>
</ul>

`filteredArr` should only contain the elements from the `arr` for which the expression `fn(arr[i], i)` evaluates to a **truthy** value. A **truthy** value is a value where `Boolean(value)` returns `true`.

Please solve it without the built-in `Array.filter` method.
