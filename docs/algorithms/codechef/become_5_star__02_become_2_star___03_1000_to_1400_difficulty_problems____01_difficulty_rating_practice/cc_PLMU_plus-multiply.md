# Plus Multiply

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PLMU |
| Difficulty Rating | 1277 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [PLMU](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/PLMU) |

---

## Problem Statement

Chef has a sequence $A_1, A_2, \ldots, A_N$. He needs to find the number of pairs $(i, j)$ ($1 \le i \lt j \le N$) such that $A_i + A_j = A_i \cdot A_j$. However, he is busy, so he asks for your help.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the desired number of pairs.

### Constraints
- $1 \le T \le 20$
- $1 \le N \le 40,000$
- $0 \le A_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 500$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
2 4 2
3
0 2 3
```

**Output**

```text
1
0
```

**Explanation**

**Example case 1:** The only valid pair is $(1, 3)$.

**Example case 2:** We can see that no valid pair exists.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 4 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
0 2 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/PLMU)

[Contest, div. 1](https://www.codechef.com/DEC19A/problems/PLMU)

[Contest, div. 2](https://www.codechef.com/DEC19B/problems/PLMU)

**Author:** [Vivek Chauhan](http://www.codechef.com/users/vivek_1998299)

**Tester:** [Ildar Gainullin](http://www.codechef.com/users/gainullinildar)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

CAKEWALK

**PREREQUISITES**:

None

**PROBLEM**:

You’re given a sequence A_1, \dots, A_n. Find the number of pairs (i,j) such that A_i + A_j = A_i \cdot A_j.

**QUICK EXPLANATION**:

Keep an eye on twos and zeros.

**EXPLANATION**:

We may rewrite it as A_i=A_j(A_i-1), or A_j = \frac{A_i}{A_i-1}. Since A_j is integer it’s only possible when either A_i=A_j=2 or A_i=A_j=0, so we just have to calculate amount of occurences of 0's and 2's in the sequence.

``void solve() {
	int n;
	cin >> n;
	map<int, int> cnt;
	for(int i = 0; i < n; i++) {
		int ai;
		cin >> ai;
		cnt[ai]++;
	}
	cout << cnt[0] * (cnt[0] - 1) / 2 + cnt[2] * (cnt[2] - 1) / 2 << endl;
}
``

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Tester’s solution can be found [here](https://ideone.com/zZPdeo).

Editorialist’s solution can be found [here](https://ideone.com/Fgcn8U).

</details>
