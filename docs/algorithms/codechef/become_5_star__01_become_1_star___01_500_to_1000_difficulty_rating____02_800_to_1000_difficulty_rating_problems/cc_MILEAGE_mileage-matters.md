# Mileage matters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MILEAGE |
| Difficulty Rating | 831 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [MILEAGE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/MILEAGE) |

---

## Problem Statement

Chef wants to rent a car to travel to his restaurant which is $N$ kilometers away. He can either rent a petrol car or a diesel car.

One litre of petrol costs $X$ rupees and one litre of diesel costs $Y$ rupees. Chef can travel $A$ kilometers with one litre of petrol and $B$ kilometers with one litre of diesel.

Chef can buy petrol and diesel in any amount, not necessarily integer. For example, if $X = 95$, Chef can buy half a litre of petrol by paying $95/2 = 47.5$ rupees.

Which car should the chef rent in order to **minimize** the cost of his travel?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $5$ space-separated integers, $N, X, Y, A,$ and $B$ - distance that chef needs to travel, the per litre prices of petrol and diesel and the distance chef can travel using one litre of petrol and diesel respectively.

---

## Output Format

For each test case, output on a new line `PETROL` if the cost of travel is less using petrol car, `DIESEL` if the cost of travel is less using diesel car or `ANY` if cost of travel is same in both the cases.

You may print each character of the string in either uppercase or lowercase (for example, the strings `PETrol`, `petrol`, `Petrol`, and `PETROL` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,x,y,a,b \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
20 10 8 2 4
50 12 12 4 3
40 3 15 8 40
21 9 9 2 9
```

**Output**

```text
DIESEL
PETROL
ANY
DIESEL
```

**Explanation**

**Test case $1$:** The cost of travelling by the petrol car will be $100$ rupees while that of using the diesel car will be $40$ rupees. Hence, diesel car is better.

**Test case $2$:** The cost of travelling by the petrol car will be $150$ rupees while that of using the diesel car will be $200$ rupees. Hence, petrol car is better.

**Test case $3$:** The cost of travel for petrol and diesel car will be $15$ rupees.

**Test case $4$:** The cost of travelling by the petrol car will be $94.5$ rupees while that of using the diesel car will be $21$ rupees. Hence, diesel car is better.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20 10 8 2 4
```

**Output for this case**

```text
DIESEL
```



#### Test case 2

**Input for this case**

```text
50 12 12 4 3
```

**Output for this case**

```text
PETROL
```



#### Test case 3

**Input for this case**

```text
40 3 15 8 40
```

**Output for this case**

```text
ANY
```



#### Test case 4

**Input for this case**

```text
21 9 9 2 9
```

**Output for this case**

```text
DIESEL
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START50)

[Practice](https://www.codechef.com/problems/MILEAGE)

**Setter:** [inov_adm](https://www.codechef.com/users/inov_adm)

**Testers:** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec), [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

831

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given cost and mileage of petrol and diesel, find which is the cheaper option to travel N kms.

#
[](#explanation-5)EXPLANATION:

The cost incurred if you use the petrol car, is the cost of petrol times the amount of petrol used. Which is x * (n/a). Similarly, the cost of using the diesel car is the cost of diesel times the amount of diesel used. Which is y * (n/b). We just find which one of these is smaller, and output that. If they are equal, output “Any”.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
#include <cmath>
using namespace std;

int T,n,x,y,a,b;

int main() {
	cin>>T;

	while(T--)
	{
	    cin>>n>>x>>y>>a>>b;

	    double petrolCost = x * ( ((double)n)/a );
	    double dieselCost = y * ( ((double)n)/b );

	    if(petrolCost < dieselCost)
	        cout<<"Petrol\n";
	    else if(petrolCost > dieselCost)
	        cout<<"Diesel\n";
	    else
	        cout<<"Any\n";
	}
	return 0;
}

``

Tester's Solution
``for _ in range(int(input())):
	n, x, y, a, b = map(int, input().split())
	if x*b == y*a:
	    print('any')
	elif x*b < y*a:
	    print('petrol')
	else:
	    print('diesel')
``

</details>
