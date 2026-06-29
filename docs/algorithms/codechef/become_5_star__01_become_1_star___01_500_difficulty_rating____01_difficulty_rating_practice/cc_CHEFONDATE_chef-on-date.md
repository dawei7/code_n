# Chef On Date

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFONDATE |
| Difficulty Rating | 294 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CHEFONDATE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFONDATE) |

---

## Problem Statement

Chef and his girlfriend went on a date. Chef took $X$ dollars with him, and was quite sure that this would be enough to pay the bill. At the end, the waiter brought a bill of $Y$ dollars. Print `"YES"` if Chef has enough money to pay the bill, or `"NO"` if he has to borrow from his girlfriend and leave a bad impression on her.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing two space-separated integers $X$ and $Y$.

---

## Output Format

For each test case, output on a new line `"YES"` if Chef has enough money to pay the bill and `"NO"` otherwise.

You may print each character of the string in either uppercase or lowercase (for example, the strings `"yEs"`, `"yes"`, `"Yes"` and `"YES"` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1 2
2 1
50 100
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** Since the money Chef has is equal to the bill, he will be able to pay the bill.

**Test case $2$:** Since the money Chef has is less than the bill, he will have to borrow from his girlfriend and leave a bad impression on her.

**Test case $3$:** Since the money Chef has is greater than the bill, he will be able to pay the bill.

**Test case $4$:** Since the money Chef has is less than the bill, he will have to borrow from his girlfriend and leave a bad impression on her.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 1
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
50 100
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START47/)

[Practice](https://www.codechef.com/problems/CHEFONDATE)

Setter: [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

Tester: [ Abhinav Sharma](https://www.codechef.com/users/inov_360), [ Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Kiran](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

294

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef and his girlfriend is on a date. Chef has X dollars and the bill amount is of Y dollars. The objective is to find out if Chef has enough money to pay the bill

#
[](#explanation-5)EXPLANATION:

-

The objective of this problem is to input two distinct values, compare its values.

-

We input two distinct values to two variables X & Y (representing the money Chef has and the bill amount respectively).

-

Solution:

-

If X>Y, Chef has enough money to pay the bill -Print `"Yes"`

-

If  X<Y, Chef has to borrow from his girlfriend -Print `"No"`

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1)

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
	cin>>t;

for(int i=0;i<t;i++)
{
    int x,y;
    cin>>x>>y;
    if(y>x)
    cout<<"No"<<"\n";
    else
    cout<<"Yes"<<"\n";
}
``

</details>
