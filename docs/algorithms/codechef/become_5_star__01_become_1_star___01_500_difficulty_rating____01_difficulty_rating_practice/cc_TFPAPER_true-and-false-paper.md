# True and False Paper

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TFPAPER |
| Difficulty Rating | 398 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TFPAPER](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TFPAPER) |

---

## Problem Statement

Alice wrote an exam containing $N$ true or false questions (i.e. questions whose answer is either true or false). Each question is worth $1$ mark and there is no negative marking in the examination. Alice scored $K$ marks out of $N$.

Bob wrote the same exam but he marked each and every question as the opposite of what Alice did, i.e, for whichever questions Alice marked `true`, Bob marked `false` and for whichever questions Alice marked `false`, Bob marked `true`.

Determine the score of Bob.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $N$ and $K$ — the total number of questions in the exam and the score of Alice.

---

## Output Format

For each test case, output on a new line the score of Bob.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \le N \le 100$
- $0 \le K \le N$

---

## Examples

**Example 1**

**Input**

```text
3
1 1
50 0
100 76
```

**Output**

```text
0
50
24
```

**Explanation**

**Test case $1$:** There was one question in the exam and Alice answered it correctly. This means that Bob will surely answer it incorrectly. Therefore Bob's score is zero.

**Test case $2$:** Alice answered all the questions incorrectly, and so Bob will surely answer all the questions correctly. Therefore Bob's score is $50$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
50 0
```

**Output for this case**

```text
50
```



#### Test case 3

**Input for this case**

```text
100 76
```

**Output for this case**

```text
24
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/TFPAPER)

**Setter:** [utkarsh_adm](https://www.codechef.com/users/utkarsh_adm)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

398

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice wrote an exam containing N true or false questions, each worth 1 mark and there is no negative marking in the examination. Bob wrote the same exam but he marked each and every question as the opposite of what Alice did. Our objective is to determine Bob’s score.

#
[](#explanation-5)EXPLANATION:

Given Alice has scored K marks and each question has 1 mark. Thus the total number of questions Alice attended is K.

Also, Bob has has marked answers opposite of what Alice has marked. Which means for all the questions which Alice marked correct, Bob has marked it incorrect  and vice versa.

Now, to find Bob’s score we just need to calculate how many questions were incorrect in Alice’s response.

Thus (N-K) will be Bob’s score

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
	    int n,k;
	    cin>>n>>k;
	    cout<<n-k<<"\n";
	}
``

</details>
