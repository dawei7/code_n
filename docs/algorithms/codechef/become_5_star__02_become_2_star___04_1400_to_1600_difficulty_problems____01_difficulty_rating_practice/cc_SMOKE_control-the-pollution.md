# Control the Pollution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMOKE |
| Difficulty Rating | 1450 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [SMOKE](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/SMOKE) |

---

## Problem Statement

There are two types of vehicles in Chefland.
- **Bus** which has a capacity of $100$ people.
- **Car** which has a capacity of $4$ people.

There are $N$ people who want to travel from place $A$ to place $B$. You know that a single bus emits $X$ units of smoke while a single car emits $Y$ units of smoke in their journey from $A$ to $B$.

You want to arrange some buses and cars to carry all these $N$ people such that total smoke emitted is minimized. Output the minimized smoke value.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains three integers $N$, $X$, $Y$ - the number of people who want to travel, the units of smoke emitted by a bus and the units of smoke emitted by a car respectively.

---

## Output Format

For each test case, output the minimum units of smoke emitted in transporting the $N$ people.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq X, Y \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
9 40 8
15 20 20
105 80 10
```

**Output**

```text
24
20
100
```

**Explanation**

**Test case-1:** In the optimal case, we will use $3$ cars where the $1$-st and $2$-nd car will carry $4$ people each and the $3$-rd car will carry $1$ person.

Therefore smoke emitted $= 3 \times 8 = 24$ units.

**Test case-2:** In the optimal case, we will use $1$ bus to carry all the $15$ people.

Therefore smoke emitted $= 1 \times 20 = 20$ units.

**Test case-3:** In the optimal case, we will use $1$ bus to carry $100$ people and use $2$ cars to carry the remaining $5$ people.

Therefore smoke emitted $= 1 \times 80 + 2 \times 10 = 100$ units.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9 40 8
```

**Output for this case**

```text
24
```



#### Test case 2

**Input for this case**

```text
15 20 20
```

**Output for this case**

```text
20
```



#### Test case 3

**Input for this case**

```text
105 80 10
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

[Contest Division 1](https://www.codechef.com/START26A/problems/SMOKE)

[Contest Division 2](https://www.codechef.com/START26B/problems/SMOKE)

[Contest Division 3](https://www.codechef.com/START26C/problems/SMOKE)

[Contest Division 4](https://www.codechef.com/START26D/problems/SMOKE)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are two types of vehicles in Chefland.

-
**Bus** has a capacity of 100 people.

-
**Car** has a capacity of 4 people.

There are N people who want to travel. You know that a single bus emits X units of smoke while a single car emits Y units of smoke.

You want to arrange some buses and cars to carry all these N people such that total smoke emitted is minimised. Output the minimised smoke value.

#
[](#explanation-5)EXPLANATION:

Consider a batch of 100 people.

If we arrange buses for them, we would require only 1 bus and the total smoke emitted would be X units.

On the other hand, if all of them travel by car, we would need \frac{100}{4} = 25 cars. The total smoke emitted by cars would be 25 \cdot Y units.

It is optimal to use a bus for all these people only if X \leq 25 \cdot Y. Else, we use a car.

The total smoke emitted for the commute of these 100 people is min(X, 25 \cdot Y).

Note that for this batch 100 people, it is never optimal to use both the vehicles.

Why?

Let us assume we use 1 bus and C cars (C>0) for these 100 people. Note that using more than one bus would never be optimal as 1 bus has a capacity of 100 people.

Now, the total smoke emitted would be X + C\cdot Y. Since X + C\cdot Y >X, it is better to use only the bus instead of both bus and car.

We divide all the people into batches of 100 and calculate the answer for each batch.

For the remaining N' people (N'<100), we require either 1 bus or C = ceil(\frac{N'}{4}) cars. Minimum smoke emitted for the commute of these N' people is min(X, C \cdot Y).

The total answer would be the sum of answers of all batches of 100 people and the answer for the batch of remaining people (which is less than 100).

#
[](#time-complexity-6)TIME COMPLEXITY:

If we calculate the answer for each batch of 100 people separately, the complexity would be O(\frac{N}{100}).

However since the answer for each batch of 100 people would be the same, we can calculate the answer in O(1) for each test case.

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;

	while(t--){
	    int n;
	    cin>>n;
	    int x, y;
	    cin>>x>>y;

	    int smoke = 0;
	    while(n>=100){
	        int busSmoke = x;
	        int carSmoke = 25*y;
	        smoke += min(busSmoke, carSmoke);
	        n -= 100;
	    }

	    if(n>0){
	        int cars = ceil(n/4.0);
	        int carSmoke = cars * y;
	        int busSmoke = x;
	        smoke += min(busSmoke, carSmoke);
	    }

	    cout<<smoke<<endl;
	}
	return 0;
}
``

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
    int T=1;
    cin >> T;
    while(T--){
        int n,x,y;
        cin>>n>>x>>y;

        int ans = 10*x;
        rep(i,10){
            ans = min(ans, i*x+((max(0,n-100*i)+3)/4)*y);
        }

        cout<<ans<<el;
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
	    int n;
	    cin>>n;
	    int x, y;
	    cin>>x>>y;

	    int smoke = 0;

	    //for batches of 100
	    int buses = n/100;
	    int cars = buses * 25;
	    int busSmoke = buses * x;
	    int carSmoke = cars * y;

	    smoke = min(busSmoke, carSmoke);

	    n = n%100;

	    //for all people left
	    if(n>0){
	        int cars = ceil(n/4.0);
	        int carSmoke = cars * y;
	        int busSmoke = x;
	        smoke += min(busSmoke, carSmoke);
	    }

	    cout<<smoke<<endl;
	}
	return 0;
}
``

</details>
