# Jump to Sibling

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JS |
| Difficulty Rating | 1888 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [JS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/JS) |

---

## Problem Statement

Lav has an array $A$ of size $N$. He noticed that Chef is initially standing at the **first** index of the array.

While standing at the $i^{th}$ index $(1 \leq i \lt N)$ of the array, Chef can perform the following types of jumps:
- $\texttt{Jump 1}$: Jump to the immediate next index $j$ such that $A_i$ and $A_j$ have the **same** [parity](https://en.wikipedia.org/wiki/Parity_(mathematics)).
- $\texttt{Jump 2}$: Jump to the immediate next index $j$ such that $A_i$ and $A_j$ have **different** parity.

Given that Chef can perform $\texttt{Jump 2}$ **at most once**, Lav wants to find the **minimum** number of jumps required by the Chef to reach the **last** index of the array.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ integers $A_{1},A_2, \ldots, A_{N}$ - the elements of the array $A$.

---

## Output Format

For each test case, output the **minimum** number of jumps required by the Chef to reach the **last** index of the array.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^4$
- $1 \leq A_{i} \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4
1 2 3 4
4
2 1 3 4
```

**Output**

```text
2
1
```

**Explanation**

**Test Case $1$:**  The minimum number of jumps required by the Chef to reach the last index is $2$.
Chef is initially standing at index $1$.
- Chef chooses $\texttt{Jump 2}$ and jumps to index $2$ as it is the immediate next element with different parity.
- Chef chooses $\texttt{Jump 1}$ and jumps to index $4$ as it is the immediate next element with the same parity.

**Test Case $2$:**  The minimum number of jumps required by the Chef to reach the last index is $1$.
Chef is currently standing at index $1$.
- Chef chooses $\texttt{Jump 1}$ and jumps to index $4$ as it is the immediate next element with the same parity.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
2 1 3 4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START35A/problems/JS)

[Contest Division 2](https://www.codechef.com/START35B/problems/JS)

[Contest Division 3](https://www.codechef.com/START35C/problems/JS)

[Contest Division 4](https://www.codechef.com/START35D/problems/JS)

Setter: [Neerav](https://www.codechef.com/users/neerav_1)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1888

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Lav has an array A of size N. He noticed that Chef is initially standing at the **first** index of the array.

While standing at the i^{th} index (1?i<N) of the array, Chef can perform the following types of jumps:

- ???????????????? ????: Jump to the immediate next index j such that Ai and Aj have the **same** [parity](https://en.wikipedia.org/wiki/Parity_(mathematics)).

- ???????????????? ????: Jump to the immediate next index j such that Ai and Aj have **different** parity.

Given that Chef can perform ???????????????? ???? **at most once**, Lav wants to find the **minimum** number of jumps required by the Chef to reach the **last** index of the array.

#
[](#explanation-5)EXPLANATION:

For each test case, the input consists of an array of size N.

Two cases are possible for this particular problem:

- When the first and last elements have **same** parity.

- When the first and last elements have **different** parity.

In the first case, if we perform Jump 2 even once then it is impossible for us to reach the destination(last element). So the number of jumps will be simply **total number of elements in the array with same parity as the first element** (obviously excluding the first element).

In the second case, we have to **perform Jump 2 once**  which can be done at any element having the same parity as the first element. The total number of jumps in this case will be the jumps required to reach this element plus the number of jumps to reach the last element. *This will be equivalent to the number of elements having the same parity as the first element till a particular element plus then the number of elements with different parity till the last element from here on.* So, we to have to find the **minimum value of this sum** for any element in the array having the same parity as the first element. This can be achieved using two extra arrays and pre-computing these values.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/vZbB)

[Setter’s Solution](http://p.ip.fi/WBQM)

[Tester-1’s Solution](http://p.ip.fi/cNe6)

[Tester-2’s Solution](http://p.ip.fi/6pFB)

</details>
