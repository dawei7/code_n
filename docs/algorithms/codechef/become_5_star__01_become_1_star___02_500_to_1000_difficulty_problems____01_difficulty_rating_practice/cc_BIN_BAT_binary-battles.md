# Binary Battles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BIN_BAT |
| Difficulty Rating | 786 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [BIN_BAT](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BIN_BAT) |

---

## Problem Statement

$N$ teams have come to participate in a competitive coding event called “Binary Battles”. It is a [single-elimination tournament](https://en.wikipedia.org/wiki/Single-elimination_tournament) consisting of several rounds.

**Note:** It is known that $N$ is a power of $2$.

In one round, each team will be paired up with and compete against one of the other teams. If there are $X$ teams before the start of a round, $\frac{X}{2}$ matches are held simultaneously during the round between $\frac{X}{2}$ pairs of teams. The winning team of each match will move on to the next round, while the losing team of each match will be eliminated. There are no ties involved. The next round will then take place in the same format between the remaining teams. The process will continue until only one team remains, which will be declared the overall winner.

The organizers want to find the total time the event will take to complete. It is given that each round spans $A$ minutes, and that there is a break of $B$ minutes between every two rounds (no break after the last round).

For example, consider a case when $N = 4$, $A = 10$ and $B = 5$. The first round will consist of two matches and will take $10$ minutes to complete. Two teams move on to round 2 and the other two get eliminated. Then there is a break of $5$ minutes. The two remaining teams compete in round 2, which lasts $10$ more minutes. The team that wins is declared the overall winner. Thus the total time taken is $10 + 5 + 10 = 25$ minutes.

Can you help the organizers determine how long the event will take to finish?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three space-separated integers $N$, $A$ and $B$ respectively — the number of teams, the duration of each round and the length of the breaks between rounds.

---

## Output Format

For each test case, output on a new line the time taken in minutes for the whole event to finish.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2^{20}$
- $1 \leq A \leq 100$
- $1 \leq B \leq 100$
- $N$ is a power of $2$.

---

## Examples

**Example 1**

**Input**

```text
4
4 10 5
16 30 5
32 45 15
1024 23 9
```

**Output**

```text
25
135
285
311
```

**Explanation**

**Test case 1:** As explained above, the total time the competition will take is $10 + 5 + 10 = 25$ minutes.

**Test case 2:** $4$ rounds will take place. The total time it will take is $30 + 5 + 30 + 5 + 30 + 5 + 30 = 135$ minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 10 5
```

**Output for this case**

```text
25
```



#### Test case 2

**Input for this case**

```text
16 30 5
```

**Output for this case**

```text
135
```



#### Test case 3

**Input for this case**

```text
32 45 15
```

**Output for this case**

```text
285
```



#### Test case 4

**Input for this case**

```text
1024 23 9
```

**Output for this case**

```text
311
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BIN_BAT)

[Contest: Division 1](https://www.codechef.com/START66A/problems/BIN_BAT)

[Contest: Division 2](https://www.codechef.com/START66B/problems/BIN_BAT)

[Contest: Division 3](https://www.codechef.com/START66C/problems/BIN_BAT)

[Contest: Division 4](https://www.codechef.com/START66D/problems/BIN_BAT)

***Author:*** [Gaurav Somai](https://www.codechef.com/users/gaurav_somai)

***Testers:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

786

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

N players play in a single-elimination tournament. Each round takes A minutes, and there is a B-minute break after every round except the last.

How much time does the tournament take?

#
[](#explanation-5)EXPLANATION:

We are given that N is a power of 2, so let N = 2^k.

Note that the tournament has exactly k rounds.

For these k rounds:

- Each one takes A minutes

- All but the last have a further break of B minutes

This gives us a total time of

k\cdot A + (k-1)\cdot B

The only thing that remains is to correctly compute k.

This can be done in many ways:

- You can iterate k on a loop and check if 2^k = N

- Alternately, most languages have builtin functions to compute this, for example:

-
`__lg(N)` or `log2(N)` in C++

-
`N.bit_length()-1` in Python

Once k is computed, use the formula above.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main(){

   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   int t;
   cin>>t;
   while(t--){
    int n,a,b;
    cin>>n>>a>>b;
    int k = log2(n);
    int ans = (a*k)+(b*(k-1));
    cout<<ans<<"\n";
   }

   return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, a, b = map(int, input().split())
    rounds = n.bit_length() - 1
    print((rounds-1)*(a+b) + a)
``

</details>
