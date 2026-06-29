# The One Who Knocks!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EOOPR |
| Difficulty Rating | 1749 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [EOOPR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/EOOPR) |

---

## Problem Statement

*“I am not in danger, Skyler. I am the danger. A guy opens his door and gets shot, and you think that of me? No! I am the one who knocks!”*

Skyler fears Walter and ponders escaping to Colorado. Walter wants to clean his lab as soon as possible and then go back home to his wife.

In order clean his lab, he has to achieve cleaning level of lab as $Y$. The current cleaning level of the lab is $X$.

He must choose one positive **odd** integer $a$ and one positive **even** integer $b$. Note that, he cannot change $a$ or $b$ once he starts cleaning.

He can perform any one of the following operations for one round of cleaning:
  1. Replace $X$ with $X+a$.
  2. Replace $X$ with $X-b$.

Find minimum number of rounds (possibly zero) to make lab clean.

###Input:

- First line will contain $T$, number of test cases. $T$ testcases follow :
- Each test case contains two space separated integers $X, Y$.

###Output:
For each test case, output an integer denoting minimum number of rounds to clean the lab.
###Constraints
- $1 \leq T \leq 10^5$
- $ |X|,|Y| \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
0 5
4 -5
0 10000001
```

**Output**

```text
1
2
1
```

**Explanation**

- For the first testcase, you can convert $X$ to $Y$  by choosing $a=5$ and $b=2$.
It will cost minimum of $1$ cleaning round. You can select any other combination of $a, b$ satisfying above condition but will take minimum of $1$ cleaning round in any case.

- For the second testcase, you can convert $X$ to $Y$ by choosing $a=1$ and $b=10$. In first round they will replace $X$ to $X+a$ and then in second round replace to $X-b$. You can perform only one operation in one round.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 -5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
0 10000001
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem : [The One Who Knocks!](https://www.codechef.com/INFY20B/problems/EOOPR)

**Setter:** [Aman Singhal](https://www.codechef.com/users/aman1108)

**Tester:** [Yashodhan Agnihotri](https://www.codechef.com/users/zappelectro)

**Editorialist:** [Aman Singhal](https://www.codechef.com/users/aman1108)

## DIFFICULTY:

Cakewalk

## PREREQUISITES:

Basic Programming, Ad-hoc

## PROBLEM:

You are given two values X and Y. You have to choose one positive odd integer ‘a’ and one positive even integer ‘b’. In one operation you can either add a to X or subtract b from X. You cannot change a and b once you start performing operations. You have to find the minimum number of operations to obtain Y from X.

## QUICK EXPLANATION:

- When X>Y, it will take 1 operation if the difference is even, else 2.

- When X<Y, it will take 1 operation when difference is odd, 2 when difference is even but not divisible by 4 else 3.

- When X=Y, it will take 0 operation.

## EXPLANATION:

There are 3 cases to be solved in this question:

#### Case 1: When X>Y

Tap to view

- In this case we have to decrease the value of X. We can only subtract the even value. So, if the difference is even then in one round we can reach Y .

          X-b=Y

- Now for odd differences, the observation here is that the difference of an even and odd number is always odd. So we can add any odd number and now subtract the difference as it will be an even number.

           X+a-b=Y

#### Case 2: When X<Y

Tap to view

-

In this case we have to increase the value of X. We can add the odd value. So, if our difference is odd then in one round we can reach Y.

           X+a= Y

-

When our difference is even then we have to perform at least two operations. We can add the odd number twice as the sum of two odd numbers will give an even number but this even number will not be divisible by 4. In such cases where our difference is even and not divisible by 4 it will take 2 operations.

          X+a+a = Y

-

Now our last case, when we have difference as even and divisible by 4, we can achieve Y by adding two odd numbers giving sum greater than difference and then subtract the even number in order to achieve Y. In this case it will take 3 operations.

          X+a+a-b = Y

#### Case 3: When X=Y

Tap to view

- In this case we don’t need to perform any operation.

          X=Y

## TIME COMPLEXITY:

- Time complexity per test case is O(1).

## SOLUTIONS

Setter’s Solution (Python 3)
``T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    diff=abs(X-Y)
    if(X>Y):
        if (diff%2==0):
            ans=1
        else:
            ans=2

    elif (X<Y):
        if (diff%2!=0):
            ans=1

        elif (diff%4==0):
            ans=3

        else:
            ans=2

    else:
        ans=0

    print(ans)

``

Tester’s Solution (C++)
``#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define zapp ios::sync_with_stdio(false);cin.tie(0)

int main()
{
	zapp;
	ll t;
	cin >> t;
	while (t--)
	{
		ll x, y;
		cin >> x >> y;
		ll moves = 0;
		if (x > y) {
			ll diff = x - y;
			if (diff % 2 == 0)
				moves = 1;
			else
				moves = 2;
		}
		else if (x < y) {
			ll diff = y - x;
			if (diff % 2)
				moves = 1;
			else if (diff % 2 == 0 && (diff / 2) % 2)
				moves = 2;
			else
				moves = 3;
		}
		cout << moves << "\n";
	}
	return 0;
}

``

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
