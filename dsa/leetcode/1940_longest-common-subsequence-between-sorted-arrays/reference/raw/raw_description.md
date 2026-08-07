## Description

Given an array of integer arrays `arrays` where each `arrays[i]` is sorted in **strictly increasing** order, return *an integer array representing the **longest common subsequence** among **all** the arrays*.

A **subsequence** is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.

**Example 1:**

```
**Input:** arrays = [[<u>1</u>,3,<u>4</u>],
                 [<u>1</u>,<u>4</u>,7,9]]
**Output:** [1,4]
**Explanation:** The longest common subsequence in the two arrays is [1,4].
```

**Example 2:**

```
**Input:** arrays = [[<u>2</u>,<u>3</u>,<u>6</u>,8],
                 [1,<u>2</u>,<u>3</u>,5,<u>6</u>,7,10],
                 [<u>2</u>,<u>3</u>,4,<u>6</u>,9]]
**Output:** [2,3,6]
**Explanation:** The longest common subsequence in all three arrays is [2,3,6].
```

**Example 3:**

```
**Input:** arrays = [[1,2,3,4,5],
                 [6,7,8]]
**Output:** []
**Explanation:** There is no common subsequence between the two arrays.
```

**Constraints:**

	- `2 <= arrays.length <= 100`

	- `1 <= arrays[i].length <= 100`

	- `1 <= arrays[i][j] <= 100`

	- `arrays[i]` is sorted in **strictly increasing** order.
