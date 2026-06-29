# Road Decoration

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AMR14B |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [AMR14B](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/AMR14B) |

---

## Problem Statement

Australia and New Zealand have started working on preparation for the World Cup 2015. There are N important venues (like hotels and stadiums) in the city. Out of these important venues, there is one central location where the opening and closing ceremony will be held. There is an existing network of bidirectional roads connecting these venues. The organizing committee has planned to decorate some of these roads that will be used for commuting. They have decided to choose the roads to decorate such that there is exactly one decorated path to all the venues from the central location.

New Zealand is supposed to decorate these roads and Australia has taken up the responsibility of providing transportation. Only decorated roads can be used for transportation. Australia wanted to save fuel costs, and so they wanted to choose the decorated roads to minimize the total sum of distances to all venues from the central location. However, New Zealand had their own plans to minimize decoration cost by choosing the decorated roads such that the sum of the length of the chosen roads will be minimized.

To prevent a fight breaking out between these two rivals before they even step on to the field, you have to help them by reporting if there is a solution in which the two rivals could choose the same set of roads while satisfying their respective constraints.

**Input:**

The first line contains the number of test cases T.

For each test first line contains N and M which are number of venues and total number of roads respectively.

Then next M lines for each case contains u, v and w - indicating that there is a bidirectional road of distance w between locations u and v.

The central location is identified with location 0.

**Output:**

For each test case, output the required answer on a separate line. If there is a valid plan, then print “YES”. Else, print “NO” (quotes for clarity).

Note: If any of the venues is not reachable from the central location, then print “NO”.

**Constraints:**

1 <= T <= 10000

1 <= N <= 20000

0 <= M <= 40000

0 <= u < N

0 <= v < N

u != v

1 <= w <= 10^9

The sum of values of N over all test cases will not be more than 1000000.

The sum of values of M over all test cases will not be more than 2000000.

**Example**:

**Sample Input:**

3

3 3

0 1 1

0 2 2

1 2 2

3 1

0 1 1

4 5

2 1 9

3 2 5

0 3 9

0 1 2

3 1 9

**Sample Output:**

YES

NO

NO

**Explanation:**

For the first case, both of them can choose the roads {0<-->1, 0<-->2}.

For the second case, venue 2 is not reachable from the central location 0.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/AMR14ROS/problems/AMR14B)

[Contest](http://www.codechef.com/problems/AMR14B)

### DIFFICULTY:

EASY-MEDIUM

### PREREQUISITES:

[Dijkstra’s algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), [Prim’s algorithm](http://en.wikipedia.org/wiki/Prim%27s_algorithm)

### PROBLEM:

Given an undirected weighted graph, find whether there exist a shortest path tree(rooted at node 0) which is also the minimum spanning tree.

### QUICK EXPLANATION:

If the weight of the Minimum Spanning Tree(MST) is equal to the weight of some Shortest Path Tree then the answer is YES else NO. Now among many shortest path trees, only the one whose weight is minimum can possibly also be the minimum spanning tree. So to find the shortest path tree with minimum weight we have to modify Dijkstra’s algorithm such that if there exist more than one path to a vertex from root which yields the same distance from root then we give preference to that path whose last edge added is minimum.

### EXPLANATION:

Weight of any tree is greater of equal to weight of MST,therefore weight of any SPT will also be greater or equal to weight of MST. So if any SPT has weight equal to weight of MST, then that SPT is also a MST since it connects all vertices. Now, the question basically boils down to finding the minimum weight shortest path tree(rooted at vertex 0). Once we find the weight of that tree and if it is equal to weight of the minimum spanning tree(MST) then answer is YES else NO. See the example below where there are 2 shortest path tree(SPT) and one of them is also the MST.

Now to find the minimum weight shortest path tree we will modify the standard Dijkstra. In Dijkstra, we initially assign distance equal to 0 to vertex 0 and insert pair < distance, vertex > = <0,0> into a heap. Then we repeatedly extract min and relax all the neighbours and insert the pairs whose distances are reduced. Now instead of that we will insert a triplet < distance, lastEdge, vertex >. So the heap structure will first follow the distance field and if distances are equal then it will follow lastEdge field. We can note this in the above graph, when vertex B is extracted, the algorithm will insert two triplets <22,2,C> and <30,10,D>. Then vertex C will be extracted and the triplet <30,8,D> will be inserted. Now notice that there are 2 shortest paths from A to D (A-B-D and A-B-C-D) but the path A-B-C-D should be preferred and this is exactly the case here as while inserting <30,8,D> we will update the lastEdge added.

Below is pseudo code of the main loop of the modified Dijkstra.

``priority_queue<triplet> Q;
Q.push(0,0,0);
while(Q is not empty)
    u = Q.third;
    Q.pop();
    if(visited[u]) continue;
    for all neighbour (w, v) of u where w is the edge weight
        if( !visited[v] && (dist[u] + w < dist[v] || (dist[u] + w == dist[v] && w < lastAdded[v])) )
            dist[v] = dist[u] + w;
            lastAdded[v] = w;
            Q.push(dist[v], lastAdded[v], v);
    visited[u] = true;
``

Now we just have to add all the values in lastAdded array and that will be our answer which is compared with weight of the MST. Further we also have to take care of the case when graph is disconnected, which can be easily accomplished by initializing lastAdded to infinity. After running the modified Dijkstra, if any of the vertex has lastAdded[] set to infinity then the answer is NO.

The proof of correctness of this algorithm is same as that of proof of correctness of prim’s algorithm which can be found in Introduction to Algorithms by CLRS.

### EDITORIALIST’S SOLUTION:

Editorialist’s solution can be found [here](http://hastebin.com/avuxegegor.avrasm).

</details>
