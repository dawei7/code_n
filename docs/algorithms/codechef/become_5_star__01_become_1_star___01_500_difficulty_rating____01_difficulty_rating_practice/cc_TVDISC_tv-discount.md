# TV Discount

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TVDISC |
| Difficulty Rating | 447 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TVDISC](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TVDISC) |

---

## Problem Statement

Chef is looking to buy a TV and has shortlisted two models. The first one costs $A$ rupees, while the second one costs $B$ rupees.

Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of $C$ rupees on the first TV, and a flat discount of $D$ rupees on the second one.

Help Chef determine which of the two TVs would be cheaper to buy during the sale.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains four space-separated integers $A$, $B$, $C$ and $D$ — the marked price (in rupees) of the first TV, the marked price (in rupees) of the second TV, the flat discount (in rupees) of the first TV, and the flat discount (in rupees) of the second TV.

---

## Output Format

For each test case, print a single line containing the string `First` if the first TV is cheaper to buy with discount, or `Second` if the second TV is cheaper to buy with discount. If both of them cost the same after discount, print `Any`.

You may print each character of the string in uppercase or lowercase (for example, the strings `first`, `First`, `fIRSt`, and `FIRST` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq A, B \leq 100$
- $0 \leq C \leq A$
- $0 \leq D \leq B$

---

## Examples

**Example 1**

**Input**

```text
3
85 75 35 20
100 99 0 0
30 40 0 10
```

**Output**

```text
First
Second
Any
```

**Explanation**

**Test case $1$:** The cost of the first TV after discount is $85 - 35 = 50$, while the cost of the second TV after discount is $75 - 20 = 55$. Thus the first TV is cheaper to buy than the second.

**Test case $2$:** The cost of the first TV after discount is $100 - 0 = 100$, while the cost of the second TV after discount is $99 - 0 = 99$. Thus the second TV is cheaper to buy than the first.

**Test case $3$:** The cost of the first TV after discount is $30 - 0 = 30$, while the cost of the second TV after discount is $40 - 10 = 30$. Since they are equal, Chef can buy any of them.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
85 75 35 20
```

**Output for this case**

```text
First
```



#### Test case 2

**Input for this case**

```text
100 99 0 0
```

**Output for this case**

```text
Second
```



#### Test case 3

**Input for this case**

```text
30 40 0 10
```

**Output for this case**

```text
Any
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TVDISC)

[Contest: Division 1](https://www.codechef.com/START51A/problems/TVDISC)

[Contest: Division 2](https://www.codechef.com/START51B/problems/TVDISC)

[Contest: Division 3](https://www.codechef.com/START51C/problems/TVDISC)

[Contest: Division 4](https://www.codechef.com/START51D/problems/TVDISC)

***Author:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Venkata Nikhil Medam](https://www.codechef.com/users/nikhil_medam)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

447

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are two TVs: the first costs A rupees and has a discount of C rupees, while the second costs B rupees and has a discount of D rupees. Which one is cheaper?

#
[](#explanation-5)EXPLANATION:

This is a simple application of if-conditions. The overall cost of the first TV is A - C rupees, while that of the second TV is B - D rupees. Compute these two values, then use if-else conditions to compare them and find out which one is less, or if they are equal.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Tester (C++)
``// Tester: Nikhil_Medam
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"

int t, a, b, c, d;
int32_t main() {
    cin >> t;
    while(t--) {
        cin >> a >> b >> c >> d;
        if(a - c < b - d) {
            cout << "First" << endl;
        }
        else if(a - c > b - d) {
            cout << "Second" << endl;
        }
        else {
            cout << "Any" << endl;
        }
    }
	return 0;
}
``

Editorialist (Python)
``for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a-c < b-d:
        print('first')
    else:
        print('second' if a-c > b-d else 'any')
``

</details>
