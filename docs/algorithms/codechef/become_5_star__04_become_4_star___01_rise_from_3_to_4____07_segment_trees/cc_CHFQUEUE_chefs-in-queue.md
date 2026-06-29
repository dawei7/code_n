# Chefs in Queue

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFQUEUE |
| Difficulty Rating | 2146 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [CHFQUEUE](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/CHFQUEUE) |

---

## Problem Statement

###  Read problems statements in Russian [here](https://www.codechef.com/download/translated/LTIME05/russian/CHFQUEUE.pdf)

All the chefs (except the Head Chef) are standing in queue to submit their bills. The chefs have different seniority. In all there are **N** chefs of **K** different seniority levels. These are given to you in an array, where **A1**, **A2**, ..., **AN** denote the seniority of chefs in the queue. **AN** denotes front of the queue and **A1** denotes end of the queue.

Head Chef gets an interesting thought past his head. He begins to think what if every chef starting from the end of the queue begins to delegate his job of submitting bills to a chef least ahead of him in the queue but junior to him. The Head Chef's fearfulness of this scenario is **f = i2 - i1 + 1**, where **i1** is the index of chef in queue and **i2** is the index of the junior chef. Head Chef's total fearfulness of chaos is the product of all the fearfulness in Head Chef's mind. Note if a chef has no junior ahead of him/her in the queue then Head Chef's fearfulness for this Chef is **1**.

You are required to find the Head Chef's total fearfulness given an arrangement of Chef's in a queue. Since this number can be quite large output it modulo **1000000007**.

### Input

Input description.

- The first line contains two integers **N** and ** K ** denoting the number of chefs and the number of seniority levels. The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the seniority of chefs in the queue. **AN** denotes front of the queue and **A1** denotes end of the queue.

### Output

Output description.

- Output a single integer denoting the total fearfulness of the Head Chef.

### Constraints

- **1** ≤ **N** ≤ **1000000**

- **1** ≤ **a_i** ≤ **1000000**

- **2** ≤ **K** ≤ **100000**

### Scoring

**Subtask 1 : N <= 5000 ( 10 points)**
** Subtask 2 : K = 2 ( 10 points) **
** Subtask 3 : K <= 10 ( 20 points ) **
** Subtask 4 : See Constraints ( 60 points ) **

---

## Examples

**Example 1**

**Input**

```text
4 2
1 2 1 2
```

**Output**

```text
2
```

**Explanation**

**Example case 1.** Only the second chef has a junior in front of him and the fearfulness he causes to the head chef is 3 - 2 + 1 = 2. Every other chef causes a fearfulness of 1 for the Head Chef.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS :

[Practice](http://www.codechef.com/problems/CHFQUEUE)

[Contest](http://www.codechef.com/LTIME05/problems/CHFQUEUE)

**Author** and **Editorialist** [Vineet Paliwal](http://www.codechef.com/users/vineetpaliwal)

**Tester** [Roman Rubanenko](http://www.codechef.com/users/rubanenko)

# DIFFICULTY :

## Cakewalk

# PREREQUISITES :

## Stacks , Queue , Modulo , Modular Arithmetic , Modular Multiplication

# PROBLEM :

Given N chefs in a queue , each chef may delegate his/her task to the junior least ahead of him and go away . The Head Chefs fearfulness of the scenario is the difference in index of the two positions + 1 . Head Chef’s total fearfulness is product of individual fearfulness corresponding to each chef . Find total fearfulness . In case no junior lies ahead the fearfulness is 1 .

# EXPLANATION:

### The Naive Solution :

For each chef look at all chefs ahead of this chef in the queue till you find a junior chef and then update the Head Chef’s fearfulness . This has a time complexity of O(N^2) .

### Using Stacks :

Start with given queue and an empty stack(of a structure of numbers and their indexes) .

For each chef put him on a stack if the top of stack is not senior to him otherwise pop out as many senior chefs from the stack as possible ( updating Head Chef’s fearfulness at each pop ) and finally push the chef on the stack .

The time complexity of this solution is O(N) .

### Example Using Stacks :

Given the queue , 8 3 7 8 9 12 13 11 3 4

Initialize ans = 1 ; sp = 1000000007

Step One : Stack == [8,1]

Step Two : Stack == [3,2] ( ans *= ( 2 - 1 + 1 ) , ans %= sp => ans = 2 )

Step Three : Stack == [3,2] [7,3] ( ans remains same )

Step Four : Stack == [3,2] [7,3] [8,4] ( ans remains same )

Step Five : Stack == [3,2] [7,3] [8,4] [9,5] ( ans remains same )

Step Six : Stack == [3,2] [7,3] [8,4] [9,5] [12,6] ( ans remains same )

Step Seven : Stack == [3,2] [7,3] [8,4] [9,5] [12,6] [13,7] ( ans remains same )

Step Seven : Stack = [3,2] [7,3] [8,4] [9,5] [11,8] ( Two elements are popped out , ans need to be multiplied by 2 and 3 corresponding to each of pop . So ans = 12 )

Step Eight : Stack == [3,2] [3,9] ( Four elements are popped out . ans need to be multiplied (modularly) by 2 , 5 , 6 , 7 )

Step Nine : Stack == [3,2] [3,9] [4,10] .

Finish and output ans .

### Point to Remember :

Take modulus with the special number given after each multiplication .

[SETTER’S SOLUTION](http://www.codechef.com/download/Solutions/LTIME05/Setter/CHFQUEUE.java)

[TESTER’S SOLUTION](http://www.codechef.com/download/Solutions/LTIME05/Tester/CHFQUEUE.cpp)

</details>
