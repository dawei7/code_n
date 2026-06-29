# India Fights Corona

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CORONA |
| Difficulty Rating | 2560 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [CORONA](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/CORONA) |

---

## Problem Statement

There are $N$ cities (numbered from $1$ to $N$) and $M$ bidirectional roads. The $i^{th}$ of these roads connects the cities $A_i$ and $B_i$ and has a length of $D_i$ Km.

There are only $K$ cities that have a hospital for corona testing. The cost of corona testing may be different in different cities. For each city, we want to know the minimum cost that needs to be spent to test a corona sample. If city you are in contains a hospital and you choose to test in that hospital itself, then the cost incurred is the cost of corona test in that hospital. Otherwise, if you choose to test in a hospital in another city, then an additional transportation cost is also incurred (Assuming Rs.1 per Km).

So from a city $i$, if you choose to send a sample to city $j$, then the total cost incurred will be $C_j + D(i,j)$. Here $C_j$ denotes the cost of corona testing in a hospital situated in city $j$ and $D(i,j)$ denotes the minimum distance between city $i$ and $j$ via some road network.

Output the *minimum* money that should be spent by a person in each of the $N$ cities for testing a corona sample.

It is guaranteed that there is a path from every city to every other city. Also, there is at most one road between any pair of cities (i.e. no multiple edges). There are no roads from one city to itself (i.e. no self-loops).

**Note:** Since the inputs and outputs are large, prefer using fast input-output methods.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each testcase contains $K + M + 1$ lines of input.
- The first line of each test case contains three space-separated integers $N, M, K$.
- $K$  lines follow. For each valid $i$, the $i^{th}$ of these lines contains two space-separated integers $x_i, C_i$ which denotes that there is a hospital in the $x_i^{th}$ city and the cost of corona testing in that hospital is $C_i$. There is at most one hospital in a city i.e. all $x_i$-s are distinct.
- Next $M$ lines follow. For each valid $i$, the $i^{th}$ of these lines contains three space-separated integers $A_i, B_i, D_i$, which denotes that there is a bidirectional road between City $A_i$ and City $B_i$ of length $D_i$ Km.

---

## Output Format

For each test case, print a single line containing $N$ space-separated integers, where the $i^{th}$ integer denotes the minimum cost of corona testing if you are in the $i^{th}$ city.

---

## Constraints

- $1 \leq T \leq 4000$
- $2 \leq N \leq 2 \cdot 10^5$
- $1 \leq M \leq 4 \cdot 10^5$
- $1 \leq K \leq N$
- $1 \leq x_i, A_i, B_i \leq N$ for each valid $i$
- $1 \leq C_i \leq 10^9$ for each valid $i$
- $1 \leq D_i \leq 10^9$ for each valid $i$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
- Sum of $M$ over all test cases does not exceed $4 \cdot 10^5$
- All $x_i$-s in a testcase are distinct.
- It is guaranteed that there is a path from every city to every other city.
- It is guaranteed that there are no self loops and multiple edges.

---

## Examples

**Example 1**

**Input**

```text
2
3 2 2
1 5
2 10
1 2 6
2 3 9
3 2 2
1 5
2 10
1 2 1
2 3 9
```

**Output**

```text
5 10 19 
5 6 15
```

**Explanation**

**Test case $1$:** The hospitals are situated at cities $1$ and $2$ with their costs being $5$ and 10 respectively. For city $1$ it is optimal to test the sample in its own hospital bearing a total cost of $5$. For city $2$ it is again optimal to test the sample in its own hospital bearing a total cost of $10$. For city $3$ it is optimal to test the sample in the hospital at city $2$ which incurs the traveling cost of $9$ and hospital cost of $10$, so the total cost is $10+9=19$.

**Test case $2$:** For city $2$, it is optimal to test the sample in hospital at city $1$ which incurs a traveling cost of $1$ and hospital cost of $5$, so the total cost is $1+5=6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 2
1 5
2 10
1 2 6
2 3 9
```

**Output for this case**

```text
5 10 19
```



#### Test case 2

**Input for this case**

```text
3 2 2
1 5
2 10
1 2 1
2 3 9
```

**Output for this case**

```text
5 6 15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START9C/problems/CORONA)

[Contest - Division 2](https://www.codechef.com/START9B/problems/CORONA)

[Contest - Division 1](https://www.codechef.com/START9A/problems/CORONA)

#
[](#difficulty-2)DIFFICULTY:

EASY-MEDIUM

#
[](#prerequisites-3)PREREQUISITES:

[Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

#
[](#problem-4)PROBLEM:

There are N cities and M bidirectional roads. Each road has a particular cost to travel on.

K cities among these have corona testing facility for a particular amount (different cities may have different prices for testing).

Determine for each city, the minimum cost to travel to any corona testing facility and get tested.

#
[](#explanation-5)EXPLANATION:

Model the problem as a weighted graph with N+1 nodes. Draw an edge between node 0 and node i with a corona testing facility (for all i), and give it weight C_i.

Now, we have reduced the problem to finding the shortest path from each city to node 0. This is equivalent to finding the shortest path from node 0 to each city, which is a classical Dijkstra problem!

#
[](#time-complexity-6)TIME COMPLEXITY:

Dijkstra (with minimum priority queue) takes

O(V+E\log V)

which is the time complexity per test case.

#
[](#solutions-7)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/49968411).

*Experimental:* For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
