## Description

You are given an integer array `nums`.

Your task is to find the number of pairs of **non-empty** <span data-keyword="subsequence-array">subsequences</span> `(seq1, seq2)` of `nums` that satisfy the following conditions:

	- The subsequences `seq1` and `seq2` are **disjoint**, meaning **no index** of `nums` is common between them.

	- The <span data-keyword="gcd-function">GCD</span> of the elements of `seq1` is equal to the GCD of the elements of `seq2`.

Return the total number of such pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

The subsequence pairs which have the GCD of their elements equal to 1 are:

	- `([**<u>1</u>**, 2, 3, 4], [1, **<u>2</u>**, **<u>3</u>**, 4])`

	- `([**<u>1</u>**, 2, 3, 4], [1, **<u>2</u>**, **<u>3</u>**, **<u>4</u>**])`

	- `([**<u>1</u>**, 2, 3, 4], [1, 2, **<u>3</u>**, **<u>4</u>**])`

	- `([**<u>1</u>**, **<u>2</u>**, 3, 4], [1, 2, **<u>3</u>**, **<u>4</u>**])`

	- `([**<u>1</u>**, 2, 3, **<u>4</u>**], [1, **<u>2</u>**, **<u>3</u>**, 4])`

	- `([1, **<u>2</u>**, **<u>3</u>**, 4], [**<u>1</u>**, 2, 3, 4])`

	- `([1, **<u>2</u>**, **<u>3</u>**, 4], [**<u>1</u>**, 2, 3, **<u>4</u>**])`

	- `([1, **<u>2</u>**, **<u>3</u>**, **<u>4</u>**], [**<u>1</u>**, 2, 3, 4])`

	- `([1, 2, **<u>3</u>**, **<u>4</u>**], [**<u>1</u>**, 2, 3, 4])`

	- `([1, 2, **<u>3</u>**, **<u>4</u>**], [**<u>1</u>**, **<u>2</u>**, 3, 4])`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,20,30]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The subsequence pairs which have the GCD of their elements equal to 10 are:

	- `([**<u>10</u>**, 20, 30], [10, **<u>20</u>**, **<u>30</u>**])`

	- `([10, **<u>20</u>**, **<u>30</u>**], [**<u>10</u>**, 20, 30])`

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1]</span>

**Output:** <span class="example-io">50</span>

</div>

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 200`
