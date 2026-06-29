# Passes for Fair

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FAIRPASS |
| Difficulty Rating | 342 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FAIRPASS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FAIRPASS) |

---

## Problem Statement

There is a fair going on in Chefland. Chef wants to visit the fair along with his $N$ friends. Chef manages to collect $K$ passes for the fair. Will Chef be able to enter the fair with all his $N$ friends?

A person can enter the fair using one pass, and each pass can be used by only one person.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers $N, K$.

---

## Output Format

For each test case, print on a new line `YES` if Chef will be able to enter the fair with all his $N$ friends and `NO` otherwise.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, K \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
5 8
6 3
2 2
1 2
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** Chef needs $5$ passes for his friends and one pass for himself and he collected $8$ passes. Thus he will be able to enter the fair with all his friends.

**Test case $2$:** Chef needs $6$ passes for his friends and one pass for himself while he collected only $3$ passes. Thus he will not be able to enter the fair with all his friends, only three of them can enter the fair.

**Test case $3$:** Chef needs $2$ passes for his friends and one pass for himself while he collected only $2$ passes. Thus either Chef or one of his friends can't enter the fair.

**Test case $4$:** Chef needs a total of $2$ passes, one for himself and one for his friend. He collected $2$ passes. Thus he will be able to enter the fair with his friend.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 8
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
6 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 2
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
1 2
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

[Contest](https://www.codechef.com/START48/)

[Practice](https://www.codechef.com/problems/FAIRPASS)

**Setter:** [soumyadeep_21](https://www.codechef.com/users/soumyadeep_21)

**Testers:** [tabr](https://www.codechef.com/users/tabr), [tejas10p](https://www.codechef.com/users/tejas10p)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

342

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to visit the fair along with his N friends. Also Chef has got K passes. Given a person can enter the fair using one pass, we need to find out Will Chef be able to enter the fair with all his N friends.

#
[](#explanation-5)EXPLANATION:

Total number of people who wish to enter the fair is (N+1)  [ i.e. Chef + N friends ]

Given one person needs one pass to enter the fair, total number of passes required is to enter the fair is (N+1) .

Thus to check if  Chef will be able to enter the fair with all his N friends, Chef should collect passes  K>N

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``  cin >> t;
    while (t--)
    {
        int n,k;
        cin >> n>> k;

        if (n < k)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
``

</details>
