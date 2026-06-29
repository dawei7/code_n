# Valentine is Coming

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VALENTINE |
| Difficulty Rating | 691 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [VALENTINE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/VALENTINE) |

---

## Problem Statement

Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.

Chef has a total of $X$ rupees and one chocolate costs $Y$ rupees. What is the **maximum** number of chocolates Chef can buy?

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$ - the amount Chef has and the cost of one chocolate respectively.

---

## Output Format

For each test case, output the **maximum** number of chocolates Chef can buy.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
5 10
16 5
35 7
100 1
```

**Output**

```text
0
3
5
100
```

**Explanation**

**Test case-1:** Chef has $5$ rupees but the cost of one chocolate is $10$ rupees. Therefore Chef can not buy any chocolates.

**Test case-2:** Chef has $16$ rupees and the cost of one chocolate is $5$ rupees. Therefore Chef can buy at max $3$ chocolates since buying $4$ chocolates would cost $20$ rupees.

**Test case-3:** Chef has $35$ rupees and the cost of one chocolate is $7$ rupees. Therefore Chef can buy at max $5$ chocolates for $35$ rupees.

**Test case-4:** Chef has $100$ rupees and the cost of one chocolate is $1$ rupee. Therefore Chef can buy at max $100$ chocolates for $100$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 10
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
16 5
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
35 7
```

**Output for this case**

```text
5
```



#### Test case 4

**Input for this case**

```text
100 1
```

**Output for this case**

```text
100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START26A/problems/VALENTINE)

[Contest Division 2](https://www.codechef.com/START26B/problems/VALENTINE)

[Contest Division 3](https://www.codechef.com/START26C/problems/VALENTINE)

[Contest Division 4](https://www.codechef.com/START26D/problems/VALENTINE)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a total of X Rs and one chocolate costs Y Rs. What is the maximum number of chocolates Chef can buy.

#
[](#explanation-5)EXPLANATION:

We are given that one chocolate costs Y rupees. Thus, in X rupees, we can buy ?\frac{X}{Y}? chocolates.

Here, ?N? is floor(N) which represents the greatest integer not greater than N.

Note that in languages like C++ and Java, a floating point number is automatically rounded down to the nearest integer.

Examples

-
X = 7, Y = 2: We know that 1 chocolate costs 2 rupees. Then, from 7 rupees, we can buy ?\frac{7}{2}? = ?3.5? = 3 chocolates.

-
X = 15, Y = 3: Single chocolate costs 3 rupees. Then, from 15 rupees, we can buy ?\frac{15}{3}? = ?5? = 5 chocolates.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    int T=1;
    cin >> T;
    while(T--){

        int x,y;
        cin>>x>>y;

        cout<<x/y<<'\n';
    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
``

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x, y;
	    cin>>x>>y;
	    cout<<(x/y)<<endl;
	}
	return 0;
}
``

</details>
