# Rectangle

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECTANGL |
| Difficulty Rating | 1146 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [RECTANGL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/RECTANGL) |

---

## Problem Statement

You are given four integers **a**, **b**, **c** and **d**. Determine if there's a rectangle such that the lengths of its sides are **a**, **b**, **c** and **d** (in any order).

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains four space-separated integers **a**, **b**, **c** and **d**.

### Output

For each test case, print a single line containing one string "YES" or "NO".

### Constraints

- 1 ≤ **T** ≤ 1,000

- 1 ≤ **a**, **b**, **c**, **d** ≤ 10,000

### Subtasks

**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1 1 2 2
3 2 2 3
1 2 2 2
```

**Output**

```text
YES
YES
NO
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 2 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 2 2 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
1 2 2 2
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/RECTANGL)

[Contest](http://www.codechef.com/JAN18/problems/RECTANGL)

**Author:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

**Tester:** [Alexey Zayakin](http://www.codechef.com/users/alex_2oo8)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Common sense

### PROBLEM:

You’re given four numbers a, b, c, d. You have to determine if you can make a rectangle of such lengthes.

### QUICK EXPLANATION

Do what the problem asks you to do.

### EXPLANATION:

In other words you have to check if two smallest and two largest numbers among this four are same. To do this you can sort all four numbers in whatever way you like and check that first two and last two numbers are both same. Example of solution:

``int a[4];
cin >> a[0] >> a[1] >> a[2] >> a[3];
sort(a, a + 4);
cout << (a[0] == a[1] && a[2] == a[3] ? "YES" : "NO") << "\n";
``

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Setter/RECTANGL.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Tester/RECTANGL.cpp).

### RELATED PROBLEMS:

</details>
