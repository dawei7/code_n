# Chef and Chocolate

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHCHCL |
| Difficulty Rating | 1343 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHCHCL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHCHCL) |

---

## Problem Statement

Chef has a standard chocolate of **n** by **m** pieces. More formally, chocolate is a rectangular plate consisting of **n** rows and **m** columns.

Here you can see an example of a standard 5 by 7 chocolate.

He has two friends and they will play with this chocolate. First friend takes the chocolate and cuts it into two parts by making either a horizontal or vertical cut. Then, the second friend takes one of the available pieces and divides into two parts by either making a horizontal or vertical cut. Then the turn of first friend comes and he can pick any block of the available chocolates and do the same thing again. The player who cannot make a turn loses.

Now Chef is interested in finding which of his friends will win if both of them play optimally. Output "Yes", if the friend who plays first will win, otherwise print "No".

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two space separated integers **n** and **m** - the sizes of the chocolate.

### Output

For each test case, output a single line containing one word "Yes" (without quotes) if there is a sequence of moves leading to the winning of the person who moves first and "No" (without quotes) otherwise.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **n, m** ≤ **109**

### Subtasks
**Subtask #1 (10 points):**

- **1 ≤ **n**, **m** ≤ 10**

**Subtask #2 (30 points):**

- **n** = **1** or **m** = **1**

**Subtask #3 (60 points): ** No additional constraints

---

## Examples

**Example 1**

**Input**

```text
2
1 2
1 3
```

**Output**

```text
Yes
No
```

**Explanation**

**Example case 1.** There is only one possible move, so the second player even won't have a chance to make move.

**Example case 2.** There are only two ways first player can make first move, after each of them only one move left, so the first player cannot win.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
1 3
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

(Note: the editorials are written in a hurry and without having solved the problems, so there may be mistakes. Feel free to correct them / inform me.)

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHCHCL)

[Contest](https://www.codechef.com/AUG16/problems/CHCHCL)

**Author:** [Vasyl Antoniuk](https://www.codechef.com/users/antoniuk1)

**Tester:** [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Editorialist:** [Xellos](https://www.codechef.com/users/xellos0)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

none

### PROBLEM:

Two players are breaking a chocolate bar of size N \times M into pieces. A player’s turn consists of choosing one piece and breaking it in two. Which player wins the game?

### QUICK EXPLANATION:

This is a classic mathematical exercise. Notice that the number of pieces of chocolate increases by 1 in each player’s turn; initially, there’s only 1 piece and when the game ends, there have to be NM pieces (otherwise, there’s still some piece that can be broken). So the outcome of the game only depends on who makes the NM-th move - or equivalently, on the parity of NM. If NM is odd, the first player has to make the NM-th move and loses; otherwise, the second player has to make it and loses. Of course, this works in constant time.

### AUTHOR’S AND TESTER’S SOLUTIONS:

The author’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG16/Setter/CHCHCL.cpp).

The tester’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG16/Tester/CHCHCL.cpp).

### RELATED PROBLEMS:

</details>
