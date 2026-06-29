# Lockpicking Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LPC |
| Difficulty Rating | 1311 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LPC](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LPC) |

---

## Problem Statement

Chef bought a new digital lock, but is quite suspicious of its actual strength in keeping out pesky thieves. So, he wants to find out how quickly he can open the lock.

The digital lock works as follows:
- On its screen, there is a string of digits $S$ of length $N$.
- There is also a secret code $K$ of length $M$ ($1 \leq M \leq 10$), which acts as the key to the lock.
The lock will open if $K$ is present *anywhere* in $S$ as a contiguous [substring](https://en.wikipedia.org/wiki/Substring#).

Operating the lock is simple: Chef can choose an index $i$, and either increment $S_i$ by $1$, or decrement it by $1$.
Here, the digits are cyclic, following the order $0\to1\to2\to3\to\ldots\to8\to9\to0\to\ldots$
In particular, incrementing $9$ will turn it into $0$ and decrementing $0$ will turn it into $9$.

You are given $S$ and $K$. What's the minimum number of moves Chef needs to open the lock?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the lengths of the string and the secret code, respectively.
    - The second line contains a string $S$ of length $N$, containing only the digits `0-9`.
    - The third line contains a string $K$ of length $M$, also containing only the digits `0-9`.

---

## Output Format

For each test case, output on a new line the minimum number of moves Chef needs to open the lock.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq M \leq \min(N, 10)$
- The sum of $N$ across all tests won't exceed $10^5$.
- Strings $S$ and $K$ will only contain the digits `0-9`.

---

## Examples

**Example 1**

**Input**

```text
4
5 2
10234
32
5 2
10234
57
5 3
10234
234
6 3
464646
000
```

**Output**

```text
2
5
0
12
```

**Explanation**

**Test case $1$:** One solution is as follows:
- Increase the third digit by $1$: $\texttt{10234} \to \texttt{10334}$
- Decrease the fourth digit by $1$: $\texttt{10334} \to \texttt{10324}$

Now $K = \texttt{32}$ is present as a substring.
It can be shown that using less than $2$ moves is not enough.

**Test case $3$:** $K = \texttt{234}$ is already present as a substring, so $0$ moves are needed.

**Test case $4$:** One solution is as follows:
- $\texttt{464646} \to \texttt{404646}$ by incrementing the second position $4$ times.
- $\texttt{404646} \to \texttt{404046}$ by incrementing the fourth position $4$ times.
- $\texttt{404046} \to \texttt{400046}$ by decrementing the third position $4$ times.

$\texttt{000}$ is now present as a substring, and we used $12$ moves in total.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
10234
32
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 2
10234
57
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5 3
10234
234
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
6 3
464646
000
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LPC)

[Contest: Division 1](https://www.codechef.com/START101A/problems/LPC)

[Contest: Division 2](https://www.codechef.com/START101B/problems/LPC)

[Contest: Division 3](https://www.codechef.com/START101C/problems/LPC)

[Contest: Division 4](https://www.codechef.com/START101D/problems/LPC)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1311

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given a string S of length N and another string K of length M, both containing the digits `0-9` only.

Find the minimum number of moves needed to make K appear as a substring of S, where a move consists of either incrementing or decrementing a digit of S.

# [](#explanation-5)EXPLANATION:

Suppose we fix *which* length-M substring of S is going to turn into K; say the substring starting at index L.

Let’s try to find the minimum number of moves we need to turn this substring into K.

That isn’t very hard:

- Notice that for each i = 1, 2, 3, \ldots, M, we’d like to turn S_{L+i-1} into K_i.

- To do that, we can either go forward or backward from S_{L+i-1}, till we reach K_i.

One of them requires |S_{L+i-1} - K_i| moves, while the other requires 10 - |S_{L+i-1} - K_i| moves (the values are small, so you can even just run a loop to compute these values, instead of using math).

So, we need the minimum of these two numbers to convert S_{L+i-1} to K_i.

Hence, for a fixed L, the required cost is

\sum_{i=1}^M \min(|S_{L+i-1} - K_i|, 10 - |S_{L+i-1} - K_i|)

This is easy to compute in \mathcal{O}(M) time.

Now, just try every possible starting position L, i.e, all 1 \leq L \leq N-M+1.

Compute the cost for each of them; and the final answer is the minimum of all these costs.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\cdot M) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    pat = input()
    ans = 10**9
    for i in range(n-m+1):
        cur = 0
        for j in range(m):
            d1, d2 = ord(s[i+j]), ord(pat[j])
            cur += min(abs(d1 - d2), 10 - abs(d1 - d2))
        ans = min(ans, cur)
    print(ans)
``

</details>
