# Fill Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FILLCANDIES |
| Difficulty Rating | 681 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FILLCANDIES](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FILLCANDIES) |

---

## Problem Statement

Chef received $N$ candies on his birthday. He wants to put these candies in some bags. A bag has $K$ pockets and each pocket can hold at most $M$ candies. Find the **minimum** number of bags Chef needs so that he can put every candy into a bag.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing three space-separated integers $N, K, M$.

---

## Output Format

For each test case, print the minimum number of bags Chef needs so that he can put all the candies in one of the bags.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N, K, M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
6 2 3
3 1 2
8 4 1
25 4 2
```

**Output**

```text
1
2
2
4
```

**Explanation**

**Test case $1$:** Chef puts $3$ candies in the first pocket of a bag and the remaining $3$ candies in the second pocket. Thus Chef will need only one bag.

**Test case $2$:** Chef puts $2$ candies in the only pocket of the first bag and the remaining $1$ candy in the only pocket of the second bag. Thus Chef will need two bags.

**Test case $3$:** Chef puts $4$ candies in the first bag, one candy in each of the $4$ pockets and the same for the second bag. Thus Chef will need two bags.

**Test case $4$:** Chef puts $2$ candies in each of the $4$ pockets of three bags, one candy in a pocket of the fourth bag.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 2 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8 4 1
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
25 4 2
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START48/)

[Practice](https://www.codechef.com/problems/FILLCANDIES)

**Setter:** [soumyadeep_21](https://www.codechef.com/users/soumyadeep_21)

**Testers:** [tabr](https://www.codechef.com/users/tabr), [tejas10p](https://www.codechef.com/users/tejas10p)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

681

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

The objective is to find the **minimum** number of bags Chef needs so that he can put every candy into bags, where each bag has K pockets and each pocket can have a maximum of M candies.

#
[](#explanation-5)EXPLANATION:

Given each bag  has K pockets which can have maximum of M candies, the maximum number of candies that a bag can hold is K\times M.

Thus if:

-
N<(K\times M), the minimum number of bags required is 1.

*N%(K\times M)=0,the minimum number of bags required is  N \div (K\times M)

*N%(K\times M)>0,the minimum number of bags required is  [N  \div (K\times M) ]+1

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
	cin>>t;
	while(t--)
	{
	    int n,m,k;
	    cin>>n>>k>>m;
	    if(n<m*k)
	    cout<<"1"<<"\n";
	    else if(n%(k*m)==0)
	    cout<<n/(k*m)<<"\n";
	    else if(n%(k*m)>0)
	    cout<<(n/(k*m))+1<<"\n";
	}
``

</details>
