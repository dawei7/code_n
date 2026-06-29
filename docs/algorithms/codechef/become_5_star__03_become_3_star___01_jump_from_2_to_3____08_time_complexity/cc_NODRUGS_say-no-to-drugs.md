# Say No To Drugs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NODRUGS |
| Difficulty Rating | 1425 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [NODRUGS](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/NODRUGS) |

---

## Problem Statement

There are $N$ people participating in a race. The $N^{th}$ participant is your friend, so you want him to win. You are not a man of ethics, so you decided to inject some units of a Performance Enhancement Drug (don't ask where that came from) in your friend's body.

- From the charts, you came to know the speed of every player. Formally, for a player $i$, his speed is denoted by $S_i$.
- The change in speed with one unit of the drug is $K$ units. Note that $K$ can be negative, which means the drug has more side effects than benefits.
- Of course, there will be a drug test before the race, so your friend will be caught if the number of units of the drug in his blood is greater than or equal to $L$.

You need to determine whether you can help your friend to win the race (with or without drugs), without getting caught.

**Note:** A player wins the race if he has the maximum speed among all the participants. If there are more than one people with a maximal speed, they tie at first place, and **no one** wins!

---

## Input Format

- First line will contain a single integer $T$, the number of test cases. Description of the test cases follows.
- First line of each test case will contain three space-separated integers, $N$ - the number of participants, $K$ - the change in speed with one unit of the drug, and $L$ - minimum units of the drug that can be detected in the drug test.
- Second line of each test case will contain $N$ space-separated integers $S_i$, the speeds of the participants.

---

## Output Format

For each test case print "Yes" if you can help your friend to win the race, otherwise "No" in a single line.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N, L \leq 1000$
- $-1000 \le K \le 1000$
- $1 \leq S_i \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 2
2 1 3 2
4 2 2
2 1 4 2
3 -10 100
12 11 9
```

**Output**

```text
Yes
No
No
```

**Explanation**

- In test case $1$, initial speeds are $\{2, 1, 3, 2\}$. You can inject $1$ unit of the drug into your friend's body, and increase his speed from $2$ to $4$. $4$ is the fastest speed, thus you helped your friend win the race. Hence, the answer is "Yes".
- In test case $2$, initial speeds are $\{2, 1, 4, 2\}$. You can inject $1$ unit of the drug into your friend's body, and increase his speed from $2$ to $4$. But you can not inject any more units of the drug, and with speed $4$ your friend can only tie at rank $1$ and not Win. Hence, the answer is "No".
- In test case $3$, initial speeds are $\{12, 11, 9\}$. Note that the impact of the drug in this case is negative, which means that the speed will only decrease if you inject it. So, there is no way you can help your friend to win. Hence, the answer is "No".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 2
2 1 3 2
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
4 2 2
2 1 4 2
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
3 -10 100
12 11 9
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/CDMN21C/problems/NODRUGS)

[Contest - Division 2](https://www.codechef.com/CDMN21B/problems/NODRUGS)

[Contest - Division 1](https://www.codechef.com/CDMN21A/problems/NODRUGS)

Setter: [Arshdeep Singh](https://www.codechef.com/users/sedlif)

Tester: [Vichitr Gandas](https://www.codechef.com/users/vichitr), [Anshu Garg](https://www.codechef.com/users/anshugarg12)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Given an array S of size N, determine if it is possible to add integer K (may be negative) to S_N at most L-1 times, such that S_N is then greater than all other elements in S.

#
[](#explanation-4)EXPLANATION:

If K \lt 0, injecting the drug will reduce his speed; so it’s better to not inject the drug at all. In this case, your friend wins only if he is faster than everyone else  \implies S_N > S_i should hold for all valid i < N.

If K > 0, we can repeatedly inject the drug until the limit is reached (that is, we can inject the drug L-1 times), increasing his speed in each dose. If after this, your friend is faster than everyone else, he wins \implies S_N+K*(L-1) > S_i should hold for all valid i < N.

#
[](#time-complexity-5)TIME COMPLEXITY:

Since we iterate over array S once to determine the answer, the time complexity for each test case is:

O(N)

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/50524973)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
