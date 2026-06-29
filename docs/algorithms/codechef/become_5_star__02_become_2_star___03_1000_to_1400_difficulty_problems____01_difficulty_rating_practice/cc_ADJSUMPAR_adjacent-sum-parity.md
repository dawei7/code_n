# Adjacent Sum Parity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADJSUMPAR |
| Difficulty Rating | 1013 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ADJSUMPAR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ADJSUMPAR) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

Chef forms a binary array $B$ of length $N$ using the parity of the sums of adjacent elements in $A$. Formally,
- $B_i = (A_i + A_{i+1}) \, \% \, 2$ for $1 \leq i \le N - 1$
- $B_N = (A_N + A_1) \, \% \, 2$

Here $x \, \% \, y$ denotes the remainder obtained when $x$ is divided by $y$.

Chef lost the array $A$ and needs your help. Given array $B$, determine whether there exists any valid array $A$ which could have formed $B$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $B_1, B_2, \dots, B_N$ denoting the array $B$.

---

## Output Format

For each testcase, output `YES` if there exists a valid array $A$, `NO` otherwise.

You can print any character in any case. For example `YES`, `Yes`, `yEs` are all considered same.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $B_i \in \{0, 1\}$
- The sum of $N$ over all test cases do not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
0 0
2
1 0
4
1 0 1 0
3
1 0 0
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case 1:** One such valid array is $A = [3, 3]$.

**Test case 2:** It can be shown that no such arrays exist and are valid.

**Test case 3:** One such valid array is $A = [1, 2, 4, 5]$.
- $B_1 = 1$ since $A_1 + A_2 = 1 + 2 = 3$ and $3 \, \% \, 2 = 1$
- $B_2 = 0$ since $A_2 + A_3 = 2 + 4 = 6$ and $6 \, \% \, 2 = 0$
- $B_3 = 1$ since $A_3 + A_4 = 4 + 5 = 9$ and $9 \, \% \, 2 = 1$
- $B_4 = 0$ since $A_4 + A_1 = 5 + 1 = 6$ and $6 \, \% \, 2 = 0$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
0 0
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2
1 0
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4
1 0 1 0
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3
1 0 0
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START45A/problems/ADJSUMPAR)

[Contest Division 2](https://www.codechef.com/START45B/problems/ADJSUMPAR)

[Contest Division 3](https://www.codechef.com/START45C/problems/ADJSUMPAR)

[Contest Division 4](https://www.codechef.com/START45D/problems/ADJSUMPAR)

**Setter:** [abhi_inav](https://www.codechef.com/users/abhi_inav)

**Testers:** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

1013

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

We are given an array B. Elements of B are formed from the elements of array A using the following operation

-
B_{i} = (A_i + A_{i+1}) % 2 for 1 <= i <= N-1

-
B_N = (A_1 + A_N) % 2

-
B_i = 0 OR B_i = 1

Given the array B, can there exist an array A such that B can be formed from A?

#
[](#explanation-5)EXPLANATION:

When do we get 0’s in B? We will get 0s if both Ai and Ai+1 are even or both are odd. When 2 numbers are even or both numbers are odd, their sum is necessarily even.

When do we get 1’s in B? We will get 1s if either A_i is even and A_{i+1} is odd or vice versa.

Implementation

Lets try and construct the array A from array B given the conditions above. Let the 1st element in array A be [1]

We can iterate across B from i = 1 to i = N - 1.

For each i in B from i = 1 to i = N - 1, if B_i = 0, then we append A_{i+1} = A_i

For each i in B from i = 1 to i = N - 1, if Bi not equal to 0, then we append A_{i+1} = (A_i + 1) basically if A_i is odd, we are appending an even number. If A_i is even, we are appending an odd number

Now, our array A is constructed with N elements and we need to check if the 1st and Nth element of A meet the condition which will create BN. We can do this by checking for the condition

If (A_1 + A_N) % 2 = B_N, then A is a valid array. Correspondingly, B then is also a valid array.

If (A_1 + A_N) % 2 is not equal to B_N, then A is invalid. Hence B cannot be constructed from A

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    n=int(input())
    brr=list(map(int,input().split()))
    arr=[]
    i=0
    arr.append(1)
    while i<n-1:
        if brr[i]==0:
            arr.append(arr[i])
        else:
            arr.append(arr[i]+1)
        i=i+1
    #print(arr)
    if (arr[0]+arr[n-1])%2==brr[n-1]:
        print('YES')
    else:
        print('NO')
``

</details>
