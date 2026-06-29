# Pied Piper vs Hooli

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PEWDSVTS |
| Difficulty Rating | 1910 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [PEWDSVTS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/PEWDSVTS) |

---

## Problem Statement

Pied Piper is a startup company trying to build a new Internet called Pipernet. Currently, they have $A$ users and they gain $X$ users everyday. There is also another company called Hooli, which has currently $B$ users and gains $Y$ users everyday.

Whichever company reaches $Z$ users first takes over Pipernet. In case both companies reach $Z$ users on the same day, Hooli takes over.

Hooli is a very evil company (like E-Corp in Mr. Robot or Innovative Online Industries in Ready Player One). Therefore, many people are trying to help Pied Piper gain some users.

Pied Piper has $N$ *supporters* with contribution values $C_1, C_2, \ldots, C_N$. For each valid $i$, when the $i$-th supporter *contributes*, Pied Piper gains $C_i$ users instantly. After contributing, the contribution value of the supporter is halved, i.e. $C_i$ changes to $\left\lfloor C_i / 2 \right\rfloor$. Each supporter may contribute any number of times, including zero. Supporters may contribute at any time until one of the companies takes over Pipernet, even during the current day.

Find the minimum number of times supporters must contribute (the minimum total number of contributions) so that Pied Piper gains control of Pipernet.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains six space-separated integers $N$, $A$, $B$, $X$, $Y$ and $Z$.
- The second line contains $N$ space-separated integers $C_1, C_2, \ldots, C_N$ — the initial contribution values.

### Output
For each test case, if Hooli will always gain control of Pipernet, print a single line containing the string `"RIP"` (without quotes). Otherwise, print a single line containing one integer — the minimum number of times supporters must contribute.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le A, B, X, Y, Z \le 10^9$
- $A, B \lt Z$
- $0 \le C_i \le 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
3
3 10 15 5 10 100
12 15 18
3 10 15 5 10 100
5 5 10
4 40 80 30 30 100
100 100 100 100
```

**Output**

```text
4
RIP
1
```

**Explanation**

**Example case 1:** After $8$ days, Pied Piper will have $50$ users and Hooli will have $95$ users. Then, if each supporter contributes once, Pied Piper will also have $95$ users. After that, they still need $5$ more users, so supporter $3$ can contribute again, with $18/2 = 9$ more users. So the answer will be $4$.

**Example case 2:** There is no way to beat Hooli.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 10 15 5 10 100
12 15 18
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 10 15 5 10 100
5 5 10
```

**Output for this case**

```text
RIP
```



#### Test case 3

**Input for this case**

```text
4 40 80 30 30 100
100 100 100 100
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/PEWDSVTS)

[Contest, div. 1](https://www.codechef.com/COOK105A/problems/PEWDSVTS)

[Contest, div. 2](https://www.codechef.com/COOK105B/problems/PEWDSVTS)

**Author:** [Udit Sanghi](http://www.codechef.com/users/mathecodician)

**Tester:** [Teja Vardhan Reddy](http://www.codechef.com/users/teja349)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

SIMPLE

**PREREQUISITES**:

Priority queue

**PROBLEM**:

Pied Piper has A users and gain X users everyday. Meanwhile Hooli has B users and gain Y users everyday. Whichever company reaches Z users first takes over Pipernet.

Pied Piper has N supporters with contribution values C_1, \dots, C_N. When i-th supporter contributes, Pied Piper get C_i users instantly. After this C_i is halved, thus it’s going to be equal to \lfloor C_i / 2 \rfloor. What is the minimum number of times supporters must contribute?

**EXPLANATION**:

It’s always profitable to make all contributions on the first day and contribute only largest possible numbers at every moment of time. To do this you may, keep a current set C_1, \dots, C_N in priority queue and pick the largest one all the time returning half of it to the queue.

How to check if Pied Piper loses to Hooli? You have to find minimum integer T_1 such that A+XT_1 \geq Z and minimum integer T_2 such that B+YT_2 \geq Z and compare them. It holds that:

T_1 = \left\lceil \dfrac{Z-A}{X}\right\rceil, T_2 = \left\lceil \dfrac{Z-B}{Y}\right\rceil

Thus this check is done in the following code:

``bool lose(int A, int X, int B, int Y, int Z) {
	int t1 = (Z - A + X - 1) / X;
	int t2 = (Z - B + Y - 1) / Y;
	return t1 >= t2;
}
``

Work with priority queue is quite straight-forward and looks like this afterwards:

``priority_queue<int> C = {C_1, ..., C_N};
while(C.top() != 0 && lose(A, X, B, Y, Z)) {
	ans++;
	A += C.top();
	C.push(C.top() / 2);
	C.pop();
}
if(lose(A, X, B, Y, Z)) {
	cout << "RIP" << endl;
} else {
	cout << ans << endl;
}
``

This solution works in O(N \log N \log C). Note that multiset wouldn’t do here due to higher constant, as well as full sorting of all possible values. But it’s possible to solve the problem in O(N \log C) using radix sort, which is a bit more complicated.

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/m8Ts8K).

Tester’s solution can be found [here](https://ideone.com/Optk34).

Editorialist’s solution can be found [here](https://ideone.com/VnMg0X).

</details>
