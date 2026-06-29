# Maximum Weight Difference

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXDIFF |
| Difficulty Rating | 1308 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [MAXDIFF](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/MAXDIFF) |

---

## Problem Statement

Chef has gone shopping with his 5-year old son. They have bought **N** items so far. The items are numbered from **1** to **N**, and the item **i** weighs **Wi** grams.

Chef's son insists on helping his father in carrying the items. He wants his dad to give him a few items. Chef does not want to burden his son. But he won't stop bothering him unless he is given a few items to carry. So Chef decides to give him some items. Obviously, Chef wants to give the kid less weight to carry.

However, his son is a smart kid. To avoid being given the bare minimum weight to carry, he suggests that the items are split into two groups, and one group contains exactly **K** items. Then Chef will carry the heavier group, and his son will carry the other group.

Help the Chef in deciding which items should the son take. Your task will be simple. Tell the Chef the maximum possible difference between the weight carried by him and the weight carried by the kid.

### Input:

The first line of input contains an integer **T**, denoting the number of test cases. Then **T** test cases follow. The first line of each test contains two space-separated integers **N** and **K**. The next line contains **N** space-separated integers **W1**, **W2**, ..., **WN**.

### Output:

For each test case, output the maximum possible difference between the weights carried by both in grams.

### Constraints:

- **1 ≤ T ≤ 100**

- **1 ≤ K < N ≤ 100**

- **1 ≤ Wi ≤ 100000 (105)**

---

## Examples

**Example 1**

**Input**

```text
2
5 2
8 4 5 2 10
8 3
1 1 1 1 1 1 1 1
```

**Output**

```text
17
2
```

**Explanation**

**Case #1:** The optimal way is that Chef gives his son **K=2** items with weights **2** and **4**. Chef carries the rest of the items himself. Thus the difference is: **(8+5+10) - (4+2) = 23 - 6 = 17**.

**Case #2:** Chef gives his son **3** items and he carries **5** items himself.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
8 4 5 2 10
```

**Output for this case**

```text
17
```



#### Test case 2

**Input for this case**

```text
8 3
1 1 1 1 1 1 1 1
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/MAXDIFF)

[Contest](http://www.codechef.com/APRIL13/problems/MAXDIFF)

**Author:** [Vamsi Kavala](http://www.codechef.com/users/vamsi_kavala)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Anton Lunyov](http://www.codechef.com/users/anton_lunyov)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

[Greedy algorithm](http://en.wikipedia.org/wiki/Greedy_algorithm), [Sorting algorithms](http://en.wikipedia.org/wiki/Sorting_algorithm)

### PROBLEM:

You are given an array **W[1], W[2], …, W[N]**. Choose **K** numbers among them such that the absolute difference between the sum of chosen numbers and the sum of remaining numbers is as large as possible.

### QUICK EXPLANATION:

There are two possibilities to try - **K** largest numbers and **K** smallest numbers (see below why). So the solution could be like this:

- Sort all numbers.

- Find the sum of all numbers. Let it be **S**.

- Find the sum of first **K** numbers. Let it be **S1**.

- Find the sum of last **K** numbers. Let it be **S2**.

- Output **max(abs(S1 ? (S ? S1)),  abs(S2 ? (S ? S2)))** as an answer.

### EXPLANATION:

Consider the following sub-problem: choose **K** numbers with largest possible sum. Then the solution obviously is **K** largest numbers. So that here greedy algorithm works - at each step we choose the largest possible number until we get all **K** numbers.

In our problem we should divide the set of **N** numbers into two groups of **K** and **N ? K** numbers respectively. Consider two cases:

-

*The group with largest sum, among these two groups, is group of **K** numbers.* Then we want to maximize the sum in it, since the sum in the second group will only decrease if the sum in the first group will increase. So we are now in sub-problem considered above and should choose **K** largest numbers.

-

*The group with largest sum, among these two groups, is group of **N ? K** numbers.* Similarly to the previous case we then have to choose **N ? K** largest numbers among all numbers.

This reasoning justify the solution in the **QUICK EXPLANATION**.

Regarding implementation details. Since **N** and **T** are small, then every simple **O(N2)** sorting algorithm from [here](http://en.wikipedia.org/wiki/Sorting_algorithm) will work. Other steps of the solution seems trivial to implement.

### ALTERNATIVE SOLUTION:

Let’s go further and ask our self which of two above cases actually gives the answer. After short thinking it became clear that larger difference would be when more numbers are included to the group of largest numbers. Hence we could set **M = max(K, N ? K)**, find the sum of **M** largest numbers (let it be **S1**) and then the answer is **S1 ? (S ? S1)**, where **S** is the sum of all numbers.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be provided soon.

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/April/Tester/MAXDIFF.cpp).

### RELATED PROBLEMS:

Will be provided soon. All readers are welcomed to provide related problems in comments.

</details>
