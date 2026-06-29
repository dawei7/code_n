# Get Lowest Free

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SALE |
| Difficulty Rating | 778 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SALE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SALE) |

---

## Problem Statement

Chef goes to the supermarket to buy some items. Luckily there's a sale going on under which Chef gets the following offer:

- If Chef buys $3$ items then he gets the item (out of those $3$ items) having the lowest price as free.

For e.g. if Chef bought $3$ items with the cost $6$, $2$ and $4$, then he would get the item with cost $2$ as free. So he would only have to pay the cost of the other two items which will be $6 + 4 = 10$.

Chef buys $3$ items having prices $A$, $B$ and $C$ respectively. What is the amount of money Chef needs to pay?

---

## Input Format

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $A, B, C$ - the prices of the items bought by Chef.

---

## Output Format

For each test case, output the price paid by Chef.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B, C \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
6 2 4
3 3 3
8 4 4
```

**Output**

```text
10
6
12
```

**Explanation**

**Test case-1:** Explained in the problem statement.

**Test case-2:** Since all the three items have the same price, Chef will get one of them free and will have to pay the cost of the other two items which will be $3 + 3 = 6$.

**Test case-3:** Chef will get one of the items having price $4$ as free and will have to pay the cost of the other two items which will be $8 + 4 = 12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 2 4
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
3 3 3
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
8 4 4
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START27A/problems/SALE)

[Contest Division 2](https://www.codechef.com/START27B/problems/SALE)

[Contest Division 3](https://www.codechef.com/START27C/problems/SALE)

[Contest Division 4](https://www.codechef.com/START27D/problems/SALE)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef goes to the supermarket to buy some items. Luckily there’s a sale going on under which Chef gets the following offer:

- If Chef buys 3 items then he gets the item (out of those 3 items) having the lowest price as free.

For e.g. if Chef bought 3 items with the cost 6, 2 and 4, then he would get the item with cost 2 as free. So he would only have to pay the cost of the other two items which will be 6 + 4 = 10.

Chef buys 3 items having prices A, B and C respectively. What is the amount of money Chef needs to pay?

#
[](#explanation-5)EXPLANATION:

We first need to find out the lowest price among A, B and C.

If A is lowest, then Chef needs to pay B + C. Similarly, if B is lowest, Chef will pay A+C and if C is lowest, Chef will pay A+B.

To find out if A is lowest, we can use two *if* conditions - (A \leq B) AND (A \leq C). We can have similar conditions for B and C.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

int main()
{
    ll t;
    cin >> t ;
    while(t--)
    {
        ll a , b , c ;
        cin >> a >> b >> c ;

        if(a <= b && a <= c)
        {
            cout << b+c << '\n' ;
        }
        else
        {
            if(b <= a && b <= c)
                cout << a+c << '\n' ;
            else
                cout << a+b << '\n' ;
        }
    }

    return 0;
}

``

</details>
