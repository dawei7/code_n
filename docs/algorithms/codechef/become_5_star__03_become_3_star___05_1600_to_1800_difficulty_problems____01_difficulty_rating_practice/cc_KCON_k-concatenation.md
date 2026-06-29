# K-Concatenation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KCON |
| Difficulty Rating | 1780 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [KCON](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/KCON) |

---

## Problem Statement

You are given an array **A** with size **N** (indexed from 0) and an integer **K**. Let's define another array **B** with size **N** · **K** as the array that's formed by concatenating **K** copies of array **A**.

For example, if **A** = {1, 2} and **K** = 3, then **B** = {1, 2, 1, 2, 1, 2}.

You have to find the maximum subarray sum of the array **B**. Fomally, you should compute the maximum value of **Bi + Bi+1 + Bi+2 + ... + Bj**, where 0 ≤ **i** ≤ **j** < **N** · **K**.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **K**.

- The second line contains **N** space-separated integers **A0, A1, ..., AN-1**.

### Output

For each test case, print a single line containing the maximum subarray sum of **B**.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **K** ≤ 105

- -106 ≤ **Ai** ≤ 106 for each valid **i**

### Subtasks

**Subtask #1 (18 points):** **N** · **K** ≤ 105

**Subtask #2 (82 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
2 3
1 2
3 2
1 -2 1
```

**Output**

```text
9
2
```

**Explanation**

**Example case 1:** **B** = {1, 2, 1, 2, 1, 2} and the subarray with maximum sum is the whole {1, 2, 1, 2, 1, 2}. Hence, the answer is 9.

**Example case 2:** **B** = {1, -2, 1, 1, -2, 1} and the subarray with maximum sum is {1, 1}. Hence, the answer is 2.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
1 2
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
3 2
1 -2 1
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/KCON)

[Contest](http://www.codechef.com/JAN18/problems/KCON)

**Author:** [Hruday Pabbisetty](http://www.codechef.com/users/hruday968)

**Tester:** [Alexey Zayakin](http://www.codechef.com/users/alex_2oo8)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

EASY

### PREREQUISITES:

None

### PROBLEM:

You are given array A_0, \dots, A_{N-1} and integer K. Array B of size N \cdot K is formed by concatenating K copies of array A. You have to find maximum subarray sum of the array B.

### QUICK EXPLANATION

Answer is maximum sum subarray from doubled A plus either 0 or K-2 sums of all elements in A.

### EXPLANATION:

Let’s denote array A concatenated with itself as 2A. You should note that any subarray in array B can be presented as arbitrary subarray in 2A plus from 0 to K-2 whole arrays A. Indeed you begin in some position i, then swallow some whole number of arrays A then continue from position which corresponds to i+1 in 2A and swallow at most N-1 elements, thus you won’t leave array 2A. So first of all you should find subarray with largest sum in 2A, which you can do with prefix sums, Kadane’s algorithm or any other algorithm you may find in [this](https://en.wikipedia.org/wiki/Maximum_subarray_problem) wikipedia article. After that if sum of elements in A is positive, you add it with coefficient K-2, otherwise you add it with coefficient 0. That gives you O(N) solution.

Example of code to find maximum subarray sum:

``const int64_t inf = 1e18;
int64_t sum = 0, mn = 0;
int64_t ans = -inf;
for(int i = 0; i < n; i++) {
    sum += a[i];
    ans = max(ans, sum - mn);
    mn = min(mn, sum);
}
return ans;
``

With this code you can find the solution as follows:

``if(k == 1) {
    cout << maxsub(a) << endl;
} else {
    int64_t sm = accumulate(begin(a), end(a), 0ll);
    for(int i = 0; i < n; i++) {
        a.push_back(a[i]);
    }
    int64_t ans = maxsub(a);
    if(sm > 0) {
        ans += sm * (k - 2);
    }
    cout << ans << endl;
}
``

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Setter/KCON.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Tester/KCON.cpp).

### RELATED PROBLEMS:

</details>
