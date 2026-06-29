# Army Training

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARMTRN |
| Difficulty Rating | 1742 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ARMTRN](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ARMTRN) |

---

## Problem Statement

Chef is a high-ranked army officer and he has been given the job to train the army.

The army consists of $N$ soldiers where each soldier has $3$ parameters:
- *Attack points*: $A_i$ where $(0\lt A_i \lt 1000)$;
- *Defense points*: $(1000-A_i)$;
- *Soldier type*: `ATTACK` or `DEFENSE`.

For the whole army:
- *Attack value* of the army is defined as the **sum** of *attack points* of all `ATTACK` type soldiers.
- *Defense value* of the army is defined as the **sum** of *defense points* of all `DEFENSE` type soldiers.
- *Rating* of the army is defined as the **product** of *Attack value* and *Defense value* of the army.

Assign the *soldier type* to each of the soldiers to **maximize** the *rating* of the army. Print the maximum *rating*.

**NOTE:** The output may exceed the range of a $32$-bit integer.
Remember to use $64$-bit data types, such as `long long` in `C++`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of soldiers in the army.
    - The next line contains the array $A$ — where $A_{i}$ denotes the *attack points* of the $i^{th}$ soldier.

---

## Output Format

For each test case, output on a new line the **maximum** possible *rating* that can be achieved.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $0 \lt A_{i} \lt 1000$
- Sum of $N$ over all test cases does not exceed $2000$.

---

## Examples

**Example 1**

**Input**

```text
4
2
500 500
3
500 500 500
4
100 800 300 500
4
300 700 800 200
```

**Output**

```text
250000
500000
2080000
2250000
```

**Explanation**

**Test case $1$:** Soldier $1$ should be used for `ATTACK` while soldier $2$ should be used for `DEFENSE`. Thus, the *attack value* as well as the *defense value* equals $500$. The *rating* $=500\cdot 500 = 250000$. It can be proven that this is the maximum possible *rating* that we can achieve for the given army.

**Test case $2$:**
- Soldier $1$ and $2$ should be used for `ATTACK`. So, *attack value* $=500+500=1000$
- Soldier $3$ should be used for `DEFENSE`. So, *defense value* $=(1000-500)=500$

So, *rating* $=1000 \cdot 500=500000$. This is the maximum possible *rating* that we can achieve for the given army.

**Test case $3$:**
- Soldier $2$ and $4$ should be used for `ATTACK`. So, *attack value* $=800+500=1300$
- Soldier $1$ and $3$ should be used for `DEFENSE`. So, *defense value* $=(1000-100)+(1000-300)=1600$

So, *rating* $=1300 \cdot 1600=2080000$. This is the maximum possible *rating* that we can achieve for the given army.

**Test case $4$:**
- Soldier $2$ and $3$ should be used for `ATTACK`. So, *attack value* $=700+800=1500$
- Soldier $1$ and $4$ should be used for `DEFENSE`. So, *defense value* $=(1000-300)+(1000-200)=1500$

So, *rating* $=1500 \cdot 1500=2250000$. This is the maximum possible *rating* that we can achieve for the given army.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
500 500
```

**Output for this case**

```text
250000
```



#### Test case 2

**Input for this case**

```text
3
500 500 500
```

**Output for this case**

```text
500000
```



#### Test case 3

**Input for this case**

```text
4
100 800 300 500
```

**Output for this case**

```text
2080000
```



#### Test case 4

**Input for this case**

```text
4
300 700 800 200
```

**Output for this case**

```text
2250000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START46A/problems/ARMTRN)

