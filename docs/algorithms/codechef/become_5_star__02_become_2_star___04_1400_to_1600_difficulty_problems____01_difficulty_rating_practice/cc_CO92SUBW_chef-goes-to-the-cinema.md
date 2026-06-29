# Chef Goes to the Cinema

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CO92SUBW |
| Difficulty Rating | 1493 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CO92SUBW](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CO92SUBW) |

---

## Problem Statement

Chef lives in Chefcity. Chefcity can be represented as a straight line with Chef's house at point 0 on this line. There is an infinite number of subway stations in Chefcity, numbered by positive integers. The first station is located at point 1 and for each **i** ≥ 1, the distance between stations **i** and **i+1** is equal to **i+1**. (Station **i+1** is always located at a higher coordinate than station **i**, i.e., the subway stations are located at points 1, 3, 6, 10, 15 etc.)

Subway trains in Chefcity allow Chef to move between any pair of adjacent stations in one minute, regardless of the distance between them. Chef can also move by walking; his walking speed is one unit of distance in one minute. Chef can enter or exit the subway at any station.

Chef has decided to go to the cinema. The only cinema in Chefcity is located at point **X**. (Note that the cinema can be placed at the same point as a subway station.) Help Chef determine the minimum possible time required to get to the cinema from his house.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains a single integer **X**.

### Output

For each test case, print a single line containing one integer - the minimum possible travel time.

### Constraints

- 1 ≤ **T** ≤ 200

- 1 ≤ **X** ≤ 109

---

## Examples

**Example 1**

**Input**

```text
4
1
2
3
9
```

**Output**

```text
1
2
2
5
```

**Explanation**

**Example case 4:** Chef will walk from **x** = 0 to **x** = 1 in one minute, then he will enter the subway and move from station 1 (at **x** = 1) to station 2 (at **x** = 3) in one minute, then from station 2 to station 3 (at **x** = 6) in one minute, from station 3 to station 4 (at **x** = 10) in one minute, and finally, he will walk from **x** = 10 to **x** = 9 in one minute, which makes the total travel time 5 minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
9
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Author:** [Trung Nguyen](http://www.codechef.com/users/chemthan)

**Tester and Editorialist:** [Alei Reyes](http://www.codechef.com/users/alei)   ## Problem Link

[Practice](https://www.codechef.com/problems/CO92SUBW)

[Contest](https://www.codechef.com/COOK92A/problems/CO92SUBW)

## Difficulty

Easy

## PREREQUISITES:

Implementation

## Problem

There are some stations on the X-axis. The distance between the i-th and i+1-th station is i+1. It takes one second to move one unit of distance, also it takes one second to move from one station to the next. We want to go from point 0 to point X in the minimum time.

## Explanation

Let di denote the position of the i-th station. The distance between station i and i-1 is equal to i. Therefore di = di-1 + i.

If we apply the recurrence recursively we get that di is equal to the sum of integers from 1 to i. In closed form:  di = (i*(i+1))/2.

Numbers of the sequence 1 3 6 10 15 are called [triangular numbers](https://en.wikipedia.org/wiki/Triangular_number).

Note that triangular numbers increases quadratically. There are not many of them below 109, actually there are only 44720.

Chef wants to go to position X. So he can walk to station 1, then go by trains to the nearest station to X, and finally go walking the remaining distance.

Now the problem is to find the leftmost and rightmost station to the cinema, and check which one is more convenient. Is possible to binary search the answer, but since constraints are small, we can just iterate over all possible triangular numbers.

## Implementation

[Author’s Solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK92/Setter/CO92SUBW.cpp)

[Tester’s and Editorialist’s Solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK92/Tester/CO92SUBW.cpp)

</details>
