# Minions and Voting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINVOTE |
| Difficulty Rating | 1830 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MINVOTE](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MINVOTE) |

---

## Problem Statement

There are **N** minions who are competing in an election of the president of the ACM (Association of Cute Minions). They are standing in a line in the order from minion 1 to minion **N**. For each **i** (1 ≤ **i** ≤ **N**), the **i**-th minion has an influence level of **Si**.

A single minion may cast any number of votes. Minion **j** will vote for minion **i** (**i** ≠ **j**) if and only if the influence level of the **j**-th minion is greater than or equal to the sum of influence levels of all the minions standing between them (excluding the **i**-th and **j**-th minion).

Your task is to find the number of votes received by each minion.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N** denoting the number of minions.

- The second line contains **N** space-separated integers **S1, S2, ..., SN**.

### Output

For each test case, print a single line containing **N** space-separated integers. For each valid **i**, the **i**-th of these integers should denote the number of votes the **i**-th minion will get.

### Constraints

- 1 ≤ **T** ≤ 105

- 1 ≤ **N** ≤ 105

- 1 ≤ **Si** ≤ 109 for each valid **i**

- sum of **N** over all test cases won't exceed 106

### Subtasks

**Subtask #1 (30 points):**

- 1 ≤ **N** ≤ 500

- sum of **N** over all test cases won't exceed 10,000

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4
4 3 2 1
5
1 2 2 3 1
```

**Output**

```text
1 2 3 2
2 3 2 3 1
```

**Explanation**

**Example case 1:**

- The first minion will get only a vote of the second minion.

- The second minion will get votes of the first and third minion.

- The third minion will get votes of the first, second and fourth minion.

- The fourth minion will get votes of the second and third minion.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 3 2 1
```

**Output for this case**

```text
1 2 3 2
```



#### Test case 2

**Input for this case**

```text
5
1 2 2 3 1
```

**Output for this case**

```text
2 3 2 3 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Div1](http://www.codechef.com/MARCH18A/problems/MINVOTE), [Div2](http://www.codechef.com/MARCH18B/problems/MINVOTE)

[Practice](http://www.codechef.com/problems/MINVOTE)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Triveni Mahatha](http://www.codechef.com/users/triveni)

**Editorialist:** [Adarsh Kumar](http://www.codechef.com/users/adkroxx)

## DIFFICULTY:

Easy-Medium

## PREREQUISITES:

Binary search

## PROBLEM:

You are given an array A of N positive integers. For all i, you need to find number of such j (j \ne i) for which sum of number between (i,j) (both exclusive) is less than or equal to j^{th} element.

## EXPLANATION:

I will try to explain the most straight forward solution that is easy to think at first.

We will try to iterate over every minion j and try to find ranges of minion that will get voted by j^{th} minion. For i^{th} minion to get voted from j^{th} one following condition must be satisfied: A[j] \ge sum(i,j).

Let’s just solve for the case i>j. We can extend this one for the case  i < j  too using the similar argument. You can observe that right side of our condition is an increasing function while the left side is a constant. We can use binary search on i to find the break-point now. Now you just need to add 1 to the range (j+1,\text{last_valid_i}).

This problem reduces to offline range update and point query at every point. There are many possible ways of doing this. One of them uses DP with O(n) time complexity. I will describe that one in brief.

Say, you are given q updates (l_i,r_i), where in each update you need to add 1 to the range (l_i,r_i). Also, in the end you are required to report all the values of the array. A simple pseudocode for solving this task:

``# arrays are initialized with zeroes
A[0...(N+1)]  # Our oiginal array
for i=1...q:
  A[r_i]+=1
  A[l_i-1]-=1
for i=N...1:
  A[i]+=A[i+1] # A[i] now contains the final value at ith position
``

## ALTERNATE SOLUTION

Even a solution that will look like a brute force at first sight is sufficient. Let’s take a look at pseudocode:

``j = 1 to N:
  i = j+1 to N:
    if sum(i,j) > A[j]:
      break
    ans[i]+=1
  i = j-1 to 1:
    if sum(i,j) > A[j]:
      break
    ans[i]+=1
``

ans[i] in the above pseudocode stores number of votes received by each minion. Time complexity of the above solution is O(N.log(MAX)). Proof is left as an exercise to reader.

## Time Complexity:

O(N.logN)

## AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/MARCH18/Setter/MINVOTE.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/MARCH18/Tester/MINVOTE.cpp)

</details>
