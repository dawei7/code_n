# Best of Two

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BESTOFTWO |
| Difficulty Rating | 284 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BESTOFTWO](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BESTOFTWO) |

---

## Problem Statement

Chef took an examination two times. In the first attempt, he scored $X$ marks while in the second attempt he scored $Y$ marks. According to the rules of the examination, the best score out of the two attempts will be considered as the final score.

Determine the final score of the Chef.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $X$ and $Y$ — the marks scored by Chef in the first attempt and second attempt respectively.

---

## Output Format

For each test case, output the final score of Chef in the examination.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \le X, Y \le 100$

---

## Examples

**Example 1**

**Input**

```text
4
40 60
67 55
50 50
1 100
```

**Output**

```text
60
67
50
100
```

**Explanation**

**Test Case 1:** The best score out of the two attempts is $60$.

**Test Case 2:** The best score out of the two attempts is $67$.

**Test Case 3:** The best score out of the two attempts is $50$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
40 60
```

**Output for this case**

```text
60
```



#### Test case 2

**Input for this case**

```text
67 55
```

**Output for this case**

```text
67
```



#### Test case 3

**Input for this case**

```text
50 50
```

**Output for this case**

```text
50
```



#### Test case 4

**Input for this case**

```text
1 100
```

**Output for this case**

```text
100
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START45A/problems/BESTOFTWO)

[Contest Division 2](https://www.codechef.com/START45B/problems/BESTOFTWO)

[Contest Division 3](https://www.codechef.com/START45C/problems/BESTOFTWO)

[Contest Division 4](https://www.codechef.com/START45D/problems/BESTOFTWO)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

284

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef scored X and Y marks in an examination in the first attempt and the second attempt respectively. As per the rule, the final score will be the best of the two attempts.

What is the Chef’s final score?

#
[](#explanation-5)EXPLANATION:

This is an implementation problem. The objective is just to check your ability to accept inputs and print an output. We just need to compare the values of X and Y and output the maximum value as Chef’s final score.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
cin>>t;
while(t--)
 {
    int x,y;
   cin>>x>>y;
   if(x>y)
  cout<<x<<"\n";
  else
  cout<<y<<"\n";
}

	return 0;
}

``

</details>
