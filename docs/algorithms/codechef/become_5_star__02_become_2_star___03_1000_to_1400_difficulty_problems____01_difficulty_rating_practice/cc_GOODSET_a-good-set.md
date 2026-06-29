# A Good Set

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GOODSET |
| Difficulty Rating | 1231 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [GOODSET](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/GOODSET) |

---

## Problem Statement

A set of integers is called *good* if there does not exist three distinct elements a, b, c in it such that a + b = c.

Your task is simple. Just output any *good* set of **n** integers. All the elements in this set should be distinct and should lie between 1 and 500, both inclusive.

### Input

- The first line of the input contains an integer **T** denoting number of test cases. The descriptions of **T** test cases follow.

- The only line of each test case contains an integer **n**, denoting the size of the needed *good* set.

### Output

For each test case, output a single line containing **n** integers denoting the elements of the *good* set, in any order. There can be more than one possible good set, and you can output any one of them.

### Constraints

- 1 ≤ **T, n** ≤ 100

### Subtasks

- **Subtask #1 (50 points)**: 1 ≤ **T, n** ≤ 10

- **Subtask #2 (50 points)**: original constraints

---

## Examples

**Example 1**

**Input**

```text
5
1
2
3
4
5
```

**Output**

```text
7
1 2
1 2 4
1 2 4 16
3 2 15 6 10
```

**Explanation**

**Example 1 and 2.** Any set of size less than or equal to 2 is good by definition.

**Example 3 onwards.** For each pair of elements in the set, you can see that their sum doesn't exist in the set.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1 2
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
1 2 4
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
1 2 4 16
```



#### Test case 5

**Input for this case**

```text
5
```

**Output for this case**

```text
3 2 15 6 10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/GOODSET)

[Contest](http://www.codechef.com/JUNE17/problems/GOODSET)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Prateek Gupta](http://www.codechef.com/users/prateekg603)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

Output any set of distinct integers from 1 to 500 such that there are no three elements s_1+s_2=s_3.

### EXPLANATION:

Since n is up to 100, one can just output integers from 500-n to 499. Sum of any two such integers is greater than 500 so requirements will be satisfied.

One other solution is to output the first n odd integers, i.e. 1, 3, 5, 7 and so on. Sum of any two odd numbers is even, which won’t be present in this set.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be updated soon.

Tester’s solution will be updated soon.

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/14243065).

</details>
