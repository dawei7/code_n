# Ciel and Tomya

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CIELTOMY |
| Difficulty Rating | 1877 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [CIELTOMY](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/CIELTOMY) |

---

## Problem Statement

Tomya is a girl. She loves Chef Ciel very much.

Today, too, Tomya is going to Ciel's restaurant.
Of course, Tomya would like to go to Ciel's restaurant as soon as possible.
Therefore Tomya uses one of the shortest paths from Tomya's house to Ciel's restaurant.
On the other hand, Tomya is boring now to use the same path many times.
So Tomya wants to know the number of shortest paths from Tomya's house to Ciel's restaurant.
Your task is to calculate the number under the following assumptions.

This town has **N** intersections and **M** two way roads.
The **i**-th road connects from the **Ai**-th intersection to the **Bi**-th intersection, and its length is

**Ci**.
Tomya's house is in the 1st intersection, and Ciel's restaurant is in the **N**-th intersection.

### Input

The first line contains an integer **T**, the number of test cases.
Then **T** test cases follow.
The first line of each test case contains 2 integers **N**, **M**.
Then next **M** lines contains 3 integers denoting **Ai**, **Bi** and **Ci**.

### Output

For each test case, print the number of shortest paths from Tomya's house to Ciel's restaurant.

### Constraints

1 ≤ **T** ≤ 10

2 ≤ **N** ≤ 10

1 ≤ **M** ≤ **N ∙ (N – 1) / 2**

1 ≤ **Ai**, **Bi** ≤ **N**

1 ≤ **Ci** ≤ 10
**Ai** ≠ **Bi**

If **i** ≠ **j** and **Ai** = **Aj**, then **Bi** ≠ **Bj**

There is at least one path from Tomya's house to Ciel's restaurant.

---

## Examples

**Example 1**

**Input**

```text
2
3 3
1 2 3
2 3 6
1 3 7
3 3
1 2 3
2 3 6
1 3 9
```

**Output**

```text
1
2
```

**Explanation**

In the first sample, only one shortest path exists, which is 1-3.

