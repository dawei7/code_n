# Rendezvous

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TR1 |
| Difficulty Rating | 1638 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [TR1](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/TR1) |

---

## Problem Statement

There are N cities in Byteland numbered 1 to N with city 1 as the capital. The road network of Byteland has a tree structure. All the roads are bi-directional. Alice and Bob are secret agents working for the Bytelandian Security Agency (BSA). Each secret agent is assigned a random city each month, where he/she must be stationed for the complete month. At the end of each month, they come to the capital to submit their reports to the head of BSA. They always take the shortest path from their city to the capital. If Alice is assigned city A and Bob is assigned city B then they meet at a city C which is common to both their routes to the capital and then travel together from C to the capital.

Alice and Bob wish to spend maximum time together in any trip. So for any pair of assigned cities (A,B) they meet at a city C such that C is the farthest city from the capital and appears in the shortest path from capital to A and capital to B. Since this happens each month they compute this for each pair of assigned cities (A,B) and store it in a matrix M, where M[A][B] = C, the city where they meet.

The importance of a city C(according to Alice and Bob), Im(C) is defined as the number of times C appears in their matrix M. Alice and Bob are interested in finding the importance of each city. Since this output can be large, output the sum S defined as S = (sum i=1 to N) i*Im(i) modulo 1000000007.

### Input

First line of input contains an integer t (t<=25), the number of test cases. Each test case starts with an integer N (1<=N<=10000), the number of cities

The next N-1 lines contain two space separated integers u v (1<=u,v<=N) denoting a road from u to v.

### Output

For each test case output the required sum S

---

## Examples

**Example 1**

**Input**

```text
3
5
1 2
1 3
2 4
2 5
3
1 2
1 3
1
```

**Output**

```text
41
12
1
```

**Explanation**

For the first test case, the matrix M is:
1 1 1 1 1
1 2 1 2 2
1 1 3 1 1
1 2 1 4 2
1 2 1 2 5

and the corresponding importance array is: 15 7 1 1 1
so the required sum is 1*15 + 2*7 + 3*1 + 4*1 + 5*1 = 41

For the second test case, the matrix M is:
1 1 1
1 2 1
1 1 3
and so the Importance array is: 7 1 1
So the required sum is 1*7 + 2*1 + 3*1 = 12

For the third test case, there is only one city, so the Matrix M just has one entry 1, so S = 1

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2
1 3
```

**Output for this case**

```text
41
```



#### Test case 2

**Input for this case**

```text
2 4
2 5
3
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
1 2
1 3
1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/TR1/)

[Contest](http://www.codechef.com/MAY10/problems/TR1/)

### DIFFICULTY

EASY

**Solution**: Tree traversal **Complexity**: O(N)

### EXPLANATION

Consider the rooted tree T, with the 1 as the root. Now the required node C for a pair (A,B) is the lowest common ancestor of A and B in this tree. Direct implementation of a text book algorithm leads to a O(N^2logN) or a O(N^2) solution to the problem depending on whether its O(logN) lca or O(1) lca algorithm. Since N <= 1e4, and there are 25 test cases, we need something better than O(N^2) to pass.

Consider a non-leaf node u in the tree. Now we have to compute the number of pairs of nodes whose lca is u. Let u have k children c1,c2,…,ck. Now the subtree rooted at each child c _ i is independent. For all combinations of vertices (a,b) with a in c _ i and b in c _ j , i ! = j , have u as their lca. So we must find 2 * (|c1| * |c2| + |c1| * |c3| + … |c1| * |ck| + |c2| * |c3| + |c2| * c4 + …  + |ck| * |ck-1|) , ie. all C(k,2) combinations of |c _ i|s where |c _ i| represents the number of nodes in the subtree rooted at c _ i. The two factor is because each pair (a,b) appears in the matrix twice as (a,b) and (b,a).

Now to compute this, there are multiple approaches:

1.The sum is equal to (sum of |c _ i|)^2 minus sum of |c _ i|^2

An alternate and neater approach to compute this sum is to keep the partial sum of c _ i’s until a point and to multiply the next c value to the present partial sum. ie.

long long partialsum = 0 , res = 0;

for ( int i=1;i<=k;i++ )

{

res += partialsum * C[i];

partialsum += C[i];

}

res * 2 is the required sum. Now all the pairs of the form (u,some node in subtree rooted at u) are not considered as we are only considering the pairs among the children of u. So we must add twice the size of subtree rooted at u (excluding u) to the solution. (u,u) also appears in the matrix, so this is another entry for Im(u). So Im(u) = res * 2 + 2 * (size of subtree rooted at u) + 1.

**Note:** If partialsum is initialized to 1, then the subtree term can be ignored completely, since the size of subtree rooted at u excluding u is equal to sum of |c _ i|s.

Once the Im values are calculated, the required sum S can easily be computed.

</details>
