# Mean Mean Medians

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEANMEDI |
| Difficulty Rating | 2719 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [MEANMEDI](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/MEANMEDI) |

---

## Problem Statement

"Medians can't be very mean!", retorted Chef's brother. One would wish Chef's ego wouldn't
	come in the way, but Chef has taken up the challenge to prove otherwise. He asks for your help. Given N numbers, select
	K out of them, such that, the absolute difference between the mean and the median of the selected numbers, is as low
	as possible.

Mean of K numbers is defined as the sum of the numbers divided by K.

Median of K numbers is defined as the number that appears at the order index, floor((K+1)/2);
	that is, the I'th element in the sorted order of the K numbers (where numbering starts from 1),
	where I = floor((K+1)/2). Note that, if K is even, the median would be the smaller value among the two values that
	lie in the center.

Input format

The first line contains the number T, the number of test cases. In the following lines,
	T test cases follow (without any newlines between them.)
Each case consists of only 2 lines.
The first line of each test case contains N and K, separated by a single space.
The second line contains N positive integers, separated by a single space.

Output format

For each test case, print the minimum absolute difference between the mean and the median
	that you can get, by selecting any K numbers, from the N numbers. Output the result rounded to 3 digits of precision
	after the decimal.

Constraints

1 ≤ T ≤ 20

1 ≤ N ≤ 60

1 ≤ K ≤ N

1 ≤ numbers ≤ 1200

Sample input

`2
8 2
4 9 1 3 5 9 4 10
5 4
10 7 4 5 9

`

Sample output

`0.000
0.500

`

Explanation

In the first case, you can select [4, 4].

In the second case, you can select [10, 7, 4, 9]. The mean would be 7.500, where as
	median would be 7.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MEANMEDI/)

[Contest](http://www.codechef.com/COOK12/problems/MEANMEDI/)

### DIFFICULTY

MEDIUM

### EXPLANATION

The time limits for this problem would seem very misguided in retrospect.

The expected complexity for the solution was O(N * S), where S was the largest sum that would be considered in the knapsack as described below.

First, needless to say, sort the numbers.

Now, iterate over each number, assuming it to be the Median, let this position be i. This forces us to select (K-1)/2 numbers towards the left of the median, and K/2 numbers towards the right of the median.

Perform a knapsack and pre-calculate the sums possible by selecting (K-1)/2 numbers in each segment from the beginning to any point within the array.

Perform a knapsack and pre-calculate the sums possible by selecting K/2 numbers in each segment from the end to any point within the array.

The optimization here, is on the fact that K/2 can be 30 at the most. So knapsack could be optimized to take only O(N * S) time, rather than O(N * K * S). This can be done by storing for each sum s the bit-mask of those values j for which s is representable as the sum of j numbers from the first i numbers of the array.

Now, we can treat the sums from the left and right of the median separately.

We can select each sum from the left, and a corresponding sum from the right; to find the sum, with which the mean is closest to the selected median. This determination step will be O(S) in complexity.

When a larger sum is selected on the left, we obviously select a smaller sum from the right. We can avoid doubles here by considering median * (K-1) and selecting the two sums, such that, their sum is closest to median * (K-1).

Most contestants were optimizing their O(N * K * S) solution. The test cases were such that such solutions were bound to fail the time limit. The time limits should not have been (but unfortunately were) tight for solutions with complexity O(N * S).

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK12/Setter/MEANMEDI.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK12/Tester/MEANMEDI.cpp).

</details>
