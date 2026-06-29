# Fence - INOI 2017

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TINOI17A |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [TINOI17A](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/TINOI17A) |

---

## Problem Statement

### INOI 2017, Problem 1, Fence

 You have a rectangular farm which consists of **R*C** fields arranged in a grid
consisting of **R** rows and **C** columns. Each field is a **1 x 1** square.
Some of these fields have been planted with potatoes while the others lie
uncultivated. We say that two fields are adjacent if one lies immediately to the left
or to the right or above or below the other. (Note that two fields which touch each other at just one corner are not considered adjacent). If two fields are adjacent
then we say we may walk from one to the other. A **patch** is a collection
of all the cultivated fields such that one may walk from any field in the patch to any other field in the same patch only
via cultivated fields. There are no uncultivated fields in a patch. That is, all the cultivated fields in the farm can be partitioned into patches, and you can walk from one cultivated field to another cultivated field, if and only if, both of them belong to the same patch.

To prevent wild animals from destroying the cultivated fields you plan to
enclose each patch within fences constructed all along the boundaries of the patch. Wild animals infest the uncultivated fields, and also beyond the **R*C** farm. We need to ensure that the fences protect all the boundaries of each patch, so that the wild animals cannot get to any cultivated field without crossing a fence.

Clearly, the length of the fence needed for each patch may differ.
If your patch consists of just a single field then the fence will be
of length 4. If it consists of two adjacent fields then the fence
will be length 6.

Your task is to output the maximum length of fence needed to enclose a patch, among all the patches in your farm.
The input to your program will be a description of the positions of all the
cultivated fields in your farm.

**(X,Y)** refers to the field on the **Xth** row and **Yth** column. So, **(1,1)** refers to the top-left corner field, and **(R,C)** refers to the bottom-right corner.

### Input

- The first line contains three space separated integers, **R, C** and **N**, which are the number of rows, number of columns and the number of cultivated fields, respectively.

- The next **N** lines contain two space separated integers, **Xi** and **Yi**, which signify that **(Xi, Yi)** is a cultivated field.

### Output

- A single integer which is the maximum length of fence needed for any patch.

### Constraints

For all test cases you may assume that:

-
**0 ≤ Number of cultivated fields = N ≤ 100000**

- **1 ≤ Xi ≤ R**

- **1 ≤ Yi ≤ C**

**Subtask 1**: For 15% of the score,

-
**1 ≤ R,C ≤ 20**

**Subtask 2**: For further 45% of the score,

-
**1 ≤ R,C ≤ 2500**

**Subtask 3**: For 40% of the score,

-
**1 ≤ R,C ≤ 1000000**

### Example
`**Input:**

**Output:**

`

### Explanation

---

## Examples

**Example 1**

**Input**

```text
4 4 9
1 4
2 1
2 2
2 3
4 3
4 1
4 2
3 1
3 3
```

**Output**

```text
16
```

**Explanation**

The input corresponds to the figure

`
		. . . x
		x x x .
		x . x .
		x x x .
`

'x' corresponds to a cultivated field, and '.' corresponds to an uncultivated field.

There are two patches. One patch, which includes only the (1,4) field needs a fence of length 4. The other patch, which has 8 fields in it, needs fence of length 16. A length of 12 to cover its outer boundary, and length 4 to cover its inner boundary.

Maximum(4,16) = 16. Hence, the answer is 16.

Note:

You may download the problem statements PDF and test cases zipped files here: http://pd.codechef.com/com/inoi/problems.zip. Please feel free to use them during the contest.

Password for the PDF and test cases zip files: DPtrumpsGreedy2017

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Fence - INOI 2017](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/TINOI17A)

### [](#problem-statement-1)Problem Statement -

 You have a rectangular farm which consists of **R*C** fields arranged in a grid
consisting of **R** rows and **C** columns. Each field is a **1 x 1** square.
Some of these fields have been planted with potatoes while the others lie
uncultivated. We say that two fields are adjacent if one lies immediately to the left
or to the right or above or below the other. (Note that two fields which touch each other at just one corner are not considered adjacent). If two fields are adjacent
then we say we may walk from one to the other. A **patch** is a collection
of all the cultivated fields such that one may walk from any field in the patch to any other field in the same patch only
via cultivated fields. There are no uncultivated fields in a patch. That is, all the cultivated fields in the farm can be partitioned into patches, and you can walk from one cultivated field to another cultivated field, if and only if, both of them belong to the same patch.

To prevent wild animals from destroying the cultivated fields you plan to
enclose each patch within fences constructed all along the boundaries of the patch. Wild animals infest the uncultivated fields, and also beyond the **R*C** farm. We need to ensure that the fences protect all the boundaries of each patch, so that the wild animals cannot get to any cultivated field without crossing a fence.

Clearly, the length of the fence needed for each patch may differ.
If your patch consists of just a single field then the fence will be
of length 4. If it consists of two adjacent fields then the fence
will be length 6.

Your task is to output the maximum length of fence needed to enclose a patch, among all the patches in your farm.
The input to your program will be a description of the positions of all the
cultivated fields in your farm.

**(X,Y)** refers to the field on the **Xth** row and **Yth** column. So, **(1,1)** refers to the top-left corner field, and **(R,C)** refers to the bottom-right corner.

### [](#approach-2)Approach -

The solution uses Breadth-First Search `(BFS)` to explore each patch of cultivated fields and determine the required fence length for that patch. The `BFS` begins from each unvisited cultivated field and explores all connected cultivated fields in its patch by marking each as visited. Each field in a patch starts with a fence requirement of 4 units, representing its four sides. For each cultivated neighbor, one side of the fence is shared, so the required fence length is reduced by 1 for each adjacent cultivated field. If a neighbor is cultivated and unvisited, it is added to the queue for further exploration. The BFS completes once all connected fields in the patch are visited, yielding the total fence length for that patch. By tracking the maximum fence length across all patches, we can find the maximum required fence length among all patches.

### [](#time-complexity-3)Time Complexity -

O(n), where n is the number of cultivated fields.

### [](#space-complexity-4)Space Complexity -

O(n), for storing cultivated field coordinates and the BFS queue.

</details>
