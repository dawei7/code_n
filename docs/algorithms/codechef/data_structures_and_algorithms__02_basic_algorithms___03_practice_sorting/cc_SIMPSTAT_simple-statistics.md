# Simple Statistics

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SIMPSTAT |
| Difficulty Rating | 1222 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [SIMPSTAT](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/SIMPSTAT) |

---

## Problem Statement

Sergey has made **N** measurements. Now, he wants to know the average value of the measurements made.

In order to make the average value a better representative of the measurements, before calculating the average, he wants first to remove the highest **K** and the lowest **K** measurements. After that, he will calculate the average value among the remaining **N - 2K** measurements.

Could you help Sergey to find the average value he will get after these manipulations?

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two space-separated integers **N** and **K** denoting the number of measurements and the number of the greatest and the lowest values that will be removed.

The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the measurements.

### Output

For each test case, output a single line containing the average value after removing **K** lowest and **K** greatest measurements.

Your answer will be considered correct, in case it has absolute or relative error, not exceeding **10-6**.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **104**

- **0** ≤ **2K** < **N**

- **-106** ≤ **Ai** ≤ **106**

### Subtasks

- Subtask #1 (50 points): **K = 0**

- Subtask #2 (50 points): **no additional constraints**

---

## Examples

**Example 1**

**Input**

```text
3
5 1
2 9 -10 25 1
5 0
2 9 -10 25 1
3 1
1 1 1
```

**Output**

```text
4.000000
5.400000
1.000000
```

**Explanation**

**Example case 1.** After removing **1** greatest and **1** lowest measurement, we get the set **{2, 9, 1}**. The average value in this set is **(2+9+1)/3=4**.

**Example case 2.** The average value in the set **{2, 9, -10, 25, 1}** is **(2+9-10+25+1)/5=5.4**.

**Example case 3.** After removing the **1** largest and smallest measurements, Sergey will be left with only one measurement, i.e. **1**. Average of this is **1** itself.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 1
2 9 -10 25 1
```

**Output for this case**

```text
4.000000
```



#### Test case 2

**Input for this case**

```text
5 0
2 9 -10 25 1
```

**Output for this case**

```text
5.400000
```



#### Test case 3

**Input for this case**

```text
3 1
1 1 1
```

**Output for this case**

```text
1.000000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/SIMPSTAT)

[Contest](http://www.codechef.com/LTIME34/problems/SIMPSTAT)

**Author:** [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Tester:** [Vlad Mosko](https://www.codechef.com/users/zedthirtyeight)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Sorting

### PROBLEM:

Given an array A of length N, remove the smallest and largest K elements from it and then calculate the average.

### EXPLANATION:

**Subtask 1**

For this subtask, K = 0. This means that we don’t have to remove any element from the given input array A. The only thing that remains now is to calculate the average of this array. For that, we simply take the cumulative sum of all the elements and divide it by the length of the array. Care needs to be taken about the data types used. We want to do all the operations in the double type so that the final answer is precise to the required decimal places.

This algorithm requires a simple scan of the array. Therefore, the complexity is \mathcal{O}(N).

**Subtask 2**

In this subtask, K > 0. This means that we have two exclude certain number of smallest and certain greatest numbers in the input array. What is the fastest method to determine the smallest and the greatest K numbers? Sorting. We can sort the array in ascending order. Then the first K elements are the smallest K elements and the last K elements are the greatest K elements. After sorting, we simply sum over the elements excluding the first and the last K elements and divide the result by N-2K. Again, care is to be taken regarding data types being double.

We can’t use an \mathcal{O}(N^2) sorting method because that wouldn’t run in time (note that there are 100 test cases per file). So, we have to use an \mathcal{O}(N\log N) sorting like the quicksort, mergesort, or the in-built sorts in most of the programming languages. Since sorting is the heaviest operation in the algorithm, the complexity is \mathcal{O}(N\log N).

Editorialist’s program follows the editorial. Please see for implementation details.

### OPTIMAL COMPLEXITY:

\mathcal{O}(N\log N) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/LTIME34/Setter/SIMPSTAT.cpp)

[Tester](http://www.codechef.com/download/Solutions/LTIME34/Tester/SIMPSTAT.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/LTIME34/Editorialist/SIMPSTAT.cpp)

</details>
