# Reversal Sorting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REVSORT |
| Difficulty Rating | 1288 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [REVSORT](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/REVSORT) |

---

## Problem Statement

Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays in increasing order by reversing some of his subarrays.

To make it more challenging for himself, Chef decides that he can reverse only those subarrays that have sum of its elements **at most** $X$. Soon he notices that it might not be always possible to sort the array with this condition.

Can you help the Chef by telling him if the given array can be sorted by reversing subarrays with sum at most $X$.

More formally, for a given array $A$ and an integer $X$, check whether the array can be sorted in increasing order by reversing some (possibly none) of the subarrays such that the sum of all elements of the subarray is **at most** $X$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains of two space-separated integers $N$ and $X$ denoting the length of the array and the maximum sum of subarrays that you can reverse.
- The second line contains $N$ space-separated integers $A_1, A_2,..., A_N$ representing the initial array.

---

## Output Format

For each test case, output $\texttt{YES}$ if Chef can sort the array using a finite number of operations, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 5\cdot 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 2\cdot 10^9$
- $1 \leq X \leq 2\cdot 10^9$
- Sum of $N$ over all test cases does not exceeds $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4 1
1 2 3 4
4 1
2 1 3 4
5 7
3 2 2 3 3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The array is already sorted so we need not make any operations.

**Test case $2$:** There is no subarray with sum less than or equal to $1$ so we cannot sort the array.

**Test case $3$:** We can reverse the subarray $A[1, 3]$ which has a sum of $3+2+2=7$. Thus, the reversed subarray is $[2, 2, 3]$. The resulting array is $[2, 2, 3, 3, 3]$. The array is sorted in $1$ operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1
1 2 3 4
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 1
2 1 3 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5 7
3 2 2 3 3
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE222A/problems/REVSORT)

[Contest Division 2](https://www.codechef.com/JUNE222B/problems/REVSORT)

[Contest Division 3](https://www.codechef.com/JUNE222C/problems/REVSORT)

[Contest Division 4](https://www.codechef.com/JUNE222D/problems/REVSORT)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1288

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays in increasing order by reversing some of his subarrays.

To make it more challenging for himself, Chef decides that he can reverse only those subarrays that have sum of its elements **at most** X. Soon he notices that it might not be always possible to sort the array with this condition.

Can you help the Chef by telling him if the given array can be sorted by reversing subarrays with sum at most X.

More formally, for a given array A and an integer X, check whether the array can be sorted in increasing order by reversing some (possibly none) of the subarrays such that the sum of all elements of the subarray is **at most** X.

#
[](#explanation-5)EXPLANATION:

In order to solve this problem we will iterate from right to left and sort array accordingly. Now while doing so say we reach an index i, then there can be two cases :

-
A_i \leq min(A_{i+1},A_{i+2}....A_n): Nothing needed to be done since array A[i,i+1....n] would already be sorted.

- Otherwise we will find position j, such that A_j is the largest element in A[i+1...n] , which is less than A_i. Now eventually we would need to swap A_i and A_j and if their sum is greater than x, then it won’t be possible to perform this swap and hence sort the array. All other swaps would involve elements less than A_j(since it is a sorted array) so if swap of A_i and A_j is possible so all other swaps would also be possible.

We can use a set here to store the sorted array.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(NlogN), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/Jfg-)

[Setter’s Solution](http://p.ip.fi/kzy0)

[Tester1’s Solution](http://p.ip.fi/pzXg)

[Tester2’s Solution](http://p.ip.fi/8lp3)

</details>
