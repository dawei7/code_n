# The One with All the Candy

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | S07E09 |
| Difficulty Rating | 1804 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [S07E09](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/S07E09) |

---

## Problem Statement

*Monica decides that she would like to get to know the neighbours in the apartment better. She makes a batch of wonderful chocolates and hangs them on the door in a basket hoping that her neighbors will take some and they can meet. The neighbours (including Joey) eventually go crazy over the candy and demand more. Eventually, she keeps a bowl full of chocolates at the door for the last time.*

There are $N$ neighbours. The $i^{th}$ neigbhour has initial energy equal to $A_i$. There is one bowl filled with chocolates. The neighbours are made to stand in a row and the bowl is passed around by obeying the following rules:

- Any person can hold the bowl initially.
- If the person holding the bowl has positive energy, he/she passes the bowl to the person on the immediate right of him/her. The rightmost person in the row passes the bowl to the leftmost person in the row.
- The act of passing the bowl takes $1$ second.
- If the person holding the bowl has non-positive energy, he/she drops the bowl.
- After each pass, the energy of the person reduces by $1$.

Among all possible ways in which the $N$ neighbours start the game, find the **maximum time** until the bowl is dropped.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains one integer $N$.
- Second line of each testcase contains of $N$ integers, denoting the elements of array $A$.

---

## Output Format

For each testcase, output in a single line the maximum time until the bowl is dropped.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $0 \leq A[i] \leq 10^6$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3
2 1 1
3
0 5 0
4
3 0 2 1
```

**Output**

```text
4
1
3
```

**Explanation**

**Test case 1**: One of the optimal orders in which all the neighbours can stand in the row is:
$1$ $\rightarrow$ $2$ $\rightarrow$ $3$ $\rightarrow$ $1$. The bowl is initially with person $1$.
- Person $1$, in one second, passes the bowl to person $2$ and his/her own energy becomes $1$.
- Person $2$, in one second, passes the bowl to person $3$ and his/her own energy becomes $0$.
- Person $3$, in one second, passes the bowl to person $1$ and his/her own energy becomes $0$.
- Person $1$, in one second, passes the bowl to person $2$ and his/her own energy becomes $0$.
- Person $2$ has $0$ energy, so he/she drops the bowl.
Thus, the bowl is dropped after $4$ seconds.

**Test case 2**: One of the optimal orders in which all the neighbours can stand in the row is:
$2$ $\rightarrow$ $1$ $\rightarrow$ $3$ $\rightarrow$ $2$. The bowl is initially with person $2$. Thus, it would travel as $2$ $\rightarrow$ $1$. The bowl can not be passed further due to $0$ energy of person $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 1 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
0 5 0
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
3 0 2 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/FOUR21A/problems/S07E09)

[Contest Division 2](https://www.codechef.com/FOUR21B/problems/S07E09)

[Contest Division 3](https://www.codechef.com/FOUR21C/problems/S07E09)

**Setter:** [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [ Nishant Shah](https://www.codechef.com/users/nishant403)

**Editorialist:** [ Bhavya Mittal](https://www.codechef.com/users/bhavy24)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Given an array A of length N. You need to rearrange the elements of A such that:

- the value of the element decreases by 1 upon visiting.

- the number of elements visited is maximum

- elements are visited in circular order until 0 is encountered

#
[](#explanation-5)EXPLANATION

**Observation 1**

The first zero will be encountered at one of the minimum values of the array.

Proof

Since each element decreases by 1 upon visiting and we are traversing the array in a circular fashion, the first element where we will encounter 0 will be one of the minimums.

Since we can rearrange the elements in any order, we sort the array in increasing order, so that all the minimum elements come together in one place.

**Observation 2**

If we complete one loop on the whole array then the value of every element decreases exactly by 1.

**Observation 3**

We can traverse through the array at a[0] (of the sorted array) times, i.e. we can visit at least a[0] * N elements.

Proof

Let’s take an example to understand this point:

Let the sorted array be [2, 2, 3, 5, 6]

After 1 traversal: [1, 1, 2, 4, 5] Elements visited = 5

After 2 traversals: [0, 0, 1, 3, 4] Elements visited = 5

Total elements visited = 5 + 5 = 2 * 5

Since the first element has become$ 0$, we can’t traverse the array any more.

Now, to maximize the number of elements visited we can start our traversal from the element next to the element with the minimum value, which isn’t equal to it.

Let’s say that value is at index i, then our final answer = a[0] * N + (N - i).

To understand this let’s take the above example again.

The sorted array: [2, 2, 3, 5, 6]

We start our traversal from 3.

After 1 traversal: [2, 2, 2, 4, 5]. Elements visited = 3.

The remaining 2 traversals are the same.

Total elements visited = 2 * 5 + 3.

#
[](#solutions-6)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

int n;
void solve()
{
    cin >> n;
    long long int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort(a, a + n);
    int ans = 0;
    int mn = a[0];
    for (int i = 0; i < n; i++)
    {
        if (a[i] > mn)
        {
            cout << a[0] * n + n - i;
            return;
        }
    }
    cout << a[0] * n;
}
int main()
{
    int t = 1;
    cin >> t;
    while (t--)
    {
        solve();
        cout << "\n";
    }
    return 0;
}
``

</details>
