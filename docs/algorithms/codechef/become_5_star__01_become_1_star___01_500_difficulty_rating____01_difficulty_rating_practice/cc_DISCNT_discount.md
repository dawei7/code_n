# Discount

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISCNT |
| Difficulty Rating | 401 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DISCNT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DISCNT) |

---

## Problem Statement

Alice buys a toy with a selling price of $100$ rupees. There is a discount of $x$ percent on the toy. Find the amount Alice needs to pay for it.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer, $x$ — the discount on the toy.

---

## Output Format

For each test case, output on a new line the price that Alice needs to pay.

---

## Constraints

- $1 \leq T \leq 100$
- $0 \leq x \lt 100$

---

## Examples

**Example 1**

**Input**

```text
4
5
9
11
21
```

**Output**

```text
95
91
89
79
```

**Explanation**

**Test case $1$:** The discount is $5$ percent, i.e. $5$ rupees. So, Alice will have to pay $100-5=95$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
95
```



#### Test case 2

**Input for this case**

```text
9
```

**Output for this case**

```text
91
```



#### Test case 3

**Input for this case**

```text
11
```

**Output for this case**

```text
89
```



#### Test case 4

**Input for this case**

```text
21
```

**Output for this case**

```text
79
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START50)

[Practice](https://www.codechef.com/problems/DISCNT)

**Setter:** [inov_adm](https://www.codechef.com/users/inov_adm)

**Testers:** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec), [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

401

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice buys a toy with a selling price of 100 rupees. There is a discount of x percent on the toy. Find the amount Alice needs to pay for it.

#
[](#explanation-5)EXPLANATION:

A discount of x percentage on 100 rupees corresponds to a discount of x rupees. So the amount needed to be paid is 100 - x.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int T,x;

int main() {

	cin>>T;

	while(T--)
	{
	    cin>>x;
	    cout<<100-x<<"\n";
	}
	return 0;
}
``

Tester's Solution
``for _ in range(int(input())):
	x = int(input())
	print(100-x)
``

</details>
