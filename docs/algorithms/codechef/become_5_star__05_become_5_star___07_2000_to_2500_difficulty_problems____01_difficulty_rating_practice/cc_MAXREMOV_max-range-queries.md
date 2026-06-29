# Max Range Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXREMOV |
| Difficulty Rating | 2057 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAXREMOV](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAXREMOV) |

---

## Problem Statement

You have $C = 100,000$ cakes, numbered $1$ through $C$. Each cake has an integer height; initially, the height of each cake is $0$.

There are $N$ operations. In each operation, you are given two integers $L$ and $R$, and you should increase by $1$ the height of each of the cakes $L, L+1, \ldots, R$. One of these $N$ operations should be removed and the remaining $N-1$ operations are then performed.

Chef wants to remove one operation in such a way that after the remaining $N-1$ operations are performed, the number of cakes with height exactly $K$ is maximum possible. Since Chef is a bit busy these days, he has asked for your help. You need to find the maximum number of cakes with height exactly $K$ that can be achieved by removing one operation.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- Each of the next $N$ lines contains two space-separated integers $L$ and $R$ describing one operation.

### Output
For each test case, print a single line containing one integer — the maximum possible number of cakes with height $K$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 10^5$
- $1 \le K \le N$
- $1 \le L \le R \le 10^5$
- the sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
1
3 2
2 6
4 9
1 4
```

**Output**

```text
3
```

**Explanation**

**Example case 1:** Let's look at what happens after an operation is removed.
- Removing operation $1$: The heights of cakes $4$ through $9$ increase by $1$. Then, the heights of cakes $1$ through $4$ increase by $1$. The resulting sequence of heights is $[1, 1, 1, 2, 1, 1, 1, 1, 1]$ (for cakes $1$ through $9$; the other cakes have heights $0$). The number of cakes with height $2$ is $1$.
- Removing operation $2$: The resulting sequence of heights of cakes $1$ through $9$ is $[1, 2, 2, 2, 1, 1, 0, 0, 0]$. The number of cakes with height $2$ is $3$.
- Removing operation $3$: The resulting sequence of heights of cakes $1$ through $9$ is $[0, 1, 1, 2, 2, 2, 1, 1, 1]$. The number of cakes with height $2$ is $3$.

The maximum number of cakes with height $2$ is $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXREMOV)

[Contest](https://www.codechef.com/COOK103A/problems/MAXREMOV)

**Author:** [Abhinav Jain]

**Tester:** [Michael Nematollahi](https://www.codechef.com/users/watcher)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

None

### PROBLEM:

You have C=100,000 cakes, numbered 1 through C. Each cake has an integer height. Initially, the height of each cake is 0. There are Q operations. In each operation, you are given two integers L and R and you should increase by 1 the height of all cakes at positions [L,L+1,…,R].

One of these Q operations should be removed and the remaining Q?1 operations are then performed. Given K, help chef by finding one operation to remove such that after performing remaining operations the number of cakes with a height of exactly K is maximum possible.

### EXPLANATION:

We will discuss a linear solution to this problem.  Let’s first assume that all operations are performed. How can we calculate cakes’ heights after all operations are finished?

Let’s read all the operations first. Then, let’s iterate through cakes from the first one till the last one. Suppose that we are processing currently the i_{th} cake. If there is some operation which has L=i that means that we must increase the heights of all cakes while we are moving forward until R+1=i. When R+1=i that mentioned operation won’t affect any more cakes.

So we should keep an array change[1\,...\,C].

change_i denotes the number of queries with L=i minus the number of queries with R=i-1.

(R=i-1 because the R_{th} cake should be incremented and the increment must be canceled at R+1).

So how to calculate the final heights? (Think a little bit).

``for(int i = 1 ; i ? C ; i++)
   height[i] = height[i-1] + change[i];
``

Simple !!

Now which query we should remove?

Let’s think about the outcome of removing one operation and canceling its effects. All cakes between the L_{th} and the R_{th} (inclusive) will have their heights decreased by 1. So after removing a certain operation, the number of cakes with height K is equal to A+B+C

**A** = number of cakes with a height equal to exactly K between the 1^{st} cake and the (L-1)^{th} cake

**B** = number of cakes with a height equal to exactly K+1 between the L^{th} cake and the R^{th} cake

**C** = number of cakes with a height equal to exactly K between the (R+1)^{th} cake and the last cake.

So after calculating the heights resulting from applying the operations, we are interested in only 2 heights. K and (K+1).

Keep 2 prefix sum arrays, target[1\,...\,C] , targetplus[1\,...,C]

target_i denotes the number of cakes with final height equal to K among the first i cakes.

targetplus_i denotes the number of cakes with final height equal to K+1 among the first i cakes.

Now, it’s easy to check each operation and check the effect of removal and update our answer accordingly. Check codes for more details.

Complexity O(N + Q)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[**AUTHOR’s solution**](https://pastebin.com/siv5mwSb)

[**TESTER’s solution**](https://pastebin.com/4hN0wV5E)

</details>
