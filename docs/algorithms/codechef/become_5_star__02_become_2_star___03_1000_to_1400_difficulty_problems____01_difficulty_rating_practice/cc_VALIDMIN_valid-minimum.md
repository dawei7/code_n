# Valid Minimum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VALIDMIN |
| Difficulty Rating | 1132 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [VALIDMIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/VALIDMIN) |

---

## Problem Statement

There are $3$ hidden numbers $A, B, C$.

You somehow found out the values of $\min(A, B), \min(B, C),$ and $\min(C, A)$.

Determine whether there exists any tuple $(A, B, C)$ that satisfies the given values of $\min(A, B), \min(B, C), \min(C, A)$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $3$ space-separated integers denoting the values of $\min(A, B), \min(B, C),$ and $\min(C, A)$.

---

## Output Format

For each test case, output `YES` if there exists any valid tuple $(A, B, C)$, and `NO` otherwise.

You can print each letter of the output in any case. For example `YES`, `yes`, `yEs` will all be considered equivalent.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq min(A, B), min(B, C), min(C, A) \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
5 5 5
2 3 4
2 2 4
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** One valid tuple $(A, B, C)$ is $(5, 5, 5)$.

**Test case $2$:** It can be shown that there is no valid tuple $(A, B, C)$.

**Test case $3$:** One valid tuple $(A, B, C)$ is $(4, 2, 5)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 3 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 2 4
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START49/)

[Practice](https://www.codechef.com/problems/VALIDMIN)

**Setter:** [abhi_inav](https://www.codechef.com/users/abhi_inav)

**Testers:** [iceknight1093 ](https://www.codechef.com/users/iceknight1093), [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

1132

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are 3 hidden numbers A, B , C

Given the values of min(A, B), min(B, C), min(C,A). Determine whether there exists any tuple (A, B, C) that satisfies the given values of min(A, B), min(B, C), min(C, A).

#
[](#explanation-5)EXPLANATION:

Read the inputs to an array and sort them.

Let the sorted elements be a[0],  a[1] and a[2].

If a[0]=a[1] , output YES else NO.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``int t;
	cin >> t;
	while(t--)
	{
	    int a[3];
	    for(int i=0;i<3;i++)
	    {
	        cin>>a[i];
	    }

	    sort(a, a + 3);
	    if(a[0] == a[1])
	    cout << "YES"<<"\n";

	    else cout << "NO"<<"\n";

	}
``

</details>
