# Janmansh at Fruit Market

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JMARKET |
| Difficulty Rating | 947 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [JMARKET](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/JMARKET) |

---

## Problem Statement

Janmansh is at the fruit market to buy fruits for Chingari. There is an infinite supply of three different kinds of fruits with prices $A$, $B$ and $C$.

He needs to buy a total of $X$ fruits having at least $2$ different kinds of fruits. What is the least amount of money he can spend to buy fruits?

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space separated integers $X$, $A$, $B$, $C$ - the number of fruits to buy and the prices of the three different types of fruits respectively.

---

## Output Format

For each test case, output the least amount of money he can spend to buy fruits.

---

## Constraints

- $1 \le T \le 10^5$
- $2 \le X \le 1000$
- $1 \le A, B, C \le 100$

---

## Examples

**Example 1**

**Input**

```text
2
2 1 1 1
3 4 3 2
```

**Output**

```text
2
7
```

**Explanation**

**Test case-1:** He can buy any two fruits of different kinds for a total price of $2$.

**Test case-2:** He can buy $1$ fruit of price $3$ and $2$ fruits of price $2$ for a total price of $7$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1 1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 4 3 2
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK139A/problems/JMARKET)

[Contest Division 2](https://www.codechef.com/COOK139B/problems/JMARKET)

[Contest Division 3](https://www.codechef.com/COOK139C/problems/JMARKET)

[Contest Division 4](https://www.codechef.com/COOK139D/problems/JMARKET)

**Setter:** [Janmansh Agarwal](https://www.codechef.com/users/janmansh)

**Tester:** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

[Greedy](https://en.wikipedia.org/wiki/Greedy_algorithm)

#
[](#problem-4)PROBLEM:

Janmansh is at the fruit market to buy fruits for Chingari. There is an infinite supply of three different kinds of fruits with prices A, B and C.

He needs to buy a total of X fruits having at least 2 different kinds of fruits. What is the least amount of money he can spend to buy fruits?

#
[](#explanation-5)EXPLANATION:

- It is always optimal to choose the fruit with the lowest price.

- To have 2 different kinds of fruits, we can select exactly **one** fruit not having the lowest price.

Without the loss of generality, let us assume A \leq B \leq C.

To have the minimum price for buying X fruits having at least 2 different kinds of fruits, we can buy (X-1) fruits with cost A and 1 fruit with cost B.

Thus, the answer is (X-1)\cdot A + B (where A \leq B \leq C).

#
[](#time-complexity-6)TIME COMPLEXITY:

Sorting 3 elements takes constant time. Thus, the time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int x, a, b, c;
        cin >> x >> a >> b >> c;
        vector<int> v = {a, b, c};
        sort(v.begin(), v.end());
        cout << (x - 1) * v[0] + v[1] << endl;
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;

	    int a[3];
	    cin>>a[0]>>a[1]>>a[2];
	    sort(a, a+3);

	    cout<<(x-1)*a[0] + a[1]<<endl;
	}
	return 0;
}
``

</details>
