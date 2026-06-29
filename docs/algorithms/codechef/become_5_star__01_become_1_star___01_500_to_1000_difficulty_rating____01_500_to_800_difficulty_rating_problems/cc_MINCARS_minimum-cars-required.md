# Minimum Cars required

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINCARS |
| Difficulty Rating | 608 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MINCARS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINCARS) |

---

## Problem Statement

A single car can accommodate at most $4$ people.

$N$ friends want to go to a restaurant for a party. Find the **minimum** number of cars required to accommodate all the friends.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - denoting the number of friends.

---

## Output Format

For each test case, output the minimum number of cars required to accommodate all the friends.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
4
2
7
98
```

**Output**

```text
1
1
2
25
```

**Explanation**

**Test Case $1$:** There are only $4$ friends and a single car can accommodate $4$ people. Thus, only $1$ car is required.

**Test Case $2$:** There are only $2$ friends and a single car can accommodate $4$ people. Thus, only $1$ car is required

**Test Case $3$:** There are $7$ friends and $2$ cars can accommodate $8$ people. Thus, $2$ cars are required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
7
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
98
```

**Output for this case**

```text
25
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START33A/problems/MINCARS)

[Contest Division 2](https://www.codechef.com/START33B/problems/MINCARS)

[Contest Division 3](https://www.codechef.com/START33C/problems/MINCARS)

[Contest Division 4](https://www.codechef.com/START33D/problems/MINCARS)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A single car can accommodate at most 4 people.

N friends want to go to a restaurant for a party. Find the **minimum** number of cars required to accommodate all the friends.

#
[](#explanation-5)EXPLANATION:

For each test case, we are given the number of friends going to the party.

Given 4 friends can use 1 car. Using this logic we can deduce that for N friends the minimum cars required will be:

- 1, if N \le 4

-
(N/4), if N %  4=0

-
(N/4) + 1, if N %  4>0

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    if(n<=4)
	    cout<<"1"<<"\n";
	   else if(n%4==0)
	    cout<<n/4<<"\n";
	    else if(n%4>0)
	    cout<<(n/4)+1<<"\n";

	}
``

[Setter’s Solution](https://p.ip.fi/sh4F)

[Tester-1’s Solution]

[Tester-2’s Solution](http://p.ip.fi/K_mM)

</details>
