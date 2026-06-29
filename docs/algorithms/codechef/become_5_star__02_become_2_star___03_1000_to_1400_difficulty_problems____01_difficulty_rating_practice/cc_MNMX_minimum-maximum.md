# Minimum Maximum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MNMX |
| Difficulty Rating | 1392 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MNMX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MNMX) |

---

## Problem Statement

Chef loves to play with arrays by himself. Today, he has an array **A** consisting of **N** distinct integers. He wants to perform the following operation on his array **A**.

- Select a pair of adjacent integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation will be equal to the smaller of them.

Find out minimum sum of costs of operations needed to convert the array into a single element.

### Input

First line of input contains a single integer **T** denoting the number of test cases. First line of each test case starts with an integer **N** denoting the size of the array **A**. Next line of input contains **N** space separated integers, where the **ith** integer denotes the value **Ai**.

### Output

For each test case, print the minimum cost required for the transformation.

### Constraints

- **1 ≤ T ≤ 10 **

- **2 ≤ N ≤ 50000 **

- **1 ≤ Ai ≤ 105 **

### Subtasks

- **Subtask 1 :** 2 ≤ N ≤ 15** : 35 pts **

- **Subtask 2 :** 2 ≤ N ≤ 100** : 25 pts **

- **Subtask 3 :** 2 ≤ N ≤ 50000** : 40 pts **

---

## Examples

**Example 1**

**Input**

```text
2
2
3 4
3
4 2 5
```

**Output**

```text
3
4
```

**Explanation**

**Test 1 : ** Chef will make only 1 move: pick up both the elements (that is, 3 and 4), remove the larger one (4), incurring a cost equal to the smaller one (3).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
4 2 5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK

[Practice](http://www.codechef.com/problems/MNMX)

[Contest](http://www.codechef.com/LTIME27/problems/MNMX)

**Author:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Alex Gu](http://www.codechef.com/users/minimario) and [Pushkar Mishra](http://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Prateek Gupta](https://www.codechef.com/users/prateekg603)

**Russian Translator:** [Vitalij Kozhukhivskij](https://www.codechef.com/users/witalij_hq)

**Vietnamese Translator:** [Khanh Xuan Nguyen](https://www.codechef.com/users/khanhptnk)

**Mandarian Translator:** [Gedi Zheng](https://www.codechef.com/users/stzgd)

**Contest Admin:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen) and [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

## DIFFICULTY:

Simple

## PREREQUISITES:

None

## PROBLEM:

Given an array of size N, you have to reduce the array into a single element by repeatedly applying a single operation.

The operation involves picking up two adjacent elements in the array and remove larger of them by paying a cost equal to smaller of them. Minimize the total cost.

## EXPLANATION

**Solution for Subtask 1:**

This subtask can indeed be solved by Bit Masking DP. Check [this](https://www.codechef.com/node/225100) link to know more about Bit Masking.

In this case, we maintain a state F(mask) where in, set bits of mask represent which all indexes have been removed uptill now. We want to arrive at a state where only the last element i.e only 1 unset bit remains in the final array. The last index remaining will always be the position of minimum element in the array regardless of the order of applied operations. Lets look at the pseudo code to understand how this recurrence works.

``F(mask) {
   if ( __builtin_popcount(mask) == n-1 ) return 0
   long long ans = 0
   for ( int i = 0; i < n; i++ ) {
       if ( !(mask & (1<<i)) ) {
            int j = i+1
            while ( j < n && (mask&(1<<j)) ) j++
            if ( j != n ) {
                int remove_idx = (A[i] > A[j]) ? i : j
                ans = min(ans, min(A[i],A[j]) + f(mask | (1<<remove_idx)) )
            }
       }
   }
   return ans
}
``

Basically, at any particular state, we are checking what all indices are there which have not been removed yet. So for this, we try to apply all kinds of X-1 operations for any X unset bits. We take a bit which is not set, lets call it i, we find the just next unset bit j, which would mean these two are consecutive elements at that particular state and hence, the greater of them can be removed. We do this for all such (i,j) pairs to take the minimum of all answers. Minimum value returned by calling function F(0) will hence be the minimum cost spent to convert the array into a single element. Overall Complexity for this naive approach is \mathcal{O}(2^N*N^2)

**Solution for subtask 2 & 3:**

In order to minimize the total cost, you should surely choose the pair of consecutive integers consisting of the smallest element in the given array. The minimum element will anyway be the last remaining element after all operations have been applied. So, why not choose a pair of consecutive numbers involving this minimum element till the whole array reduces to this minimum element. Since, we need to perform this operation N - 1 times, total cost incurred will hence be equal to (N - 1)*(MINVAL). As answer can be little large, use a data type which can handle larger numbers.

## COMPLEXITY

As minimum value in the array can just be found in a single traversal, overall complexity of the solution is \mathcal{O}(N).

## SOLUTIONS

[Tester](https://www.codechef.com/viewplaintext/7965305)

</details>
