## Description

Given the `head` of a linked list containing `k` **distinct** elements, return *the head to a linked list of length *`k`* containing the <span data-keyword="frequency-linkedlist">frequency</span> of each **distinct** element in the given linked list in **any order**.*

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,1,2,3] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [3,2,1] </span>

**Explanation: ** There are `3` distinct elements in the list. The frequency of `1` is `3`, the frequency of `2` is `2` and the frequency of `3` is `1`. Hence, we return `3 -> 2 -> 1`.

Note that `1 -> 2 -> 3`, `1 -> 3 -> 2`, `2 -> 1 -> 3`, `2 -> 3 -> 1`, and `3 -> 1 -> 2` are also valid answers.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [1,1,2,2,2] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [2,3] </span>

**Explanation: ** There are `2` distinct elements in the list. The frequency of `1` is `2` and the frequency of `2` is `3`. Hence, we return `2 -> 3`.

</div>

**Example 3: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> head = [6,5,4,3,2,1] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> [1,1,1,1,1,1] </span>

**Explanation: ** There are `6` distinct elements in the list. The frequency of each of them is `1`. Hence, we return `1 -> 1 -> 1 -> 1 -> 1 -> 1`.

</div>

**Constraints:**

	- The number of nodes in the list is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^5`
