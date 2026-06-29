# Train Partner

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANKTRAIN |
| Difficulty Rating | 1187 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ANKTRAIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ANKTRAIN) |

---

## Problem Statement

Rahul and Rashi are off to the wedding of a close relative. This time they have to travel without their guardians. Rahul got very interested in the arrangement of seats inside the train coach.

The entire coach could be viewed as an arrangement of consecutive blocks of size 8.

``
Berth Number   	Compartment

 1 -  8               1
 9 - 16               2
17 - 24               3
... and so on
``

Each of these size-8 blocks are further arranged as:

``
 1LB,  2MB,  3UB,  4LB,  5MB,  6UB,  7SL,  8SU
 9LB, 10MB, ...
 ...
 ...
``

Here `LB` denotes lower berth, `MB` middle berth and `UB` upper berth.

The following berths are called **Train-Partners**:

``
3UB   |  6UB
2MB   |  5MB
1LB   |  4LB
7SL   |  8SU
``

and the pattern is repeated for every set of 8 berths.

Rahul and Rashi are playing this game of finding the train partner of each berth. Can you write a program to do the same?

### Input

The first line of input contains a single integer **T**, denoting the number of test cases to follow.

Each of the next **T** lines contain a single integer **N**, the berth number whose neighbor is to be found out.

### Output

The output should contain exactly **T** lines each containing the berth of the neighbor of the corresponding seat.

### Constraints

### Subtasks

**Subtask #1 (50 points):**

- **1** ≤ **T** ≤ **8**

- **1** ≤ **N** ≤ **8**

**Subtask #2 (50 points):**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **500**

---

## Examples

**Example 1**

**Input**

```text
3
1
5
3
```

**Output**

```text
4LB
2MB
6UB
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
4LB
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
2MB
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
6UB
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ANKTRAIN)

[Contest](https://www.codechef.com/DEC16/problems/ANKTRAIN)

**Author:** [Ankit Srivastava](https://www.codechef.com/users/code_master01)

**Tester:** [Kevin Charles Atienza](https://www.codechef.com/users/kevinsogo)

**Editorialist:** [Vaibhav Tulsyan](https://www.codechef.com/users/wittyceaser)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

Given a pattern of arrangement of berths in a train, find the *train partner* of a given berth number. The pattern repeats for every 8 berths.

### QUICK EXPLANATION:

Maintain a map that stores neighbouring berth of the first 8 berths. For a given berth number N, find it’s neighbour M that lies in the *same compartment*, say C.

In order to do this, find the berth equivalent to N in the 1^{st} compartment and it’s neighbour M'. Add appropriate offset to find equivalent

berth of M' in the compartment C. The berth number of the number is: N - N \% 8 + M'.

### EXPLANATION:

**Subtask 1:**

The approach used for this subtask will be extended and used for subtask 2.

From the constraints of Subtask 1, we know that 1 \le N \le 8. This means that we are dealing with only 1 compartment.

Let’s store the neighbours of each berth - this can be hard-coded in the program, as there are only 8 berths.

``
neighbours = {
    0 -> "4LB",
    1 -> "5MB",
    2 -> "6UB",
    3 -> "1LB",
    4 -> "2MB",
    5 -> "3UB",
    6 -> "8SU",
    7 -> "7SL"
}

``

For a given value of N, we just need to fetch the value from the neighbours table for (N - 1) since our table has 0-indexed keys.

This can be implemented using a list/array/hashmap.

**Subtask 2:**

Note that the pattern repeats after every 8 berths - hence, group of berths [9…16] is identical to group [1…8],

and [17…24] is also identical to [1…8].

Thus, all we have to do is find the equivalent neighbour (M') of N in the 1^{st} compartment and add an offset to this neighbour.

Let’s say N was present in compartment C. The *first berth* of that compartment would have the number N - (N \% 8).

Hence, the berth number of the neighbour would be: (N - (N \% 8) + M').

Note: Since we’re working with integers under a given Modulo, we are using 0-indexing for our neighbours map for simplicity.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/problems/ANKTRAIN).

Tester’s solution can be found [here](https://www.codechef.com/problems/ANKTRAIN).

Editorialist’s solution can be found [here](https://www.codechef.com/problems/ANKTRAIN).

</details>
