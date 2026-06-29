# Chef and Subset Additions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSTADD |
| Difficulty Rating | 1263 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SUBSTADD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SUBSTADD) |

---

## Problem Statement

Chef is asked to write a program that takes an array $A$ of length $N$ and two integers $X, Y$ as input and modifies it as follows:

- Choose a random subset of elements of $A$ (possibly empty)
- Increase all the elements of the chosen subset by $X$
- Increase the remaining elements in $A$ by $Y$

You are given $N$, $X$, $Y$, $A$ and the array $B$ that is returned by Chef's program. Determine whether Chef's program gave the correct output.

---

## Input Format

- The first line contains an integer $T$, the number of testcases. The description of the $T$ testcases follow.
- Each testcase contains $3$ lines.
- The first line of each testcase contains a three space separated integers $N, X, Y$ respectively.
- The second line of each testcase contains $N$ space separate integers, the elements of the array $A$.
- The third line of each testcase contains $N$ space separate integers, the elements of the array $B$.

---

## Output Format

- For each testcase, print in a single line either `yes` or `no`, according to whether Chef's program gave a valid output or not.
- You may output the answers in any case, for example the words `Yes`, `YeS`, `YES`, `yES` are all considered equivalent to `yes`.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 1000$
- $0 \leq X, Y \leq 1000$
- $0 \leq A_i \leq B_i \leq 1000$ for all indices $i$

---

## Examples

**Example 1**

**Input**

```text
3
3 2 5
9 5 1
11 10 3
3 2 5
9 5 1
11 7 3
3 2 5
9 5 1
11 7 7
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Test Case 1:** The array $A$ is $\{9, 5, 1\}$. If the chosen elements are $9, 1$ then the expected output would be $\{11, 10, 3\}$, so the answer is `yes`.

**Test Case 2:** The array $A$ is $\{9, 5, 1\}$. If the chosen elements are $9, 5, 1$ then the expected output would be $\{11, 7, 3\}$, so the answer is `yes`.

**Test Case 3:** The array $A$ is $\{9, 5, 1\}$. There is no subset that can be chosen so that the expected output would be $\{11, 7, 7\}$, so Chef's implementation must be incorrect and the answer is `no`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 5
9 5 1
11 10 3
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3 2 5
9 5 1
11 7 3
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
3 2 5
9 5 1
11 7 7
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

[Division 3](https://www.codechef.com/LTIME104C/problems/SUBSTADD)

[Practice](https://www.codechef.com/problems/SUBSTADD)

***Author:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Srikkanth R.](https://www.codechef.com/users/srikkanth_adm)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

Loops, Arrays, Logical Operators

#
[](#problem-4)PROBLEM:

You are given two arrays A and B and two integers X and Y. Determine if there exists a subset of indices of A so that B can be obtained by

- Increasing the values of chosen indices by X

- Increasing the remaining values by Y

#
[](#explanation-5)EXPLANATION:

Suppose the random subset chosen to convert A to B was S. Consider an index i.

- If the index i was present in S then B[i] must be equal to A[i] + X.

- If the index i was not present in S then B[i] must be equal to A[i] + Y.

Therefore we can iterate through the indices and figure out the subset S by simply looking at the values of A[i], B[i]. If we encounter an index i such that B[i] is neither equivalent to A[i] + X nor A[i] + Y, then such an S clearly does not exist and the answer is `No`, otherwise the answer is `Yes`.

The pseudocode is shown below:

``string answer = "Yes"; // Initialise the answer to "Yes"
for (i=0;i<n;++i) { // Iterate through elements of the array (0 based index)
    if (A[i] != B[i] + X && A[i] != B[i] + Y) {
        answer = "No"; // Set the answer to "No"
        break; // Once the answer is found to be "No", we can break out of the loop, this line is optional as it prevents unnecessary comparisons but does not reduce worst case complexity
    }
}
cout << answer << '\n' // Print the answer and move to next line
``

The time complexity of the solution is O(n) as we perform a single linear scan of the arrays A and B.

</details>
