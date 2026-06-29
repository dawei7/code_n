# Home Delivery

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HDELIVER |
| Difficulty Rating | 1621 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [HDELIVER](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/HDELIVER) |

---

## Problem Statement

Chef has decided to start home delivery from his restaurant. He hopes that he will get a lot of orders for delivery, however there is a concern. He doesn't have enough work forces for all the deliveries.  For this he has came up with an idea - he will group together all those orders which have to be delivered in nearby areas.
In particular, he has identified certain bidirectional roads which he calls as fast roads. They are short and usually traffic free, so the fast travel is possible along these roads. His plan is that he will send orders to locations **A** and **B** together if and only if it is possible to travel between **A** and **B** using only fast roads. Your task is, given the configuration of fast roads, identify which orders are to be sent together.

### Input

First line of input contains an integer **T**, the number of test cases. Then **T** test cases follow. First line of each test case contains two space separated integers **N** and **M**, denoting number of locations and the number of fast roads. Then **M** lines follow each containing two space separated integers **A** and **B**, denoting that there is a fast road between locations **A** and **B**. Assume that locations are indexed by numbers from 0 to **N-1**.

Next line contains an integer **Q** denoting the number of queries. Each of the next **Q** lines contain two integers **X** and **Y**. For each query you have to find out if orders meant for locations **X** and **Y** are to be sent together or not.

Note that there might be multiple fast roads between same pair of locations, also there might be a fast road that links a location to itself.

### Output

For each test case print **Q** lines - one for each query. Output "YO" if the orders are to be
delivered together and "NO" otherwise (quotes for clarity).

### Constraints
`
1 ≤ **T** ≤ 100
1 ≤ **N** ≤ 100
1 ≤ **M** ≤ 1000
0 ≤ **A, B, X, Y** ≤ **N-1**
1 ≤ **Q** ≤ 3000
`

### Warning!

**There are large input and output files in this problem. Make sure you use fast enough I/O methods.**

---

## Examples

**Example 1**

**Input**

```text
1
4 2
0 1
1 2
3
0 2
0 3
2 1
```

**Output**

```text
YO
NO
YO
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/HDELIVER)

[Contest](http://www.codechef.com/MARCH12/problems/HDELIVER/)

### DIFFICULTY

EASY

### EXPLANATION

Restating the problem in terms of Graph Theory, we’re given a set of edges, and we’ve to identify if two given query points are connected via these edges or not. One could do a depth first search (DFS) from one of the vertices and monitor if the other vertex is visited or not, but time limits were set in such a way that it was difficult to get accepted if one is doing a dfs at each query. Instead, after only one DFS, we could store all the connected components. After that each query can be answered in constant time. Look at tester’s solution.

Alternate approach could be to build union-find data structure over the graph. As before, each query could now be answered in constant time. Look at setter’s solution for this approach. So in both the solutions, desired time complexity was O(E +V + Q)

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/March/Setter/HDELIVER.cpp).

### TESTER’S SOLUTION**

Can be found [here](http://www.codechef.com/download/Solutions/2012/March/Tester/HDELIVER.cpp).

</details>
