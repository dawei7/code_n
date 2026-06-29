# Make all equal using Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PAIREQ |
| Difficulty Rating | 928 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [PAIREQ](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/PAIREQ) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

In one operation, Chef can choose any two **distinct** indices $i, j$ $(1 \leq i, j \leq N, i \neq j)$ and **either** change $A_i$ to $A_j$ **or** change $A_j$ to $A_i$.

Find the **minimum** number of operations required to make all the elements of the array **equal**.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case consists of an integer $N$ - denoting the size of array $A$.
- Second line of each test case consists of $N$ space-separated integers $A_1, A_2, \dots, A_N$ - denoting the array $A$.

---

## Output Format

For each test case, output the minimum number of operations required to make all the elements equal.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $1 \leq A_i \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
3
1 2 3
4
5 5 5 5
4
2 2 1 1
3
1 1 2
```

**Output**

```text
2
0
2
1
```

**Explanation**

**Test Case $1$:** You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 2$ and convert $A_1$ to $A_2$. So the array becomes $[2, 2, 3]$. Now you can choose indices $1, 3$ and convert $A_3$ to $A_1$, so the final array becomes $[2, 2, 2]$.

**Test Case $2$:** Since all the elements are already equal there is no need to perform any operation.

**Test Case $3$:** You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 3$ and convert $A_1$ to $A_3$. So the array becomes $[1, 2, 1, 1]$. Now you can choose indices $1, 2$ and convert $A_2$ to $A_1$, so the final array becomes $[1, 1, 1, 1]$.

**Test Case $4$:** You can make all the elements equal in $1$ operation. You can pick indices $2, 3$ and convert $A_3$ to $A_2$ after which the array becomes $[1, 1, 1]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
5 5 5 5
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4
2 2 1 1
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
3
1 1 2
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

[Contest Division 1](https://www.codechef.com/JUN222A/problems/PAIREQ)

[Contest Division 2](https://www.codechef.com/JUN222A/problems/PAIREQ)

[Contest Division 3](https://www.codechef.com/JUN222A/problems/PAIREQ)

[Contest Division 4](https://www.codechef.com/JUN222A/problems/PAIREQ)

**Setter:** [abhi_inav](https://www.codechef.com/users/abhi_inav)

**Testers:** [inov_360](https://www.codechef.com/users/inov_360), [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

928

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has an array A of length N. In one operation, Chef can choose 2 distinct indices i,j and either change Ai to Aj or Aj to Ai. Any number of operations can be carried out. Find the minimum number of operations required to make all the elements of the array equal.

#
[](#explanation-5)EXPLANATION:

*Concept*

Each test case has 2 lines of input. Our input acceptance should take this into consideration.

What does the problem actually need us to do? - We need to make all elements equal.

- If all elements of the array are different, then (N - 1) elements of the array can be converted into any 1 element in (N - 1) operations

- Suppose some elements of the array are common. In this case, we need to find which element should we convert the entire array into such that we need minimum number of operations

This element will be the element which has the most frequency in the array. Supposed frequency of this element is F, then we need to output (N - F)

*Implementation*

- Sort the array in an ascending order

- Traverse through the array from left to right and maintain a counter which stores the frequency of each unique element

- Take the maximum value of this counter as F - and then output (N - F)

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N logN).

#
[](#solution-7)SOLUTION:

Tester's Solution
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	print(n - max([a.count(x) for x in a]))
``

Editorialist's Solution
``t=int(input())
for _ in range(t):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    final=1
    count=1
    i=0
    while i<(n-1):
        if arr[i]==arr[i+1]:
            count=count+1
            i=i+1
            if final<count:
                final=count
            continue
        count=1
        i=i+1
    print(n-final)
``

</details>
