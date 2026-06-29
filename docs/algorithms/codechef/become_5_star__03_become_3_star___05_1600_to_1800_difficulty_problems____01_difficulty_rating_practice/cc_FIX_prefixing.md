# Prefixing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIX |
| Difficulty Rating | 1736 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [FIX](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/FIX) |

---

## Problem Statement

Given an array $A$ of size $N$, construct an array $B$ of size $N$ such that :
- Every element of $B$ is present **at least once** in $A$;
- For all $1\le i \le N$, every element in prefix $[A_1,A_2, \ldots, A_i]$ is present **at least once** in prefix $[B_1,B_2,\ldots, B_i]$.

If multiple such arrays $B$ exist, find the **lexicographically largest** $B$.

Note that for two arrays $X$ and $Y$, each of size $N$, where $i$ is the smallest index at which they differ, array $X$ is said to be lexicographically larger than array $Y$ when $X_i \gt Y_i$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line, lexicographically largest array $B$ satisfying the conditions.

It can be guaranteed that one such array $B$ always exists.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i\leq 10^5$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
5 5 2 3
2
8 9
3
7 1 7
```

**Output**

```text
5 5 2 3 
8 9 
7 1 7
```

**Explanation**

**Test case $1$:** Consider $B = [5, 5, 2, 3]$. Every element of $B$ is present **at least once** in $A$.
- $i=1$: Prefix of $A$ is $[5]$ and $B$ is $[5]$. Every element in prefix of $A$ is present in prefix of $B$ at least once.
- $i=2$: Prefix of $A$ is $[5,5]$ and $B$ is $[5,5]$.
- $i=3$: Prefix of $A$ is $[5,5,2]$ and $B$ is $[5,5,2]$.
- $i=4$: Prefix of $A$ is $[5,5,2,3]$ and $B$ is $[5,5,2,3]$.

Also, this is the lexicographically largest possible $B$.

**Test case $2$:** Consider $B = [8, 9]$. Every element of $B$ is present **at least once** in $A$.
- $i=1$: Prefix of $A$ is $[8]$ and $B$ is $[8]$.
- $i=2$: Prefix of $A$ is $[8,9]$ and $B$ is $[8,9]$.

Also, this is the lexicographically largest possible $B$.

**Test case $3$:** It can be proved that this is the lexicographically largest possible $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
5 5 2 3
```

**Output for this case**

```text
5 5 2 3
```



#### Test case 2

**Input for this case**

```text
2
8 9
```

**Output for this case**

```text
8 9
```



#### Test case 3

**Input for this case**

```text
3
7 1 7
```

**Output for this case**

```text
7 1 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIX)

[Contest: Division 1](https://www.codechef.com/START111A/problems/FIX)

[Contest: Division 2](https://www.codechef.com/START111B/problems/FIX)

[Contest: Division 3](https://www.codechef.com/START111C/problems/FIX)

[Contest: Division 4](https://www.codechef.com/START111D/problems/FIX)

***Author:*** [ro27](https://www.codechef.com/users/ro27)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [raysh07](https://www.codechef.com/users/raysh07)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

An array A of length n is given, and we need to construct the lexicographically maximal array B of length n, such that every element of B is present in A, and each element in prefix of A, i.e. A_1, A_2, ...., A_i is present at least once in the corresponding prefix of B, i.e. B_1, B_2, ...., B_i.

# [](#explanation-5)EXPLANATION:

The general idea behind a lot of lexicographically maximal (or minimal) problems is to try to construct the sequence starting from the first element and greedily trying to choose the maximal (or minimal) element which still allows a valid sequence to be formed.

Let M denote the maximum element in A.

For now, assume that we have constructed the sequence upto (i - 1) elements B_1, B_2,..., B_{i - 1}, and need to decide B_i. if A_i has already occured in the sequence B_1, B_2, ...., B_{i - 1}, then set B_i = M (recall that every element of B has to be present in A) otherwise set B_i = A_i.

It is easy to see this algorithm always constructs a valid sequence, and we always choose the largest element which still allows a valid sequence, thus making it lexicographically maximal possible. To check if A_i occurs in the prefix of B, we can use a set.

A slightly more intuitive way to think of it is: if i is the first time A_i has occured in the array A, then set B_i = A_i, else B_i = M. It’s not hard to see that this is also equivalent to the previous solution.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(nlogn)  per testcase.

# [](#code-7)CODE:

Editorialist's Code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main(){
    int t; cin >> t;

    while (t--){
        int n; cin >> n;

        vector <int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        int mx = 0;
        for (int i = 0; i < n; i++) mx = max(mx, a[i]);

        set <int> st;
        for (int i = 0; i < n; i++){
            if (st.find(a[i]) == st.end()){
                cout << a[i] << " ";
            } else {
                cout << mx << " ";
            }
            st.insert(a[i]);
        }

        cout << "\n";
    }
    return 0;
}
``

</details>
