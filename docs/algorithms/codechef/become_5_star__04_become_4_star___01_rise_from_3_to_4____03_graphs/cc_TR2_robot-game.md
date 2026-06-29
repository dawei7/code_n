# Robot Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TR2 |
| Difficulty Rating | 1754 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [TR2](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/TR2) |

---

## Problem Statement

Byteland is a kingdom of islands. Alice has N maps of the different islands constituting Byteland. Map of each island consists of cities, connected by roads. Being Byteland, the road layout of each island has a binary tree structure. Each island has a capital, which is the root of the binary tree of its map.

Alice is bored and plays the following game:

She chooses k out of these N maps and places a robot on the capital city of each map. Every robot is controlled by a common control string. If the present character of the control string is L(R), then all the robots move to the left(right) subtree on their map. All the robots follow the same control string and move on their respective maps.

A control string is valid with respect to a given map if it corresponds to a valid path on that map. A control string is considered valid for a given set of k maps if it is valid for each of the k chosen maps.

For example in a complete binary tree of 3 nodes, control strings "L" and "R" are valid and "LL" is an example of an invalid control string.

Alice is interested in knowing the longest control
string which is valid for at least k maps, for each value of k. Can you find this for her?

### Input

First line of input contains an integer t (t<=5), the number of test cases. Each test case starts with an integer M (1<=M<=100), the number of maps. Then M maps description follow.

The ith map description starts with an integer N (2<=N<=1000), the number of cities on the island. Each of the following N-1 lines contain two space separated integers u c v (1<=u,v<=N , c=L or R) which means a road between city u and city v on the ith island and if c is L(R) then v is in the left(right) subtree of u. The capital city of each island is the city with number 1.

### Output

For each test case output M space separated integers, where the ith integer denotes the length of the longest valid control string she can obtain assuming she can choose i maps.

---

## Examples

**Example 1**

**Input**

```text
2
3
5
1 L 2
1 R 3
3 L 4
3 R 5
4
1 R 2
1 L 3
2 L 4
3
1 L 2
1 R 3
2
5
1 L 2
2 L 3
3 L 4
4 L 5
6
1 L 2
2 R 3
3 L 4
4 R 5
5 L 6
```

**Output**

```text
2 2 1
5 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/TR2/)

[Contest](http://www.codechef.com/JUNE10/problems/TR2/)

### DIFFICULTY

MEDIUM

### Solution: Tree traversal, DFS

### Complexity: O(N)

### EXPLANATION

Consider a complete binary tree T with 2^d-1 nodes, where d is the maximum depth of any of the given maps. Each city in this binary tree has a unique path from the root of T (and therefore a unique control string). For a given map, every city has a unique control string. Now each city on the map can uniquely be mapped to a city on T by following its control string on T.

To solve the problem, at each city in T, store a variable count, which denotes the number of maps which has a valid control string from root to the present city in T. Initially, all counts are 0. On adding a map, we can update the count of a city in T, by doing a depth first search (or any other traversal) on the given map and also computing the corresponding city number in T. Note that the length of the control string of any city is equal to the level of the city, assuming that root is at level-0.

Now we can just splice all the maps into T, renaming the cities in the map whenever necessary and find the required answer by looking at the count and level of each node in T. Since the total number of cities are 100 * 1000, we only need to consider atmost 100000 nodes in T as the rest of the cities in T will never correspond to a valid control string.

</details>
