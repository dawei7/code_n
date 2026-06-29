# Dazzling Even-Odd Challenge

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EANDO |
| Difficulty Rating | 1817 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [EANDO](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/EANDO) |

---

## Problem Statement

Dazzler has an interesting task for you.

You will be given an array $A$ of $N$ positive integers such that:
- $N$ is always **even**.
- Exactly $\frac{N}{2}$ elements in the array are **even** and $\frac{N}{2}$ elements are **odd**.

In one operation, you should do the following steps:
- Choose two different indices $i$ and $j$  $(1 \le i,j \le N)$.
- Set $A_i := A_i + 1$.
- Set $A_j := A_j - 1$.

You need to apply some finite (possibly zero) number of operations on the array such that:
- The [parity](https://en.wikipedia.org/wiki/Parity_(mathematics)) of the final element at each index is same as the parity of the initial element at that index. For example, if the $i^{th}$ element in the initial array is even, then, the $i^{th}$ element in the final array must be even as well.
- All the $\frac{N}{2}$ odd elements in the final array are equal.
- All the $\frac{N}{2}$ even elements in the final array are equal.

Print `YES` if it is possible to meet all the above conditions after doing some finite (possibly zero) number of operations. Otherwise, print `NO`.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains $N$, number of elements in the array $A$. Note that, $N$ is even.
- Second line of each test case contains $N$ space-separated positive integers, the elements of the array.

---

## Output Format

For each test case, output in a single line, `YES` if it is possible to meet all the given conditions after doing some finite (possibly zero) number of operations. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `yEs`, `yes` and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 2\cdot 10^5$
- $1 \leq A[i] \leq 10^9$
- $N \% 2 = 0$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 1 2 4
4
1 2 5 6
2
1 2
4
1 2 3 4
```

**Output**

```text
NO
YES
YES
YES
```

**Explanation**

**Test case $1$:** It is not possible to satisfy all the given conditions using any number of operations.

**Test case $2$:** One of the possible sequence of operations is listed below:
- In the first operation, choose $i=2$ and $j=4$. Thus, $A_2 = 2+1=3$ and $A_4 = 6-1=5$. The array will become $[1,3,5,5]$.
- In the second operation, choose $i=2$ and $j=4$. Thus, $A_2 = 3+1=4$ and $A_4 = 5-1=4$. The array will become $[1,4,5,4]$.
- In the third operation, choose $i=1$ and $j=3$. Thus, $A_1 = 1+1=2$ and $A_3 = 5-1=4$. The array will become $[2,4,4,4]$.
- In the fourth operation, choose $i=1$ and $j=3$. Thus, $A_1 = 2+1=3$ and $A_3 = 4-1=3$. The array will become $[3,4,3,4]$.

Here, all the odd elements are equal and all the even elements are equal. Also, the parity at each index is preserved.

**Test case $3$:** The array $[1,2]$ satisfies all the conditions. Thus, $0$ operations are needed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 2 4
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4
1 2 5 6
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4
1 2 3 4
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

[Contest Division 1](https://www.codechef.com/START37A/problems/EANDO)

[Contest Division 2](https://www.codechef.com/START37B/problems/EANDO)

[Contest Division 3](https://www.codechef.com/START37C/problems/EANDO)

[Contest Division 4](https://www.codechef.com/START37D/problems/EANDO)

Setter: [Sandeep V](https://www.codechef.com/users/dazlersan1)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1817

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Dazzler has an interesting task for you.

You will be given an array A of N positive integers. N is always even.

Exactly N/2 elements in the array will be Even and N/2 elements will be Odd.

In one operation you should do the following steps:

- Choose two different indices i  (1 \le i \le N)  and j (1 \le j \le N)

- Make A[i] = A[i] + 1

- Make A[j] = A[j] - 1

After doing all the necessary number of operations (possibly none) you need to preserve the parity of each element as in the initial array A. For example if an element at the index i (1 \le i \le N) is even, at the end A[i] should be even

You need to find whether you can make all the odd elements in the array equal and all the even elements equal separately.

Print **YES** if it is possible to meet the above conditions after doing any number of operations, else print **NO**.

#
[](#explanation-5)EXPLANATION:

First thing to observe is that, since we can select any i and j and change A[i] = A[i] + 1 and A[j] = A[j] - 1, so we can essentially change the array to any other array A' as long as it holds the condition \sum_{i=1}^{i=n} A'[i] = sum, where sum = \sum_{i=1}^{i=n} A[i]

Now we want the final array A' to be such that N/2 of its elements are even, say 2X and rest N/2 elements to be odd, say (2Y + 1). Thus

sum = \frac{N}{2} \times (2X + 2Y + 1)

If we subtract \frac{N}{2} from sum, we would have:

sum - \frac{N}{2} = N \times (X + Y)

Thus for such X and Y to exist, (sum - \frac{N}{2}) would have to be divisible by N.

Thus if (sum - \frac{N}{2}) is divisible by N then it is possible, otherwise its not possible.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/-GrL)

[Setter’s Solution](http://p.ip.fi/50Wd)

[Tester1’s Solution](http://p.ip.fi/E3hZ)

[Tester2’s Solution](http://p.ip.fi/SCSR)

</details>
