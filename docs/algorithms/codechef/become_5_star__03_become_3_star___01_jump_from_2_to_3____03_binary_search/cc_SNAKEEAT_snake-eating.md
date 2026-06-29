# Snake Eating

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNAKEEAT |
| Difficulty Rating | 1950 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [SNAKEEAT](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/SNAKEEAT) |

---

## Problem Statement

The Chef has acquired a vicious bunch of snakes, and these snakes are ever hungry and end up eating each other. In particular, each snake i has a length **Li**, whose initial value is given to you. A snake can eat any other snake which is not longer than itself. That is, snake i can eat snake j (i ≠ j), if **Li** ≥ **Lj**. And when a snake eats another snake, its length increases by 1. That is, **Li** increases by 1. A snake can eat multiple other snakes.

The Chef doesn't care about snakes eating each other. All he wants is to have as many snakes as possible, which are at least some particular lengths long. You are given **Q** values: **K1, K2, .., KQ**. Treat each of them independently and output the answer for each. That is, for each **Ki**, assume that you start out from the beginning with all the snakes alive and the lengths as the initial values given in the input, and find out the maximum number of snakes you can get whose length is at least **Ki**.

### Input

- The first line contains an integer **T**, which is the number of testcases. The description of each testcase follows.

- The first line of each testcase contains two integers: **N** and **Q**, which denote the number of snakes initially, and the number of queries, respectively.

- The second line contains **N** space separated integers: **L1, L2, .., LN**, the initial lengths of the snakes.

- The i-th of the next **Q** lines contains a single integer, **Ki**.

### Output

- For each testcase, output **Q** lines, the i-th of which should have a single integer: The maximum number of snakes the Chef can get which are of length at least **Ki**.

### Constraints

- 1 ≤ **T** ≤ 5

- 1 ≤ **N, Q** ≤ 105

- 1 ≤ **Li** ≤ 109

- 1 ≤ **Ki** ≤ 109

### Explanation

---

## Examples

**Example 1**

**Input**

```text
2
5 2
21 9 5 8 10
10
15
5 1
1 2 3 4 5
100
```

**Output**

```text
3
1
0
```

**Explanation**

In the first testcase, first query, the second snake (length 9) can eat the fourth snake (length 8), and hence make its length 10. Now, there are four snakes left, and their lengths are {21, 10, 5, 10}. So, we have three snakes with length ? 10: Two snakes of length 10 and one snake of length 21. This is the best you can do.

In the second query, no matter what happens, you cannot get more than one snake of length ? 15.

In the second testcase, no matter what happens, you cannot get any snake of length ? 100. Hence the answer is 0.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PREREQUISITES** -

