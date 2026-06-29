# Andrew and the Meatballs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AMMEAT |
| Difficulty Rating | 1275 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [AMMEAT](https://www.codechef.com/practice/course/sorting/SORTINGPRO/problems/AMMEAT) |

---

## Problem Statement

Andrew likes meatballs very much.

He has **N** plates of meatballs, here the **i**th plate contains **Pi** meatballs. You need to find the minimal number of plates Andrew needs to take to his trip to Las Vegas, if he wants to eat there at least **M** meatballs. Note that each plate is already packed, i.e. he cannot change the amount of meatballs on any plate.

### Input

The first line of the input contains an integer **T**, denoting the number of test cases. The description of **T** test cases follows. The first line of each test case contains two space-separated integers **N** and **M**. The second line contains **N** space-separated integers **P1**, **P2**, ..., **PN**.

### Output

For each test case, output an integer, denoting the minimum number of plates. If it's impossible to take at least **M** meatballs, print **-1**.

### Constraints

- **1** ≤ **T** ≤ **7777**

- **1** ≤ **N** ≤ **7**

- **1** ≤ **M, Pi** ≤ **1018**

---

## Examples

**Example 1**

**Input**

```text
1
4 7
1 2 3 4
```

**Output**

```text
2
```

**Explanation**

If he takes **3**rd and **4**th plates, then we may eat **P3 + P4 = 7** meatballs in Las Vegas. This is the only way for eating at least **M = 7** meatballs with **2** plates.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/AMMEAT)

[Contest](http://www.codechef.com/COOK33/problems/AMMEAT)

[Video Editorial](https://youtu.be/IsQ-5Z77wMc)

# Difficulty:

CAKEWALK

# Pre-requisites:

ad-hoc

# Problem:

You have **N** plates of meatballs, the ith having **Pi** meatballs. What is the minimum number of plates you need to choose so that you have atleast **M** meatballs in total.

# Explanation:

Sort the plates in descending order of meatballs. Then keep adding plates until you cross the threshold **M**. This number is your answer.

### Proof of Correctness:

This is a greedy way of choosing your plates. Most greedy algorithms are proved using some kind of switching method - by converting an optimal solution to your greedy solution. We use this method here too.

After sorting, we know that greedy has chosen p1, p2, p3, …, pg. Let us assume an optimal solution chooses plates pi1, pi2, …, piOPT. We wish to transform the optimal solution to greedy. We know that:

p1 + p2 + … +

pg >= M,

p1

- p2 + … + pg-1 < M, and

pi1 +

pi2 + … +

piOPT >= M.

Let j be the first index from i1, i2, i3, …, iOPT that does not match the greedy choice. That is, i1 = 1, i2 = 2, …, ij-1 = j-1. Now, pj >= pij, and so the choice (i1, i2, i3, …, ij-1, *j*, ij+1, …, iOPT) also satisfies sum of number of meatballs >= M.

By repeating this switching, we have transformed this OPT into Greedy. But since OPT has the optimal number, thus greedy must also have the optimal number (since p1 + p2 + … + pg-1 < M).

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK33/Setter/AMMEAT.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK33/Tester/AMMEAT.cpp)

### Video Editorial

</details>
