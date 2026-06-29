# Drumpf for President!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STUDVOTE |
| Difficulty Rating | 1205 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [STUDVOTE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/STUDVOTE) |

---

## Problem Statement

Donald Drumpf has spent the entire summer lobbying to gather votes for the upcoming student government election. At his University, there are a total of **N** students. Each student in the university casts a vote. The size of student government is determined by the number of students that get at least **K** votes.

Each person that receives at least **K** votes is given a post in the student government. The Dean noticed that every year, there are a few students who vote for themselves. He decided to add a rule to disqualify any such individuals who vote for themselves i.e they cannot be part of the student government.

You are given an array **A**, where **Ai** denotes the person who the **i**-th person voted for. Can you compute the size of the student government?

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

For each test case, first line consists of two space separated integers **N**, **K**.

Second line consists of **N** space separated integers denoting the array **A**,  where **i**-th integer denotes **Ai**.

### Output

For each test case, output a single line containing an integer corresponding to the size of the student government.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **K** ≤ **N**

- **1** ≤ **Ai** ≤ **N**

### Subtasks
**Subtask #1: (30 points)**

- **1** ≤ **N** ≤ **3**

**Subtask #2: (70 points)**

- **1** ≤ **N** ≤ **100**

---

## Examples

**Example 1**

**Input**

```text
2
3 2
2 1 2
2 1
1 2
```

**Output**

```text
1
0
```

**Explanation**

In **first test case**, there are **3** students. A student must receive at least **2**
votes to be part of the student government. Student **1** votes for student **2**, student **2** votes for student **1** and student **3** votes for student **2**. Thus, Student **2** receives **2** votes and is the only one eligible for student government.

In **second test case**, although both students receive the required amount of votes, they are both disqualified as they had voted for themselves. Thus, size of the student
government is **0**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
2 1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 1
1 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/STUDVOTE)

[Contest](http://www.codechef.com/LTIME38/problems/STUDVOTE)

**Author:** [Praveen Dhindhwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given is an array A, A[i] tells us which person from 1 to N did the person i vote for to be good. We need to count the number of good people depending on these votes. A person is good if he got at least K votes AND didn’t vote for himself/herself.

### EXPLANATION:

The problem is pretty straightforward for the given constraints. Since N \leq 100, we can keep an array Count to count the votes that each person got. After that, we just need to iterate over the array and check who all got at least K votes. If someone has got K votes or more, we check whether he/she voted for himself/herself or not. If not, then we can increase the count of good persons. Below is a pseudocode of the same:

``countGoodPeople(A[], N):
	for (i = 1 to N) {
		Count[A[i]] = Count[A[i]] + 1; // increase the vote for the person who i voted for.
	}

	CountGood = 0;
	for (i = 1 to N) {
		if(Count[i] >= K and A[i] != i) {
			CountGood = CountGood + 1;
		}
	}

	return CountGood;
``

Please see tester’s/setter’s program for implementation details.

### COMPLEXITY:

\mathcal{O}(N) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/LTIME38/Setter/STUDVOTE.cpp)

[Tester](http://www.codechef.com/download/Solutions/LTIME38/Tester/STUDVOTE.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/LTIME38/Editorialist/STUDVOTE.cpp)

</details>
