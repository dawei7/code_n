## Description

The Leetcode file system keeps a log each time some user performs a *change folder* operation.

The operations are described below:

<ul>
	<li>`"../"` : Move to the parent folder of the current folder. (If you are already in the main folder, **remain in the same folder**).</li>
	<li>`"./"` : Remain in the same folder.</li>
	<li>`"x/"` : Move to the child folder named `x` (This folder is **guaranteed to always exist**).</li>
</ul>

You are given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i^th` step.

The file system starts in the main folder, then the operations in `logs` are performed.

Return *the minimum number of operations needed to go back to the main folder after the change folder operations.*
