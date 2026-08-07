## Description

You are given the `head` of a linked list of **even** length containing integers.

Each **odd-indexed** node contains an odd integer and each **even-indexed** node contains an even integer.

We call each even-indexed node and its next node a **pair**, e.g., the nodes with indices `0` and `1` are a pair, the nodes with indices `2` and `3` are a pair, and so on.

For every **pair**, we compare the values of the nodes in the pair:

	- If the odd-indexed node is higher, the `"Odd"` team gets a point.

	- If the even-indexed node is higher, the `"Even"` team gets a point.

Return *the name of the team with the **higher** points, if the points are equal, return* `"Tie"`.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [2,1] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> "Even" </span>

**Explanation: ** There is only one pair in this linked list and that is `(2,1)`. Since `2 > 1`, the Even team gets the point.

Hence, the answer would be `"Even"`.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [2,5,4,7,20,5] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> "Odd" </span>

**Explanation: ** There are `3` pairs in this linked list. Let's investigate each pair individually:

`(2,5)` -> Since `2 < 5`, The Odd team gets the point.

`(4,7)` -> Since `4 < 7`, The Odd team gets the point.

`(20,5)` -> Since `20 > 5`, The Even team gets the point.

The Odd team earned `2` points while the Even team got `1` point and the Odd team has the higher points.

Hence, the answer would be `"Odd"`.

</div>

**Example 3: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [4,5,2,1] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> "Tie" </span>

**Explanation: ** There are `2` pairs in this linked list. Let's investigate each pair individually:

`(4,5)` -> Since `4 < 5`, the Odd team gets the point.

`(2,1)` -> Since `2 > 1`, the Even team gets the point.

Both teams earned `1` point.

Hence, the answer would be `"Tie"`.

</div>

**Constraints:**

	- The number of nodes in the list is in the range `[2, 100]`.

	- The number of nodes in the list is even.

	- `1 <= Node.val <= 100`

	- The value of each odd-indexed node is odd.

	- The value of each even-indexed node is even.
