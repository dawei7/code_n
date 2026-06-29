# Devu and Perfume

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DEVPERF |
| Difficulty Rating | 1708 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [DEVPERF](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/DEVPERF) |

---

## Problem Statement

There is a haunted town called HauntedLand. The structure of HauntedLand can be thought of as a grid of size **n * m**. There is a house in each cell of the grid. Some people have fled from their houses because they were haunted. '.' represents a haunted house whereas '*' represents a house in which people are living.

One day, Devu, the famous perfumer came to town with a perfume whose smell can hypnotize people. Devu can put the perfume in at most one of the houses. This takes Devu one second. Then, the perfume spreads from one house (need not be inhabited by people) to all its adjacent houses in one second, and the cycle continues. Two houses are said to be a adjacent to each other, if they share a corner or an edge, i.e., each house (except those on the boundaries) will have 8 adjacent houses.

You want to save people from Devu's dark perfumery by sending them a message to flee from the town. So, you need to estimate the minimum amount of time Devu needs to hypnotize all the people? Note that if there are no houses inhabited by people, Devu doesn't need to put perfume in any cell.

### Input

The first line of input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

First line of each test case contains two space separated integers **n, m** denoting the dimensions of the town.

For each of next **n** lines, each line has **m** characters (without any space) denoting a row of houses of the town.

### Output
For each test case, output a single integer corresponding to the answer of the problem.

### Constraints

- **1** ≤ **T** ≤ **20**

**Subtask #1:** (40 points)

- **1** ≤ **n, m** ≤ **100**

**Subtask #2:** (60 points)

- **1** ≤ **n, m** ≤ **1000**

---

## Examples

**Example 1**

**Input**

```text
2
2 2
*.
..
3 4
.*..
***.
.*..
```

**Output**

```text
1
2
```

**Explanation**

**In the first example**, it will take Devu one second for putting the perfume at the only house. So, the answer is 1.

**In the second example**, He will first put the perfume at the * at cell (1, 1) (assuming 0-based indexing).
Now, it will take Devu 1 secs to put perfume. In the next second, the perfume will spread to all of its adjacent cells, thus making each house haunted.
So, the answer is 2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/DEVPERF)

[Contest](http://www.codechef.com/JAN16/problems/DEVPERF)

**Author:** [Praveen Dhindwa](https://www.codechef.com/users/sereja)

**Tester:** [Antoniuk Vasyl](https://www.codechef.com/users/antoniuk1) and [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given a grid filled with ‘*’ and ‘.’, find the cell in the grid from where the distance to the farthest ‘*’ marked cell is travelled in least time. Report that time.

### EXPLANATION:

** Subtask 1 **

For each row in the given grid, let us maintain two variables: max\_left and max\_right. The first one stores the column number of the left-most ‘*’ marked cell in the row. Similarly, the other variable stores the column number of the right-most ‘*’ marked cell in the row. Once we have processed the grid for these 2N values, all we need to do is iterate over all cells in the grid and check the time it will take the perfume to reach these 2N preprocessed cells. The cell which minimizes the maximum of times taken to reach the 2N cells is the answer.

How do we calculate this time? Let us say the perfume is released at cell (x_1,\,\, y_1) and reaches cell (x_2,\,\, y_2). How much time will it take given the movement constraints? The answer is max(x_2 - x_1,\,\, y_2-y_1) + 1.

How did we get this? Let us assume without loss of generality that x_2 - x_1 < y_2 - y_1. Since, diagonal movement is allowed, both x-coordinate and y-coordinate can be incremented by 1 simultaneously in the required direction of movement. Once the required row or column has been reached, the remaining distance along other dimension can be travelled in a straight line. Hence, max(x_2 - x_1,\,\, y_2-y_1). The extra plus 1 is because it takes 1 second for the perfume to act on the cell it is released in.

The proof of why we only need to consider the 2N points is trivial and left to the reader to work out. The complexity of this approach is \mathcal{O}(TN^2M) which is sufficient for the constraints of this subtask.

** Subtask 2 **

We need to drop a factor of N from the complexity some how. Let us at the 2N deeper points we processed. Do we need to take into account all of them to find the answer? Some amount of thinking tells us we just need to consider four ‘*’ marked cells in the grid: the one with max column number, the one with min column number, the one with max row number, and the one with min row number.

Then the answer we are looking for is \frac{max(max\_col-min\_col,\,\, max\_row-min\_row)}{2} + 1. Why are we taking the averages of the min and max column and row numbers? This is because it is optimal to release the perfume at the mean point. If the perfume is released at any other point, the time taken to reach at least one of the extremes will be more than in the case when it is released at the mean. The time is calculated by the same logic as given in the subtask 1 solution. This solution is \mathcal{O}(TNM).

### OPTIMAL COMPLEXITY:

\mathcal{O}(NM) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/JAN16/Setter/DEVPERF.cpp)

[Tester](http://www.codechef.com/download/Solutions/JAN16/Tester/DEVPERF.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/JAN16/Editorialist/DEVPERF.cpp)

</details>
