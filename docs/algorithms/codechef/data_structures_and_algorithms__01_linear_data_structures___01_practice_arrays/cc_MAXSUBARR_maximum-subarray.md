# Maximum Subarray 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXSUBARR |
| Difficulty Rating | 1613 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [MAXSUBARR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/MAXSUBARR) |

---

## Problem Statement

Given two arrays $A$ and $B$ of sizes $N$ and $M$ respectively. You can apply the following operation until the array $B$ is non-empty:
- Choose either the **first** or the **last** element of array $B$.
- Insert the chosen element to either the **front** or the **back** of array $A$.
- Delete the chosen element from array $B$.

For example, let $A = [9, 7]$ and $B = [1, 3, 2]$. In one operation, we can choose either $X = 1$ or $X = 2$ (first or last element of array $B$). We can insert $X$ in array $A$ and make it either $A = [X, 9, 7]$ or $A = [9, 7, X]$. The chosen $X$ is deleted from array $B$. Thus, it will become either $B = [3, 2]$ (when chosen $X$ is $1$) or $B = [1, 3]$ (when chosen $X$ is $2$).

Find the **maximum sum** of any subarray of the array $A$ that you can achieve after performing exactly $M$ operations.

Note: A subarray of an array is formed by deleting some (possibly zero) elements from the beginning of the array and some (possible zero) elements from the end of the array. A subarray can be empty as well.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $4$ lines of input.
    - The first line of each test contains a single integer $N$, the size of array $A$.
    - The next line contains $N$ space-separated integers, denoting elements of array $A$.
    - The third line of each test contains a single integer $M$, the size of array $B$.
    - The next line contains $M$ space-separated integers, denoting elements of array $B$.

---

## Output Format

For each test case, output on a new line the **maximum sum** of any subarray of the array $A$ that you can achieve after performing exactly $M$ operations.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- $-10^8 \leq A_i, B_i \leq 10^8$

---

## Examples

**Example 1**

**Input**

```text
3
5
3 26 -79 72 23
2
66 44
1
81
1
-97
5
10 -5 14 -20 4
3
-10 5 -2
```

**Output**

```text
205
81
24
```

**Explanation**

**Test case $1$:**
- Operation $1$: Add the first element of array $B$ to the back of array $A$. Thus, $A = [3, 26, -79, 72, 23, 66]$ and $B = [44]$.
- Operation $2$: Add the first element of array $B$ to the back of array $A$. Thus, $A = [3, 26, -79, 72, 23, 66, 44]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[72, 23, 66, 44]$ having sum $72+23+66+44=205$.

**Test case $2$:**
- Operation $1$: Add the first element of array $B$ to the front of array $A$. Thus, $A = [-97, 81]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[81]$ having sum $81$.

**Test case $3$:**
- Operation $1$: Add the last element of array $B$ to the back of array $A$. Thus, $A = [10, -5, 14, -20, 4, -2]$ and $B = [-10, 5]$.
- Operation $2$: Add the last element of array $B$ to the front of array $A$. Thus, $A = [5, 10, -5, 14, -20, 4, -2]$ and $B = [-10]$.
- Operation $3$: Add the first element of array $B$ to the front of array $A$. Thus, $A = [-10, 5, 10, -5, 14, -20, 4, -2]$ and $B = []$.

The, maximum sum subarray of array $A$ is $[5, 10, -5, 14]$ having sum $5+10-5+14 = 24$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
3 26 -79 72 23
2
66 44
```

**Output for this case**

```text
205
```



#### Test case 2

**Input for this case**

```text
1
81
1
-97
```

**Output for this case**

```text
81
```



#### Test case 3

**Input for this case**

```text
5
10 -5 14 -20 4
3
-10 5 -2
```

**Output for this case**

```text
24
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXSUBARR)

[Contest: Division 1](https://www.codechef.com/START59A/problems/MAXSUBARR)

[Contest: Division 2](https://www.codechef.com/START59B/problems/MAXSUBARR)

[Contest: Division 3](https://www.codechef.com/START59C/problems/MAXSUBARR)

[Contest: Division 4](https://www.codechef.com/START59D/problems/MAXSUBARR)

***Author:*** [Arpit Dutt Dixit](https://www.codechef.com/users/arpit121)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

[Maximum sum subarray](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

#
[](#problem-4)PROBLEM:

You have two arrays A and B. In one move, you can choose either the first or last element of B, and move it to either the front or back of A.

What is the maximum possible sum of a subarray in the final array?

#
[](#explanation-5)EXPLANATION:

We’d like a large subarray sum, so it makes sense to ignore negative elements from B as much as possible and take as many positive elements as we can.

One obvious way to do this is to just move all the negative elements to one side and positive elements to the other — for example, move all negative elements of B to the back of A, and all positive elements of B to the front of A. Alternately, we can move all the negative elements to the front and the positive ones to the back.

It turns out that these are the only two cases we need to consider!

Proof

This can be proved by analyzing what the final answer looks like.

- If the maximum subarray doesn’t contain any elements from B, it doesn’t matter how the distribution is done, since subarrays of A remain unchanged.

- If the maximum subarray doesn’t contain any elements from A, the best we can do is obviously just the sum of all positive elements in B, which both cases of ours cover.

- Finally, suppose the maximum subarray includes elements from both A and B. Note that since elements of B can only be inserted at the start or end, the structure of such a subarray is:

- Some elements of B and a prefix of A, or

- Some elements of B and a suffix of A

"Some elements of B" is optimally every positive integer of B, and then we choose a prefix or suffix of A with maximum sum. Note that this is exactly what our two cases cover, hence completing the proof.

There are only two cases. For each one, find the maximum subarray sum of the resulting array in linear time (this is a well-known algorithm, and is linked above in the prerequisites).

The final answer is the maximum of the two cases.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;
#define lli long long

lli maxSubArraySum(vector<lli> a, int n)
{
    lli max_tot = INT_MIN, m = 0;

    for (int i = 0; i < n; i++) {
        m = m + a[i];
        if (max_tot < m)
            max_tot = m;

        if (m < 0)
            m = 0;
    }
    return max_tot;
}

int main(){

    // freopen("output.txt","r",stdin);
    // freopen("output1.txt","w",stdout);
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n;
        vector<lli> a(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        cin>>m;
        vector<lli> b(m);
        lli p=0;
        for(int i=0;i<m;i++){
            cin>>b[i];
            if(b[i]>0)p+=b[i];
        }
        long long maxx;

        a.insert(a.begin(),p);
        maxx=maxSubArraySum(a,n+1);
        a.erase(a.begin(),a.begin()+1);
        a.insert(a.begin()+n,p);
        maxx=max(maxx,maxSubArraySum(a,n+1));
        cout<<maxx<<endl;
    }
}
``

Editorialist's code (Python)
``def calc(a):
    ans = cur = 0
    for x in a:
        cur = max(x, x + cur)
        ans = max(ans, cur)
    return ans
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    b.sort()
    pos = 0
    while pos < m and b[pos] < 0:
        pos += 1
    print(max(calc(b[pos:] + a), calc(a + b[pos:])))
``

</details>
