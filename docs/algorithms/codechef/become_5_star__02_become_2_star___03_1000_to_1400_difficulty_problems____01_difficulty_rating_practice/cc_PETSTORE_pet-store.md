# Pet Store

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PETSTORE |
| Difficulty Rating | 1126 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PETSTORE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PETSTORE) |

---

## Problem Statement

Alice and Bob went to a pet store. There are $N$ animals in the store where the $i^{th}$ animal is of type $A_i$.

Alice decides to buy some of these $N$ animals. Bob decides that he will buy **all** the animals **left** in the store after Alice has made the purchase.

Find out whether it is possible that Alice and Bob end up with **exactly same** [multiset](https://en.wikipedia.org/wiki/Multiset) of animals.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of animals in the store.
    - The next line contains $N$ space separated integers, denoting the type of each animal.

---

## Output Format

For each test case, output on a new line, `YES`, if it is possible that Alice and Bob end up with **exactly same** multiset of animals and `NO` otherwise.

You may print each character in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes`, and `yES` are considered identical.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 100$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
4 4 4
4
2 3 3 2
4
1 2 2 3
6
5 5 1 5 1 5
```

**Output**

```text
NO
YES
NO
YES
```

**Explanation**

**Test case $1$:** There are $4$ possible cases:
- Alice does not buy anything: Bob will buy all the animals and will have $3$ animals of type $4$.
- Alice buys $1$ animal of type $4$: Bob will buy the remaining two animals of type $4$.
- Alice buys $2$ animals of type $4$: Bob will buy the remaining one animal of type $4$.
- Alice buys all $3$ animals of type $4$: Bob will not buy anything.

In no case, both Alice and Bob can have the exactly same multiset of pets.

**Test case $2$:** If Alice buys animals $1$ and $2$, having types $2$ and $3$ respectively, Bob will buy animals $3$ and $4$, having types $3$ and $2$ respectively. Thus, both Alice and Bob have $1$ animal of type $2$ and $1$ animal of type $3$.

**Test case $3$:** It can be proven that Alice and Bob cannot have the same multiset of pets in any case.

**Test case $4$:** If Alice buys animals $1, 2, $ and $5$, having types $5, 5,$ and $1$ respectively, Bob will buy animals $3, 4,$ and $6$, having types $1, 5,$ and $5$ respectively. Thus, both Alice and Bob have $1$ animal of type $1$ and $2$ animals of type $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
4 4 4
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4
2 3 3 2
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
4
1 2 2 3
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
6
5 5 1 5 1 5
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

[Practice](https://www.codechef.com/problems/PETSTORE)

[Contest: Division 1](https://www.codechef.com/START71A/problems/PETSTORE)

[Contest: Division 2](https://www.codechef.com/START71B/problems/PETSTORE)

[Contest: Division 3](https://www.codechef.com/START71C/problems/PETSTORE)

[Contest: Division 4](https://www.codechef.com/START71D/problems/PETSTORE)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1126

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A pet store has N types of animals, the i-th of which has type A_i.

Alice will buy some of these animals and Bob will buy the rest. Is there a way for them to end up with exactly the same multiset of types of animals?

#
[](#explanation-5)EXPLANATION:

Each type of animal bought by Alice must have a copy that she didn’t buy, so that Bob can buy this copy.

In other words, for a valid split to exist, *every* type of animal must be present an even number of times.

It’s easy to see that this condition is both necessary and sufficient.

So, all that needs to be done is to check whether each type of animal occurs an even number of times.

One way to do that is as follows:

- Create an array c of length 100, where c_x denotes the number of times x occurs in A.

- This is easy to do in \mathcal{O}(N), by simply iterating i from 1 to N and incrementing c_{A_i} by 1 each time.

- Then, check whether every c_x is even.

Alternately, you can also sort A and check whether A_{2i-1} = A_{2i} (in 1-indexing) for every i.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 'Yes' if n%2 == 0 else 'No'
    for i in range(1, n, 2):
        if a[i] != a[i-1]: ans = 'No'
    print(ans)
``

</details>
