# Hungry Ashish

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PIZZA_BURGER |
| Difficulty Rating | 1064 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PIZZA_BURGER](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PIZZA_BURGER) |

---

## Problem Statement

It's dinner time. Ashish is very hungry and wants to eat something. He has $X$ rupees in his pocket. Since Ashish is very picky, he only likes to eat either `PIZZA` or `BURGER`. In addition, he prefers eating `PIZZA` over eating `BURGER`. The cost of a `PIZZA` is $Y$ rupees while the cost of a `BURGER` is $Z$ rupees.

 Ashish can eat at most one thing. Find out what will Ashish eat for his dinner.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers $X$, $Y$ and $Z$ - the money Ashish has, the cost of a `PIZZA` and the cost of a `BURGER`.

---

## Output Format

For each test case, output what Ashish will eat. (`PIZZA`, `BURGER` or `NOTHING`).

You may print each character of the string in uppercase or lowercase. (for example, the strings `Pizza`, `pIzZa` and `piZZa` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y, Z \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
50 40 60
40 55 39
30 42 37
```

**Output**

```text
PIZZA
BURGER
NOTHING
```

**Explanation**

**Test case-1:** Ashish has $50$ rupees while the cost of `PIZZA` is $40$. Therefore he can buy a `PIZZA` for his dinner.

**Test case-2:** Ashish has $40$ rupees. The cost of `PIZZA` is $55$ and the cost of `BURGER` is $39$. Therefore Ashish can not buy a `PIZZA` but can buy a `BURGER` for his dinner.

**Test case-3:** Ashish has $30$ rupees which are not sufficient to buy either `PIZZA` or `BURGER`. Thus he can not buy anything and remains hungry :(.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
50 40 60
```

**Output for this case**

```text
PIZZA
```



#### Test case 2

**Input for this case**

```text
40 55 39
```

**Output for this case**

```text
BURGER
```



#### Test case 3

**Input for this case**

```text
30 42 37
```

**Output for this case**

```text
NOTHING
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PIZZA_BURGER)

[Contest: Division 3 ](https://www.codechef.com/COOK137C/problems/PIZZA_BURGER)

[Contest: Division 2 ](https://www.codechef.com/COOK137B/problems/PIZZA_BURGER)

[Contest: Division 1 ](https://www.codechef.com/COOK137A/problems/PIZZA_BURGER)

**Author:** [ Jeevan Jyot Singh ](https://www.codechef.com/users/jeevanjyot)

**Tester :** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Ashish is very hungry and wants to eat something. He has X rupees in his pocket. Since Ashish is very picky, he only likes to eat either `PIZZA` or `BURGER`. In addition, he prefers eating `PIZZA` over eating `BURGER`. The cost of a `PIZZA` is Y rupees while the cost of a `BURGER` is Z rupees.

Ashish can eat at most one thing. Find out what will Ashish eat for his dinner.

#
[](#explanation-5)EXPLANATION:

-

If X \ge Y, then he will eat `PIZZA`.

-

if X \ge Z and X < Y, then he is gonna eat `BURGER`.

-

If X < Z, then he will eat Nothing.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solutions-7)SOLUTIONS:

Author's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

void solve()
{
    int x, y, z; cin >> x >> y >> z;
    if(x >= y)
        cout << "Pizza\n";
    else if(x >= z)
        cout << "Burger\n";
    else
        cout << "Nothing\n";
}

int32_t main()
{
    IOS;
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        solve();
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int x, y, z;
        cin >> x >> y >> z;
        if (x >= y) {
            cout << "PIZZA" << '\n';
        } else if (x >= z) {
            cout << "BURGER" << '\n';
        } else {
            cout << "NOTHING" << '\n';
        }
    }
    return 0;
}
``

Editorialist Solution
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
    int x,y,z;
    cin>>x>>y>>z;

    if(x>=y)
      cout<<"PIZZA"<<"\n";
    else if(x>=z)
      cout<<"BURGER"<<"\n";
    else
      cout<<"NOTHING"<<"\n";
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
