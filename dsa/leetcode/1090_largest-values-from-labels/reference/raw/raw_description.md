## Description

You are given `n` item's value and label as two integer arrays `values` and `labels`. You are also given two integers `numWanted` and `useLimit`.

Your task is to find a subset of items with the **maximum sum** of their values such that:

	- The number of items is **at most** `numWanted`.

	- The number of items with the same label is **at most** `useLimit`.

Return the maximum sum.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The subset chosen is the first, third, and fifth items with the sum of values 5 + 3 + 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

The subset chosen is the first, second, and third items with the sum of values 5 + 4 + 3.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

The subset chosen is the first and fourth items with the sum of values 9 + 7.

</div>

**Constraints:**

	- `n == values.length == labels.length`

	- `1 <= n <= 2 * 10^4`

	- `0 <= values[i], labels[i] <= 2 * 10^4`

	- `1 <= numWanted, useLimit <= n`
