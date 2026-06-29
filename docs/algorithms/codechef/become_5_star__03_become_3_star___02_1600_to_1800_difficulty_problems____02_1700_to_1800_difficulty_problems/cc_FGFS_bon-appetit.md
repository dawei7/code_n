# Bon Appetit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FGFS |
| Difficulty Rating | 1734 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [FGFS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/FGFS) |

---

## Problem Statement

Our chef has recently opened a new restaurant with a unique style. The restaurant is divided into **K** compartments (numbered from **1** to **K**) and each compartment can be occupied by at most one customer.

 Each customer that visits the restaurant has a strongly preferred compartment **p** (**1 ≤ p ≤ K**), and if that compartment is already occupied, then the customer simply leaves. Now obviously, the chef wants to maximize the total number of customers that dine at his restaurant and so he allows (or disallows) certain customers so as to achieve this task. You are to help him with this.

 Given a list of **N** customers with their arrival time, departure time and the preferred compartment, you need to calculate the maximum number of customers that can dine at the restaurant.

### Input

 The first line contains an integer **T** denoting the number of test cases. Each of the next **T** lines contains two integers **N** and ** K **, the number of customers that plan to visit the chef's restaurant and the number of compartments the restaurant is divided into respectively. Each of the next **N** lines contains three integers **si**, **fi** and **pi** , the arrival time, departure time and the strongly preferred compartment of the **ith** customer respectively.

Note that the **ith** customer wants to occupy the **pith** compartment from **[si, fi) ** i.e the **ith** customer leaves just before  ** fi** so that another customer can occupy that compartment from  ** fi** onwards.

### Output

 For every test case, print in a single line the maximum number of customers that dine at the restaurant.

### Constraints

- ** 1 **≤  **T** ≤ **  30 **

- ** 0 ** ≤ **N**  ≤ ** 105**

- ** 1 ** ≤ ** K**  ≤ ** 109**

- ** 0 ** ≤  **si** < **fi** ≤ **  109**

- ** 1 ** ≤ ** pi** ≤ ** K **

---

## Examples

**Example 1**

**Input**

```text
2
3 3
1 3 1
4 6 2
7 10 3
4 2
10 100 1
100 200 2
150 500 2
200 300 2
```

**Output**

```text
3
3
```

**Explanation**

**Example case 1.**

All three customers want different compartments and hence all 3 can be accommodated.

**Example case 2.**

If we serve the **1st**, **2nd** and **4th** customers, then we can get a maximum of 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/FGFS)

[Contest](http://www.codechef.com/JAN14/problems/FGFS)

**Author:** [Vivek Hamirwasia](http://www.codechef.com/users/viv001)

**Tester:** [Mahbub](http://www.codechef.com/users/white_king)

**Editorialist:** [Jingbo Shang](http://www.codechef.com/users/shangjingbo)

### DIFFICULTY:

Easy

### PREREQUISITES:

Sort, Greedy.

### PROBLEM:

Given some sets of open intervals (exclusive at two ends), for each set, find the maximum number of disjoint intervals.

### EXPLANATION:

First of all, we need to observe that the intervals in different sets are independent (in the original statement, the customers preferred in different compartments are independent).

For a single set, it is a classical greedy problem, called [Activity Selection problem](http://en.wikipedia.org/wiki/Activity_selection_problem). The greedy method is as following:

- Sort the intervals by their right end ascending.

- Initialized the select intervals as an empty set

- Consider the sorted intervals one by one, add it if it is possible (only need to check the last select interval and the current one).

The intuition of this greedy is that, we need to make sure the space remained for the later intervals is as large as possible. The proof is also easy. For the first interval, we definite choose the interval which ends earliest. Otherwise, we can replace the first interval in the best solution with that earliest ended interval (with at least same best solution). Therefore, we can achieve the maximum interval selections with choosing the earliest ended interval. Recursively, we can see that the greedy is correct.

In summary, we can solve this problem in O(**N** log **N**), where **N** is the total number of intervals in all sets.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/January/Setter/FGFS.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/January/Tester/FGFS.cpp).

</details>