[Contest Division 2](https://www.codechef.com/START46B/problems/ARMTRN)

[Contest Division 3](https://www.codechef.com/START46C/problems/ARMTRN)

[Contest Division 4](https://www.codechef.com/START46D/problems/ARMTRN)

[Practice](https://www.codechef.com/problems/ARMTRN)

**Setter:** [Utkarsh Darolia](https://www.codechef.com/users/utkarsh_utk)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Utkarsh Darolia](https://www.codechef.com/users/utkarsh_utk)

#
[](#difficulty-2)DIFFICULTY

1742

#
[](#prerequisites-3)PREREQUISITES

Sorting

#
[](#problem-4)PROBLEM

There are N soldiers in an army and the i^{th      } soldier has 3 parameters — *Attack points* : A_i, *Defense points* : 1000-A_i and *Soldier type* : `ATTACK` or `DEFENSE`.

For the whole army:

-
*Attack value* of the army is defined as the **sum** of *attack points* of all `ATTACK` type soldiers.

-
*Defense value* of the army is defined as the **sum** of *defense points* of all `DEFENSE` type soldiers.

-
*Rating* of the army is defined as the **product** of *Attack value* and *Defense value* of the army.

The task is to assign the *soldier type* to each of the soldiers to **maximize** the *rating* of the army and find out that maximum *rating*.

#
[](#explanation-5)EXPLANATION

To solve this problem, let’s first try solving a subproblem, which is to find the maximum achievable *rating* if you are given the count of soldiers of `ATTACK` and `DEFENSE` type.

Let’s define *rating(r)* as the maximum possible *rating* that can be achieved, given that we can assign any r soldiers to `ATTACK` type and the remaining n-r soldiers to `DEFENSE` type. The solution to this subproblem can be constructed as follows —

- Sort the *Attack points* array A in descending order.

- Assign first r soldiers to `ATTACK` type and remaining n-r to `DEFENSE` type.

- So, *Attack points* of every soldier of `ATTACK` type are greater than or equal to attack points of every soldier of `DEFENSE` type.

Proof that the proposed approach gives the assignment with maximum rating

A[i] are *Attack points* of soldier at index i and D[i] are the *Defence points* of soldier at index i.

After following the proposed approach, we can divide the soldiers into 2 groups Atk and Def —

-
Atk_{1}, Atk_{2}, …, Atk_{r} are indexes of the soldiers of `ATTACK` type.

-
Def_{1}, Def_{2}, …, Def_{n-r} are indexes of the soldiers of `DEFENSE` type.

-
A[Atk_{i}] \geq A[Def_{j}] and D[Atk_{i}] \leq D[Def_{j}] (1 \leq i \leq r ; 1 \leq j \leq n-r)

Let’s assume that the proposed approach is wrong and there is a better value of *rating(r)* that can be achieved by swapping types of soldiers Atk_{i} and Def_{j} (1 \leq i \leq r ; 1 \leq j \leq n-r). Let that the current *Attack value* and *Defense value* are Atkval and Defval respectively. Then the new values after swapping the types of soldiers would be —

-
*New Attack value* =Atkval-(A[Atk_{i}]-A[Def_{j}]). As A[Atk_{i}] \geq A[Def_{j}], *New Attack value* is lesser than or equal to Atkval.

-
*New Defense value* =Defval-(D[Def_{j}]-D[Atk_{i}])=. As D[Atk_{i}] \leq D[Def_{j}], *New Defense value* is lesser than or equal to Defval.

As both *New Attack value* and *New Defense value* are lesser than or equal to Atkval and Defval respectively, the *New Rating* would also be lesser than or equal to the initial *rating*.

So, we have a contradiction as we couldn’t get a better value of *rating(r)* and hence the approach that we proposed would always give the maximum value of *rating(r)*.

Let B be the array that we got by sorting *Attack points* array A in descending order, Sum(r) be the sum of attack points of first r soldiers in array B and TotSum be the total sum of attack points of all soldiers.

We can simplify the expression of *rating(r)* using the steps below —

-
*Attack value* \times *Defense value*

- [B_{1}+B_{2}...+B_{r}] \times [(1000-B_{r+1})+(1000-B_{r+2})...+(1000-B_{n})]

- [Sum(r)] \times [(1000*(n-r))-(B_{r+1}+B_{r+2}...+B_{n})]

- [Sum(r)] \times [(1000*(n-r))-(TotSum-Sum(r))]

Our final answer would be maximum value of *rating(r)* where r ranges from 0 to n. This can be implemented by iterating over array B and finding Sum(r) for every r as Sum(r-1)+B_{r} and putting all required values into the expression of *rating(r)* formulated above.

#
[](#time-complexity-6)TIME COMPLEXITY

The overall time complexity is dependent on the sorting technique used. Everything except sorting can be done in O(N). If we use fast sorting techniques, then an overall time complexity O(Nlog(N)) per test case can be achieved.

#
[](#solutions-7)SOLUTIONS

Editorialist's Solution
``// Utkarsh Darolia
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int n;
        cin >> n;

        int TotSum = 0, Sum = 0;
        int A[n];

        for (int j = 0; j < n; ++j)
        {
            cin >> A[j];
            TotSum += A[j];
        }

        sort (A, A+n, greater<int>()); //greater<int>() is used for sorting in descending order

        long long finalAnswer = 0;

        for (int r = 0; r < n; ++r)
        {
            finalAnswer = max (finalAnswer,(long long)(Sum)*((1000*(n-r))-(TotSum-Sum)));
            Sum += A[r];
        }

        cout << finalAnswer << endl;
    }
    return 0;
}
``

Feel free to share your approach. Suggestions are welcome.

</details>
