# Mix the Colors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MIXCOLOR |
| Difficulty Rating | 1419 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [MIXCOLOR](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/MIXCOLOR) |

---

## Problem Statement

Chef likes to mix colors a lot. Recently, she was gifted **N** colors **A1, A2, ..., AN** by her friend.

Chef wants to make the values of all her colors pairwise distinct, as they will then look stunningly *beautiful*. In order to achieve that, she can perform the following mixing operation zero or more times:

- Choose any two colors. Let's denote their values by **x** and **y**.

- Mix the color with value **x** into the color with value **y**. After the mixing, the value of the first color remains **x**, but the value of the second color changes to **x + y**.

Find the minimum number of mixing operations Chef needs to perform to make her colors beautiful.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N** denoting the number of colors.

- The second line contains **N** space-separated integers **A1, A2, ..., AN** denoting Chef's initial colors.

### Output

For each test case, print a single line containing one integer — the minimum number of required mixing operations.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **Ai** ≤ 109 for each valid **i**

### Subtasks

**Subtask #1 (30 points):** 1 ≤ **N** ≤ 100

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2 3
3
2 1 2
```

**Output**

```text
0
1
```

**Explanation**

**Example case 1:** No two colors have the same value. Hence, they are already beautiful. No mixing is required.

**Example case 2:** Take the second color (with value **x** = 1) and mix it into the first color (with value **x** = 2). After the mixing, the colors will be 3 1 2. Now the colors are beautiful. This is the minimum number of mixing operations that are required. Hence, the answer is 1.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
2 1 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Div1](http://www.codechef.com/MARCH18A/problems/MIXCOLOR), [Div2](http://www.codechef.com/MARCH18B/problems/MIXCOLOR)

[Practice](http://www.codechef.com/problems/MIXCOLOR)

**Author:** [Shivangi Gupta](http://www.codechef.com/users/shivangi_gupta)

**Tester:** [Triveni Mahatha](http://www.codechef.com/users/triveni)

**Editorialist:** [Adarsh Kumar](http://www.codechef.com/users/adkroxx)

## DIFFICULTY:

Easy

## PREREQUISITES:

Sorting

## PROBLEM:

You are given an array with N elements. In one operation you can replace A[i] by A[i]+A[j] where j \neq i. Find minimum number of operations required to make each element of array pairwise distinct.

## EXPLANATION:

Lets keep a track on the current maximum of the array. If we add maximum to any element already present in the array, it will give us a new maximum as well as new element that was not present in the array before. We can do this process for all the elements that are repeating. Hence total no. of operation required = N - (total unique elements already present in the array). You can prove this using contradiction if you want to.

Main problem here reduces to finding total number of unique elements present in the array. This task can be solved using sorting and linear traversal of the array.

## Time Complexity:

O(N.logN)

## AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/MARCH18/Setter/MIXCOLOR.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/MARCH18/Tester/MIXCOLOR.cpp)

</details>
