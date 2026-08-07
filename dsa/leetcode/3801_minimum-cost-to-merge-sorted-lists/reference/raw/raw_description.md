## Description

You are given a 2D integer array `lists`, where each `lists[i]` is a non-empty array of integers **sorted** in **non-decreasing** order.

You may **repeatedly** choose two lists `a = lists[i]` and `b = lists[j]`, where `i != j`, and merge them. The **cost** to merge `a` and `b` is:

`len(a) + len(b) + abs(median(a) - median(b))`, where `len` and `median` denote the list length and median, respectively.

After merging `a` and `b`, remove both `a` and `b` from `lists` and insert the new merged **sorted list** in **any** position. Repeat merges until only **one** list remains.

Return an integer denoting the **minimum total cost** required to merge all lists into one single sorted list.

The **median** of an array is the middle element after sorting it in non-decreasing order. If the array has an even number of elements, the median is the left middle element.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">lists = [[1,3,5],[2,4],[6,7,8]]</span>

**Output:** <span class="example-io">18</span>

**Explanation:**

Merge `a = [1, 3, 5]` and `b = [2, 4]`:

	- `len(a) = 3` and `len(b) = 2`

	- `median(a) = 3` and `median(b) = 2`

	- `cost = len(a) + len(b) + abs(median(a) - median(b)) = 3 + 2 + abs(3 - 2) = 6`

So `lists` becomes `[[1, 2, 3, 4, 5], [6, 7, 8]]`.

Merge `a = [1, 2, 3, 4, 5]` and `b = [6, 7, 8]`:

	- `len(a) = 5` and `len(b) = 3`

	- `median(a) = 3` and `median(b) = 7`

	- `cost = len(a) + len(b) + abs(median(a) - median(b)) = 5 + 3 + abs(3 - 7) = 12`

So `lists` becomes `[[1, 2, 3, 4, 5, 6, 7, 8]]`, and total cost is `6 + 12 = 18`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">lists = [[1,1,5],[1,4,7,8]]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

Merge `a = [1, 1, 5]` and `b = [1, 4, 7, 8]`:

	- `len(a) = 3` and `len(b) = 4`

	- `median(a) = 1` and `median(b) = 4`

	- `cost = len(a) + len(b) + abs(median(a) - median(b)) = 3 + 4 + abs(1 - 4) = 10`

So `lists` becomes `[[1, 1, 1, 4, 5, 7, 8]]`, and total cost is 10.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">lists = [[1],[3]]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Merge `a = [1]` and `b = [3]`:

	- `len(a) = 1` and `len(b) = 1`

	- `median(a) = 1` and `median(b) = 3`

	- `cost = len(a) + len(b) + abs(median(a) - median(b)) = 1 + 1 + abs(1 - 3) = 4`

So `lists` becomes `[[1, 3]]`, and total cost is 4.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">lists = [[1],[1]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The total cost is `len(a) + len(b) + abs(median(a) - median(b)) = 1 + 1 + abs(1 - 1) = 2`.

</div>

**Constraints:**

	- `2 <= lists.length <= 12`

	- `1 <= lists[i].length <= 500`

	- `-10^9 <= lists[i][j] <= 10^9`

	- `lists[i]` is sorted in non-decreasing order.

	- The **sum** of `lists[i].length` will not exceed 2000.