In the second sample, both paths 1-2-3 and 1-3 are the shortest paths.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
1 2 3
2 3 6
1 3 7
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 3
1 2 3
2 3 6
1 3 9
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](http://www.codechef.com/problems/CIELTOMY)

[Contest](http://www.codechef.com/COOK24/problems/CIELTOMY)

### DIFFICULTY

SIMPLE

### PREREQUISITES

[Backtracking](http://en.wikipedia.org/wiki/Backtracking)

### PROBLEM

You need to find the number of different shortest paths between two given vertexes in the non-oriented weighted graph.

### EXPLANATION

Since the number of intersections is small we can simply consider all possible paths that connect **1**st intersection with **N**-th intersection and do not pass through the same intersection twice (otherwise such path will definitely be not shortest). The easiest way to do this is to use recursive backtracking. Let’s discuss the implementation in detail.

At first we should create the so-called [adjacency matrix](http://en.wikipedia.org/wiki/Adjacency_matrix) of the town. This is a two-dimensional array **A** where **A[i][j]** denotes the length of the road between **i**-th and **j**-th intersections if this road exists and **A[i][j] = 0** otherwise. Note that each road has positive length hence zeros will not lead to any ambiguity. Initially all elements in this array should be set to zero and then when we input some road of length **L** that connects intersections **i** and **j** we should set **A[i][j]** as well as **A[j][i]** to **L** since all roads are two-way.

Let us discuss at first how to iterate over all possible paths connecting **1**st and **N**-th intersection and find their lengths. At each step we will be at some intersection and we should know what intersections we have already passed and what distance we have already walked to know how to proceed further. Hence we can create the global boolean array **visited** of size **N** where information about visited intersections will be stored. Namely, **visited[k] = true** if and only if we have already passed **k**-th intersection. Then we can create recursive routine with definition **go(k, len)** where **k** is the current intersection where we stay and **len** is the length of the path that we already walked. When we are staying at some intersection **k** we can choose arbitrary non-visited intersection **j** that connected with **k** by two-way road and walk to **j** incrementing **len** by the length of the road between **k** and **j**. Hence **go(k, len)** can be implemented like this:

`go(k, len)
  visited[k] := true
  for j=1 to N
    if (not visited[j]) and (A[k][j] > 0)
      go(j, len + A[k][j])
  visited[k] := false
`

Note that we set **visited[k]** to **true** when we enter **go(k, len)** and set it to **false** before exit.

Current version of **go(k, len)** simply iterates over all paths starting from **1**st intersection if we run **go(1, 0)**. To process paths that finishing at **N**-th intersection we should add some lines in the beginning:

`go(k, len)
**  if k = N
    do something with len**
  visited[k] := true
  for j=1 to N
    if (not visited[j]) and (A[k][j] > 0) then
      go(j, len + A[k][j])
  visited[k] := false
`

For example we can save lengths of all paths that finishes at **N**-th intersection in some array and then process this array to find the number of shortest paths. Having this array we can do this by two passes through it. At the first pass we can find the actual length of the shortest path and at the second pass find the number of paths having the same length as the shortest path. In fact we can do this by one pass. Let **L** be the current value of shortest path and **C** the current number of paths having length **L**. Then when we process some path of length **len** we can do the following:

`if L > len
  L := len
  C := 1
else if L = len
  C := C + 1
`

Indeed, if **L > len** than all previous paths are longer than the current one hence we should set **L** to **len** and **C** to **1** indicating that we have currently only one shortest path. If **L = len** then the current path is of the same length as the shortest path so we should increase **C** by **1**. Finally if **L < len** then the current path is longer than the shortest path and we simply ignore it.

Clearly in the end of the pass **L** will be the shortest path and **C** will be the number of shortest paths. Since we are now able to find the answer in one pass by the array of all paths we in fact don’t need this array anymore – we can process paths in the fly. In other words we can simply replace **do something with len** in the code of **go(k, len)** by the above code with **L** and **C**:

`go(k, len)
  if k = N
    if L > len
      L := len
      C := 1
    else if L = len
      C := C + 1

  visited[k] := true
  for j=1 to N
    if (not visited[j]) and (A[k][j] > 0) then
      go(j, len + A[k][j])
  visited[k] := false
`

In fact when we reach **N**-th intersection we can stop further walking. Hence we can exit from the **go** routine if **k = N**. Another optimization that we can make is to exit from **go** if **len > L**. Indeed, even if we reach later **N**-th intersection **len** could only increase so we will ignore this path anyway. Thus the final version of **go** will look like:

`go(k, len)
**  if len > L
    exit**
  if k = N
    if L > len
      L := len
      C := 1
    else if L = len
      C := C + 1
    **exit**

  visited[k] := true
  for j=1 to N
    if (not visited[j]) and (A[k][j] > 0) then
      go(j, len + A[k][j])
  visited[k] := false
`

To get the full solution for the problem we need to init all elements of **visited** by **false**, set **L** to **INF**, **C** to **0** and run **go(1, 0)**. In the end **C** will be the final answer. **INF** here is some number larger than the length of ecah path. In this problem we can safely take **INF = 100**. In general **INF** should be taken as **maxC * (N - 1) + 1** where **maxC** is the maximal length of the road in the town.

The complexity of this algorithm is equal to the number of paths that starts at the first intersection and does not have **N**-th intersection as an intermediate intersection. Of course in general pruning **if len > L then exit** could decrease this number. But in the worst case when all pairs of intersections connected by the roads the total number of such paths equals to **2 * (N-2)! * (1/0! + 1/1! + … + 1/(N-2)!)** which is approximately equals to **2 * e * (N-2)!**. Here **e** is the base of natural logarithm. We leave this as an exercise to the reader. Thus the complexity of the algorithm in terms of **N** is **O((N-2)!)**. Note that even with pruning by **len** the **go** routine can in general consider all paths. Indeed, let all roads connecting **N**-th intersection with other intersections has length **N** and all other roads have length **1**. Then it is easy to see that the shortest path between **1**st and **N**-th intersection is **N** on the other hand each path not having **N** has length **<= N-2**. Hence **go** routine with **len** pruning will consider all paths.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK24/Setter/CIELTOMY.c).

Setter used the approach described above with one small difference. Instead of array **visited** he uses integer variable **mask**, **i**-th bit of which equals to **visited[i]** and pass this variable directly to **go** routine instead of making it global. See code for details.

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK24/Tester/CIELTOMY.java).

Tester used the approach described above.

### ALTERNATIVE APPROACH

The problem in fact can be solved in **O(M + N * log N))** time. We will discuss it briefly. At first let’s find the length of shortest path from **1**st intersection to every other intersection using [Dijkstra’s algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) in **O(M + N * log N))** time (or in **O((M + N) * log N))** time if you are using usual heap). So we are now have the array **D** of size **N** such that **D[i]** is the length of shortest path between **1**st and **i**-th intersection. Now to find the number of different shortest paths to the **N**-th intersection one can observe that the path **(V0 = 1, V1, …, VK = i)** will be the shortest path from **1** to **i** if and only if the length of the road between **Vj-1** and **Vj** is equal to **D[Vj] - D[Vj-1]** for all **j** from **1** to **K**. This allows to use [dynamic programming](http://en.wikipedia.org/wiki/Dynamic_programming) to find the number of different shortest paths. Let **F[i]** be the number of shortest paths between **1**st and **i**-th intersection. Then **F[1] = 1**, **F[N]** is the final answer and **F[i]** equals to the sum of **F[j]** for all **j** such that there is a road between **i** and **j** with length **D[i] - D[j]**. To calculate all correctly we need to iterate over vertexes in increasing order of **D[j]** or use recursive DP with memoization. This is very important. If you try to code such solution with some other order of vertexes then be ready for the following test:

4 3

1 3 1

3 2 1

2 4 1

You will obtain the correct result only if you calculate values of **F[]** in the order: **F[1], F[3], F[2], F[4]**.

This step of the solution requires only **O(M)** basic operations.

Alternatively you can combine DP step with the Dijkstra’s algorithm itself. Namely, if for some edge **(u, v)** of the length **c** you have a situation that **D[v] > D[u] + c** then according to the Dijkstra’s algorithm you set **D[v]** to **D[u] + c**. For calculating DP in this case simply make **F[v] = F[u]**. Note that according to the logic of Dijkstra’s algorithm **D[u]** is already correct and so **F[u]** is also.

Similarly to the piece of code

`    else if L = len
      C := C + 1
`

of the above solution we need to do the following

`if D[v] = D[u] + c
  F[v] := F[v] + F[u]
`

This gives us a solution that much easier to code than the previous one where DP was a separate step.

### RELATED PROBLEMS

[Social Constraints (UVA 11742)](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=117&page=show_problem&problem=2842)

[Getting in Line (UVA 216)](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=4&page=show_problem&problem=152)

[The N Queens Puzzle Revisited (Codechef J3)](http://www.codechef.com/problems/J3)

</details>