[Sorting](http://www.geeksforgeeks.org/merge-sort/), [Binary Searching](http://www.geeksforgeeks.org/binary-search/), [Sliding Window](http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)

**QUICK EXPLANATION** -

Sort the lengths array. For each query K, binary search for the largest element smaller than K and name it cur. Then binary search again on the prefix difference sum array (which will give the number of snakes to be fed to snakes in [prev+1, cur] to make their length at least K) in the region [1, cur] for finding the least index of snake to be killed and let it be prev. The answer is N-prev.

**EXPLANATION** -

Some key observations before we jump to the solution -

-

The most optimal choice would be to feed the largest snakes shorter than **K[i]** on the smallest snakes and to not feed the snakes greater than **K[i]** in length in i^{th} query.

-

If we get some **X** smallest snakes killed for some query **K[i]**, then, for all queries where **K[j] > K[i]** for some **j**, we get **Y** smallest snakes killed where the condition **(Y \geq X)** will be satisfied.

There are many solutions to this problem some of which are discussed below -

**ONLINE SOLUTION** -

Let us sort the lengths array as the order doesn’t matter for the answer.

Let us solve the problem for a query having its value as **K**. The most naive solution would be to keep iterating forward from 1 till we reach an element just smaller than **K** and name this index as **cur**. Let us keep one more pointer/variable **prev** which denotes the number of smallest snakes eaten, initially at 0. We will start feeding from cur^{th} snake. Now, to make it of length **K**, we need to feed it on **(K-l[i])** smallest snakes available, where **i** is initially **cur**. We increase the **prev** by **(K - l[i])** and decrease **i** by 1 to reflect this change. We do this process of increasing **prev** and decreasing **i** while the condition **(i > prev)** remains satisfied. Then we print the answer to be simply **N - i - 1**.

**Complexity** - O(Q*N)

This solution is inefficient but can be passed in TL if we optimise the solution by binary searching the **cur** and **prev** as both functions are monotonic in nature.

Now, let us also make a prefix sum array defined as follows -

**

presum[x] = presum[x-1] + (10^9 - l[x]),\hspace{4mm} \forall \hspace{4mm}1 \leq x \leq N

**

For every query having value **K**, we first find the value of **cur** by binary searching on length array as it is in increasing order. Then, we also find the largest index **prev** which is going to get killed. In the naive solution also, we were taking the summation of **(K - l[i])** from **cur** by iterating backwards and set the **prev** equal to that summation and it can be observed that the function **(i > prev)** is monotonic as **i** is decreasing and **prev** increasing.

**prev** can be found simply by binary searching method on sample space **[1, cur]**. Binary searching method works because we are finding the smallest **j** for which the condition

**

presum[cur] - presum[j] - (cur-j)*(10^9 - K) \hspace{4mm} \leq \hspace{4mm} j

**

is satisfied and this function is monotonic with increasing **j** and then we set **prev = j**. We want the shortest **j** as this is the demand of the question to minimize the snakes being eaten **OR** maximize the snakes of length ** \geq K** which is **(N - j)**.

The need for the **presum** array is that it is the number of snakes required to be killed to make the length of snakes in **[prev+1, cur]** to be more than or equal to **K** and which is the demand of the question to maximize the number of snakes of length **K**.

After finding **prev**, answer is **(N - prev)** for the query having value **K**.

**Complexity** - O((N+Q)*log(N))

**OFFLINE SOLUTION** -

Let us again sort the length array in increasing order as the order doesn’t matter. Also, let us sort the queries array along with their indices in increasing order of **K** values.

Hence, a 2-pointer offline solution will be to maintain 3 variables - **cur**, **prev**, **prefix** - where **cur** means that **cur^{th}** element is the largest element smaller than **K** value of current query which we are processing. **prev** refers to the largest index smaller than **cur** which is killed and can also be said that **prev** smallest snakes will be killed. Another thing to observe is that **cur** and **prev** can only increase if the queries are sorted according to **K** value of queries according to **observation 2**.

Let us assume that currently we are processing answer for **j^{th}** query in sorted order. **prefix** refers to

\sum \hspace{2mm} (K[j] - l[h]), \hspace{4mm} \forall \hspace{4mm} cur \geq h > prev

To calculate **prefix**, we keep on increasing **cur** and update **prefix** by adding **(K[j] - l[cur])** to **prefix** till we get **l[cur+1]** to be greater than **K[j]**. Then, We keep on increasing **prev** and keep updating **prefix** by subtracting **(K[j] - l[prev])** while **(prefix > prev)**. Then we get the answer for that query to be simply **(N - prev)** as **prev** refers to the largest index of snake which will be killed. Before proceeding to the next query, we also update the **prefix** by adding

**[(cur -

prev) * (K[j+1] - K[j])]**. The need for the **prefix** is that it is the number of snakes required to be killed to make the length of snakes in **[prev+1, cur]** to be exactly equal to **K[j]** and which is the demand of the question to maximize the number of snakes of length **K[j]**.

Remember, that we sorted the query and length arrays both in increasing order.

**Complexity** - O(N*log(N) + Q*log(Q))

There also exists another solution which is to do the naive solution as explained above, but to not do computation again for some **K** previously encountered. This can be implemented easily by mapping **K** value of query to its answer and checking everytime before computing answer for a query, that if the answer for same **K** value has been computed before using a **BST (map or set in C++)**. It can be proved easily that it is also efficient.

Offline solution implementation - [ here ](http://ideone.com/7Nxcl4)

</details>
