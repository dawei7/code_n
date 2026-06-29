# Chain of Doughnuts

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DONUTS |
| Difficulty Rating | 1611 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [DONUTS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/DONUTS) |

---

## Problem Statement

There is new delicious item in Chef's menu - a doughnut chain. Doughnuts connected successively in line forming a chain.

*Chain of 3 doughnuts*

Chef has received an urgent order for making a chain of **N** doughnuts. He noticed that there are exactly **N** cooked doughnuts in the kitchen, some of which are already connected in chains. The only thing he needs to do is connect them in one chain.

He can cut one doughnut (from any position in a chain) into two halves and then use this cut doughnut to link two different chains.

Help Chef determine the minimum number of cuts needed to complete the order.

### Input

- The first line of the input contains an integer **T** denoting the number of test cases.

- The first line of each test case contains two integer **N** and **M** denoting the size of order and number of cooked chains respectively.

- The second line contains **M** space-separated integers **A1**, **A2**, ..., **AM** denoting the size of the chains.

*It is guaranteed that **N** is equal to the sum of all **Ai**'s over **1<=*i*<=M**.*

### Output

For each test case, output a single line containing an integer corresponding to the number of cuts needed Chef to make the order.

### Constraints and Subtasks

- **1** ≤ **T** ≤ **200**

- **1** ≤ **N** ≤ **2*109**

- **1** ≤ **Ai** ≤ **105**

**Subtask 1: 10 points**

- **1** ≤ **M** ≤ **2*104**

- **Ai = 1**

**Subtask 2: 30 points**

- **1** ≤ **M** ≤ **100**

**Subtask 3: 60 points**

- **1** ≤ **M** ≤ **2*104**

---

## Examples

**Example 1**

**Input**

```text
2
11 3
4 3 4
6 3
3 2 1
```

**Output**

```text
2
1
```

**Explanation**

**Example 1:** We could cut 2 doughnut from any "chain" and use them to connect chains to the one.
 For example, let's cut it from the first chain. After this we will have chains of sizes 2, 3, 4 and two doughnuts that have been cut. So we could connect the first chain with second and second with third using these two doughnuts.

**Example 2:** We cut doughnut from the last "chain" and connect the first two chains.

*Image for second example. Yellow doughnut has been cut.*

**Separated test cases**

#### Test case 1

**Input for this case**

```text
11 3
4 3 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6 3
3 2 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/DONUTS)

[Contest](http://www.codechef.com/SEPT15/problems/DONUTS)

**Author:** [Andrii Mostovyi](https://www.codechef.com/users/m0stik)

**Tester:** [Kevin Atienza](https://www.codechef.com/users/kevinsogo)

**Editorialists:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra) and [Suhash Venkatesh](https://www.codechef.com/users/suh_ash2008)

### DIFFICULTY:

Easy

### PREREQUISITES:

Sorting, Greedy

### PROBLEM:

Given chains of doughnuts of different lengths, we need to join them to form a single chain. Two chains can be joined by cutting a doughnut into two and using it to clip the chains together. We need to minimize the number of cuts needed to form a single chain consisting of all the N doughnuts.

### EXPLANATION:

**Subtask 1**

Since all the chains are of length 1, we can simply take them one by one and attach to form larger chain. Thus, the answer each time is \lfloor\frac{M}{2}\rfloor.

**Subtask 2 and 3**

We can observe that a single doughnut is capable of joining two chains of lengths l_1 and l_2 in one cut to form a chain of length l_1 + l_2 + 1. This hints towards a greedy solution. We need to decide the number of single doughnuts we need in order to join all the chains together. It can be noted that it is best to join longer chains together. For example, consider the case when we have chains of lengths 1, 2, 3. It is best to join chains of lengths 2 and 3 with the help of the unit-length chain. Any other order of joining doesn’t yield an optimal result.

Thus, we begin by sorting the chains by their lengths. Next, we iterate from i = 1 to M. We stop at that i where cumulative sum of chain lengths from 1 to i becomes greater than M-i-1. This is the point where we have the sufficient number of single doughnuts to join all chains. As a last step, we need to check whether cumulative sum up to i is exactly equal to M-i-1 or more than M-i-1. In the former case, the answer is M-i-1. In the latter case, it is M-i because the i^{th} chain will have to be attached in the end too.

### COMPLEXITY:

\mathcal{O}(M \log M) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/SEPT15/Setter/DONUTS.cpp)

[Tester](http://www.codechef.com/download/Solutions/SEPT15/Tester/DONUTS.py)

[Editorialist](http://www.codechef.com/download/Solutions/SEPT15/Editorialist/DONUTS.cpp)

</details>
