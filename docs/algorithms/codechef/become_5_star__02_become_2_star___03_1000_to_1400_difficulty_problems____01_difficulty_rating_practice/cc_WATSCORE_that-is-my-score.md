# That Is My Score!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATSCORE |
| Difficulty Rating | 1094 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [WATSCORE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/WATSCORE) |

---

## Problem Statement

You are participating in a contest which has $11$ problems (numbered $1$ through $11$). The first eight problems (i.e. problems $1, 2, \ldots, 8$) are *scorable*, while the last three problems ($9$, $10$ and $11$) are *non-scorable* ― this means that any submissions you make on any of these problems do not affect your total score.

Your total score is the sum of your best scores for all scorable problems. That is, for each scorable problem, you look at the scores of all submissions you made on that problem and take the maximum of these scores (or $0$ if you didn't make any submissions on that problem); the total score is the sum of the maximum scores you took.

You know the results of all submissions you made. Calculate your total score.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$ denoting the number of submissions you made.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains two space-separated integers $p_i$ and $s_i$, denoting that your $i$-th submission was on problem $p_i$ and it received a score $s_i$.

### Output
For each test case, print a single line containing one integer ― your total score.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 1,000$
- $1 \le p_i \le 11$ for each valid $i$
- $0 \le s_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (15 points):** all submissions are on the same problem, i.e. $p_1 = p_2 = \ldots = p_N$

**Subtask #2 (15 points):** there is at most one submission made on each problem, i.e. $p_i \neq p_j$ for each valid $i, j$ ($i \neq j$)

**Subtask #3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
5
2 45
9 100
8 0
2 15
8 90
1
11 1
```

**Output**

```text
135
0
```

**Explanation**

**Example case 1:** The scorable problems with at least one submission are problems $2$ and $8$. For problem $2$, there are two submissions and the maximum score among them is $45$. For problem $8$, there are also two submissions and the maximum score is $90$. Hence, the total score is $45 + 90 = 135$.

**Example case 2:** No scorable problem is attempted, so the total score is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
2 45
9 100
8 0
```

**Output for this case**

```text
135
```



#### Test case 2

**Input for this case**

```text
2 15
8 90
1
11 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/WATSCORE)

[Contest, div. 1](https://www.codechef.com/DEC19A/problems/WATSCORE)

[Contest, div. 2](https://www.codechef.com/DEC19B/problems/WATSCORE)

**Author:** [Abhishek Pandey](http://www.codechef.com/users/vijju123_adm)

**Tester:** [Ildar Gainullin](http://www.codechef.com/users/gainullinildar)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

CAKEWALK

**PREREQUISITES**:

None

**PROBLEM**:

You’re given N pairs of integers (p_i, s_i) where 1 \leq p_i \leq 11. For each p_i<9 calculate maximum number of s_i with this p_i and output the sum of these numbers.

**QUICK EXPLANATION**:

You should basically do what’s written in the statement.

**EXPLANATION**:

Maintain array mx with maximum scores for each problem and output the sum of first 9 elements.

``void solve() {
	int n;
	cin >> n;
	vector<int> mx(11);
	for(int i = 0; i < n; i++) {
		int p, s;
		cin >> p >> s;
		mx[p] = max(mx[p], s);
	}
	cout << accumulate(begin(mx), begin(mx) + 9, 0LL) << endl;
}
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/XgtjFs).

Tester’s solution can be found [here](https://ideone.com/dYfqbj).

Editorialist’s solution can be found [here](https://ideone.com/LW2Lur).

</details>
